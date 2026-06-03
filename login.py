def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login Successful"
    return "Login Failed"

print(login("admin", "admin123"))