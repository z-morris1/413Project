import requests

def send_prompt_to_chatgpt(prompt, api_key):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",  # or another model name if you prefer
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}

# Replace 'your_api_key_here' with your actual OpenAI API key
api_key = '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'
prompt = ""
with open("prompt.txt", 'r') as file:
    for line in file:
        prompt+=line.rstrip('\n') + "\n"

response = send_prompt_to_chatgpt(prompt, api_key)
print(response)

