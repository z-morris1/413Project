import os

# Create testcasesAI directory
directory = "testcasesAI"
if not os.path.exists(directory):
    os.makedirs(directory)

# Temporary array of strings. Should be replaced by array of test cases 
strings = ["\"String 1\"", "String 2", "String 3", "String 4"]  
strings = zip(strings[0::2], strings[1::2])
# Iterate through strings array and outputs each line into a text file
for i, s in enumerate(strings):
    with open(os.path.join(directory, f'test{i}.txt'), 'w') as f:
        f.write(s)
# Gets the current directory
cwd = os.getcwd()
# Outputs the current directory for the user to paste into AFL++
print(cwd + "/testcasesAI")