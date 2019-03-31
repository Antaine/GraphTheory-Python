#Antaine Ó Conghaile - G00347577 
#Variables
specialChars = {'*','.','|'}
#State
class node:
    label = None
    edge1 = None
    edge2 = None

#Nfa states
class nfa:
    initial = None
    accept = None
    #Constructor
    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept
        
#Shunt
def convertToPostfix(infix):
    """ Takes in a string(infix expression) and converts it into a postfix expression
    by passing it through a for loop and adding and removing from a stack based on the presidence
    of the special operators otherwise adds the character"""
    #Variables
    stack = ""
    postfix = ""
    operatorChars = {'*': 50,'.': 40,'|': 30}
    specialChars = {'*','.','|','(',')'}
    
    #Parse infix Characters
    for temp in infix:
        #If special character is found
        if temp in specialChars:
        #Automatically Add (
            if temp == '(':
                stack = stack + temp
        #Remove from stack & add to postfix until the open bracket is found
            elif temp == ')':
                #While closing bracket is not found
                while stack[-1] != '(':
                    postfix = postfix + stack[-1]
                    stack = stack[:-1]
                stack = stack[:-1]
        #If operator is found
            elif temp in operatorChars:
                while stack and operatorChars.get(temp,0) <= operatorChars.get(stack[-1],0):
                    postfix = postfix + stack[-1]
                    stack = stack[:-1]
                stack = stack + temp
        #Add Normar character    
        else:
            postfix = postfix + temp
    #Make Sure List is Clear
    while stack:
        postfix = postfix + stack[-1]
        stack = stack[:-1]

    return postfix

def createNFA(postfix):
    """ Takes in a postfix value and builds a series of NFA's by combing them Through edges and making
    new nodes that will lead to accept if it meets the expression or will go somewhere else which will lead to the answer being false"""
    nfaStack = []
    print("Postfix ",postfix)
    #Parse postfix 
    for c in postfix:
      #  if c in specialChars:
        if c == '.':
            #Pop from top of stack LIFO
            nfa2 = nfaStack.pop()
            nfa1 = nfaStack.pop()

            #Connect edge between end 
            nfa1.accept.edge1 = nfa2.initial

            #Join into one node & add to stack
            newNfa = nfa(nfa1.initial, nfa2.accept)
            nfaStack.append(newNfa)

            
        elif c == '|':
            #Pop from top of stack LIFO
            nfa2 = nfaStack.pop()
            nfa1 = nfaStack.pop()

            #Set initial nodes for both paths
            initial = node()
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial
            #Set Accept Node
            accept = node()
            nfa1.accept.edge1 = accept
            nfa2.accept.edge1 = accept
            #Join and send to Stack
            newNfa = nfa(initial, accept)
            nfaStack.append(newNfa)

        elif c == '*':
            #Pop from top of stack LIFO
            nfa1 = nfaStack.pop()
            #Create Node
            initial = node()
            accept = node()
            #Set Edges to Connect
            initial.edge1 = nfa1.initial
            initial.edge2 = accept
            #Connect 
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept
            #Join and send to Stack
            newNfa = nfa(initial, accept)
            nfaStack.append(newNfa)

        else:
            #Accepts Character straight into accept Node
            accept = node()
            initial = node()

            initial.label = c
            initial.edge1 = accept
            #nfaStack.append(nfa(initial, accept))
            newNfa = nfa(initial, accept)
            nfaStack.append(newNfa)

    return nfaStack.pop()

def followes(node):
    """Helps with the match() by storing the nodes where they are relevant with edges to other nodes"""
    #Create empty node and add to Nodes
    nodes = set()
    nodes.add(node)

    #If no connection
    if node.label is None:
        #If not null add to nodes
        if node.edge1 is not None:
            nodes |= followes(node.edge1)

        if node.edge2 is not None:
            nodes |= followes(node.edge2)

    return nodes

def match(infix, string):
    """ Takes a Infix and calls converToPostfix() to turn it into postfix notation where it is passed to the createNFA() to generate the NFA's.
    Then current is set to the initial state and passed through the loop where it checks the string against the the label in the current node
    and sets the current equal to he next and clears after a run of the for loop"""
    postfix = convertToPostfix(infix)
    nfa = createNFA(postfix)
    #Create empty node
    current = set()
    nexts = set()

    current |= followes(nfa.initial)
    #compare String to All Current nodes and set current to next node 
    for s in string:
        for c in current:
            if c.label == s:
                nexts |= followes(c.edge1)
     #           print("Nexts ", nexts)
        current = nexts
    #    print("Current ", current)
    #Clear next
        nexts = set()

    return(nfa.accept in current)


#Main
infix = input("Enter expression: ")

string = input("Enter String: ")
print(match(infix, string))

#Test Code
#print(infix)
#postfix = convertToPostfix(infix)
#print("PostFix: " + postfix)
#print(createNFA(postfix))

#Test Material
#infixes = ["a.b.c*", "a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c"]
#testValues = ["","abc", "abbc", "abcc", "abad", "abbbc"]

#Loop test material
#for i in infixes:
 #   for s in testValues:
  #      print(match(i, s),i,s)