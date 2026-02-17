import requests
import json


stream = True  #true/false regarding the flow
model_name = "gemma3:4b"
url = "http://localhost:11434/api/chat"

#system prompt - guardrails
messages = [
    {
        "role": "system",
        "content": """
You are the Punjab Government Citizen Assistant.

Rules:
- Keep answers short and clear
- Be polite and formal
- If unsure, say:
'Please contact the 1786 helpline for verified information.'
- Do NOT make up policies.
"""
    }
]

print("Punjab AI Assistant (type 'exit' to quit)\n")

#chat structure loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    # Add user message to conversation memory
    messages.append({"role": "user", "content": user_input})

    payload = {
        "model": model_name,
        "messages": messages,
        "stream": stream
    }

    # Send request to Ollama
    response = requests.post(url, json=payload, stream=stream)

   #stream condition
    if stream:
        # Streaming mode: build reply token-by-token
        reply = ""
        for line in response.iter_lines():
            if line:
                data_line = json.loads(line.decode("utf-8"))
                if "message" in data_line:
                    content = data_line["message"].get("content", "")
                    reply += content
                    # Optional: print token as it arrives
                    print(content, end="", flush=True)
        print("\n")  # final newline after streaming finishes
    else:
        # Non-streaming mode: get full reply at once
        data = response.json()
        reply = data.get("message", {}).get("content", "[No reply received]")
        print("\nAssistant:", reply, "\n")

    #recurrant behavior
    messages.append({"role": "assistant", "content": reply})
