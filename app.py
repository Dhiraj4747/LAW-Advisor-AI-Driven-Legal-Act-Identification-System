
import streamlit as st
import os
import time
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

# Streamlit UI setup
st.set_page_config(page_title="LawAdvisor")
st.title("Law Advisor ChatBot ⚖️")

# Disclaimer
st.markdown("""
  ####  *Disclaimer:*  

*Hello, I am an AI-powered bot that can answer your legal queries related to Indian Laws and provide relevant answers to your questions.*  

*I am not a legal advisor or lawyer. Please consult a lawyer with your query to find a solution for your legal issues.*  

*I can only provide a starting point so you understand your rights better and get more information before consulting a lawyer.*  
""")

# Reset conversation function
def reset_conversation():
    st.session_state.messages = []
    st.session_state.memory.clear()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferWindowMemory(k=3, memory_key="chat_history", return_messages=True)

# Initialize embeddings and vector store
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
db = FAISS.load_local("my_vector_store", embeddings, allow_dangerous_deserialization=True)
db_retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 4})

# Define the prompt template
prompt_template = """
<s>[INST]As a legal chatbot, provide responses in 8-10 lines. Use previous chat history to maintain context. 
Do not generate unnecessary details. If the question is unrelated to legal topics, respond accordingly.
CONTEXT: {context}
CHAT HISTORY: {chat_history}
QUESTION: {question}
ANSWER:
</s>[INST]
"""
prompt = PromptTemplate(template=prompt_template, input_variables=['context', 'question', 'chat_history'])

# Initialize the LLM
llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama3-70b-8192")

# Set up the QA chain
qa = ConversationalRetrievalChain.from_llm(
    llm=llm,
    memory=st.session_state.memory,
    retriever=db_retriever,
    combine_docs_chain_kwargs={'prompt': prompt}
)

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message.get("role")):
        st.write(message.get("content"))

# User input
input_prompt = st.chat_input("Ask your legal question...")

if input_prompt:
    with st.chat_message("user"):
        st.write(input_prompt)
    st.session_state.messages.append({"role": "user", "content": input_prompt})

    with st.chat_message("assistant"):
        with st.status("Thinking 💡...", expanded=True):
            result = qa.invoke(input=input_prompt)
            response = result["answer"]
            
            # Limit response length
            response_lines = response.split("\n")
            trimmed_response = "\n".join(response_lines[:20])

            message_placeholder = st.empty()
            full_response = ""
            for chunk in trimmed_response:
                full_response += chunk
                time.sleep(0.02)
                message_placeholder.markdown(full_response + " ▌")

        # Follow-up button appears after the response is generated
        col1, col2 = st.columns([2, 2])
        with col1:
            st.button("Not satisfied? Ask a follow-up ➞", key="follow_up")
        with col2:
            st.button("Reset Chat 🗑", on_click=reset_conversation)

    st.session_state.messages.append({"role": "assistant", "content": trimmed_response})
