from PyQt5 import uic

project = QgsProject.instance()
projectPath = project.absolutePath()
dialogFilePath = projectPath + '/qt/dialog.ui'

DialogUi, DialogType = uic.loadUiType(dialogFilePath)

class MyDialog(DialogType, DialogUi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
dialog = MyDialog()
#dialog.show()
dialog.exec()