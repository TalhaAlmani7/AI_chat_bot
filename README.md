# AI Tool-Calling Agent

An AI agent built with Python, Qwen 2.5, Ollama, and Streamlit.

The agent can understand user requests and decide when to use external tools to complete tasks.

## Features

* 🤖 Qwen 2.5 + Ollama
* 🧮 Calculator tools
* 🌤️ Weather information
* 🌐 Web search
* 🕐 Date and time
* 📏 Unit conversion
* 🔄 Multi-step tool-calling agent loop
* 💬 Streamlit chat interface
* 🛡️ Tool error handling

## Architecture

```text
User
  ↓
Streamlit UI
  ↓
Agent
  ↓
Qwen 2.5 + Ollama
  ↓
Tool Selection
  ↓
Python Tool
  ↓
Tool Result
  ↓
Qwen 2.5
  ↓
Final Answer
```

## Technologies

* Python
* Ollama
* Qwen 2.5
* Streamlit
* Requests
* Python-dotenv
* Tavily
* Open-Meteo

## Project Structure

```text
AI_chat_bot/
├── agent.py
├── app.py
├── tools.py
├── test_tool.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

## Setup

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your required API keys.

## Run the Application

Start Ollama and make sure the required Qwen model is available.

Then run:

```bash
streamlit run app.py
```

Open the local Streamlit URL shown in the terminal.

## Example Questions

```text
What is 25% of 800?

What is the weather in Lahore?

Search the web for the latest AI news.

Convert 10 kilometers to miles.

What is the current date and time?
```

## Learning Goals

This project demonstrates the fundamentals of:

* LLM tool calling
* Agent loops
* Function execution
* External APIs
* Conversation state
* Error handling
* Streamlit application development

## Future Improvements

* LangChain integration
* LangGraph workflows
* RAG
* Vector databases
* Multi-agent systems
* Docker
* Cloud deployment
* Authentication
* Persistent conversation memory
