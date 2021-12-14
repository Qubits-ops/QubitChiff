"""
methode de chiffrement simple par Qubit
pour dechiffrer convertir les 7 premiers bits du code binaire jusqu'a la fin
exemple:
11101001110101110110011000011110011 = 1110100 1110101 1101100 1100001 1110011
                                        116    117     108      97      115
ensuite
116 = t
117 = u
108 = l
97 = a
115 = s
c'est le code ASCII des lettre puis on a juste a inverser le tout
115 97 108 117 116
 s   a  l   u   t
11101001110101110110011000011110011 = salut
voila comment dechiffrer ma methode de chiffrement
"""
import random as r

liste1 = [101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
def convertirEnBinaire(num):
    list = []
    while num > 0:
        if (num % 2) == 0:#si divisible par 2
            list.append(0)
        else:
            list.append(1)
        num//=2 #division euclidienne par 2
    return int(''.join(map(str, list[::-1])))
def QubitChiff(message_a_chiff,cle):
    mess = []
    mess_chiff = []
    k = []
    j = []
    for i in message_a_chiff:
        mess.append(i)
    mess = list(reversed(mess))
    for i in mess:
        mess_chiff.append(ord(i) + cle)
    for i in mess_chiff:
        k.append(convertirEnBinaire(i))
    for i in k:
        j.append(str(i))
    return "".join(j)
    #return "".join(mess)
        
#print(QubitChiff("salut"))
    
