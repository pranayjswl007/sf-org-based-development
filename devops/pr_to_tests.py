

import os
cwd = os.getcwd()
print(cwd)
test_to_run = ""

def write_test_to_file(testNames):
    file = open("tests_to_run.txt", "w") 
    file.write(testNames)
    file.close() 

    
# Open the file in read mode
with open('pr_body.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # Print each line
        if("Apex::" in line and '::Apex' in line):
            # found the apex test block , now find the tests
            start = line.find('[')
            end = line.find(']')
            if start != -1 and end != -1 and end > start:
                test_to_run= line[start+1:end]
                print(test_to_run)
                write_test_to_file(test_to_run)





