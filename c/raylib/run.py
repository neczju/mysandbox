# program for running raylib examples and small projects
import subprocess

print('Type file name without extension: ', end='')
filename = input()
file_extension = '.c'
file = filename + file_extension

try:
    subprocess.run(['cc', file, '-lraylib', '-o', filename],
                   check=True, stderr=subprocess.DEVNULL)
    print('Compilation successful!')
    subprocess.run('./' + filename, stdout=subprocess.DEVNULL)
    if subprocess.CompletedProcess:
        subprocess.run(['rm', filename])
        print(filename + ' binary file removed!')

except subprocess.CalledProcessError:
    print('Wrong filename!')
