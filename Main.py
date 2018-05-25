from FrontEnd.MainWindow import MainWindow
import getpass
import os
from FrontEnd.Asking import Asking
from PyQt4 import QtGui,QtCore
import subprocess


if __name__ == '__main__':
    user=getpass.getuser()

    if not (os.path.isfile('/home/' + user + '/Documents/Findr/configuration')):
        app = QtGui.QApplication(['Findr'])
        app.setWindowIcon(QtGui.QIcon('resources/'+'Findr.png'))

        s=Asking(app)
        s.main_window.show()
        d = open('requirements', 'r')
        r = d.read().splitlines()
#        for i in r:
#            os.system('python -m pip install ' + str(i))
        app.exec_()

    if (os.path.isfile('/home/' + user + '/Documents/Findr/configuration')):
        w=MainWindow()