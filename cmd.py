info = f"""
Hello I am Hibana, I am a bot created by Madrix.
Commands-
    !help : All the info
    !hello : Greets
    !roll <No.> : Guessing game 
    !roles : view all the roles 
    !gif <query> : gif in chat 
"""


def check_role(arr):
    for i in range(len(arr)):
        if arr[i] == "Developer":
            return True
        else:
            return False