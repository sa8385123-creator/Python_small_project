def login(username, password):
    username = username.strip()
    password = password.strip()

    if username == "":
        return "Username required"

    if password == "":
        return "Password required"

    if username.lower() != "admin":
        return "Invalid Username"

    if password != "1234":
        return "Invalid Password"

    return "Login Successful"


message=login("admin","1234 ")
print(message)



