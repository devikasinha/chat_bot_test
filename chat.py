import streamlit as st
import os
from dotenv import load_dotenv

# Import the correct Google-specific LangChain components
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

# Load environment variables from .env file
load_dotenv()

# Set up the API key from environment variables
api_key = os.getenv("GOOGLE_API_KEY")

# Check if the API key is set
if not api_key:
    st.error("Google API key not found. Please set it in your .env file.")
else:
    # --- LangChain Setup ---

    # Use a valid model name from the list you provided
    # Let's use the fast and efficient Gemini 1.5 Flash model
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", google_api_key=api_key)

    # Define the prompt template
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful AI assistant."),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}"),
        ]
    )

    # Set up message history storage
    store = {}

    def get_session_history(session_id: str) -> ChatMessageHistory:
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        return store[session_id]

    # Create the conversational chain with message history
    with_message_history = RunnableWithMessageHistory(
        prompt | llm,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history",
    )

    # --- Streamlit UI ---

    st.title("Google Gemini Chatbot (Updated)")

    # Initialize chat history in Streamlit session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt_text := st.chat_input("What is up?"):
        # Add user message to chat history and display it
        st.session_state.messages.append({"role": "user", "content": prompt_text})
        with st.chat_message("user"):
            st.markdown(prompt_text)

        # Get a unique session ID for the message history
        session_id = "single_user_session"

        # Get response from the LangChain chain
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = with_message_history.invoke(
                    {"input": prompt_text},
                    config={"configurable": {"session_id": session_id}},
                )
                st.markdown(response.content)

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response.content})