"# GraphTheory-G00347577" 


Enter Infix expression.


Programm Converts Infix expression to Postfix.


Enter String expression to Compare to Postfix.


Calls match()


 match() calls createNfa() which passes the infix String through the method and creates small NFA's which slowly get added to a bigger Overall
 NFA.
 
 
 match() then compares the String to the NFA and returns false if it doesn't match & true if it does.
 
 
 At the bottom of the page code is commented out which will run multiple infixes and strings. 
 
 convertToPodtfix()
 Takes in a string(infix expression) and converts it into a postfix expression
    by passing it through a for loop and adding and removing from a stack based on the presidence
    of the special operators otherwise adds the character.
    
    createNFA
  Takes in a postfix value and builds a series of NFA's by combing them Through edges and making
    new nodes that will lead to accept if it meets the expression or will go somewhere else which will lead to the answer being false
    
 
 def followes(node):
    """Helps with the match() by storing the nodes where they are relevant with edges to other nodes"""
    
   Takes a Infix and calls converToPostfix() to turn it into postfix notation where it is passed to the createNFA() to generate the NFA's.
    Then current is set to the initial state and passed through the loop where it checks the string against the the label in the current node
    and sets the current equal to he next and clears after a run of the for loop
 
