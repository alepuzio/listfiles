import sys
import os
import settings
import Position



class Rootpath:

    def __init__(self, opts):
        self.root_path = opts[Position.PATH]

    def data(self):
       return str(self.root_path )



