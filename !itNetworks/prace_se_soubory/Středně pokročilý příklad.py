#Středně pokročilý příklad
#Naprogramujte aplikaci pro zjišťování svátků (jmenin). Aplikace při spuštění vypíše kdo dnes slaví svátek 
# a následně se zeptá uživatele na jeho jméno a zjistí kdy slaví svátek on.
#Potřebná data načtěte z následujícího textového souboru, který jsme pro vás připravili. 
# Každá řádka reprezentuje jeden den v měsíci. Měsíce jsou postupně od ledna do prosince 
# a jsou mezi sebou odděleny prázdnou řádkou. Nemělo by vás překvapit, že 2. měsíc má 29 jmen, jelikož únor je někdy přestupný :)
#https://www.itnetwork.cz/python/soubory/python-resene-priklady-textove-soubory

import os
import datetime
from tkinter import messagebox

class StrednePokrocilyPriklad():
    def __init__(self, soubor):
        print("Startuji aplikaci...")
        self.soubor = soubor

        try:
            self.cesta = os.path.join(os.getenv("APPDATA"), "ResenePriklady-prace_se_soubory_lekce_1-5")
            if not os.path.exists(self.cesta):
                os.mkdir(self.cesta)
        except:
            messagebox.showerror("Chyba", "Nepodařilo se vytvořit složku " + self.cesta + ", zkontrolujte prosím svá oprávnění.") 

        self.soubor = os.path.join(self.cesta, self.soubor)
        if not os.path.exists(self.soubor):
            print("Soubor neexistuje:", self.soubor)
            return
    
    def nacti_radky(self):
        self.svatky = {}
        
        with open(self.soubor, "r", encoding="utf-8") as f:
            month, day = (1, 1)
            for radek in f.readlines():                
                if radek == "\n":
                    month += 1
                    day = 1
                    continue
                jmena = radek.strip().split(",")
                self.svatky[(month, day)] = jmena
                #print(self.svatky)
                day += 1

    def svatek_by_date(self, month, day):     
        return ",".join(self.svatky.get((month, day)))

    def svatek_by_jmeno(self, jmeno):
        for (mesic, den), jmena in self.svatky.items():
            if jmeno in jmena:
                return f"{den}.{mesic}."

    def dnes_slavi(self, jmeno = ""):
        self.todayDay = datetime.datetime.now().day
        self.todayMonth = datetime.datetime.now().month          
        if jmeno == "":
            print(f"Dnes {self.todayDay}.{self.todayMonth} ma svatek: {self.svatek_by_date(self.todayMonth, self.todayDay)}")  
        else:      
            print(f"{jmeno} ma svatek: {self.svatek_by_jmeno(jmeno)}")

prikladNo2 = StrednePokrocilyPriklad("STREDNE_POKROCILY_PRIKLAD.csv")
prikladNo2.nacti_radky()
prikladNo2.dnes_slavi()
#print(f"Zadejte sve jmeno:")
#prikladNo2.dnes_slavi("Eliška")
user_text = input(f"Zadejte sve jmeno:")
prikladNo2.dnes_slavi(user_text)