Punjab AI Citizen Assistant (Ollama LLM Chatbot)

A local chatbot using Ollama + Gemma LLM model that acts as a citizen assistant for the Punjab Government.
It demonstrates how to interact with an LLM via Python, implement conversation memory, system prompt guardrails, and optionally stream responses token-by-token.


Features

Local LLM chatbot using Gemma3:4b model
System prompt-based guardrails to ensure safe and formal responses
Conversation memory: remembers previous messages in the session
Streaming support: toggle live token-by-token output (True and False)
Simple Python interface using requests
Designed for government applications like citizen helplines


Requirements
Python 3.10+
Ollama 0.16.1+ running locally
Installed Gemma Model in Ollama (3:4b)


Setup
Make sure Ollama is installed and running on your machine
Download a Gemma model (Gemma3:4b preferred)
Ensure Ollama server is running on localhost:11434
Clone this repository or save chat_ollama2.py.


Usage

Open a terminal (not VS Code output panel).

Run the chatbot:
python chat_ollama.py

Type your message:
You: Hi my name is [your name]

The assistant will respond according to system guardrails.
Type exit to quit.


Configuration
Streaming Mode: True/False can be controlled on top - to alter the flow of responses.
Model Selection: you can select model of your preference from the Ollama GUI - make sure it can run on your machine seamlessly
Guardrails: Build the personality of your AI assistant by guiding the rules and regulations to it via system prompt chunk in the code.
