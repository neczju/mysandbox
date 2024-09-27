#! python3
# bwbt.py -- tool for backing up my minecraft beta and bta worlds

import subprocess
import time
import os
import sys

home_dir = os.environ['HOME']
target_dir = 'backups'

if len(sys.argv) < 2:
    print('Type an argument!')
    sys.exit()

argument = sys.argv[1]

if argument == 'beta': # beta backup
    source_dir = home_dir + '/.var/app/org.prismlauncher.PrismLauncher/data/PrismLauncher/instances/b1.7.3/.minecraft/saves/'
    backup_dir_name = 'beta_worlds'
elif argument == 'bta': # better than adventure backup
    source_dir = home_dir + '/.var/app/org.prismlauncher.PrismLauncher/data/PrismLauncher/instances/BTA_MANAGED_INSTANCE/.minecraft/saves/'
    backup_dir_name = 'bta_worlds'
else:
    print('No argument named ' + argument + '!')
    sys.exit()


# check if target directory not exist
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# checks if source direcotry exist and creates backup with current localtime
if os.path.exists(source_dir):
    localtime_format = time.strftime('_%d_%m_%Y_%H_%M_%S', time.localtime())
    subprocess.run(['cp', '-r', source_dir, target_dir + '/' + backup_dir_name + localtime_format])
    if subprocess.CompletedProcess:
        print('Backup successfuly created in %s directory' % (target_dir))
else:
    print('Source directory does not exist :(')
