#! python3
# bwbt.py -- tool for backing up my minecraft beta worlds

import subprocess
import time
import os
import os.path

source_dir = '/home/neczju/.var/app/org.prismlauncher.PrismLauncher/data/PrismLauncher/instances/b1.7.3/.minecraft/saves/'
target_dir = 'backups'
backup_name = 'beta_worlds'

# check if target directory not exist
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# checks if source direcotry exist and creates backup with current localtime
if os.path.exists(source_dir):
    localtime_format = time.strftime('_%d_%m_%Y_%H_%M_%S', time.localtime())
    subprocess.run(['cp', '-r', source_dir, target_dir + '/' + backup_name + localtime_format])
    if subprocess.CompletedProcess:
        print('Backup successfuly created in %s directory' % (target_dir))
else:
    print('Source directory does not exist :(')
