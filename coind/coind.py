import os
from subprocess import Popen, PIPE, STDOUT
from datetime import datetime


# Coind
# Class for run coind script commands
class Coind:
    # coind types
    TYPE_D = 1  # Use own initilialized script. Ex: bitcoind
    TYPE_CLI = 2  # Use terminal cli command script. Ex: bicoin-cli

    # noinspection PyShadowingBuiltins
    def __init__(self, name, type, path='', debug=False):
        """
        Constructor

        :param name: cryptocurrency name. Ex: bitcoin
        :type name: string

        :param type: script execution type
        :type type: int

        :param path: coind executable path if its not recognizable
        :type path: string

        :param debug: enable debug logs during execution
        :type debug: bool
        """

        self.__name = name
        self.__type = type
        self.__path = path
        self.__debug = debug

    def run(self, action):
        """
        Run coind commands

        :param action: coind command
        :type action: string
        """

        cmd = self.__form_cmd(action)
        if '-daemon' in cmd:
            return self.__run_daemon(cmd)
        else:
            return self.__run(cmd)

    def has_cli(self):
        """
        Check if has cli

        :returns: bool
        """

        cmd = 'find / -iname ' + self.__name + '-cli'
        result = self.__run(cmd)
        return result != ''

    def is_running(self):
        """
        Check if coind is running
        """

        result = self.__run('pidof '+self.__name+'d')
        return result != ''

    def __getattr__(self, name):
        """
        Call command dynamically
        """
        if name.startswith('_') is False:
            def wrapper(*args):
                cmd = name
                if len(args) > 0 and args[0]:
                    cmd += ' ' + args[0]
                return self.run(cmd)
            return wrapper

    def __form_cmd(self, action):
        """
        Mount full command

        :param action: coind command
        :type action: string
        """

        cmd = ''
        if self.__path:
            cmd += self.__path + '/'
        cmd += self.__name
        if self.__type is self.TYPE_D or '-daemon' in action:
            cmd += 'd'
        elif self.__type is self.TYPE_CLI:
            cmd += '-cli'
        else:
            raise Exception('Invalid coind type')

        cmd += ' ' + action
        self.__log('Mounting command: ' + cmd)
        return cmd

    def __run(self, cmd):
        """
        Run command

        :param cmd: coind command
        :type cmd: string
        """

        self.__log('Running command')
        out = Popen(cmd, stderr=STDOUT, stdout=PIPE, shell=True)
        result = out.stdout.read()
        out.communicate()  # It will finish Popen after read data
        out.terminate()

        self.__log('Finished running command')
        return str(result, 'utf-8').strip()

    def __run_daemon(self, cmd):
        self.__log('Running command')
        os.system(cmd+' 2>&1')
        self.__log("is_running: %s" % self.is_running())

        result = self.__name.capitalize() + ' server starting' if self.is_running() else ''
        self.__log('Finished running command')
        return result.strip()

    def __log(self, text):
        if self.__debug:
            print('['+datetime.today().strftime("%Y-%m-%d %H:%M:%S")+'] '+text)
