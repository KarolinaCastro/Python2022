baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
Balik = input("Zadejte kod balíku ")

if Balik in baliky:
  if baliky[Balik] == True:
    print(f"Váš balík {Balik} byl již předán kurýrovi")
  if baliky[Balik] == False:
    print(f"Bohuzel, Váš balík {Balik} ještě nebyl předán kurýrovi")
else:
    print(f"Bohuzel, Váš balík {Balik} neevidujeme, zkontrolujte, jestli jste správně vyplnili kod balíku")