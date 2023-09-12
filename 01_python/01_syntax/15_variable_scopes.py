num = 10

def print_global_num():
    print(num)

def print_num():
    num = 20
    print(num)

def print_num2():
    # to change num globally import global num and then change it
    global num
    num = 30
    print(num)

print_global_num() # 10
print_num() # 20
print_global_num() # 10
print_num2() # 30
print_global_num() # 30
