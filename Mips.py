# Reading the text file and save it in a list called program
filepath = "FactorialTest.txt"
program = []
with open(filepath) as fp:
   line = fp.readline()
   counter = 1
   while line:
       program += [line.strip()]
       line = fp.readline()
       counter += 1
for i in range(len(program)):
    program[i] = program[i].replace(" ", "")

# Seperating instructions and inputs into two lists
instructions = []
inputs = []
flag = False
for i in program:
    if i != "" and flag == False:
        instructions += [i]
    if i == "":
        flag = True
    if i != "" and flag == True:
        inputs += [i]

# Checking for valid instruction set
runflag1 = True
for i in instructions:
    if len(i) != 15:
        print("ERROR! Wrong instruction set.")
        runflag1 = False

# Checking if all of the inputs are integer
for i in range(len(inputs)):
    inputs[i] = int(inputs[i])
        
# Having a storage named memory containing 10,000 cells
memory = [0 for i in range(10000)]

# Checking if Instructions are valid to be ready to run
runflag2 = False
AssemblyInstructions = ["BRU", "LDA", "STO", "ADD", "SUB", "MPY", "DIV", "HLT", "BMI", "RWD", "WWD"]
for i in instructions:
    string = i
    if string[4] == "+" and ((string[5:8] in AssemblyInstructions) or (string[5:8] == "000")):
        runflag2 = True
    else:
        print("ERROR! Wrong instruction.")
        
# Running the program
def Run(instruction_set, memory):
    # Seperate input and do instructions step by step
    ACC, IC = 0, 0
    user_input = []
    for i in range(len(instruction_set)):
        if len(instruction_set[i]) == 2:
            memory[i] = instruction_set[i][1]
        else:
            if instruction_set[i] != [""]:
                user_input += [instruction_set[i][0]]
    
    # Doing Instructions operation
    flag = True
    while(flag):
        instruction = memory[IC][1:4]
        address = int(memory[IC][7:11])
        IC += 1
        if instruction == "LDA":
            ACC = int(memory[int(address)])
        if instruction == "STO":
            memory[address] = ACC
        if instruction == "ADD":
            ACC += int(memory[address])
        if instruction == "SUB":
            ACC -= int(memory[address])
        if instruction == "MPY":
            ACC *= int(memory[address])
        if instruction == "DIV":
            ACC /= int(memory[address])
        if instruction == "HLT":
            break
        if instruction == "BRU":
            IC = int(address)
        if instruction == "BMI":
            if ACC < 0:
                IC = int(address)
        if instruction == "RWD":
            if len(user_input) == 0:
                print("ERROR! Invalid input.")
                break
            memory[address] = int(user_input[0])
            user_input = user_input[1:]
        if instruction == "WWD":
            print(memory[address])

# Run the program if there were no errors and get the input ready
if (runflag1 == True) and (runflag2 == True):
    instruction_set = []
    for i in instructions:
        instruction_set += [[i[:4], i[4:]]]
    instruction_set += [[""]]
    for i in inputs:
        instruction_set += [[str(i)]]
    Run(instruction_set, memory)