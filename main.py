import sys
import os 
import threading
from time import strftime, gmtime, sleep

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow
from PyQt6.QtCore import QObject, pyqtSignal


class Backend(QObject):

    def __init__(self):
        QObject.__init__(self)

    updated = pyqtSignal(str, arguments=['updater'])

    def bootUp(self):
        t_thread = threading.Thread(target=self._bootUp)
        t_thread.daemon = True
        t_thread.start()

    def _bootUp(self):
        while True:
            curr_time = strftime("%H:%M:%S", gmtime())
            self.updater(curr_time)
            sleep(0.1)
    
    def updater(self, curr_time):
        self.updated.emit(curr_time)

QQuickWindow.setSceneGraphBackend('software')


app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)

if getattr(sys, 'frozen', False):
    # If bundled by PyInstaller
    base_path = sys._MEIPASS
else:
    # If running from source
    base_path = os.path.dirname(os.path.abspath(__file__))

qml_file = os.path.join(base_path, "UI/main.qml")
engine.load(qml_file)

if not engine.rootObjects():
    sys.exit(-1)

back_end = Backend()

engine.rootObjects()[0].setProperty('backend', back_end)

back_end.bootUp()



# curr_time = strftime("%H:%M:%S", gmtime())
# engine.rootObjects()[0].setProperty('currTime', curr_time)


sys.exit(app.exec())

