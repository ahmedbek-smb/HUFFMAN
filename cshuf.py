# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 07:33:42 2021

@author: formation
"""

def alphabet(text ):
    L=[0]*127
    final=[]
    for i in text:
        L[ord(i.upper())]+=1
    a=True
    while a:
        a=False
        maxi=max(L)
        if maxi!=0:
            final.append(chr(L.index(maxi))+':'+str(maxi))
            L[L.index(maxi)]=0
            a=True
    return final
def arbre(alpha):
    arb=[]
    for i in alpha:
        arb.append([int(i[2:]),i[0],[]])
    while len(arb)!=1:
        minimal=100000
        MINIMAL=100000
        index_minimal=0
        index_MINIMAL=0
        for i in range(len(arb)):
            if minimal>=arb[i][0]:
                MINIMAL=minimal
                index_MINIMAL=index_minimal
                minimal=arb[i][0]
                index_minimal=i
            elif MINIMAL >=arb[i][0] :
                MINIMAL=arb[i][0]
                index_MINIMAL=i
        if index_minimal<index_MINIMAL:
            nouvel_arbre=[arb[index_minimal][0]+arb[index_MINIMAL][0],arb[index_minimal],arb[index_MINIMAL]]
        else:
            nouvel_arbre=[arb[index_minimal][0] + arb[index_MINIMAL][0], arb[index_MINIMAL], arb[index_minimal]]
        arb.pop(index_minimal)
        arb.insert(index_minimal,nouvel_arbre)
        arb.pop(index_MINIMAL)
    return arb[0]
def codechar(arb,char):
    global a
    global code
    if a and arb!=[]:
        if not isinstance(arb[1],str):
            code.append('1')
            codechar(arb[1],char)
            if a:
                code.remove('1')
                code.append('0')
                codechar(arb[2],char)
                if a:
                    code.remove('0')
        elif arb[1]==char:
            a=False
fichier=open('fichh.txt','r')
fichiercompresse=open('textcomp.txt','w')
fichieralpha=open('alphabet.txt','w')
texte=fichier.read()
alph=alphabet(texte)
for i in alph:
    fichieralpha.write(i+'\n')
arb=arbre(alph)
bits=0
compteur=0
for i in texte:
    a=True
    code=[]
    codechar(arb,i.upper())
    compteur+=1
    bits+=len(code)
    while len(code)!=8:
        code.insert(0,'0')
    code="".join(code)
    fichiercompresse.write(code)
print('moyenne de stockage par caractere est :',bits/compteur)
fichier.close()
fichiercompresse.close()
fichieralpha.close()