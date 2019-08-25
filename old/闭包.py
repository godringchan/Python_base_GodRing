def fun_1():
    a = 1

    def print_fun():
        print(a)
    return print_fun

if __name__ == "__main__":
    
    func = fun_1()
    func()
    # func()
    fun_1()()
    fun_1()
