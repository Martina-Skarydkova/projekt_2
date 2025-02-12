"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Martina Škarydková
email: mskarydkova@gmail.com
"""
import random

def pozdrav():
    print("Ahoj! Vítej ve hře Bulls and Cows.")
    print("Myslím si čtyřmístné číslo, kde každá cifra je unikátní a nezačíná nulou.")
    print("Tvým úkolem je uhádnout toto číslo.")
    

def tajne_cislo():
    cisla = list("123456789")  # První číslice nesmí být nula
    prvni_cislo = random.choice(cisla)
    cisla.remove(prvni_cislo)
    ostatni_cisla = random.sample(cisla + ["0"], 3)  # Přidáme nulu, protože už nemůže být první
    return prvni_cislo + ''.join(ostatni_cisla)

def chybny_tip(tip):
    if not tip.isdigit():
        print("Chyba: Zadejte pouze číslice!")
        return False
    if len(tip) != 4:
        print("Chyba: Číslo musí mít přesně 4 číslice!")
        return False
    if tip[0] == '0':
        print("Chyba: Číslo nesmí začínat nulou!")
        return False
    if len(set(tip)) != 4:
        print("Chyba: Číslo nesmí obsahovat duplicitní číslice!")
        return False
    return True

def spravny_tip(utajeny, tip):
    bulls = sum(1 for u, t in zip(utajeny, tip) if u == t)
    cows = sum(1 for t in tip if t in utajeny) - bulls
    return bulls, cows

def print_odpoved(bulls, cows):
    bull_text = "bull" if bulls == 1 else "bulls"
    cow_text = "cow" if cows == 1 else "cows"
    print(f"{bulls} {bull_text}, {cows} {cow_text}")

def main():
    pozdrav()
    utajene_cislo = tajne_cislo()
    pocet_pokusu = 0
    
    while True:
        tip = input("Zadej svůj tip: ")
        if not chybny_tip(tip):
            continue
        
        pocet_pokusu += 1
        bulls, cows = spravny_tip(utajene_cislo, tip)
        print_odpoved(bulls, cows)
        
        if bulls == 4:
            print(f"Gratuluji! Uhádl jsi číslo {utajene_cislo} za {pocet_pokusu} pokusů.")
            break

if __name__ == "__main__":
    main()
