import threading

from logic_brain import friday_brain

def friday():
    t1 = threading.Thread(target=friday_brain)
    t1.start()
    t1.join()

friday()