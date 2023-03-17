from PyQt5 import uic

project = QgsProject.instance()
projectPath = project.absolutePath()
dialogFilePath = projectPath + '/qt/dialogAction.ui'

DialogUi, DialogType = uic.loadUiType(dialogFilePath)

class MyDialog(DialogType, DialogUi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pressmeButton.setText('** Do not press me **')
        
        self.pressmeButton.clicked.connect(self.buttonClicked)
        
    def buttonClicked(self):
        iface.messageBar().pushMessage('No you pressed')
        
dialog = MyDialog()
#dialog.show()
dialog.exec()