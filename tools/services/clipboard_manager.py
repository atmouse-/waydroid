# Copyright 2021 Erfan Abdi
# SPDX-License-Identifier: GPL-3.0-or-later
import logging
import threading
from tools.interfaces import IClipboard

try:
    import pyperclip as pyclip
    canClip = True
except Exception as e:
    logging.debug(str(e))
    canClip = False

def start(args):
    def sendClipboardData(value):
        try:
            pyclip.copy(value)
        except Exception as e:
            logging.debug(str(e))

    def getClipboardData():
        try:
            return pyclip.paste()
        except Exception as e:
            logging.debug(str(e))

    def service_thread():
        IClipboard.add_service(args, sendClipboardData, getClipboardData)

    if canClip:
        args.clipboard_manager = threading.Thread(target=service_thread)
        args.clipboard_manager.start()
    else:
        logging.warning("Failed to start Clipboard manager service, check logs")

def stop(args):
    try:
        if args.clipboardLoop:
            args.clipboardLoop.quit()
    except AttributeError:
        logging.debug("Clipboard service is not even started")
