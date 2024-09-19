#! python3
# rayc.py -- program for building and running raylib programs

import subprocess
import sys

def build(filename, name):
    try:
        subprocess.run(['cc', filename, '-lraylib', '-o', name],
                       check=True)
        print('Compilation successful!')
    except subprocess.CalledProcessError: # if c compiler returns error then sys.exit
        sys.exit()

def run(name):
    subprocess.run('./' + name, stdout=subprocess.DEVNULL)
    if subprocess.CompletedProcess: # removes binary when subprocess is complete
        subprocess.run(['rm', name])
    print(filename + ' binary file removed!')


if len(sys.argv) < 3: # checks if user entered 2 arguments
    print('You need to enter an argument and filename!')
    print('Example: ./rayc.py build name_of_your_file.c')
    sys.exit()

argument = sys.argv[1]

filename = sys.argv[2]
name, sep, extension = filename.partition('.')

if argument == 'build':
    build(filename, name)
elif argument == 'run':
    build(filename, name)
    run(name)
else:
    print('Invalid argument!')
    sys.exit()

