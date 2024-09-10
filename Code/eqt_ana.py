import numpy as np
import matplotlib.pyplot as plt
from datetime import date

# L'anomalie moyenne M (en radian), proportionnelle au temps, permet
# d'obtenir l'anomalie excentrique E (en radian)
# (résolution itérative de l'équation de Kepler M=E-e*sin(E))
# puis l'anomalie vraie V (en radian)


def eq_kepler(M, e):
    E = np.pi
    M = np.remainder(M, 2*np.pi)
    for n in range(5):
        E = (M-e*(E*np.cos(E)-np.sin(E)))/(1-e*np.cos(E))
    return E


def calc_anom_vraie(E, e):
    V = 2*np.arctan(np.sqrt((1+e)/(1-e))*np.tan(E/2))
    return V

# Epsilon : inclinaison de l'axe de rotation terrestre (en degré)
# W : longitude écliptique du Soleil au périhélie (en degré)
# M0 : anomalie moyenne au 1er janvier (en degré)
# e : excentricité de l'orbite terrestre
# Les paramètres par défaut sont ceux permettant de décrire
# le mouvement apparent du Soleil au cours d'une année.


def calc_eqt(Epsilon=23.44, W=282.99, M0=356.83, e=0.0167):
    Epsilon = Epsilon*np.pi/180.0
    W = W*np.pi/180
    pas_calc = 0.1
    M = np.pi*(np.arange(0, 360, pas_calc)+M0)/180
    E = [eq_kepler(Ml, e) for Ml in M]
    V = np.array([calc_anom_vraie(El, e) for El in E])
    lambda_V = W+V
    lambda_M = W+M
    Delta = np.arcsin(np.sin(Epsilon)*np.sin(lambda_V))
    DL = np.arcsin((np.cos(lambda_M)*np.sin(lambda_V)*np.cos(Epsilon) -
                    np.sin(lambda_M)*np.cos(lambda_V))/np.cos(Delta))
    DL = 180*DL/np.pi
    Delta = 180*Delta/np.pi
    M = M*180/np.pi
    return DL, Delta, M, M0


def trace_eqt_ana(DL, Delta, M, M0):
    T = 365.25
    temps = (M-M0)*T/360
    DT = 60*DL/15
    jour_mois = [(date(2024, n, 1)-date(2024, 1, 1)
                  ).days for n in range(1, 13)]
    nom_mois = ['1er janvier', '1er février', '1er mars', '1er avril', '1er mai', '1er juin',
                '1er juillet', '1er août', '1er septembre', '1er octobre', '1er novembre', '1er décembre']
    index_mois = [np.where(temps >= jour_mois[n])[0][0]
                  for n in range(len(jour_mois))]

    fig, ax = plt.subplots()
    ax.plot(temps, DT)
    ax.set_xlabel('Date (année 2024)')
    ax.set_ylabel('Temps solaire moyen - temps solaire vrai (en mn)')
    ax.set_title('Equation du temps')
    ax.set(xlim=(0, T))
    plt.xticks(temps[index_mois], labels=nom_mois, rotation=90)
    plt.yticks(np.arange(2*np.floor(min(DT)/2),
               2+2*np.ceil(max(DT)/2), 2))
    plt.grid('on')

    fig, ax = plt.subplots()
    ax.plot(DL, Delta)
    ax.scatter(DL[index_mois], Delta[index_mois], color='k')
    for n in range(len(index_mois)):
        plt.text(DL[index_mois[n]], Delta[index_mois[n]], nom_mois[n], ha='center', va='bottom', color='r',
                 fontsize=8, weight='bold', alpha=1)
    ax.set_xlabel('Ecart ascension droite (°)')
    ax.set_ylabel('Déclinaison (°)')
    ax.set_title('Analemme (coordonnées équatoriales)')
    ax.invert_xaxis()
    plt.xticks(np.arange(np.floor(min(DL)),
               1+np.ceil(max(DL))))
    plt.yticks(np.arange(10*np.floor(min(Delta)/10),
               10+10*np.ceil(max(Delta)/10), 10))
    plt.grid('on')

    plt.show()
