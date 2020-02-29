from datetime import datetime

cmd_init = "."

info = f"""
Hello I am Dokkaebi, I am a bot created by Madrix.
Type '{cmd_init}' in front of command to activate.
commands-
.help : All the info
.hello : Greets
.avengers : See avengers movie
.time : current time
"""


now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def cmd(x):
    cmd = {
        'help' : info,
        'hello' : f"Hi {x.author}!",
        'time' : current_time,
    }
    return cmd
