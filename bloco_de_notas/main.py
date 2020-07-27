import sys
from bloco_de_notas.interface import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtWidgets import QShortcut


class Note(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnSalvar.clicked.connect(self.salvar_arquivo)
        self.btnAbrir.clicked.connect(self.abrir_arquivo)

        self.comboBox.addItem('Dark')
        self.comboBox.addItem('Light')
        self.comboBox.activated.connect(self.mudar_tema)

    def salvar_arquivo(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar arquivo',
            '/home/joao/Documents'
        )

        with open(file_path, 'w', encoding='UTF-8') as file:
            text = self.txtArea.toPlainText()
            file.write(text)

    def abrir_arquivo(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir arquivo',
            '/home/joao/Documents'
        )

        with open(file_path, 'r', encoding='UTF-8') as file:
            for line in file.readlines():
                self.txtArea.setText(self.txtArea.toPlainText() + line)

    def mudar_tema(self):
        tema = self.comboBox.currentText()
        if tema == 'Dark':
            self.setStyleSheet(
                '*{background: black;'
                ' color: #affc41;'
                'border-color: white;}'
            )
        else:
            self.setStyleSheet(
                '*{background: white;'
                ' color: black;'
                'border-color: black;}'
            )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Note()
    novo.show()
    qt.exec_()
