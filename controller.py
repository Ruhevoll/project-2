from PyQt5.QtWidgets import *
from view import *
import quadratic
import re
import os

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton_submit.clicked.connect(lambda: self.submit())
        self.pushButton_clear.clicked.connect(lambda: self.clear())
        self.pushButton_roots.clicked.connect(lambda: self.roots())
        self.pushButton_factor.clicked.connect(lambda: self.factor())
        self.pushButton_vertex.clicked.connect(lambda: self.vertex())

    def submit(self):
        """
        Submits the typed quadratic in order to create a quadratic class.
        :return: Displays the mathematical expression for the quadratic and displays a plot in the GUI.
        """
        try:
            x = self.lineEdit.text().split("x^2")

            if x[0] == '':
                a = 1
            elif x[0] == '-':
                a = -1
            elif x[0] != 0:
                a = eval(x[0])
            else:
                pass

            x.remove(f'{x[0]}')

            try:
                try:
                    y = x[0].split("x")

                    if len(y) == 2:
                        if y[0].strip() == '':
                            z = '1'
                        elif y[0].strip() == '-':
                            z = '-1'
                        elif y[0].strip() == '+':
                            z = '1'
                        else:
                            z = y[0].strip()

                        if y[1].strip() == '':
                            w = '0'
                        else:
                            w = y[1].strip()

                    elif len(y) == 1:
                        if y[0].strip() == '':
                            z = '1'
                        elif y[0].strip() == '+':
                            z = '1'
                        elif y[0].strip() == '-':
                            z = '-1'
                        else:
                            z = y[0].strip()
                        b = 0
                        c = eval(z)
                    else:
                        b = 0
                        c = 0

                    b = eval(z)
                    c = eval(w)
                except:
                    z = x[0].strip()
                    b = 0
                    c = eval(z)
            except:
                b = 0
                c = 0

            try:
                os.remove("graph.png")
            except:
                pass

            self.label_enterad_3.setText("")
            self.parabola = quadratic.quad(a, b, c)

            self.parabola.graph()

            self.label_input.setText(f'<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">{self.parabola.equation()}</span></p></body></html>')
            self.label_graph.setText('')
            self.label_graph.setText('<html><head/><body><p><img src="graph.png" width = "433" height = "272"/></p></body></html>')
        except:
            self.lineEdit.setText('')
            self.label_input.setText('')
            self.label_graph.setText('')
            self.label_computation.setText('')
            self.label_enterad_3.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">Error! </span><span style=\" font-size:12pt;\">Please enter the equation of a parabola (as a function of x).</span></p><p align=\"center\"><span style=\" font-size:12pt;\">e.g. 2x^2 - x + 10</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Leading coefficient cannot be nonzero!</span></p></body></html>')

    def clear(self):
        """
        Clears everything.
        :return: Clears the GUI.
        """
        self.lineEdit.setText('')
        self.label_input.setText('')
        self.label_graph.setText('')
        self.label_computation.setText('')
        self.label_enterad_3.setText('')

    def roots(self):
        """
        Displays the roots of the quadratic.
        :return: Displays the roots of the quadratic in the bottom area.
        """
        try:
            self.label_computation.setText('')
            self.label_computation.setText(f'<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">{self.parabola.roots()}</span></p></body></html>')
        except:
            self.label_computation.setText('')
            self.label_computation.setText(f'<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">"First enter a parabola!"</span></p></body></html>')
    def factor(self):
        """
        Displays the factorization of the quadratic.
        :return: Displays the factors of the quadratic in the bottom area.
        """
        try:
            self.label_computation.setText('')
            self.label_computation.setText(f'<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">{self.parabola.factor()}</span></p></body></html>')
        except:
            self.label_computation.setText('')
            self.label_computation.setText(f'<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">"First enter a parabola!"</span></p></body></html>')

    def vertex(self):
        """
        Displays the vertex of the quadratic.
        :return: Displays the vertex of the quadratic in the bottom area.
        """
        try:
            self.label_computation.setText('')
            self.label_computation.setText(f'<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">{self.parabola.vertex()}</span></p></body></html>')
        except:
            self.label_computation.setText('')
            self.label_computation.setText(f'<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">"First enter a parabola!"</span></p></body></html>')