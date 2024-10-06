#! python3
# bwbt.py -- tool for backing up my minecraft beta and bta worlds

import time
from pathlib import Path
import os
import sys
import shutil

home_dir = Path.home()
target_dir = 'backups'

if len(sys.argv) < 2:
    print('Type an argument!')
    sys.exit()

argument = sys.argv[1]

world_dir = { 'beta': '.var/app/org.prismlauncher.PrismLauncher/data/PrismLauncher/instances/b1.7.3/.minecraft/saves/', 
             'bta': '.var/app/org.prismlauncher.PrismLauncher/data/PrismLauncher/instances/bta_babric_instance_7.2_01/.minecraft/saves/' }

# checks if argument is in dictionary
if argument in world_dir:
    source_dir = Path(home_dir / world_dir[argument])
    backup_filename = argument
else:
    print('No argument named ' + argument + '!')
    sys.exit()

# check if target directory not exist
if not Path(target_dir).exists():
    Path(target_dir).mkdir() # creates backup directory

# checks if source direcotry exist and creates backup with current localtime
if Path(source_dir).exists():
    localtime_format = time.strftime('_%d_%m_%Y_%H_%M_%S', time.localtime())
    os.chdir(target_dir) # changes directory to target directory
    shutil.make_archive(backup_filename + localtime_format, 'zip', source_dir) # makes zip archive file of saves directory
else:
    print('Source directory does not exist :(')
