msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
result = 'not set'


def is_one_digit(v):
    try:
        int(v)
        v = str(v)
        if len(v) == 1 and v.isnumeric():
            output = True
        else:
            output = False
    except:
        output = False
    return output
    #  из функции ожидается вывод где-то далее


def check_lazy(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg = msg + msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)


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
                if x.isnumeric() == True:
                    x = int(x)
                else:
                    x = float(x)
            else:
                x = memory
            if y != 'M':
                if y.isnumeric() == True:
                    y = int(y)
                else:
                    y = float(y)
            else:
                y = memory
        except (TypeError, ValueError):
            print(msg_1)
        else:
            if oper in {'+', '-', '/', '*'}:
                v1, v2, v3 = x, y, oper
                check_lazy(v1, v2, v3)
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
                    print(float(result))
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


