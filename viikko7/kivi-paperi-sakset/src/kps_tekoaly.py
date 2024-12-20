from kivi_paperi_sakset import KiviPaperiSakset
from tekoaly import Tekoaly


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        super().__init__()
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        toisen_siirto = self.tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {toisen_siirto}")

        return toisen_siirto