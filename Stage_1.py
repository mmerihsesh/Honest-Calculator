msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"


def test_func():
    while True:
        print(msg_0)
        try:
            x, oper, y = input().split()
            float(x)
            float(y)
        except (TypeError, ValueError):
            print(msg_1)
        else:
            if oper in {'+', '-', '/', '*'}:
                break
            print(msg_2)

test_func()
