import os
import time
import sys
from colorama import Style, Back, Fore


def main():
    os.system("cls")
    os.system("clear")
    print(
        f"""{Fore.RED} Jam{Fore.BLUE}Spymer
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
        main()
main()
