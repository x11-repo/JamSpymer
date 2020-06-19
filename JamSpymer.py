import os
import time
import sys
from colorama import Style, Back, Fore


def yes():
    os.system("cls")
    os.system("clear")
    print(
        f"""
{Fore.RED} Jam{Fore.BLUE}Spymer
{Fore.GREEN}Выберите ОС:
{Fore.GREEN}1.{Style.RESET_ALL} Android
{Fore.GREEN}2.{Style.RESET_ALL} Windows
{Fore.GREEN}3.{Style.RESET_ALL} Unix
{Fore.GREEN}4.{Style.RESET_ALL} Mac OS
	"""
    )

    oss = input("@ > ")

    if oss == "1":
        from core import android
    elif oss == "2":
        from core import other
    elif oss == "3":
        from core import other
    elif oss == "4":
        from core import other
    else:
        print(f"{Fore.RED}Введено некорректоное значение.{Style.RESET_ALL}")
        time.sleep(3)
        yes()


def no():
    os.system("cls")
    os.system("clear")
    print(
        f"""
{Fore.RED} Jam{Fore.BLUE}Spymer
{Fore.GREEN}Выберите ОС:
{Fore.GREEN}1.{Style.RESET_ALL} Android
{Fore.GREEN}2.{Style.RESET_ALL} Windows
{Fore.GREEN}3.{Style.RESET_ALL} Unix
{Fore.GREEN}4.{Style.RESET_ALL} Mac OS
	"""
    )

    oss = input("@ > ")

    if oss == "1":
        os.system(
            "pkg update && pkg upgrade && pkg install pip && pkg install python3-pip && pip install colorama requests fake_useragent"
        )
        from core import android
    elif oss == "2":
        os.system(
            "apt update && apt upgrade && apt install pip && pkg install python3-pip && pip install colorama requests fake_useragent"
        )
        from core import windows
    elif oss == "3":
        os.system(
            "apt update && apt upgrade && apt install pip && pkg install python3-pip && pip install colorama requests fake_useragent"
        )
        from core import unix
    elif oss == "4":
        os.system(
            "brew update && brew upgrade && apt install pip && pkg install python3-pip && pip install colorama requests fake_useragent"
        )
        from core import macos
    else:
        print(f"{Fore.RED}Введено некорректоное значение.{Style.RESET_ALL}")
        time.sleep(3)
        no()


def main():
    os.system("cls")
    os.system("clear")
    q = Fore
    print(
        f"""
У Вас установленны все зависимости?
{q.GREEN}1.{Style.RESET_ALL} Да
{q.GREEN}2.{Style.RESET_ALL} Нет
{q.GREEN}3.{Style.RESET_ALL} Не знаю
{q.RED}99.{Style.RESET_ALL} Выход
	"""
    )
    zavis = input("@ > ")
    if zavis == "1":
        yes()
    elif zavis == "2":
        no()
    elif zavis == "3":
        print("Если вы не знаете, установленны ли у Вас все зависимости, нажмите '2'")
        time.sleep(3)
        main()
    elif zavis >= "99":
        exit()
    else:
        print(f"{Fore.RED}Введено некорректоное значение.{Style.RESET_ALL}")
        time.sleep(3)
        main()


main()
