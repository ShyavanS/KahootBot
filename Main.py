from KahootBot import KahootBot
from threading import Thread

threads = list()
pin = int(input("Please enter your Kahoot! game pin: "))
num = int(input("Please enter the number of bots you would like to join your game: "))
name = input("Please enter the prefix name for all your bots: ")

# Using exec to iterate the variable names and create multiple instances of bot
def createBot(i):
    exec("bot_" + str(i) + " = KahootBot()")
    exec("bot_" + str(i) + ".play(kahoot_nickname=f'{name}' + str(i), kahoot_pin=f'{pin}', is_realistic=False)")

# for loop that creates threads for each bot and makes each run in parallel
for i in range(num):
    print("Thread Started")
    t = Thread(target=createBot, args=(i,))
    threads.append(t)
    t.start()
