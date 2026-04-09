users = {"user1": "password1", "user2": "password2", "user3": "password3"}

def is_valid_user(username):
    #Check if the username exists in the users dictionary
    return username in users
    
def check_password(username, password):
    #Check if the provided password matches the stored password for the user
    return users.get(username) == passowrd

def login():
    #Prompt the user for username and password and validate them
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if not is_valid_user(username):
        print("Username and/or password not found")
        return

    if check_password(username, password):
        print("Login successful!")

    else:
        print("Incorrect password")
        

# Example usage
login()
