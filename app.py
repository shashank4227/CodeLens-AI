import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API Key from environment
api_key = os.getenv("GROQ_API_KEY")

# --- Page Config ---
st.set_page_config(
    page_title="Groq AI Code Reviewer",
    page_icon="🤖",
    layout="wide"
)

# --- Sidebar: Configuration ---
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # API Key Status Indicator
    if api_key:
        st.success("API Key detected ✅")
    else:
        st.error("API Key missing ❌")
        st.info("Please set GROQ_API_KEY in your .env file or system environment variables.")

    # Model Selection
    model_option = st.selectbox(
        "Select Model",
        options=["llama-3.3-70b-versatile", "llama-3.1-70b-versatile", "llama-3.1-8b-instant"],
        index=0
    )
    
    st.divider()
    st.markdown("### How to use:")
    st.markdown("1. Upload a file OR paste code.")
    st.markdown("2. Click 'Analyze Code'.")

# --- Main Interface ---
st.title("🤖 CodeLens AI")

# Stop execution if no key is found
if not api_key:
    st.warning("⚠️ No API key found. Please create a `.env` file with `GROQ_API_KEY=your_key`.")
    st.stop()

# Input Method Selection
tab1, tab2 = st.tabs(["📁 Upload File", "📝 Paste Code"])

code_content = ""

with tab1:
    uploaded_file = st.file_uploader("Upload a file", type=["py", "js", "java", "cpp", "html", "css", "ts"])
    if uploaded_file is not None:
        try:
            code_content = uploaded_file.read().decode("utf-8")
        except Exception as e:
            st.error(f"Error reading file: {e}")

with tab2:
    text_input = st.text_area("Paste your code here...", height=300)
    if text_input:
        code_content = text_input

# --- Analysis Logic ---
if st.button("🚀 Analyze Code", type="primary"):
    if not code_content:
        st.warning("⚠️ Please upload a file or paste some code.")
    else:
        client = Groq(api_key=api_key)
        
        with st.expander("View Source Code"):
            st.code(code_content)

        st.subheader("🔍 Analysis Report")
        
        system_prompt = """
        You are an expert Senior Software Engineer. Analyze the provided code.
        Format your response in Markdown.
        Include these sections:
        1. 🔴 **Critical Issues** (Bugs/Errors)
        2. ⚠️ **Security Warnings**
        3. ⚡ **Performance Improvements**
        4. 🧹 **Refactoring Suggestions**
        5. ✅ **Corrected Code Snippet** (Refactored version of the most critical part)
        """

        try:
            with st.spinner("Analyzing with Llama 3..."):
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"Analyze this code:\n\n{code_content}"}
                    ],
                    model=model_option,
                    temperature=0.2,
                    max_tokens=2048,
                    stream=True
                )

                # Stream response
                response_container = st.empty()
                full_response = ""
                
                for chunk in chat_completion:
                    if chunk.choices[0].delta.content:
                        full_response += chunk.choices[0].delta.content
                        response_container.markdown(full_response + "▌")
                
                response_container.markdown(full_response)
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")