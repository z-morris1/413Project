import shutil

fileName = input('Enter the name of the file the code is in\n')
shutil.copyfile(fileName, './prompt.txt')
numTest = input('Enter the number of testcases to generate\n')
inputs = input('Enter what the inputs should be labeled as ex:(num1:, num2:)\n')
pro = "generate a list of " + numTest + " test inputs with no other test for this code to check if it works, make sure to test edge cases, when listing the tests: start every input with " + inputs + " and incase them with \" without saying anything about the output"
f = open("prompt.txt", "a")
f.write("\n" + pro)
f.close()
print("Done, prompt file is ready")