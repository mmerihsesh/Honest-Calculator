msg_0 = "Enter an equation"

calc = input(msg_0)
x, oper, y = calc.split()

try:
    x, y = float(x), float(y)
except ValueError:
    print('ValueError')

if oper == '+' or oper == '-' or oper == '*' or oper == '/':
    print('ok')
else:
    print('ne ok')


msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
