msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
result = 'not set'


def last_func():
    while True:
        print(msg_5)
        answer = input()
        if answer == 'y':
            return
        elif answer == 'n':
            return answer


def test_func():
    memory = 0
    while True:
        print(msg_0)
        try:
            x, oper, y = input().split()
            if x != 'M':
                x = float(x)
            else:
                x = memory
            if y != 'M':
                y = float(y)
            else:
                y = memory
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
                    while True:
                        print(msg_4)
                        answer = input()
                        if answer == 'y':
                            memory = result
                            answer = last_func()
                            break
                        elif answer == 'n':
                            answer = last_func()
                            break
                        break
                    if answer == 'n':
                        break
                    continue
            print(msg_2)


test_func()

