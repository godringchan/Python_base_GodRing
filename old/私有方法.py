class Aa():
    cou = "chi"
    # def change(self):
    #     __class__.cou = "bb"
    def set_aa(self):
        print(self.cou)
ba = Aa()
# aa.change()
print(id(ba.__class__.cou))
print(id(ba.cou))
ba.set_aa()
print(ba.cou)
print(id(Aa.cou))