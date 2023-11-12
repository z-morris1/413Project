import os

# Create testcasesAI directory if it does not exist
directory = "testcasesAI"
if not os.path.exists(directory):
    os.makedirs(directory)

# Define an array of strings
strings = ["\"String 1\"", "String 2", "String 3", "String 4"]  # Replace with your actual strings

# For each string, create a new .txt file and write the string to the file
for i, s in enumerate(strings):
    with open(os.path.join(directory, f'test{i}.txt'), 'w') as f:
        f.write(s)
cwd = os.getcwd()
print(cwd + "/testcasesAI")