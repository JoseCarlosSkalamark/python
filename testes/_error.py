import sys

class ERROR(object):
    def __init__(self, error=None):
        if error != None:
            print("[SYSTEM => Error]: ", error)
            sys.exit(0)
