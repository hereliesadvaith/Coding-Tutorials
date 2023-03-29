num = 10


def print_global_num():
    print(num)


print_global_num()


def print_num():
    num = 20
    print(num)


def print_nu():
    global num
    num = 30
    print(num)


print_nu()
print_global_num()
print_num()
