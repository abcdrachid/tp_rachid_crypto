
from string import ascii_lowercase as letters


def chiffre(phrase, cle, flag=0):
    i = 0
    phrase_traitee = ""
    for c in phrase:
        if c in " '":
            phrase_traitee += c
            continue
        if i == len(cle):
            i = 0
        l = letters.find(c)
        lc = letters.find(cle[i])
        if flag:
            phrase_traitee += letters[(l + lc) % 26]
        else:
            if lc > 1:
                phrase_traitee += letters[(26 - lc) + 1]
            else:
                phrase_traitee += letters[l - lc]
        i += 1
        return phrase_traitee

    def trouve_cle(phrase):
        cle = ""
        while 1:
            try:
                lcl = int(input("entrer la longeur de la clé : "))
                break
            except ValueError:
                print("entrer un numero !")
        phrase = ''.join(l for l in phrase if l in letters)
        tab_letters = []
        for i in range(lcl):
            n = 0
            letter_prov = ""
            while n + i < len(phrase):
                letter_prov += phrase[n + i]
                n += lcl
            tab_letters.append(letter_prov)

        tab_freq = []
        for e in tab_letters:
            dic = {}
            for c in e:
                if c in dic:
                    dic[c] = dic.get(c) + 1
                else:
                    dic[c] = 1
            for c, v in dic.items():
                val = (v * 100) / len(e)
                val = float((int(val * 100)) / 100)
                dic[c] = val
            tab_freq.append(dic)

        liste_letteres_francais = ['e', 'a', 'i', 's', 't', 'n', 'r']

        for dic in tab_freq:
            liste_letteres_chiffrees = []
            for i in range(7):
                liste_letteres_chiffrees.append([c for c, v in dic.items()
                                                 if v == max(dic.values())][0])
                del dic[liste_letteres_chiffrees[-1]]
            dec = letters.find(liste_letteres_chiffrees[0]) - \
                  letters.find(liste_letteres_francais[0])
            cle += letters[dec]
        return cle

    def enleve_accents(phrase):

        ch_acc = "àâäçéèêëîïôöùûü"
        ch_s_acc = "aaaceeeeiioouuu"
        for i in phrase:
            phrase = phrase.replace(i, ch_s_acc[ch_acc.index(i)])
        return phrase

    def saisie(action):

        while 1:
            try:
                phrase = input("Entre la phrase à {} : ".format(action)) \
                    .lower().strip("\r")
                phrase = enleve_accents(phrase)

                cle = input("Entre la clé : ").lower().strip("\r")
                cle = enleve_accents(cle)

                return phrase, cle

            except ValueError:
                print("Phrase non correcte")

    print(" / déchiffrement\ ")


    while 1:
        print("Entre ton choix :\n[0] - Quitter\n[1] - Chiffrer\n[2] - Déchiffrer")
        choix = int(input("-> "))

        if choix == 1:
            print("Chiffrement")
            phrase, cle = saisie("chiffrer")
            print("Phrase chiffrée : {}".format(chiffre(phrase, cle, 1)))

        elif choix == 2:
            print("Déchiffrement")
            phrase, cle = saisie("déchiffrer")
            print("Phrase déchiffrée : {}".format(chiffre(phrase, cle)))

        elif choix == 3:
            print("Crack - Hidden mode")
            while 1:
                try:
                    phrase = input("Entre la phrase à cracker : ") \
                        .lower().strip("\r")
                    phrase = enleve_accents(phrase)
                    break
                except ValueError:
                    print("Phrase non correcte")
            cle = trouve_cle(phrase)
            print("La clé est {}".format(cle))
            print("Phrase déchiffrée : {}".format(chiffre(phrase, cle)))

        elif choix == 4:
            print("annaly")

        elif choix == 0:
            print("Fin du programme")
            break

        else:
            print("J'ai dis 0, 1 ou 2 !")




