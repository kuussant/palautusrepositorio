from tuomari import Tuomari

class KiviPaperiSakset:
    def __init__(self):
        self.tuomari = Tuomari()

    def pelaa(self):
        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)

            print(self.tuomari)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        print("Kiitos!")
        print(self.tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        raise Exception("Tämä metodi pitää korvata aliluokassa")

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

    @staticmethod    
    def luo_peli(tyyppi):
        if tyyppi == 'a':
            from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja

            return KPSPelaajaVsPelaaja()
        if tyyppi == 'b':
            from kps_tekoaly import KPSTekoaly

            return KPSTekoaly()
        if tyyppi == 'c':
            from kps_parempi_tekoaly import KPSParempiTekoaly

            return KPSParempiTekoaly()
        
        return None
