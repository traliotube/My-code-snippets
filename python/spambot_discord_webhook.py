from os import system
from discord_webhook import DiscordWebhook
import time

webhook_url = input("Enter URL of the webhook")


def send_webhook(msg):
    webhook = DiscordWebhook(
        url=webhook_url, content=msg)
    response = webhook.execute()


def spam_spamtext():
    print("go to the window to spam")

    print("Countdown to type starts now!!")
    time_countdown = 5
    while(time_countdown != 0):
        print(time_countdown)
        time.sleep(1)
        time_countdown -= 1
    print("Start  Spamming!!")

    spamtext_file = open("spamtext", "r")

    for word in spamtext_file:
        send_webhook(word)


def repeat_text():
    msg_to_repeat = input("Enter the message: ")
    times_to_repeat = input("How many times ?: ")

    print("Countdown to type starts now!!")
    time_countdown = 5
    while(time_countdown != 0):
        print(time_countdown)
        time.sleep(1)
        time_countdown -= 1
    print("Start  Spamming!!")

    for i in range(0, int(times_to_repeat)):
        send_webhook(msg_to_repeat)


while True:
    print("Chose which type to spam \n 1.Repeat same text multiple times \n 2. Type text from spamtext file \n 3. Exit")
    FuncToRun = input()
    if FuncToRun == "1":
        repeat_text()
    elif FuncToRun == "2":
        spam_spamtext()
    else:
        system.exit()
