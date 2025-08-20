#Pokročilý příklad
#Vytvořte aplikaci pro zkoušení uživatele z anglických slovíček. Aplikace se zeptá uživatele na několik náhodných anglických slovíček 
# (např. 10) z větší databáze slov. Pokud zadá správně český překlad, přičte mu bod, jinak ukáže jaký je správný překlad. 
# Po skončení testu spočítá body a čas uživatele.
#Pro reprezentaci slovíček v paměti využijte ideálně kolekci slovník, představte si, že je slovíček milion, přístup k překladům 
# by tedy měl být optimalizovaný a neměli bychom stále iterovat v nějakém listu.
#Pokud má uživatel více nebo stejně bodů jako dosavadní rekord a zároveň má nižší čas, vyzve ho aplikace k zadání jména a nový 
# rekord uloží. K reprezentaci rekordu využijte formát CSV.

import os
import random
import msvcrt
from datetime import datetime
from tkinter import messagebox

class PokrocilyPriklad():
    def __init__(self, soubor_in, soubor_output):
        print("Startuji aplikaci...")
        self.soubor_in = soubor_in
        self.soubor_output = soubor_output

        try:
            self.cesta = os.path.join(os.getenv("APPDATA"), "ResenePriklady-prace_se_soubory_lekce_1-5")
            if not os.path.exists(self.cesta):
                os.mkdir(self.cesta)
        except:
            messagebox.showerror("Chyba", "Nepodařilo se vytvořit složku " + self.cesta + ", zkontrolujte prosím svá oprávnění.") 

        self.soubor_in = os.path.join(self.cesta, soubor_in)
        if not os.path.exists(self.soubor_in):
            print("Soubor neexistuje:", self.soubor_in)
            return
        
        self.soubor_output = os.path.join(self.cesta, soubor_output)
        if not os.path.exists(self.soubor_output):
            with open(self.soubor_output, "w", encoding="utf-8") as f:
                f.write('')
    
    def nacti_radky_dict(self, soubor):
        zaznamy = {}
        with open(soubor, "r", encoding="utf-8") as f:
            for radek in f.readlines():                
                raw_items = radek.strip().split(" ")
                cleaned_items = [item for item in raw_items if item != '']
                #print(raw_items)
                #print(cleaned_items)
                #self.zaznamy[cleaned_items[0]] = cleaned_items[1]
                zaznamy[cleaned_items[0]] = cleaned_items[1]
                #print(self.slovicka)   
        return zaznamy

    def nacti_radek_list(self, soubor): #cteni pouze 1 radku v soboru 
        zaznamy = []
        with open(soubor, "r", encoding="utf-8") as f:
            radek = f.readline()
            raw_items = radek.strip().split(";")
            cleaned_item = [item.strip() for item in raw_items if item.strip() != '']  
            return cleaned_item            

    def preloz_slovo(self):
        zaznamy = self.nacti_radky_dict(self.soubor_in)
        random_key = random.choice(list(zaznamy))
        user_text = input(f"Co znamená {random_key}? \n")
        #print(random_key, self.slovicka[random_key])
        #print(f"anglicke slovo: {user_text}, cesky preklad: {self.slovicka[random_key]}")
        zaznamy_all = [x.strip() for x in zaznamy[random_key].split(",")]
        print(zaznamy_all)
        #if user_text in zaznamy[random_key]:
        if user_text in zaznamy_all:
            #print(f"YES: input: {user_text}, preklad: {self.slovicka[random_key]}")
            print(f"Vyborne. Preklad je '{zaznamy[random_key]}'")
            self.pocet_bodu += 1
            return True, self.pocet_bodu
        else:
            #print(f"NO: input: {user_text}, preklad: {self.slovicka[random_key]}")
            print(f"Spravny preklad je '{zaznamy[random_key]}'")
            return False, self.pocet_bodu

    def zkouseni(self, pocet_opakovani):
        print("Vítej v testu anglických slovíček")
        print("=================================")
        
        zaznam = self.nacti_radek_list(self.soubor_output)
        if len(zaznam) != 0:
            print(f"Nejvyšší rekord drží: {zaznam[0]}, body: {zaznam[1]}, cas: {zaznam[2]}")
        
        print("Nový test spustíš libovolnou klávesou...")
        msvcrt.getch()  # zachytí libovolnou klávesu

        time_start = datetime.now()
        self.pocet_bodu = 0
        for i in range(pocet_opakovani):
            self.preloz_slovo()
        time_diff = (datetime.now() - time_start).total_seconds()            
        print(zaznam)
        
        if len(zaznam) == 0:
            print("--- nic v souboru nebylo ---")
        
        if len(zaznam) != 0:
            #key, predesly_max_bodu = list(zaznam.items())[0]
            predesly_max_bodu = zaznam[1]            

        if ((len(zaznam) == 0 and self.pocet_bodu > 0) or 
            (len(zaznam) != 0 and (self.pocet_bodu > int(predesly_max_bodu))) or 
            (len(zaznam) != 0 and (self.pocet_bodu == int(predesly_max_bodu)) and (time_diff < float(zaznam[2])))):
            print(f"Získal jsi {self.pocet_bodu}/{pocet_opakovani} bodu s časem {time_diff} vteřin.")
            print("Máš nový rekord!")

            jmeno = input("Zadej sve jmeno: ")
            with open(self.soubor_output, "w", encoding="utf-8") as f:
                f.write(f"{jmeno}; {self.pocet_bodu}; {time_diff}")
            
            
prikladNo3 = PokrocilyPriklad("POKROCILY_PRIKLAD.csv", "POKROCILY_PRIKLAD-output.csv")
while True:
    prikladNo3.zkouseni(2)
    while True:        
        odpoved = input("Přeješ si pokračovat?? [a/n] ").lower()
        if odpoved == "a":
            break
        elif odpoved == "n":
            exit()
        else:
            print("Neplatná volba, zadej 'a' nebo 'n'.")