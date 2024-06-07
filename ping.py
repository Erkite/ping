import platform
import subprocess

def ping(host, count):

    if platform.system().lower()=='windows': 
        parameter = '-n'
    else:
        parameter = '-c'

    command = ['ping', parameter, str(count), host]

    print(subprocess.call(command) == 0)

def getInput():
    try:
        return int(input("Enter an integer of how many packets you want to send: "))
    except:
        return getInput()

host_name = input("Enter a host/IP: ")
count = getInput()

ping(host_name, count)