class Savemoney():
    def __init__(self, name, money):
        self.name = name
        self.__money = money
    # @property
    # def money(self):
    #     return self.__money

    # @money.setter
    # def money(self, money):
    #     self.__money = money

    def __get_money(self):
        try:
            return self.__money
        except Exception:
            return "不存在了"
    
    def __set_money(self, money):
        self.__money = money
    
    def __del_money(self):
        del self.__money
        
    money = property(__get_money, __set_money, __del_money)

if __name__ == "__main__":
    # pass
    save_m = Savemoney("chan", 3000)
    print(save_m.money)
    save_m.money = 10000
    print(save_m.money)
    del save_m.money
    print(save_m.money)