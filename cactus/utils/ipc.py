import os
import logging
from blinker import signal as blinker_sig

sig = blinker_sig('default')

def signal(signal, data=None):
    if data is None:
        data = {}

    #if not os.environ.get('DESKTOPAPP'):
    #    return
    sig.send(signal)
    data["signal"] = signal
    logging.warning("", data)
