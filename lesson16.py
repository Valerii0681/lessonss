while True:
    username1 = input("name1:")
    username2 = input("name2:")
    passwordOne = input("password 1:")
    passwordTwo = input("password 2:")
    a = True
    if len(passwordOne)<8:
        a = False
        print("Короткий")
    if username1 !=username2:
        a = False
        print("Различаются")
    if passwordOne != passwordTwo:
        a = False
        print("Различаются")
    if "123" in passwordOne:
        a = False
        print("Простой")
    if a:
        break
print("OK")