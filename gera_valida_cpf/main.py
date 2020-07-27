"""
    Programa que valida e gera CPFs
    Interface feita com o Qt Designer
"""
import sys
from gera_valida_cpf.gera_cpf import gerar_cpf
from gera_valida_cpf.valida_cpf import validar_cpf
from gera_valida_cpf.interface import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


class AplicativoCPF(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setFixedSize(626, 536)

        self.btnGerar.clicked.connect(self.gerar)
        self.btnValidar.clicked.connect(self.validar)

    def gerar(self):
        novo_cpf = gerar_cpf()
        self.lineSaida.setText(novo_cpf)
        self.lineSaida.setStyleSheet(
            'color: #03045e;'
            'background: #90e0ef;'
        )

    def validar(self):
        cpf = self.inputCPF.text()
        resultado = validar_cpf(cpf)

        self.lineSaida.setText(resultado)
        if resultado == 'CPF válido.':
            self.lineSaida.setStyleSheet(
                'color: #fff;'
                'background: #028090;'
            )
        elif resultado == 'CPF inválido.':
            self.lineSaida.setStyleSheet(
                'color: #0a0908;'
                'background: #f29e4c;'
            )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = AplicativoCPF()
    app.show()
    qt.exec_()
