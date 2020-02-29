info = "fuck off!"
cmd_init = "."

def cmd(x):
    cmd = {
        'help' : info,
        'hello' : f"Hi {x.author}!"
    }
    return cmd