import time
from colorama import Fore


def print_img_info(index, degs, mins, img_time, dist, angle, d_time):
    print(
        f'{Fore.GREEN}№={Fore.RESET}{index}:\
        \n  {Fore.GREEN}data-in:{Fore.RESET}\
        \n    {Fore.CYAN}degs/mins: {Fore.RESET}{degs}°{mins}\'\
        \n    {Fore.CYAN}time: {Fore.RESET}{time.asctime(img_time)}\
        \n  {Fore.GREEN}data-out:{Fore.RESET}\
        \n    {Fore.CYAN}dist btw hor&sun: {Fore.RESET}{dist}px\
        \n    {Fore.CYAN}horizon angle: {Fore.RESET}{angle}°\
        \n    {Fore.CYAN}Δtime: {Fore.RESET}{d_time}s'
    )


def print_end_info(end_time):
    print(f'{Fore.CYAN}time spent: {Fore.RESET}{end_time}s')
