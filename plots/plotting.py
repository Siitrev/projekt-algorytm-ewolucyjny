import matplotlib.pyplot as plt # TO DO SZEMKU DODAJ
import numpy as np
from database.DbController import *
from gui.MainWindow import MainWindow

def plotting(choice):
    obiekt = DbController('../database/db.sqlite3')

    if choice == 1:
        ypoints = obiekt.get_column('najlepszy')
        # print(ypoints)
        length = len(ypoints)
        xpoints = [i for i in range(1, length + 1)]  # liczba epok = liczba najlepszych

        plt.plot(xpoints, ypoints)
        plt.show()

    if choice == 2:
        ypoints = obiekt.get_column('srednia_populacji')
        # print(ypoints)
        length = len(ypoints)
        xpoints = [i for i in range(1, length + 1)]

        plt.plot(xpoints, ypoints)
        plt.show()

    if choice == 3:
        ypoints = obiekt.get_column('odchylenie_standardowe_populacji')
        # print(ypoints)
        length = len(ypoints)
        xpoints = [i for i in range(1, length + 1)]

        plt.plot(xpoints, ypoints)
        plt.show()

plotting(2)