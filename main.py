import streamlit as st
from chatbot import create_chain

st.set_page_config(
    page_title="CVR College Chatbot",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 CVR College Chatbot")

if "chain" not in st.session_state:
    with st.spinner("Loading chatbot..."):
        st.session_state.chain = create_chain()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat Input
user_input = st.chat_input(
    "Ask a question about CVR College..."
)

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = st.session_state.chain.invoke(
                {"question": user_input}
            )

            answer = response["answer"]

            st.markdown(answer)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )