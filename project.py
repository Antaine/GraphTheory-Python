#Antaine Ó Conghaile - G00347577 
import sys
infix = input("Enter expression: ")
print(infix)


def convertToPostfix(infix):
    stack = ""
    postfix = ""
    operatorChars = {'*': 50,'.': 40,'|': 30}
    specialChars = {'*','.','|','(',')'}
    
    for temp in infix:
        if temp in specialChars:
                #Automatically Add (
            if temp == '(':
                stack = stack + temp
                #Automatically Add until ) is found
            elif temp == ')':
                while stack[-1] != '(':
                    postfix = postfix + stack[-1]
                    stack = stack[:-1]
                stack = stack[:-1]
                #Sort Stack by value
            elif temp in operatorChars:
                while stack and operatorChars.get(temp,0) <= operatorChars.get(stack[-1],0):
                    postfix = postfix + stack[-1]
                    stack = stack[:-1]
                stack = stack + temp
            else:
                print("Error")
        else:
            print("Entered Normal Characters")
            postfix = postfix + temp
    #Make Sure List is Clear
    while stack:
        postfix = postfix + stack[-1]
        stack = stack[:-1]

    return postfix

print("PostFix: "+convertToPostfix(infix))
# for temp in inputList:   
#     print(temp)