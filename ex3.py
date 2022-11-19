print("FILO")
stack = ["A", "B", "C", "D", "E", "F"]
array = []
for i in stack:
    array.append(i)
    print(array)

for i in stack:
    array.pop()
    print(array)
print ("FIFO")
stack1 = ["A", "B", "C", "D", "E", "F"]
for i in stack1:
    array.append(i)
    print(array)

for i in stack1:
    array.pop(0)
    print(array)
print("ex 2")
array2 = []
stack = ["A", "B", "C", "D", "E", "F"]
while stack:
    array2.append(stack.pop())
print(array2)
while array2:
    array.append(array2.pop(0))
    
    stack = "( A + B )*C"
equation = list(stack) 
operator = ["+","-","*","/"]
Current = "" 
Out = [ ] 
Operator = [ ] 
Result = '' 
def postfix(input):
    if input in operator:
        if (((input == "/") or (input == "*")) and (Operator != [ ])):
            if ((Operator[-1] == "*") or (Operator[-1] == "/")):
                Out.append(Operator.pop())
                Operator.append(equation.pop(0))
            else:
                Operator.append(equation.pop(0))
        else:
            if (Operator != [ ]):
                if (((input == "+") or (input == "-")) and ((Operator[-1] == "*") or (Operator[-1] == "/"))):
                    Out.append(Operator.pop())
                    while len(Operator) > 0:
                        Out.append(Operator.pop())
                else:
                    Operator.append(equation.pop(0))
            else:
                    Operator.append(equation.pop(0))
    else:
                    Operator.append(equation.pop(0))
                    
while len(equation) > 0:
    Current = equation[0]
    postfix(equation[0])
    
while len(Operator) > 0:
    Out.append(Operator.pop())
for i in Out: 
    Result += i
print("stack value : " + stack)
print("Result value : " + Result)