import sys
import os
import settings
import Position



class Rootpath:
    """
        It read the rootpath
        ----------
        opts: array    input parameters
    """

    def __init__(self, opts):
        self.root_path = opts[Position.PATH]

    def data(self):
       return str(self.root_path )



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
