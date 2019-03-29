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
            #  print("Entered Special Characters")
                #Automatically Add (
            if temp == '(':
                stack = stack + temp
                print('( Stack Value ' + stack)
                print('( Postfix Value ' + postfix)
                #Automatically Add until ) is found
            elif temp == ')':
                while stack[-1] != '(':
                    postfix = postfix + stack[-1]
                    stack = stack[:-1]
                stack = stack[:-1]
                print(') Stack Value ' + stack)
                print(') Postfix Value ' + postfix)
                #Sort Stack by value
            elif temp in operatorChars:
                print("Entered operator")
                while stack and operatorChars.get(temp,0) <= operatorChars.get(stack[-1],0):
                    postfix = postfix + stack[-1]
                    stack = stack[:-1]
                stack = stack + temp
                print('*/./| Stack Value ' + stack)
                print('*/./| Postfix Value ' + postfix)

            else:
                print("Error")
        else:
            print("Entered Normal Characters")
            postfix = postfix + temp
            print('Normal Stack Value ' + stack)
            print('Normal Postfix Value ' + postfix)
    #Make Sure List is Clear
    while stack:
        postfix = postfix + stack[-1]
        stack = stack[:-1]

        
    print(postfix)
    return postfix

print("PostFix: "+convertToPostfix(infix))
# for temp in inputList:   
#     print(temp)