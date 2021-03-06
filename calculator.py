from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QMessageBox

class Okienko(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):

        et2 = QLabel("Pole kalkulatora:", self) #Tekst wyświetlany w oknie
        et3 = QLabel("wynik:", self)  #Tekst wyświetlany w oknie

        self.edt1 = QLineEdit() #pole z możliwością wpisywania tekstu
        self.edt2 = QLineEdit()
        self.edt3 = QLineEdit()
        self.edt4 = QLineEdit()

        self.edt4.readonly = True  #ustalamy edt3 jako okno tylko do odczytu

        przycisk1 = QPushButton("&-", self) #tworzymy przyciski z roznymi funkcjami
        przycisk2 = QPushButton("&+", self)
        przycisk3 = QPushButton("&*", self)
        przycisk4 = QPushButton("&/", self)
        przycisk5 = QPushButton("&0", self)
        przycisk6 = QPushButton("&1", self)
        przycisk7 = QPushButton("&2", self)
        przycisk8 = QPushButton("&3", self)
        przycisk9 = QPushButton("&4", self)
        przycisk10 = QPushButton("&5", self)
        przycisk11= QPushButton("&6", self)
        przycisk12= QPushButton("&7", self)
        przycisk13= QPushButton("&8", self)
        przycisk14= QPushButton("&9", self)
        przycisk15= QPushButton("√", self)
        przycisk16= QPushButton("&=", self)
        przycisk17= QPushButton("CE", self)
        przycisk18= QPushButton("mod",self)
        przycisk19 = QPushButton(".", self)
        przycisk20 = QPushButton("+/-", self)

        uklad = QGridLayout() #tworzymy układ przycisków

        uklad.addWidget(et2, 0, 0) #umieszczamy etykietę w pierwszym(zerowym) wierszu i kolumnie
        uklad.addWidget(et3, 0, 3)


        uklad.addWidget(self.edt1, 1, 0) # wybieramy lokalizacje przycisków
        uklad.addWidget(self.edt2, 1, 1)
        uklad.addWidget(self.edt3, 1, 2)
        uklad.addWidget(self.edt4, 1, 3)
        uklad.addWidget(przycisk1, 2, 1)
        uklad.addWidget(przycisk2, 2, 0)
        uklad.addWidget(przycisk3, 2, 2)
        uklad.addWidget(przycisk4, 2, 3)
        uklad.addWidget(przycisk12, 3, 0)
        uklad.addWidget(przycisk13, 3, 1)
        uklad.addWidget(przycisk14, 3, 2)
        uklad.addWidget(przycisk9, 4, 0)
        uklad.addWidget(przycisk10, 4, 1)
        uklad.addWidget(przycisk11, 4, 2)
        uklad.addWidget(przycisk6, 5, 0)
        uklad.addWidget(przycisk7, 5, 1)
        uklad.addWidget(przycisk8, 5, 2)
        uklad.addWidget(przycisk5, 6, 1)
        uklad.addWidget(przycisk15, 3, 3)
        uklad.addWidget(przycisk16, 6, 3)
        uklad.addWidget(przycisk17, 5, 3)
        uklad.addWidget(przycisk18, 4, 3)
        uklad.addWidget(przycisk19, 6, 2)
        uklad.addWidget(przycisk20, 6, 0)


        self.setLayout(uklad) # nakazujemy  programowi użyć układu o nazwie uklad (przed chwila dodalismy do niego wszystkie elementy


        self.tekst="" #zmienne które przydadzą nam sie przy definiowaniu metod
        self.liczba1=0
        self.liczba2=0
        self.znak=""

        przycisk5.clicked.connect(self.c0) # przy przycisnięciu danego przycisku wywoła się funkcja w tym przypadku c0
        przycisk6.clicked.connect(self.c1) # itd..
        przycisk7.clicked.connect(self.c2)
        przycisk8.clicked.connect(self.c3)
        przycisk9.clicked.connect(self.c4)
        przycisk10.clicked.connect(self.c5)
        przycisk11.clicked.connect(self.c6)
        przycisk12.clicked.connect(self.c7)
        przycisk13.clicked.connect(self.c8)
        przycisk14.clicked.connect(self.c9)

        przycisk2.clicked.connect(self.plus)
        przycisk16.clicked.connect(self.wynik)
        przycisk1.clicked.connect(self.minus)
        przycisk3.clicked.connect(self.mnoz)
        przycisk4.clicked.connect(self.dziel)
        przycisk17.clicked.connect(self.CE)
        przycisk15.clicked.connect(self.pierwiastek)
        przycisk18.clicked.connect(self.modulo)
        przycisk19.clicked.connect(self.ulamek)
        przycisk20.clicked.connect(self.znak1)

        self.setGeometry(400,500, 300, 200)  #pozycjax, pozycjay, szer, wys naszego okna
        self.setWindowTitle("Kalkulator") # tytuł okna (napis w lewym górnym rogu)
        self.show()

    def znak1(self): ## funkcja odpowiedzialna za zmianę znaku liczby
        if self.edt4.text() == "":  ## wynik musi byc rowny 0 zeby zaczac od nowa liczyc, więc aby policzyc cos nowego bedzie trzeba wcisnąć CE
            if self.znak == "":
                self.tekst = "-" + self.edt1.text()
                self.edt1.setText(self.tekst)
                self.liczba1 = float(self.edt1.text())
            else:
                self.tekst = "-" + self.edt3.text()
                self.edt3.setText(self.tekst)
                self.liczba2 = float(self.edt3.text())

    def ulamek(self): ## funkcja odpowiedzialna za zapisanie ułamka
        if self.edt4.text() == "":
            if self.znak=="":
                if "." not in self.edt1.text(): ## kropka moze wystepowac tylko raz w ulamku dziesietnym
                    self.tekst = self.edt1.text()+ "."
                    self.edt1.setText(self.tekst)
            else:
                if "." not in self.edt3.text(): ## kropka moze wystepowac tylko raz w ulamku dziesietnym
                    self.tekst = self.edt3.text() + "."
                    self.edt3.setText(self.tekst)

    def modulo(self): ## funkcja odpowiedzialna za policzenie liczba w pierwszej komórce mod liczba w trzeciej komórce
        if self.edt4.text() == "":                  ##(druga komórka odpowiedzialna za przetrzymywanie znaku dzialania)
            if self.edt1.text() != "":  ## modulo musimy liczyc z pewnej liczby, podobnie z dodawaniem, odejmowaniem itd..
                self.liczba1 = float(self.edt1.text())
                self.tekst = ""
                self.znak = "mod"
                self.edt2.setText("mod")

    def plus(self): #dodawanie
        if self.edt4.text() == "":
            if self.edt1.text() != "":
                self.liczba1 = float(self.edt1.text())
                self.tekst=""
                self.znak="+"
                self.edt2.setText("+")

    def minus(self): #odejmowanie
        if self.edt4.text() == "":
            if self.edt1.text() != "":
                self.liczba1 = float(self.edt1.text())
                self.tekst=""
                self.znak="-"
                self.edt2.setText("-")

    def mnoz(self): #mnozenie
        if self.edt4.text() == "":
            if self.edt1.text() != "":
                self.liczba1 = float(self.edt1.text())
                self.tekst=""
                self.znak="*"
                self.edt2.setText("*")

    def dziel(self): #dzielenie
        if self.edt4.text() == "":
            if self.edt1.text() != "":
                self.liczba1 = float(self.edt1.text())
                self.tekst=""
                self.znak="/"
                self.edt2.setText("/")

    def pierwiastek(self): #pierwiastek
        if self.edt4.text() == "":
            if self.edt1.text() != "":
                self.liczba1 = float(self.edt1.text())
                if self.liczba1>0 or self.liczba1==0:
                    self.edt2.setText("√")
                    self.tekst = ""
                    self.edt4.setText(str(self.liczba1**(1/2)))
                else:
                    QMessageBox.warning(self, "Błąd", "nie mozemy wyciagac pierwiastka z liczby ujemnej", QMessageBox.Ok)
                    # wyskoczy nam okno o nazwie^     z tekstem ^     o przycisku^ czyli przycisku z napisem "ok"

    def CE(self): #zerowanie komórek
        self.tekst = ""
        self.znak= ""
        self.edt1.setText("")
        self.edt2.setText("")
        self.edt3.setText("")
        self.edt4.setText("")

    def wynik(self): # przycisk "="
        if (self.znak=="+"):
            self.edt4.setText(str(self.liczba1 + self.liczba2))
        if (self.znak == "-"):
            self.edt4.setText(str(self.liczba1 - self.liczba2))
        if (self.znak == "*"):
            self.edt4.setText(str(self.liczba1 * self.liczba2))
        if (self.znak == "mod"):
            self.edt4.setText(str(self.liczba1 % self.liczba2))
        if (self.znak == "/"):
            if self.liczba2==0:
                QMessageBox.warning(self, "Błąd", "Nie dziel przez zero!", QMessageBox.Ok)
                self.edt4.setText("")
                self.tekst=""
            else:
                self.edt4.setText(str(self.liczba1 / self.liczba2))

    def c1(self): #jedynka na klawiaturze
        self.tekst += "1"
        if self.edt4.text() == "":  ##gdy juz obliczymy wynik nie zmieniamy zawartosci komórki trzeciej, jesli chcesz cos policzyc od nowa to wcisnij CE
            if self.znak!="":
                self.edt3.setText(self.tekst)
                self.liczba2 = float(self.edt3.text())
            else:
                self.edt1.setText(self.tekst)

    def c2(self): # itd..
        self.tekst+="2"
        if self.edt4.text() == "":
            if self.znak != "":
                self.edt3.setText(self.tekst)
                self.liczba2 = float(self.edt3.text())
            else:
                self.edt1.setText(self.tekst)

    def c3(self):
        self.tekst += "3"
        if self.edt4.text() == "":
            if self.znak!="":
                self.edt3.setText(self.tekst)
                self.liczba2 = float(self.edt3.text())
            else:
                self.edt1.setText(self.tekst)

    def c4(self):
        self.tekst += "4"
        if self.edt4.text() == "":
            if self.znak!="":
                self.edt3.setText(self.tekst)
                self.liczba2 = float(self.edt3.text())
            else:
                self.edt1.setText(self.tekst)

    def c5(self):
        self.tekst += "5"
        if self.edt4.text() == "":
            if self.znak!="":
                self.edt3.setText(self.tekst)
                self.liczba2 = float(self.edt3.text())
            else:
                self.edt1.setText(self.tekst)

    def c6(self):
        self.tekst += "6"
        if self.edt4.text() == "":
            if self.znak!="":
                self.edt3.setText(self.tekst)
                self.liczba2 = float(self.edt3.text())
            else:
                self.edt1.setText(self.tekst)

    def c7(self):
        self.tekst += "7"
        if self.edt4.text() == "":
            if self.znak!="":
                self.edt3.setText(self.tekst)
                self.liczba2 = float(self.edt3.text())
            else:
                self.edt1.setText(self.tekst)

    def c8(self):
        self.tekst += "8"
        if self.edt4.text() == "":
            if self.znak!="":
                self.edt3.setText(self.tekst)
                self.liczba2 = float(self.edt3.text())
            else:
                self.edt1.setText(self.tekst)

    def c9(self):
        self.tekst += "9"
        if self.edt4.text() == "":
            if self.znak!="":
                self.edt3.setText(self.tekst)
                self.liczba2 = float(self.edt3.text())
            else:
                self.edt1.setText(self.tekst)

    def c0(self):
        self.tekst += "0"
        if self.edt4.text()=="":
            if self.znak!="":
                self.edt3.setText(self.tekst)
                self.liczba2 = float(self.edt3.text())
            else:
                self.edt1.setText(self.tekst)

if __name__ == '__main__': #inicjowanie okna
    import sys
    app = QApplication(sys.argv)
    okno = Okienko()
    sys.exit(app.exec_())