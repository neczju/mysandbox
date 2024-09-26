from bs4 import BeautifulSoup
import requests
import os
import re


def get_version():
    VERSIONS = ['beta_OptiFine_1.8.1_HD_D2', 'beta_OptiFine_1.7.3_HD_G',
                'beta_OptiFog_Optimine_1.7.2_HD',
                'beta_OptiFog_Optimine_1.6.6_F_HD',
                'beta_OptiFog_1.5_01_F']

    while True:
        print('What version you want to download?')
        for i in range(len(VERSIONS)):
            print(str(i + 1) + '. ' + VERSIONS[i])
        print('> ', end='')
        inp = int(input())
        if inp in range(len(VERSIONS)):
            return VERSIONS[inp]
            break
        else:
            print('Version not found!')


def get_download_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    soup = str(soup)
    download_regex_1 = re.compile(r'downloadx([a-zA-Z0-9_.?=])+')
    download_regex_2 = re.compile(r'x=([a-z0-9])+')
    download_url_piece = []
    # TODO: Nie wiem kurwa requests zwraca amp; XDXDXDXD
    for groups in 
    print(download_url_piece)
    base_url = 'https://optifine.net/'
    return base_url + str(download_url_piece)


def download(url, path):
    response = requests.get(url)
    with open(path, mode="wb") as file:
        file.write(response.content)


DOWNLOAD_DIR = 'downloads/'
postfix = '.zip'

if not os.path.exists(DOWNLOAD_DIR):
    os.mkdir(DOWNLOAD_DIR)


optifine_files_url = 'https://optifine.net/adloadx?f='
version = get_version()
url = optifine_files_url + version + postfix
download_path = DOWNLOAD_DIR + version + postfix

download_url = get_download_url(url)
download(download_url, download_path)
