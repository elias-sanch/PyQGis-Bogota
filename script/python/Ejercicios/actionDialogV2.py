from PyQt5 import uic

project = QgsProject.instance()
projectPath = project.absolutePath()
dialogFilePath = projectPath + '/qt/dialogAction.ui'

DialogUi, DialogType = uic.loadUiType(dialogFilePath)

class MyDialog(DialogType, DialogUi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pressmeButton.clicked.connect(self.buttonClicked)
        self.optionComboBox.currentTextChanged.connect(self.comboBoxChanged)
        
    def buttonClicked(self):
        iface.messageBar().pushMessage('Well done! here I am.')
        
    def comboBoxChanged(self):
        message = self.optionComboBox.currentText()
        iface.messageBar().pushMessage(message)
        self.nameLineEdit.setText(message)
        
dialog = MyDialog()
#dialog.show()
dialog.exec()