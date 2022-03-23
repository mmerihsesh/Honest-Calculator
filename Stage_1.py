msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
result = 'not set'


def test_func():
    while True:
        print(msg_0)
        try:
            x, oper, y = input().split()
            x = float(x)
            y = float(y)
        except (TypeError, ValueError):
            print(msg_1)
        else:
            if oper in {'+', '-', '/', '*'}:
                if oper == '+':
                    result = x + y
                elif oper == '-':
                    result = x - y
                elif oper == '*':
                    result = x * y
                elif oper == '/' and y != 0:
                    result = x / y
                else:
                    print(msg_3)
                    continue
                if result != 'not set':
                    print(result)
                    break
            print(msg_2)


test_func()
