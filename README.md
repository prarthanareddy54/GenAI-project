# Python AI Chatbot

A terminal-based AI assistant built with LangChain, LangGraph, and Groq. The assistant can hold a conversation and use simple tools for addition and greetings.

## Features

- Groq-powered language model responses
- ReAct agent orchestration through LangGraph
- Calculator tool for adding two numbers
- Greeting tool for personalized responses
- Streaming output in the terminal
- Environment-based configuration with `python-dotenv`

## Architecture

```text
User
  |
  v
main.py - terminal interface and application entry point
  |
  +--> ChatGroq - sends requests to the Groq API
  |
  +--> LangGraph ReAct agent - decides when to respond or call a tool
          |
          +--> calculator(a, b)
          |
          +--> say_hello(name)
```

### Main components

- **Environment configuration:** `load_dotenv()` loads `GROQ_API_KEY` and the optional `GROQ_MODEL` setting from a `.env` file.
- **Tools:** `calculator` and `say_hello` are decorated with LangChain's `@tool`, making them available to the agent.
- **Model:** `ChatGroq` connects the application to Groq with temperature set to `0` for more deterministic responses.
- **Agent:** `create_react_agent` combines the model and tools so the model can choose an appropriate tool during a conversation.
- **CLI loop:** `main()` reads user input, streams agent output, and exits when the user enters `quit`.

## Workflow

1. The application starts and loads environment variables from `.env`.
2. It reads the Groq API key and model name.
3. It creates the `ChatGroq` model.
4. It registers the calculator and greeting tools with a LangGraph ReAct agent.
5. The terminal accepts a user message.
6. The agent determines whether it should answer directly or call a tool.
7. Tool results are returned to the agent when needed.
8. The final response is streamed to the terminal.
9. The loop continues until the user enters `quit`.

## Project Structure

```text
.
├── main.py           # Application code, tools, agent, and CLI loop
├── requirements.txt  # Python dependencies
├── .env              # Local secrets and optional configuration (create this)
└── README.md         # Project documentation
```

## Project Startup

### Prerequisites

- Python 3.10 or newer
- A Groq account and API key
- Windows PowerShell, Command Prompt, or another terminal

### 1. Create and activate a virtual environment

From the project directory:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution for the current user, run PowerShell as your normal user and execute:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then activate the environment again.

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a file named `.env` in the project root:

```dotenv
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=qwen/qwen3.6-27b
```

`GROQ_MODEL` is optional. If it is omitted, the application uses `qwen/qwen3.6-27b` by default. Do not commit `.env` or expose the API key.

### 4. Start the chatbot

```powershell
python main.py
```

The application will display a prompt. Try messages such as:

```text
Add 12 and 8
Say hello to Priya
What can you help me with?
```

Enter `quit` to stop the application.

## Troubleshooting

- **API key warning:** Confirm that `.env` is in the same directory as `main.py` and that `GROQ_API_KEY` is set correctly.
- **Model errors:** Set `GROQ_MODEL` to a model currently available in your Groq account.
- **Import errors:** Activate the virtual environment and rerun `pip install -r requirements.txt`.
- **PowerShell activation errors:** Use the execution-policy command in the setup section or activate the environment from Command Prompt with `.venv\Scripts\activate.bat`.

## Security Notes

- Keep API keys in `.env` or another secret manager.
- Add `.env` to `.gitignore` before committing the project.
- Avoid printing secrets in application logs.
