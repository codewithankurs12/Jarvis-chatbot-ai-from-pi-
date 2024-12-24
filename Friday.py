import threading

from logic_brain import friday_brain
import eel


def ui():
    eel.start("index.html",mode='chrome', port=6756, cmdline_args=['--start-fullscreen'])


def friday():
    t1 = threading.Thread(target=friday_brain)
    t1.start()
    t1.join()

friday()
