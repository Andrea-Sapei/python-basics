#!/usr/bin/env python3
# -*- coding: cp1252 -*-
# -- Questo programma gioca a testa o croce --
import random as rnd


replay = 's'                #replay attivo dall'inizio
soldi = 10                  #soldi iniziali
moneta = ['testa', 'croce'] #risultati possibili del tiro di una moneta
casa = 1000                 #soldi iniziali della casa, tiene conto di quanto gli stai dando

n = 0

while replay == 's':
    s = soldi + 1       #s variabile scommessa, sempre sopra soldi per far partire ciclo while
    g = 'invalid'       #g variabile testa o croce, dev'essere una dei due
    
    print('Giochiamo a testa o croce!')
    print('Puoi scommettere dei soldi, se vinci li raddoppi e se perdi spariscono')

    
    while s>soldi:      #ciclo che chiede quanto scommetti
        try:
            s = int(input('Quanti soldi scommetti? '))
        except ValueError:
            print('Error code 000000xc01, NAME : bet.exception.python3env.valueerror, retry') #scommessa invalida per ValueError
        if s>soldi:
            print('Non hai abbastanza soldi')   #scommessa invalida perchè era più alta del bilancio

    while g.lower() not in moneta:
        g = str(input('Testa o croce? '))       #testa o croce? non serve a nulla ma almeno sembra che si stia facendo qualcosa

    if n < 3:
        vittoria = 1                        #le prime tre giocate vincono sempre, per dare l'idea che ci si possa arricchire
        n = n+1 
    else:                                   #dopo le prime tre partono i numeri random
        vittoria = rnd.randrange(10)        #randomizza per vedere se si vince o no, con probabilità a favore della casa ovviamente
        n = n+1

    if vittoria <4 :
        soldi = soldi + s               #aggiunge i soldi
        print('Congratulazioni! hai vinto ' + str(s) + ', adesso hai ' + str(soldi) + ' euro')
        casa = casa - s
    elif vittoria >= 4:
        soldi = soldi - s               #toglie i soldi
        print('Hai perso, sarai più fortunato la prossima volta, hai ' + str(soldi) + ' euro')
        casa = casa + s

    if soldi == 0:
        print('GAME OVER')              #game over perchè soldi = 0, resetta a 10
        replay = input('Hai finito i soldi, vuoi andare a casa a riprenderne 10? (s/n)')
        print('Riavvio gioco... \nsoldi : 10 \n')
        soldi = 10
        n = 0
        print(casa)                     #tiene conto di quanto ha guadagnato la casa

    
    
    #replay = input('Vuoi continuare a giocare? s/n: ')
    
input('Grazie per aver giocato! premi ENTER per uscire')

