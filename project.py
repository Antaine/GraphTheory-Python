#Antaine Ó Conghaile - G00347577 
import sys
input1 = input("Enter expression: ")
print(input1)
inputList = list(input1)
#inputList = list(input)
print(inputList)
stack = list()

for temp in inputList:
    if temp in ['*','.','|']:
        stack.extend(temp)
        print("Special Operator: "+ temp)
        
    else:
        stack.extend(temp)
        print("Normal Character: "+ temp)

print(stack)

# for temp in inputList:   
#     print(temp)