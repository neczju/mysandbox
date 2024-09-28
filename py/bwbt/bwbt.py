#! python3
# bwbt.py -- tool for backing up my minecraft beta and bta worlds

import subprocess
import time
import os
import sys
import shutil

home_dir = os.environ['HOME']
target_dir = 'backups'

if len(sys.argv) < 2:
    print('Type an argument!')
    sys.exit()

argument = sys.argv[1]

world_dir = ['/.var/app/org.prismlauncher.PrismLauncher/data/PrismLauncher/instances/b1.7.3/.minecraft/saves/',
             '/.var/app/org.prismlauncher.PrismLauncher/data/PrismLauncher/instances/bta_babric_instance_7.2_01/.minecraft/saves/']

if argument == 'beta': # beta backup
    source_dir = home_dir + world_dir[0]
    backup_filename = 'beta_worlds'
elif argument == 'bta': # better than adventure backup
    source_dir = home_dir + world_dir[1]
    backup_filename = 'bta_worlds'
else:
    print('No argument named ' + argument + '!')
    sys.exit()


# check if target directory not exist
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# checks if source direcotry exist and creates backup with current localtime
if os.path.exists(source_dir):
    localtime_format = time.strftime('_%d_%m_%Y_%H_%M_%S', time.localtime())
    os.chdir(target_dir)
    shutil.make_archive(backup_filename + localtime_format, 'zip', source_dir) # makes zip archive file of saves directory
else:
    print('Source directory does not exist :(')
