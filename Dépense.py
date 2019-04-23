# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 23:51:54 2017

@author: Riad
"""

import sqlite3
def CREATABLE():
# CREATION DE LA BASE DE DONNEES
    conn = sqlite3.connect('Dépense.db')

# CREATION DES TABLES
    cursor = conn.cursor()
#Table des noms
    cursor.execute(""" CREATE TABLE IF NOT EXISTS name(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            names TEXT )""")
    conn.commit()
#Table dépense
    cursor.execute(""" CREATE TABLE IF NOT EXISTS commun(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            activité TEXT,
            prix INT,
            date DATE,
            id_name INT,
            id_for INT )""")
    conn.commit()
    conn.close()
    return 0

#Fonction montrer les noms
def Liste():
    conn = sqlite3.connect('Dépense.db')
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM name """)
    print(cursor.fetchall())
    conn.commit()
    conn.close()
    return 0
    


#FONCTION AJOUT DES NOMS
def NOMS():
    print(Liste())
    décision = int(input('Ajouter un NOM ? \n 1 = OUI \n 2 = NON \n')) 
    if décision == 1:
        nom = str(input('le nom ?'))
        numéro = int(input('Numéro ?'))
        conn = sqlite3.connect('Dépense.db',timeout = 10)
        cursor = conn.cursor()
        cursor.execute(""" INSERT INTO name(id,names) VALUES(:id , :names)""", (numéro , nom))
        conn.commit()
        print('ok')
        conn.close()
        return 0
    elif décision == 2:
        print('ok')
        return 0
    
#Fonction qui montre toute les dépenses    
def Ldépense():
    conn = sqlite3.connect('Dépense.db')
    cursor = conn.cursor()
    cursor.execute(""" SELECT commun.id , activité , prix , date , A.names , P.names  
                       FROM commun , name AS A , name AS P 
                       WHERE A.id = commun.id_name AND P.id = commun.id_for  """)
    print(cursor.fetchall())
    conn.commit()
    conn.close()
    return 0
    

def idFrom(id):
    conn = sqlite3.connect('Dépense.db')
    cursor = conn.cursor()
    cursor.execute(""" SELECT names FROM name WHERE id = :id""", (id))
    res = cursor.fetch()
    conn.commit()
    conn.close()
    return res
#Fonction qui montre 
def dépense():
    print(Ldépense())
    p=0
    while p!=1:
        menu = int(input('Ajouter une dépense ? \n 1 = OUI \n 2 = NON \n'))
        if menu == 1:
            print(Ldépense())
            print(Liste())
            numéro = int(input('Numéro ? '))
            activité = str(input('l activité ? '))
            prix = float(input('Prix ? '))
            date = str(input('Date ? '))
            id_name = int(input('id de celui qui a payé '))
            id_for = idFrom(int(input('id pour qui l achat a été fait ')))
            conn = sqlite3.connect('Dépense.db',timeout = 10)
            cursor = conn.cursor()
            cursor.execute(""" INSERT INTO commun 
                           VALUES(:id , :activité , :prix , :date , :id_name , :id_for )""",
                                (numéro , activité , prix , date , id_name , id_for ))
            conn.commit()
            print('ok')
            conn.close()
        elif menu == 2:
            print('ok')
            p = 1
    return 0

def dividende():
    #Dépense Clair pour tous
    conn = sqlite3.connect('Dépense.db',timeout = 10)
    cursor = conn.cursor()
    cursor.execute("""SELECT prix FROM commun WHERE id_for = 1 AND id_name = 3""")
    Dev3 = cursor.fetchall()
    tot1=0
    x = len(Dev3)
    for i in range(0,x):
        tot1= tot1 + float(Dev3[i][0])
    conn.commit()
    conn.close()
    #Dépense CLair pour Riad
    conn = sqlite3.connect('Dépense.db',timeout = 10)
    cursor = conn.cursor()
    cursor.execute("""SELECT prix FROM commun WHERE id_for = 2 AND id_name = 3""")
    Dev4 = cursor.fetchall()
    tot2=0
    y = len(Dev4)
    for i in range(0,y):
        tot2= tot2 + float(Dev4[i][0])
    conn.commit()
    conn.close()  
    #Dépense Riad pour tous
    conn = sqlite3.connect('Dépense.db',timeout = 10)
    cursor = conn.cursor()
    cursor.execute("""SELECT prix FROM commun WHERE id_for = 1 AND id_name = 2""")
    Dev2 = cursor.fetchall()
    tot3=0
    z = len(Dev2)
    for i in range(0,z):
        tot3= tot3 + float(Dev2[i][0])
    conn.commit()
    conn.close()
    #Dépense Riad pour Clair
    conn = sqlite3.connect('Dépense.db',timeout = 10)
    cursor = conn.cursor()
    cursor.execute("""SELECT prix FROM commun WHERE id_for = 3 AND id_name = 2""")
    Dev5 = cursor.fetchall()
    tot4=0
    w = len(Dev5)
    for i in range(0,w):
        tot4= tot4 + float(Dev5[i][0])
    conn.commit()
    conn.close()  
    Clair = tot1/2 + tot2
    Riad = tot3/2 + tot4
    print("Clair a payé ",Clair,"€ pour Riad")
    print("Riad a payé ",Riad,"€ pour CLair")
    print("Clair doit à Riad ",Riad-Clair,"€ !!!!")


