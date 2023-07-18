#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2023 formaldehyde_701

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TO OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ######################################
# Author  : formaldehyde_701           #
# Project : IP_GURU                    #
# Type    : IP_Searching(osint)        #
#                                      #
# language: python v3.* (py3)          #
# Owner   : NATHANS pref: formaldehyde #
# ######################################

import urllib.request
import json
import os
import sys
import webbrowser
try:
    import colorama
except ModuleNotFoundError:
    os.system('pip install colorama')
from colorama import Fore
import socket
import time
R = Fore.RED
G = Fore.GREEN
B = Fore.BLUE
C = Fore.CYAN
L = Fore.LIGHTCYAN_EX
M = Fore.MAGENTA
Y = Fore.YELLOW
m = Fore.LIGHTMAGENTA_EX
bld = colorama.Style.BRIGHT


def sprint(string):
    for i in string:
        print(i, end="", flush=True)
        time.sleep(0.009)


def check_python_version():
    if sys.version_info[0] != 3:
        sprint(f"{bld}{L}You are using python version {sys.version_info[0]} "
               f"which is not compatible with this program\n")
        sys.exit()
    else:
        sprint(f"{bld}{L}Your version of python is compatible\n\n")


def search_for_ip(url):
    try:
        try:
            response = urllib.request.urlopen(url)
            data = json.load(response)
            b"""
            Analysing the data
            obtained from the api request
            """
            ip = data['query']
            planet = 'earth'
            continent = data.get('continent', 'Not Found')
            continent_code = data.get('continentCode', 'Not Found')
            country = data.get('country', 'Not Found')
            country_code = data.get('countryCode', 'Not Found')
            region = data.get('region', 'Not Found')
            region_name = data.get('regionName', 'Not Found')
            city = data.get('city', 'Not Found')
            district = data.get('district', 'Not Found')
            zip_code = data.get('zip', 'Not Found')
            timezone = data.get('timezone', 'Not Found')
            currency = data.get('currency', 'Not Found')
            isp = data.get('isp', 'Not Found')
            organization = data.get('org', 'Not Found')
            reverse = data.get('reverse', 'Not Found')
            anonymity = data.get('proxy', 'Not Found')
            as_number = data.get('as', 'Not Found')
            as_name = data.get('asname', 'Not Found')
            mobile = data.get('mobile', 'Not Found')
            longitude = data.get('lon', 'Not Found')
            latitude = data.get('lat', 'Not Found')
            device_name = socket.gethostname()
            device_ip = socket.gethostbyname(device_name)
            print(f'{bld}{B}-{L}*{B}------{Y}YOUR DEVICE INFO{B}------{L}*{B}-\n')
            print(f'{bld}{L}|  {M}Device name {Y}:-{G} {device_name}{L}|\n')
            print(f'{bld}{L}|  {M}Device IP   {Y}:-{G} {device_ip}  {L}|\n')
            print(f'{bld}{L}|                              |\n')
            print(f'{bld}{B}-{L}*{Y}----------------------------{L}*{B}-\n')
            print('\n')
            print(f'{bld}{R}-*------------------------------------*-\n')
            print(f'{bld}{L}|--------{B}*{Y}LOCATION INFORMATION{B}*{L}---------\n')
            print(f'{bld}{L}| {m}IP address                    {Y}:- {G}{ip}\n')
            print(f'{bld}{L}| {m}Planet                        {Y}:- {G}{planet}\n')
            print(f'{bld}{L}| {m}Continent                     {Y}:- {G}{continent}\n')
            print(f'{bld}{L}| {m}Two letter continent code     {Y}:- {G}{continent_code}\n')
            print(f'{bld}{L}| {m}Country                       {Y}:- {G}{country}\n')
            print(f'{bld}{L}| {m}Two letter country code       {Y}:- {G}{country_code}\n')
            print(f'{bld}{L}| {m}City                          {Y}:- {G}{city}\n')
            print(f'{bld}{L}| {m}Region                        {Y}:- {G}{region}\n')
            print(f'{bld}{L}| {m}Region Name                   {Y}:- {G}{region_name}\n')
            print(f'{bld}{L}| {m}District                      {Y}:- {G}{district}\n')
            print(f'{bld}{L}| {m}ZIP code                      {Y}:- {G}{zip_code}\n')
            print(f'{bld}{L}| {m}Organization                  {Y}:- {G}{organization}\n')
            print(f'{bld}{L}| {m}Time Zone                     {Y}:- {G}{timezone}\n')
            print(f'{bld}{L}| {m}Currency                      {Y}:- {G}{currency}\n')
            print(f'{bld}{L}| {m}Latitude                      {Y}:- {G}{latitude}\n')
            print(f'{bld}{L}| {m}Longitude                     {Y}:- {G}{longitude}\n')
            print(f'{bld}{L}| {m}AS number                     {Y}:- {G}{as_number}\n')
            print(f'{bld}{L}| {m}AS number and organization    {Y}:- {G}{as_name}\n\n')
            print(f'{bld}{L}| -------{R}*{Y}NETWORK INFORMATION{R}*{L}----------')
            print(f'{bld}{L}| {M}AS number and organization    {Y}:- {G}{as_name}\n')
            print(f'{bld}{L}| {M}Internet service provider     {Y}:- {G}{isp}\n')
            print(f'{bld}{L}| {M}TOR, VPN or Proxy             {Y}:- {G}{anonymity}\n')
            print(f'{bld}{L}| {M}Mobile or cellular connection {Y}:- {G}{mobile}\n\n')
            print(f'{bld}{L}| {B}----------------{L}*{Y}OTHER{L}*{B}---------------')
            print(f'{bld}{L}| {M}Reverse DNS lookup for host   {Y}:- {G}{reverse}\n\n\n')

            print(f'*-GOOGLE MAPS-*')
            link = f'https://www.google.com/maps/place/{latitude}+{longitude}'
            print(link)
            open_link = str(input(f'\n{L}Open link in browser ?Use"y","Y","n"or"N"\n>>>---'))
            if open_link == 'y' or open_link == 'Y' or open_link == '':
                try:
                    webbrowser.open(link)
                except ConnectionAbortedError:
                    os.system(f'xdg-open {link}')
            elif open_link == 'n' or open_link == 'N':
                pass
            else:
                pass
        except KeyError as e:
            sprint(f'{R}Exception occurred: {Y}{e}')
    except ConnectionError:
        print(f"{m}Connection error, check your internet")


def main():
    try:
        os.system('clear')
    except KeyError:
        os.system('cls')
    check_python_version()
    logo = fr"""{bld}
    {Y}-*----------------------------------------------------*-
    {R}$$$$\  $$$$$$\    $$$$$\  $$|    $$| $$$$$$\  $$|    $$|
     {R}$$|   $$   $$|  $$  ___  $$|    $$| $$|_ $$| $$|    $$|
     {R}$$|   $$$$$ /   $$| $$$| $$\    $$| $$$$$\   $$\    $$/
    {R}$$$$\  $$|        $$$$$ /   $$$$  /  $$  $$$|   $$$$ /
    {Y}____/ ___/        _____/    _____/   _/  __/     ___/
    {L}           AUTHOR {Y}:- {m}formaldehyde-701
    {L}           IG     {Y}:- {m}formaldehyde_701
    {Y}-*----------------------------------------------------*-
    """
    sprint(logo)
    menu = f"""{bld}
    {C}[{B}1{C}]{G}Check your IP information\n
    {C}[{B}2{C}]{G}Check other IP information\n
    {C}[{B}3{C}]{G}Exit\n
    """
    sprint(menu)
    try:
        choice = int(input(f'{Y}::>>>- '))
        if choice == 1:
            try:
                os.system('clear')
            except KeyError:
                os.system('cls')
            url = f"http://ip-api.com/json/"
            search_for_ip(url)
        elif choice == 2:
            try:
                os.system('clear')
            except KeyError:
                os.system('cls')
            ip = str(input(f"{m}Enter the IP address {Y}:- "))
            url = f"http://ip-api.com/json/{ip}"
            search_for_ip(url)
        elif choice == 3:
            try:
                os.system('clear')
            except KeyError:
                os.system('cls')
            sprint("Bye you legend")
            sys.exit()
        else:
            sprint(f'{R}Invalid option')
            main()
    except TypeError as e:
        sprint(f"{Y}Exception occurred:\n{R}{e}\n")
        main()


if __name__ == '__main__':
    main()
