import shelve
import pyinputplus as pyip

def system_login():
    login = pyip.inputStr("Login: ", allowRegexes=['[a-zA-z0-9]+'], blockRegexes=['.*'])
    password = pyip.inputStr("Password: ", allowRegexes=['[a-zA-Z0-9*-=+,.:;_]'], blockRegexes=['.*'])
    dataFile = shelve.open('bank_data')

    if login in dataFile and password in dataFile[login]:
        print('Login ss')

def system_register():
    login = pyip.inputStr("Login: ", allowRegexes=['[a-zA-z0-9]+'], blockRegexes=['.*'])
    password = pyip.inputStr("Password: ", allowRegexes=['[a-zA-Z0-9*-=+,.:;_]'], blockRegexes=['.*'])
    dataFile = shelve.open('bank_data')
    dataFile[login] = password
    dataFile.close()

system_register()
system_login()
