import psutil
import time
from subprocess import call

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    while True:
        for proc in psutil.process_iter():
            try:
                # Check if process name contains the given name string.
                if processName.lower() in proc.name().lower():
                    return True
                else:
                    call(processName)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                return False


if __name__ == '__main__':
    checkIfProcessRunning('firefox')
