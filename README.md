# 🤖 AI Tool-Calling Agent

An AI assistant built with **Python, Gemini, Streamlit, and custom tool calling**.

The agent can understand user requests, decide when a tool is required, execute the appropriate Python function, and use the tool result to generate a final response.

## 🚀 Live Demo

👉 **[Open the AI Tool-Calling Agent](https://aichatbot-994mnofnphckfa9wp2dcwg.streamlit.app/)**

## ✨ Features

* 🤖 Gemini-powered AI assistant
* 🔧 LLM tool calling
* 🧮 Calculator
* ➕ Addition
* ✖️ Multiplication
* ➖ Subtraction
* ➗ Division
* 📊 Percentage calculation
* 🌤️ Weather information
* 🌐 Web search using Tavily
* 🕐 Current date and time
* 📏 Unit conversion
* 💬 Streamlit chat interface
* 🛡️ Tool error handling
* 🔄 Multi-step agent loop
* 🔐 API key management using environment variables and Streamlit Secrets

## 🏗️ Architecture

```text
                    User
                      │
                      ▼
              ┌───────────────┐
              │  Streamlit UI │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │   AI Agent    │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │    Gemini     │
              │     LLM       │
              └───────┬───────┘
                      │
                Tool Calling
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
     Calculator    Weather    Web Search
          │           │           │
          └───────────┼───────────┘
                      │
                      ▼
                 Tool Result
                      │
                      ▼
                  Gemini
                      │
                      ▼
                Final Answer
```

## 🛠️ Technologies

* **Python**
* **Google Gemini API**
* **Google GenAI SDK**
* **Streamlit**
* **Tavily API**
* **Open-Meteo API**
* **Requests**
* **python-dotenv**
* **Git & GitHub**

## 📂 Project Structure

```text
AI_chat_bot/
│
├── agent.py          # Agent logic and tool-calling loop
├── app.py            # Streamlit user interface
├── llm.py            # Gemini client configuration
├── tools.py          # Python tools used by the agent
├── test_tool.py      # Tool testing
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
└── .gitignore        # Ignored files and secrets
```

## 🔧 Available Tools

### Calculator

The agent can perform:

```text
Addition
Multiplication
Subtraction
Division
Percentage calculations
```

### 🌤️ Weather

The weather tool uses **Open-Meteo** to retrieve current weather information for a requested city.

Example:

```text
What is the weather in Lahore?
```

### 🌐 Web Search

The agent can use **Tavily** to search for current web information.

Example:

```text
Search the web for the latest AI developments.
```

### 🕐 Date & Time

The agent can retrieve the current date and time.

### 📏 Unit Conversion

The agent supports several unit conversions, including:

```text
Kilometers ↔ Miles
Kilograms ↔ Pounds
Meters ↔ Feet
Celsius ↔ Fahrenheit
```

## 🧠 What I Learned

This project was built to understand the fundamentals of modern AI agents and tool calling.

Key concepts practiced:

* LLM APIs
* Function/tool calling
* Agent loops
* Function execution
* Tool schemas
* External APIs
* Conversation state
* Error handling
* Environment variables
* API key management
* Streamlit application development
* Git and GitHub
* Cloud deployment

## 🔐 Environment Variables

For local development, create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

For Streamlit Cloud, configure the API keys through **Streamlit Secrets**.

Never commit API keys or `.env` files to GitHub.

## ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/TalhaAlmani7/AI_chat_bot.git
```

Move into the project:

```bash
cd AI_chat_bot
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create your `.env` file with the required API keys.

Run Streamlit:

```bash
streamlit run app.py
```

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud**.

**Live application:**

👉 https://aichatbot-994mnofnphcka9wp2dcwg.streamlit.app

The GitHub repository is the source code for the deployed application.

## 📌 Project Status

This project is a practical learning and portfolio project focused on understanding **LLM tool calling and AI agent architecture**.

The core application, tool implementations, Gemini integration, Streamlit interface, and cloud deployment have been completed.

Further improvements could include more robust function-call handling, improved observability, authentication, persistent memory, and production-level error handling.

## 🔮 Future Improvements

* LangChain integration
* LangGraph workflows
* RAG
* Vector databases
* Persistent conversation memory
* Authentication
* Docker
* Better monitoring and logging
* More external tools
* Production-grade error handling
* Multi-agent workflows

## 👨‍💻 Author

**Talha Almani**

Data Science & AI Enthusiast

---

⭐ If you find this project useful, feel free to explore the repository and the live demo.
