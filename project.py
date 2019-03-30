#Antaine Ó Conghaile - G00347577 

#Variables
postfix = ""
specialChars = {'*','.','|'}
#State
class node:
    label = None
    edge1 = None
    edge2 = None

#Definition
class nfa:
    initial = None
    accept = None
    #Constructor
    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept

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
            postfix = postfix + temp
    #Make Sure List is Clear
    while stack:
        postfix = postfix + stack[-1]
        stack = stack[:-1]

    return postfix

def createNFA(postfix):
    nfaStack = []

    for c in postfix:
        if c in specialChars:
            if c == '.':
                nfa2 = nfaStack.pop()
                nfa1 = nfaStack.pop()
                nfa1.accept.edge1 = nfa2.initial
                nfaStack.append(nfa1.initial, nfa2.accept)
            
            elif c == '|':
                nfa2 = nfaStack.pop()
                nfa1 = nfaStack.pop()
                initial = node()
                accept = node()
                initial.edge1 = nfa1.initial
                initial.edge2 = nfa2.initial

                nfa1.accept.edge1 = accept
                nfa2.accept.edge1 = accept
                nfaStack.append(nfa(initial,accept))

            elif c == '*':
                nfa1 = nfaStack.pop()
                initial = node()
                accept = node()
                initial.edge1 = nfa1.initial
                initial.edge2 = accept
                nfa1.accept.edge1 = nfa.initial
                nfa1.accept.edge2 = accept
                nfaStack.append(nfa(initial,accept))


        else:
            accept = node()
            initial = node()
            initial.label = c
            initial.edge1 = accept
            nfaStack.append(nfa(initial, accept))
           # newNfa = nfa(initial, accept)
            #nfaStack.append(newNfa)

    return nfaStack.pop()

#Main
infix = input("Enter expression: ")
print(infix)
postfix = convertToPostfix(infix)
print("PostFix: " + postfix)
print(createNFA(postfix))