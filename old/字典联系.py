import random, socket
a = 5
while a > 0:

    dict1 = {1: "a", 2: "b", 3: "c"}
    random_num = random.randint(1, 3)
    print(dict1[random_num])
    a -= 1
b_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
