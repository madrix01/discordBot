info = f"""
Hello I am Hibana, I am a bot created by Madrix.
Commands-
    !helpme : All the info
    !hello : Greets   
"""


def check_role(arr):
    for i in range(len(arr)):
        if arr[i] == "Developer":
            return True
        else:
            return False