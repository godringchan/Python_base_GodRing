import io
s = "hello, python"
sio = io.StringIO(s)
ssi = sio.getvalue()
sio.seek(5)
sio.write(",love,python")
ssi = sio.getvalue()
print(ssi)


a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(c)
print(id(a))
print(id(b))
print(id(c))
