import time, sys
message = "fool you are, you know, you know!"
#This creates a loop in which it iterates over the message, and sleeps for a short duration before typing the next character, providing a typewriter aesthetic
def typewrite(message, delay_between_char = 0.01):
    """This will take a provided message
    and a supplied time (in seconds) which it will wait for between typing letters"""
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay_between_char)
    #Print an empty line to reduce the need for \n after every typewrite()
    print()

typewrite(message, 0.03)