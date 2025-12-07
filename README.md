# 🤖 AI Code Analyzer

A modern, web-based code analysis tool built with **Streamlit** and powered by **Groq (Llama 3)**. This tool acts as an automated Senior Software Engineer, reviewing your code for bugs, security vulnerabilities, and performance bottlenecks in real-time.

## ✨ Features

* **⚡ Blazing Fast Analysis**: Uses Groq's LPU inference engine for near-instant results.
* **🧠 Advanced Logic**: Powered by Meta's **Llama 3** (70B & 8B models).
* **🛡️ Secure**: API keys are loaded via environment variables, never exposed in the UI.
* **📂 Dual Input**: Upload code files (`.py`, `.js`, `.java`, etc.) or paste code directly.
* **📝 Comprehensive Reports**:
    * 🔴 Critical Bug Detection
    * ⚠️ Security Vulnerability Checks
    * ⚡ Performance Optimization Tips
    * ✅ Refactoring & Corrected Code Snippets

## 🛠️ Tech Stack

* **Python** 3.8+
* **Streamlit** (Frontend UI)
* **Groq SDK** (LLM Inference)
* **Python-Dotenv** (Environment Management)

---

## 🚀 Getting Started

### 1. Prerequisites

You need a free API Key from Groq.

* Get it here: [https://console.groq.com/keys](https://console.groq.com/keys)

### 2. Installation

Clone the repository (or create a new folder) and install the dependencies:

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install streamlit groq python-dotenv
```

### 3. Configuration

Create a file named `.env` in the root directory of the project to store your API key securely.

**File: `.env`**

```ini
GROQ_API_KEY=gsk_your_actual_api_key_here
```

### 4. Running the App

Launch the application using Streamlit:

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

-----

## 📂 Project Structure

```
├── app.py           # Main application logic (Streamlit)
├── .env             # Environment variables (API Key) - DO NOT COMMIT THIS
├── README.md        # Project documentation
└── requirements.txt # Dependencies
```

## 📦 Requirements.txt

If you want to freeze your dependencies, run:

`pip freeze > requirements.txt`

The content should look like this:

```text
streamlit
groq
python-dotenv
```

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/)

