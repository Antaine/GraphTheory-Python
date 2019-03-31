"# GraphTheory-G00347577" 
Enter Infix expression.
Programm Converts Infix expression to Postfix.
Enter String expression to Compare to Postfix.
Calls match()
 match() calls createNfa() which passes the infix String through the method and creates small NFA's which slowly get added to a bigger Overall
 NFA.
 match() then compares the String to the NFA and returns false if it doesn't match & true if it does.
 At the bottom of the page code is commented out which will run multiple infixes and strings. 
