import requests
import shutil

#Josh Podlich
fileName = input('Enter the name of the file the code is in\n')
shutil.copyfile(fileName, './prompt.txt')
numTest = input('Enter the number of testcases to generate\n')
# inputs = input('Enter what the inputs should be labeled as ex:(num1:, num2:)\n')
pro = "generate a list of " + numTest + " test inputs with no other test for this code to check if it works, make sure to test edge cases, when listing the tests: start every input and incase them with \" without saying anything about the output in this format \'Input: \nparameter1: value1 \nparameter2: value2\n\nInput: \nparameter1: value1 \nparameter2: value2\'.  If the test case value is a string, surround it in "". Do not include any text or descriptions aside from the test cases."
f = open("prompt.txt", "a")
f.write("\n" + pro)
f.close()
#print("Done, prompt file is ready")

#Quang Le
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

#Zach
response = {'id': 'chatcmpl-8Px7H7LLAH6etALiylt9kIsavMnmX', 'object': 'chat.completion', 'created': 1701196135, 'model': 'gpt-3.5-turbo-0613', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': 'Input:\ninput_string: "abcd"\nsubstring: "bc"\n\nInput:\ninput_string: "hello"\nsubstring: "lo"\n\nInput:\ninput_string: "123"\nsubstring: "45"'}, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 203, 'completion_tokens': 39, 'total_tokens': 242}}
# variable1 = input("name of the first variable: ")
# variable2 = input("name of the second variable: ")
# Extracting input strings and substrings
numPrompts = 2
choices = response['choices']
for choice in choices:
    content = choice['message']['content']
    #input_strings = []
    #substrings = []
    condensed_list = []

    # Split content into individual input_string and substring pairs
    content = content.split('\n')
    content = str(content).split('"')

    for substr in content:
        if ':' in substr:
            content.remove(substr)
    if "']" in content:
        content.remove("']")
    
    print(content)

    

