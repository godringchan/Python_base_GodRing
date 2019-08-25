for i  in range(1346):
    a = str(i)
    if i == 15:
        break
    elif a.endswith("3") or a.endswith("4") or a.endswith("5"):
        continue
    # elif i == 15:
    #     break
    print(i)
