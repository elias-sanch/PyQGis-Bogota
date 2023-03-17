from PyQt5 import uic

DialogUi, DialogType = uic.loadUiType('D:/Local/Documentos/Elias/Cursos/Qgis/qt/dialog.ui')

class MyDialog(DialogType, DialogUi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
dialog = MyDialog()
#dialog.show()
dialog.exec()