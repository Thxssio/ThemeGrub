#!/usr/bin/env python3
#          
#  ______ _    ___   __ _____ _____ _____ ____  
# |__   __| |  | \ \ / // ____/ ____|_   _/ __ \ 
#    | |  | |__| |\ V /| (___| (___   | || |  | |
#    | |  |  __  | > <  \___ \\___ \  | || |  | |
#    | |  | |  | |/ . \ ____) |___) |_| || |__| |
#    |_|  |_|  |_/_/ \_\_____/_____/|_____\____/ GRUB THEME
#
# Version: 2.1                    adapted by Thxssio (DEX)
#
# 
# Github : https://github.com/thxssio

# imports

import subprocess
import os
import shutil
import sys


# colors
C = "\033[0m"     # clear (end)
R = "\033[0;31m"  # red (error)
G = "\033[0;32m"  # green (process)
B = "\033[0;36m"  # blue (choice)
Y = "\033[0;33m"  # yellow (info)

# functions
def check_root():
    id = int(subprocess.check_output("id -u", shell=True).decode("utf-8"))
    if id != 0:
        print(f"\n{R}(!){C} Execute o script com privilégios 'sudo' ou como usuário root !!\n")
        exit()


def check_distro():
    try:
        lsb_id = subprocess.check_output("lsb_release -i", shell=True).decode("utf-8")
        id = lsb_id.split(":")[-1].lower().strip()
    except Exception:
        id = ""
    return id


def change_grub_theme(grub_theme_path):
    with open("/etc/default/grub", "r") as grub_file:
        data = grub_file.readlines()
        flag = False
        for i, line in enumerate(data):
            if line.startswith("GRUB_TERMINAL_OUTPUT"):
                data.pop(i)
                data.insert(i, f"#{line}\n")
            elif line.startswith("GRUB_TIMEOUT_STYLE"):
                data.pop(i)
                data.insert(i, f"#{line}\n")
            elif line.startswith("GRUB_ENABLE_BLSCFG"):
                data.pop(i)
                data.insert(i, "GRUB_ENABLE_BLSCFG=false\n")
            elif line.startswith("GRUB_THEME"):
                flag = True
                data.pop(i)
                data.insert(i, f'GRUB_THEME="{grub_theme_path}"\n')

        if not flag:
            data.append(f'GRUB_THEME="{grub_theme_path}"\n')

    with open("/etc/default/grub", "w") as grub_file:
        grub_file.writelines(data)


def reset_grub_theme():
    with open("/etc/default/grub", "r") as grub_file:
        data = grub_file.readlines()

        for i, line in enumerate(data):
            if line.startswith("GRUB_THEME"):
                data.pop(i)  # removing existing line
                # data.insert(i, f'#GRUB_THEME=""\n')  # adding new line

    with open("/etc/default/grub", "w") as grub_file:
        grub_file.writelines(data)


def prompt(choices):
    options = list(choices)
    while True:
        print(f"{B}(?){C} Choose an option [{options[0]}-{options[-1]}] : ", end="")
        choice = input().upper()
        if choice not in options:
            print(f"\n{R}(!){C} Select one of the available options !!\n")
            continue
        return choice


def banner():
    print(B)
    print(r"""  
    
 ________ __  ____   __ _____ _____ _____ ____  
 |__   __| |  | \ \ / // ____/ ____|_   _/ __ \ 
    | |  | |__| |\ V /| (___| (___   | || |  | |
    | |  |  __  | > <  \___ \\___ \  | || |  | |
    | |  | |  | |/ . \ ____) |___) |_| || |__| |
    |_|  |_|  |_/_/ \_\_____/_____/|_____\____/
    
    """,end="")
    print(f"{C} GRUB THEME\n")
    print(f"   adapted by {B}Thxssio{C} (DEX)")


def install():
    # installer script
    print("\n   INSTALLER ✔️")
    
    THEME = "darkmatter"

    # debian | arch
    if os.path.exists("/boot/grub/"):
        GRUB_THEMES_DIR = "/boot/grub/themes/"
        GRUB_UPDATE_CMD = "grub-mkconfig -o /boot/grub/grub.cfg"

        if not os.path.exists(GRUB_THEMES_DIR):
            os.mkdir(GRUB_THEMES_DIR)

    # fedora | redhat
    elif os.path.exists("/boot/grub2/"):
        GRUB_THEMES_DIR = "/boot/grub2/themes/"
        GRUB_UPDATE_CMD = "grub2-mkconfig -o /boot/grub2/grub.cfg"

        if not os.path.exists(GRUB_THEMES_DIR):
            os.mkdir(GRUB_THEMES_DIR)

    else:
        print(f"\n{R}(!){C} Não foi possível encontrar o diretório GRUB. Saindo do roteiro ...")
        exit()

    styles = {
        "1": "arch",
        "2": "archstrike",
        "3": "artix",     
        "4": "avix",      
        "5": "blackarch", 
        "6": "centos",    
        "7": "chromeos",  
        "8": "debian",    
        "9": "deepin",    
        "10": "devuan",
        "11": "elementary",
        "12": "endeavouros",
        "13": "fedora",
        "14": "freebsd",
        "15": "garuda",
        "16": "gentoo",
        "17": "kali",
        "18": "kdeneon",
        "19": "kubuntu",
        "20": "linux",
        "21": "linuxlite",
        "22": "linuxmint",
        "23": "lubuntu",
        "24": "manjaro",
        "25": "mx",
        "26": "opensuse",
        "27": "parrot",
        "28": "pentoo",
        "29": "popos",
        "30": "redhat",
        "31": "slackware",
        "32": "solus",
        "33": "sparky",
        "34": "steamos",
        "35": "ubuntu",
        "36": "ubuntumate",
        "37": "void",
        "38": "windows10",
        "39": "windows11",
        "40": "zorin",
        "41": "guixsd",
        "42": "nixos",
        "43": "xubuntu",
        "44": "dtos",
        "45": "nobara",
        "46": "hacking",
        "47": "hydrone",
    }

    print(f"\n{B}(?){C} \033[0;33mChoose the STYLE\033[0m :")

    style_sheet_menu = f"""
    (01)  Arch Linux   (02)  Arch Strike    (03)  Artix Linux
    (04)  Avix Linux   (05)  BlackArch      (06)  CentOS
    (07)  Chrome OS    (08)  Debian         (09)  Deepin
    (10)  Devuan       (11)  ElementaryOS   (12)  EndeavourOS
    (13)  Fedora       (14)  FreeBSD        (15)  Garuda Linux
    (16)  Gentoo       (17)  Kali Linux     (18)  KDE neon
    (19)  Kubuntu      (20)  Linux          (21)  Linux Lite
    (22)  Linux Mint   (23)  Lubuntu        (24)  Manjaro
    (25)  MX Linux     (26)  openSUSE       (27)  ParrotOS
    (28)  Pentoo       (29)  PopOS          (30)  Red Hat
    (31)  Slackware    (32)  Solus          (33)  Sparky Linux
    (34)  SteamOS      (35)  Ubuntu         (36)  Ubuntu Mate
    (37)  Void Linux   (38)  Windows 10     (39)  Windows 11
    (40)  ZorinOS      (41)  GuixSD         (42)  NixOS
    (43)  Xubuntu      (44)  DTOS           (45)  Nobara
    (46)  Hacking      (47)  Hydrone

    """
    print(style_sheet_menu)
    choice = prompt(styles.keys())

    THEME_DIR = f"{GRUB_THEMES_DIR}{THEME}/"

    if os.path.exists(THEME_DIR):
        print("\n")
        print(f"{Y}(#){C} Se você já tiver uma versão deste tema instalada, desinstale-a primeiro.\n")
        exit()
    else:
        os.mkdir(THEME_DIR)  # making the theme dir in '/boot/grub/themes'

    # selecting resolution
    print(f"\n{B}(?){C} Choose the RESOLUTION {Y}[default = 1]{C} :\n\n    (1) {G}1080p{C} {Y}[Full HD]{C}    (2) {G}1440p{C} {Y}[2K]{C}\n")
    icon_theme_choice = input(f"{B}(?){C} choice : ")
    if icon_theme_choice == "2":
        RESOLUTION = "1440p"
    else:
        RESOLUTION = "1080p"

    # selecting icon theme
    print(f"\n{B}(?){C} Choose the ICON THEME {Y}[default = 1]{C} :\n\n    (1) {G}Color{C} Icons     (2) {G}White{C} Icons\n")
    icon_theme_choice = input("choice : ")
    if icon_theme_choice == "2":
        ICON_THEME = "white"
    else:
        ICON_THEME = "color"

    # defining asset paths
    BACKGROUND_PATH = (f"assets/backgrounds/{styles.get(choice).lower()}-{RESOLUTION}.png")
    ICONS_PATH = f"assets/icons-{RESOLUTION}/{ICON_THEME}/"
    FONTS_PATH = f"assets/fonts/{RESOLUTION}/"
    BASE_PATH = f"base/{RESOLUTION}/"

    print(f"\n{G}($){C} Copying assets to {THEME_DIR}")
    # copying & renaming background img
    shutil.copy(BACKGROUND_PATH, f"{THEME_DIR}background.png")
    # copying & renaming icon pack
    shutil.copytree(ICONS_PATH, f"{THEME_DIR}icons/")  # 'icons' dir created inside main theme dir
    # copying font files
    shutil.copytree(FONTS_PATH, THEME_DIR, dirs_exist_ok=True)
    # copying base files
    shutil.copytree(BASE_PATH, THEME_DIR, dirs_exist_ok=True)
    print("    done.\n")
