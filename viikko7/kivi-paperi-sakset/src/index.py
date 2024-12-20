from kivi_paperi_sakset import KiviPaperiSakset


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if len(vastaus) > 0:
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            peli_tyyppi = vastaus[-1]
            peli = KiviPaperiSakset.luo_peli(peli_tyyppi)
            peli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
