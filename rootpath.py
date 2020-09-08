import sys
import os
import datetime
import settings
import Position
import message

from SingleFile import SingleFile



class Rootpath:
    """
        It read the rootpath
        ----------
        opts: array    input parameters
    """

    def __init__(self, opts):
        self.root_path = opts[Position.PATH]

    def data(self):
       return self.root_path 



    '''
        if Position.PATH > len(opts):
            print(message.INPUT_PATH_MISSING)
            sys.exit(message.ERROR_PROGRAM)
        else:
            rootpath = opts[Position.PATH]

            if (not (os.path.isabs(rootpath)) or (os.path.isfile(rootpath))):
                print(message.INPUT_PATH_UNCORRECT)
                sys.exit(message.ERROR_PROGRAM)
            else:
                print()

    return rootpath

    '''
