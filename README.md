# 🤖 MY-FIRST-AI-AGENT

This is an AI-powered chatbot built using **LangChain** and **Ollama**. It can process and generate natural language responses efficiently. The chatbot is designed to be scalable and customizable for various applications like customer support, virtual assistants, or intelligent automation.

---

## 🚀 Features

- ✅ AI-driven natural language processing
- ⚙️ Customizable and scalable design
- ⚡ Uses LangChain and Ollama for efficient performance
- 🔌 Easy to integrate into various applications
- 🧠 Context-aware responses with memory handling
- 💽 CLI interface for interactive chat

---

## 🛠 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Debabrata7719/MY-FIRST-AI-AGENT.git
cd MY-FIRST-AI-AGENT
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install the Dependencies

```bash
pip install -r requirements.txt
```

> 💡 Make sure you have [Ollama](https://ollama.com/) installed and running locally.

---

## ✅ Prerequisites

- Python 3.10 or higher
- [Ollama](https://ollama.com/download) installed and running (`ollama run llama3`)
- Internet connection for initial model download

---

## 💬 Usage

Run the chatbot:

```bash
python main.py
```

Start chatting! Type your questions and get smart, contextual responses.

Example:
```
You: What can you do?
DebAI: I can help you with natural language understanding, answering questions, and more!
```

---

## 📁 Project Structure

```
MY-FIRST-AI-AGENT/
├── app.py                  # Main chatbot logic
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
```


---

## 🙌 Acknowledgments

- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/)
- Open source community ❤️

---

## 🚫 Challenges Faced During Integration

While building this chatbot, a few challenges were encountered:

- ❌ **Missing Dependencies**: Some modules like `langchain_ollama` or `ollama` weren’t installed by default and had to be explicitly added to `requirements.txt`.
- ❌ **Model Not Running**: The chatbot failed if `ollama run llama3` wasn’t already running in the background.
- ❌ **Incorrect Context Handling**: Early versions didn't retain conversation history properly, leading to less contextual responses.
- ❌ **PromptTemplate Misuse**: At first, the prompt template wasn't applied correctly which led to blank or broken outputs.

These were fixed through testing and improvements in chaining and prompt structure. Now, the agent provides smooth contextual replies.

