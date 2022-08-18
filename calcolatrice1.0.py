from math import sqrt
from re import X
from PyQt5.QtWidgets import QApplication, QLabel
app = QApplication([])

hello_message = """
Benvenuti al programma calcolatrice!

Di seguito un elenco delle varie funzioni disponibili:

- Per effettuare un'Addizione, seleziona 1;
- Per effettuare una Sottrazione, seleziona 2;
- Per effettuare una Moltiplicazione, seleziona 3;
- Per effettuare una Divisione, seleziona 4;

"""



#operazione 
print("1:addizone 2:sottrazione 3:moltiplicazione 4:divisione")
cosaVoiFa = input("scrvi il numero della tua operazione:")


if cosaVoiFa == "1":
    print("hai scelto addizione")
    a = float(input("inserisci primo numero:"))
    b = float(input("inserisci secondo numero:"))
    print("il risultato è:", str(a + b))
    risultato1 = str(a + b)
elif cosaVoiFa == "2":
    print("hai sottrazione")
    a = float(input("inserisci primo numero:"))
    b = float(input("inserisci secondo numero:"))
    print("il risultato è:", str(a - b))
    risultato2 = str(a - b)
elif cosaVoiFa == "3":
    print("hai scelto moltiplicazione")
    a = float(input("inserisci primo numero:"))
    b = float(input("inserisci secondo numero:"))
    print("il risultato è:", str(a * b))
    risultato3 =  str(a * b)
elif cosaVoiFa == "4":
    print("divisione")
    a = float(input("inserisci primo numero:"))
    b = float(input("inserisci secondo numero:"))
    print("il risultato è:", str(a / b))
    risultato4 = str(a / b)

    
label = QLabel()
label.show()
app.exec()