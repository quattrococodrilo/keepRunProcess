import psutil
from subprocess import call
from time import sleep


class RunProcess:

    _process_name = None

    def __init__(self, process_name: str) -> None:
        self._process_name = process_name

    @staticmethod
    def create(process_name: str):
        return RunProcess(process_name)

    def _checkIfProcessRunning(self) -> bool:
        """Check if there is any running process that contains the given name processName."""

        # Iterate over the all the running process
        for proc in psutil.process_iter():
            try:
                # Check if process name contains the given name string.
                if self._process_name.lower() in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False

    def _findProcessIdByName(self):
        '''
        Get a list of all the PIDs of a all the running process whose name contains
        the given string processName
        '''

        listOfProcessObjects = []

        # Iterate over the all the running process
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
                # Check if process name contains the given name string.
                if self._process_name.lower() in pinfo['name'].lower():
                    listOfProcessObjects.append(pinfo)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        return listOfProcessObjects

    def run(self):
        while True:
            isRunning = self._checkIfProcessRunning()
            if not isRunning:
                call(self._process_name)
                # sleep(60)
            sleep(10)
