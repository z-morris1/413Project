data = {'id': 'chatcmpl-8Px7H7LLAH6etALiylt9kIsavMnmX', 'object': 'chat.completion', 'created': 1701196135, 'model': 'gpt-3.5-turbo-0613', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': 'Input:\ninput_string: "abcd"\nsubstring: "bc"\n\nInput:\ninput_string: "hello"\nsubstring: "lo"\n\nInput:\ninput_string: "123"\nsubstring: "45"'}, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 203, 'completion_tokens': 39, 'total_tokens': 242}}
# variable1 = input("name of the first variable: ")
# variable2 = input("name of the second variable: ")
# Extracting input strings and substrings
numPrompts = 2
choices = data['choices']
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

    
