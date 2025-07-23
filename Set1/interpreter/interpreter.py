expression = input("Expression: ").strip().lower()
[x,operator,y] = expression.split(" ")
x = int(x)
y= int(y)
solution = 0;
if operator == "+":
    solution = x + y
elif operator == '-':
    solution = x - y
elif operator == '*':
    solution = x * y
elif operator == '/':
    solution = x / y

print(float(solution))
    
    
#print(float(eval(expression)), end='')

