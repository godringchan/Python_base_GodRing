class Savemoney():
    def __init__(self, name, money):
        self.name = name
        self.__money = money
    
    def show_money(self):
        print(self.__money)            # 类内部的方法，可以访问内部私有属性


save_money = Savemoney("haoren", 3000)
save_money.show_money()
print(save_money._Savemoney__money)     #     python的私有方法并不是真正的私有方法，只是偷偷改了变量名
# print(save_money.__money)# 外部不能访问私有属性
