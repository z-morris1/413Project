data = {
    'id': 'chatcmpl-8KCSURFTTREZBlgDCiddHmD08xKwe',
    'object': 'chat.completion',
    'created': 1699825142,
    'model': 'gpt-3.5-turbo-0613',
    'choices': [{
        'index': 0,
        'message': {
            'role': 'assistant',
            'content': 'Input: \ninput_string: "Hello, world!"\nsubstring: "Hello"\n\nInput: \ninput_string: "abcdefg"\nsubstring: "cde"\n\nInput: \ninput_string: "12345"\nsubstring: "6"\n\nInput: \ninput_string: "This is a test"\nsubstring: "is"\n\nInput: \ninput_string: "abcabcabc"\nsubstring: "d"\n\nInput: \ninput_string: "The quick brown fox"\nsubstring: "The quick"\n\nInput: \ninput_string: "9876543210"\nsubstring: "11"\n\nInput: \ninput_string: "Programming is fun"\nsubstring: "fun"\n\nInput: \ninput_string: "xyzxyz"\nsubstring: "xy"\n\nInput: \ninput_string: "abcdefghijklmnopqrstuv"\nsubstring: "xyz"'
        },
        'finish_reason': 'stop'
    }],
    'usage': {
        'prompt_tokens': 170,
        'completion_tokens': 162,
        'total_tokens': 332
    }
}

# Extracting input strings and substrings
choices = data['choices']
for choice in choices:
    content = choice['message']['content']
    input_strings = []
    substrings = []

    # Split content into individual input_string and substring pairs
    pairs = content.split('\n\nInput: \n')
    for pair in pairs[1:]:
        pair = pair.strip()
        input_start = pair.find('input_string: "') + len('input_string: "')
        input_end = pair.find('"', input_start)
        input_strings.append(pair[input_start:input_end])

        substring_start = pair.find('substring: "') + len('substring: "')
        substring_end = pair.find('"', substring_start)
        substrings.append(pair[substring_start:substring_end])

    # Printing the extracted input strings and substrings
    
    for i, (input_str, substring) in enumerate(zip(input_strings, substrings)):
        print(f"Example {i + 1}:")
        print(f"Input String: {input_str}")
        print(f"Substring: {substring}")
        print()
    
    ##uncomment to print list
