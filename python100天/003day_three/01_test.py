import getpass
name = input("请输入用户名")
# getpass和input的使用方法差不多，getpass在终端输入时不显示输入的内容
password = getpass.getpass("请输入密码")

if name == "admin" and password == "123456":
    print("验证成功")
else:
    print("验证失败")
