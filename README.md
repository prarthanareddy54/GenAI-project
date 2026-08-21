# Python AI Chatbot

A lightweight Groq-powered chat assistant built with Streamlit, LangChain, and LangGraph. The app includes a simple sidebar model selector, chat history, and a couple of built-in tools for calculator and greeting tasks.

## Features

- Streamlit-based chat interface
- Response streaming from Groq
- Persistent chat history during the current session
- Built-in tools:
  - calculator for adding two numbers
  - say_hello for greeting a person by name
- Default configured model: `qwen/qwen3.6-27b`
- Sidebar control for switching the Groq model and resetting the chat

## Project Structure

```text
.
├── main.py           # Streamlit app, tools, and LangGraph agent logic
├── requirements.txt  # Python dependencies
├── .env.example      # Environment variable template
├── .gitignore        # Local files and generated artifacts to ignore
├── .venv/            # Local Python virtual environment
├── __pycache__/      # Python cache files
├── README.md         # Project documentation
└── .env              # Local secret config (not committed)
```

## Setup

Create or activate a virtual environment, then install the project dependencies:

```powershell
.venv\Scripts\Activate.ps1
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

If PowerShell blocks script execution, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

## Environment Variables

Copy the sample environment file and add your Groq API key:

```powershell
Copy-Item .env.example .env
```

Then update `.env`:

```dotenv
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=qwen/qwen3.6-27b
```

`GROQ_MODEL` is optional. If it is omitted, the app falls back to `qwen/qwen3.6-27b`.

## Run the App

Start the Streamlit app:

```powershell
.venv\Scripts\python.exe -m streamlit run main.py
```

The app will open in your browser at a local Streamlit URL, typically `http://localhost:8501`.

For a headless startup check:

```powershell
.venv\Scripts\python.exe -m streamlit run main.py --server.headless true --server.port 8501
```

## Usage

- Enter a question in the chat box.
- Use the sidebar to change the Groq model.
- Click `New chat` to clear the current conversation.
- The assistant can answer general questions and also use the built-in `calculator` and `say_hello` tools.

## Troubleshooting

- Run `.venv\Scripts\python.exe -m pip install -r requirements.txt` if you see missing module errors.
- Confirm `.env` exists in the project root and contains a valid `GROQ_API_KEY`.
- If the selected model is unavailable, switch to a model that is enabled for your Groq account.
- If the app shows a connection error, verify your API key and internet access.

## Notes

This project is intentionally simple and meant for local experimentation and learning. It is not a production-ready multi-user chat system, but it is a good starting point for building more advanced LangGraph agents with tool calling.
