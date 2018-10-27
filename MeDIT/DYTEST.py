from PyQt5.QtCore import QObject, pyqtSignal


class QTypeSignal(QObject):
    sendmsg = pyqtSignal(object)

    def __init__(self):
        super(QTypeSignal, self).__init__()

    def run(self):
        self.sendmsg.emit('Hello Pyqt5')


class QTypeSlot(QObject):
    def __init__(self):
        super(QTypeSlot, self).__init__()

    def get(self, msg):
        print("QSlot get msg:", msg)


if __name__ == '__main__':
    send = QTypeSignal()
    slot = QTypeSlot()

    send.sendmsg.connect(slot.get)
    send.run()



