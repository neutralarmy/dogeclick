from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import (
    GetHistoryRequest,
    GetBotCallbackAnswerRequest,
)
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError
from time import sleep
import json, re, sys, os


try:
    import webbrowser
    import requests
    from bs4 import BeautifulSoup
except:
    print(
        "\033[1;30m# \033[1;31mHmmm Sepertinya Modul Requests Dan Bs4 Belum Terinstall\n\033[1;30m# \033[1;31mTo install Please Type pip install requests and pip install bs4"
    )
    sys.exit



c = requests.session()

for i in range(5000000):
        sys.stdout.write("\r")
        sys.stdout.write("\033[1;30m#\n\033[1;33m ☑ DOGE CLICKBOT UPDATED VERSION 1.0")
        sys.stdout.flush() 
        sleep(2)
        os.system("clear")
        break
os.system("termux-open-url  https://youtube.com/channel/UC3fHZuhmvtEFpW5h_ia0hCg ")


banner = """\033[0;35m   
\033[0;36m✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘   
                                                              
░ █▄  █ █▀▀ █  █ ▀▀█▀▀ █▀▀█ █▀▀█ █   　  
░ █ █ █ █▀▀ █  █   █   █▄▄▀ █▄▄█ █   　  
░ █  ▀█ ▀▀▀ ▀▀▀▀   ▀   ▀ ▀▀ ▀  ▀ ▀▀▀ 　  

       █▀▀█ █▀▀█ █▀▄▀█ █  █ ░
       █▄▄█ █▄▄▀ █ ▀ █ █▄▄█ ░
       █  █ ▀─▀▀ ▀   ▀ ▄▄▄█ ░

\033[0;36m✘✘✘✘✘✘✘✘✘✘✘ [BORN TO HACK] ✘✘✘✘✘✘✘✘✘✘

\033[1;32m🔷Script Credit \033[1;31m   :\033[1;0m Neutral Army
\033[1;32m🔷Telegram Channel \033[1;31m:\033[1;0m @Neutralarmy
\033[1;32m🔷Telegram Group\033[1;31m   : \033[1;0m@Neutralarmydiscuss
\033[1;32m🔷Youtube Channel\033[1;31m  :\033[1;0m @Neutral Army
\n\033[1;32m❒❒❒❒❒❒❒❒❒❒❒ [DOGE CLICK BOT] ❒❒❒❒❒❒❒❒❒\n\n"""
if not os.path.exists("session"):
    os.makedirs("session")

print(banner)
if len(sys.argv) < 2:
    print("\n\n\n\033[1;32mUsage : python doge.py  Your no. with country code")
    sys.exit(1)




def OpenLink(link): 
        os.system("termux-open-url https://youtube.com/channel/UCDzqxaxNWu-0swkFpk7PtiQ")

def tunggu(x):
    sys.stdout.write("\r")
    sys.stdout.write("                                                               ")
    for remaining in range(x, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write(
            "\033[1;30m#\033[1;0m{:2d} \033[1;32mseconds remaining".format(remaining)
        )
        sys.stdout.flush()
        sleep(1)


ua = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"
}


api_id = 5785894
api_hash = "3bbd832921adc222850990108fc9cb39"
phone_number = sys.argv[1]

client = TelegramClient("session/" + phone_number, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    try:
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number, input("\n\n\n\033[1;0mEnter Your OTP received in Telegram: "))
    except SessionPasswordNeededError:
        passw = input("\033[1;0mEnter Your 2fa Password : ")
        me = client.start(phone_number, passw)
myself = client.get_me()
os.system("clear")
print(banner)
print(
    "\033[1;31m ➢️ Welcome  User\033[1;0m:",
    myself.first_name,
    "\n\033[1;0m ➢ [Doge Click bot is running Now]",
)


#password()
print("\n\n\033[1;37mTask: Auto Visit   ")
try:
    channel_entity = client.get_entity("@Dogecoin_click_bot")
    channel_username = "@Dogecoin_click_bot"
    for i in range(5000000):
        sys.stdout.write("\r")
        sys.stdout.write(
            "                                                              "
        )
        sys.stdout.write("\r")
        sys.stdout.write("\033[1;30m# \033[1;33mVisiting Url")
        sys.stdout.flush()
        client.send_message(entity=channel_entity, message="🖥 Visit sites")
        sleep(3)
        posts = client(
            GetHistoryRequest(
                peer=channel_entity,
                limit=1,
                offset_date=None,
                offset_id=0,
                max_id=0,
                min_id=0,
                add_offset=0,
                hash=0,
            )
        )
        if (
            posts.messages[0].message.find("Sorry, there are no new ads available")
            != -1
        ):
            print("\n\033[1;30m# \033[1;31mNo site remains to visit❌\n")
            client.send_message(entity=channel_entity, message="💰 Balance")
            sleep(5)
            posts = client(
                GetHistoryRequest(
                    peer=channel_entity,
                    limit=1,
                    offset_date=None,
                    offset_id=0,
                    max_id=0,
                    min_id=0,
                    add_offset=0,
                    hash=0,
                )
            )
            message = posts.messages[0].message
            print(message)
            sys.exit()
        else:
            try:
                url = posts.messages[0].reply_markup.rows[0].buttons[0].url
                sys.stdout.write("\r")
                sys.stdout.write("\033[1;30m# \033[1;33mVisit " + url)
                sys.stdout.flush()
                os.system("termux-open-url \""+url+"\"")
                id = posts.messages[0].id
                r = c.get(url, headers=ua, timeout=15, allow_redirects=True)
                soup = BeautifulSoup(r.content, "html.parser")
                if (
                    soup.find("div", id="headbar") is None
                ):
                    sleep(2)
                    posts = client(
                        GetHistoryRequest(
                            peer=channel_entity,
                            limit=1,
                            offset_date=None,
                            offset_id=0,
                            max_id=0,
                            min_id=0,
                            add_offset=0,
                            hash=0,
                        )
                    )
                    message = posts.messages[0].message
                    if (
                        posts.messages[0].message.find("You must stay") != -1
                        or posts.messages[0].message.find("Please stay on") != -1
                    ):
                        sec = re.findall(r"([\d.]*\d+)", message)
                        tunggu(int(sec[0]))
                        sleep(1)
                        posts = client(
                            GetHistoryRequest(
                                peer=channel_entity,
                                limit=2,
                                offset_date=None,
                                offset_id=0,
                                max_id=0,
                                min_id=0,
                                add_offset=0,
                                hash=0,
                            )
                        )
                        messageres = posts.messages[1].message
                        sleep(2)
                        sys.stdout.write("\r\033[1;30m# \033[1;32m" + messageres + "\n")
                    else:
                        pass

                elif soup.find("div", id="headbar") is not None:
                    for dat in soup.find_all("div", class_="container-fluid"):
                        code = dat.get("data-code")
                        timer = dat.get("data-timer")
                        tokena = dat.get("data-token")
                        tunggu(int(timer))
                        r = c.post(
                            "https://dogeclick.com/reward",
                            data={"code": code, "token": tokena},
                            headers=ua,
                            timeout=15,
                            allow_redirects=True,
                        )
                        js = json.loads(r.text)
                        sys.stdout.write(
                            "\r\033[1;30m# \033[1;32mYou earned "
                            + js["reward"]
                            + " Doge for visiting a site!\n"
                        )
                else:
                    sys.stdout.write("\r")
                    sys.stdout.write(
                        "                                                                "
                    )
                    sys.stdout.write("\r")
                    sys.stdout.write("\033[1;30m# \033[1;31mCaptcha Detected")
                    sys.stdout.flush()
                    sleep(2)
                    client(
                        GetBotCallbackAnswerRequest(
                            channel_username,
                            id,
                            data=posts.messages[0].reply_markup.rows[1].buttons[1].data,
                        )
                    )
                    sys.stdout.write(
                        "\r\033[1;30m# \033[1;31mSkiping Captcha...!       \n"
                    )
                    sleep(2)
            except:
                sleep(3)
                posts = client(
                    GetHistoryRequest(
                        peer=channel_entity,
                        limit=1,
                        offset_date=None,
                        offset_id=0,
                        max_id=0,
                        min_id=0,
                        add_offset=0,
                        hash=0,
                    )
                )
                message = posts.messages[0].message
                if (
                    posts.messages[0].message.find("You must stay") != -1
                    or posts.messages[0].message.find("Please stay on") != -1
                ):
                    sec = re.findall(r"([\d.]*\d+)", message)
                    tunggu(int(sec[0]))
                    sleep(1)
                    posts = client(
                        GetHistoryRequest(
                            peer=channel_entity,
                            limit=2,
                            offset_date=None,
                            offset_id=0,
                            max_id=0,
                            min_id=0,
                            add_offset=0,
                            hash=0,
                        )
                    )
                    messageres = posts.messages[1].message
                    sleep(2)
                    sys.stdout.write("\r\033[1;30m# \033[1;32m" + messageres + "\n")
                else:
                    pass

finally:
    client.disconnect()