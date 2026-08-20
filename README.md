# Python AI Chatbot

A simple Groq-powered chat assistant built with LangChain, LangGraph, and Streamlit. The entire application is in `main.py`.

## Features

- Simple Streamlit chat interface
- Streaming Groq responses
- Conversation history during the session
- Calculator and greeting tools
- Lightweight free-tier-friendly default model: `llama-3.1-8b-instant`

## Project Structure

```text
.
├── main.py           # Streamlit application, tools, and agent
├── requirements.txt  # Python dependencies
├── .env.example      # Safe environment template
├── .gitignore        # Ignored local files and build artifacts
└── README.md         # Project documentation
```

## Setup

Use the existing virtual environment from the project directory.

```powershell
.venv\Scripts\Activate.ps1
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

## Environment Variables

Copy `.env.example` to `.env` and add your Groq API key:

```powershell
Copy-Item .env.example .env
```

Then edit `.env`:

```dotenv
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.1-8b-instant
```

`GROQ_MODEL` is optional. The application uses `llama-3.1-8b-instant` when it is omitted. Keep `.env` private.

## Run

Start the chat UI with:

```powershell
.venv\Scripts\python.exe -m streamlit run main.py
```

Open the URL shown by Streamlit, normally `http://localhost:8501`.

For a headless startup check:

```powershell
.venv\Scripts\python.exe -m streamlit run main.py --server.headless true --server.port 8501
```

## Troubleshooting

- Run `.venv\Scripts\python.exe -m pip install -r requirements.txt` if an import is missing.
- Confirm `.env` is in the project root and contains `GROQ_API_KEY`.
- Set `GROQ_MODEL` to a model currently available to your Groq account if the default model is unavailable.
