msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

calc = input()
def stage_1(calc):
    x, oper, y = calc.split()
    print(x, oper, y)

stage_1(calc)

try:
    x, y = float(x), float(y)
except ValueError:
    print('ValueError')

if oper == '+' or oper == '-' or oper == '*' or oper == '/':
    print('ok')
else:
    print('ne ok')
