USERS = {
    "admin": {"password": "admin123", "role": "IT"},
    "hr_user": {"password": "hr123", "role": "HR"},
    "sec_user": {"password": "sec123", "role": "SECURITY"}
}

def authenticate(username, password):
    user = USERS.get(username)

    if user and user["password"] == password:
        return {"username": username, "role": user["role"]}

    return None