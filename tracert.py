import traceback
import sys

def excepthook(etype, value, tb):
    traceback.format_exc(etype = etype, value = value, tb = tb, print_msg= False)

sys.excepthook = excepthook
