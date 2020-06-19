# -*- coding: utf-8 -*-
# ИДИ НАХУЙ ОТ МОЕГО ГОВНОКОДА ГОВНЮК
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

    xxx = 3
    loading = 0
    for xxx in range(xxx):
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
        loading = loading + 1
        if loading == 1:
            print(f"\n\nПрогрузка модулей: {g}####{sr} 20%")
        elif loading == 2:
            print(f"\n\nПрогрузка модулей: {g}############{sr} 60%")
        elif loading == 3:
            print(f"\n\nПрогрузка модулей: {g}####################{sr}  100%")
        time.sleep(1)

    now = datetime.datetime.now()
    times = now.strftime("%H:%M")
    new = input(
        f"""{r}╭━━━{g}[x11repo | {r1}Jam{r2}Spymer{g}]
{r}┃
{r}╰━━━[{sr}{times}{r}]━━━> {sr}"""
    )

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

else:
    print("Введен неверный код.")
    pass
