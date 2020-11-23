from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import tkinter
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()

textFilePath = ""
keyFilePath = ""
saveFilePath = ""

#MAGIC = 'ADFGVX'

#secretAlphabet = "cizj64tayd5gpsk7rv1qxh98flb20o3mwneu"


class Okno(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(Okno,self).__init__(*args,*kwargs)
        self.setWindowTitle("Maszyna szyfrująca/deszyfrująca strumieniowo")

        #########NAPISY#########
        
        titleText = QLabel()
        titleText.setText("Podaj tekst i klucz lub wybierz pliki")
        titleText.setAlignment(Qt.AlignCenter)
        titleText.setFont(QFont('Arial',30))
        
        self.subtitleText = QLabel()
        self.subtitleText.setText("")
        self.subtitleText.setAlignment(Qt.AlignCenter)
        self.subtitleText.setFont(QFont('Arial',20))
        
        self.opisText = QLabel()
        self.opisText.setText("Aleksander Stęplewski 140784 \n Działa na większości znaków.\n Przyjmuje tylko pliki .txt")
        self.opisText.setAlignment(Qt.AlignCenter)
        self.opisText.setFont(QFont('Arial',15))
        
        self.dzialanieText = QLabel()
        self.dzialanieText.setText("Maszyna do szyfrowania strumieniowego ciągiem bitów")
        self.dzialanieText.setAlignment(Qt.AlignCenter)
        self.dzialanieText.setFont(QFont('Arial',35))
        
        self.messageField = QLineEdit()
        self.messageField.setPlaceholderText("Podaj tekst lub szyfr")
        
        self.keyField = QLineEdit()
        self.keyField.setPlaceholderText("Podaj klucz")
        
        textFieldsLayout = QHBoxLayout()
        textFieldsLayout.addWidget(self.messageField)
        textFieldsLayout.addWidget(self.keyField)
        textFieldsLayoutW = QWidget()
        textFieldsLayoutW.setLayout(textFieldsLayout)
        
        ######PRZYCISKI#######
        
        encryptButton = QPushButton()
        encryptButton.setText("Szyfruj")
        encryptButton.clicked.connect(self.encryptClicked)
        
        decryptButton = QPushButton()
        decryptButton.setText("Deszyfruj")
        decryptButton.clicked.connect(self.decryptClicked)
        
        buttonsLayout = QHBoxLayout()
        buttonsLayout.addWidget(encryptButton)
        buttonsLayout.addWidget(decryptButton)
        buttonsLayoutW = QWidget()
        buttonsLayoutW.setLayout(buttonsLayout)
        
        textSelectButton = QPushButton()
        textSelectButton.setText("Wybierz plik tekstu")
        textSelectButton.clicked.connect(self.textSelectClicked)
        
        keySelectButton = QPushButton()
        keySelectButton.setText("Wybierz plik klucza")
        keySelectButton.clicked.connect(self.keySelectClicked)
        
        saveButton = QPushButton()
        saveButton.setText("Zapisz pole tekstu do pliku")
        saveButton.clicked.connect(self.saveClicked)
        
        infoButton = QPushButton()
        infoButton.setText("Info")
        infoButton.clicked.connect(self.infoClicked)

        selectLayout = QHBoxLayout()
        selectLayout.addWidget(textSelectButton)
        selectLayout.addWidget(keySelectButton)
        selectLayoutW = QWidget()
        selectLayoutW.setLayout(selectLayout)
        
        saveLayout = QHBoxLayout()
        saveLayout.addWidget(saveButton)
        saveLayout.addWidget(infoButton)
        saveLayoutW = QWidget()
        saveLayoutW = QWidget()
        saveLayoutW.setLayout(saveLayout)
        
        #######WIDGETY#########
        
        mainMenu = QVBoxLayout()
        mainMenu.setAlignment(Qt.AlignCenter)
        mainMenu.addWidget(self.opisText)
        mainMenu.addWidget(self.dzialanieText)
        mainMenu.addWidget(titleText)
        mainMenu.addWidget(self.subtitleText)
        mainMenu.addWidget(textFieldsLayoutW)
        mainMenu.addWidget(buttonsLayoutW)
        mainMenu.addWidget(selectLayoutW)
        mainMenu.addWidget(saveLayoutW)
        

        mainMenuW = QWidget()
        mainMenuW.setLayout(mainMenu)

        self.setCentralWidget(mainMenuW)
        
    ######FUNKCJE########
    
    def sxor(self, s1, s2):    
        # konwertuje string na pary znaków
        # zamiana kadej pary na ascii
        # XOR na ascii
        # konwertowanie z powrotem na ascii
        # konwertowanie ascii z powrotem na string
        return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))
    
    def encrypt(self):
        print("\n encrypt")
        #print("Alfabet: " + secretAlphabet)
        
        message = self.messageField.text()
        #message = message.lower()
        keyword = self.keyField.text()
        #keyword = keyword.lower()
        
        #szyfrowanie strumieniowe
        
        szyfr = self.sxor(message, keyword)
        return szyfr
        
        
    def decrypt(self):
        print("\n decrypt")
        #print("Alfabet: " + secretAlphabet)
        
        message = self.messageField.text()
        #message = message.upper()
        keyword = self.keyField.text()
        #keyword = keyword.lower()
        
        #deszyfrowanie strumieniowe
        
        szyfr = self.sxor(message, keyword)
        return szyfr
        
    
    def encryptClicked(self):
        self.subtitleText.setText("Szyfruje " + self.messageField.text() + " kluczem " + self.keyField.text())
        try:
            self.messageField.setText(self.encrypt())
        except:
            print("cos poszlo nie tak")
    
    def decryptClicked(self):
        self.subtitleText.setText("Deszyfruje " + self.messageField.text() + " kluczem " + self.keyField.text())
        try:
            self.messageField.setText(self.decrypt())
        except:
            print("cos poszlo nie tak")
        
    def textSelectClicked(self):
        textFilePath = filedialog.askopenfilename()
        self.subtitleText.setText("Biorę tekst z: " + textFilePath)
        try:
            f = open(textFilePath, "r")
            text = f.read()
            f.close()
            self.messageField.setText(text)
        except:
            print("zamknieto")
        
    def keySelectClicked(self):
        keyFilePath = filedialog.askopenfilename()
        self.subtitleText.setText("Biorę klucz z: " + keyFilePath)
        try:
            f = open(keyFilePath, "r")
            key = f.read()
            f.close()
            self.keyField.setText(key)
        except:
            print("zamknieto")
        
    def saveClicked(self):
        self.subtitleText.setText("Zapisuje")
        saveFilePath = filedialog.asksaveasfilename()
        try:
            f = open(saveFilePath, "w")
            f.write(self.messageField.text())
            f.close
        except:
            print("zamknieto")
            
    def infoClicked(self):
        self.subtitleText.setText("Otwarto informacje")
        info = QMessageBox()
        info.setWindowTitle("Info")
        info.setStyleSheet("QMessageBox { background-color : rgb(167,167,167)")
        try:
            f = open("/Users/aleksandersteplewski/Desktop/POD/szyfrator/info.txt", "r", encoding="utf-8")
            data = f.read()
            info.setText(data)
            info.setFont(QFont('Comic Sans',12))
            info.exec_()
        except:
            print("coś się nie wczytało")
        
        


########MAIN##########

app = QApplication(sys.argv)
window = Okno()
window.setFixedSize(900,500)
#window.setMaximumWidth(1000)
#window.setMaximumHeight(800)
window.setStyleSheet("background-color: rgb(167,167,167)")
window.show()
app.exec_()
