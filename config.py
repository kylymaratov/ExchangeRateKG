import sys

TOKEN = None
WEBHOOK_MODE = True
WEBHOOK_HOST = ''
WEBHOOK_PORT = 8001
WEBHOOK_LISTEN = "localhost"

try:
    r_file = open("token.txt", "r")
    TOKEN = r_file.read()
except:
    TOKEN = input("Peste bot token: ")
    file = open("token.txt", "a")
    file.write(TOKEN)
    file.close()

open("logger.log", "w").close()
