from kivi_paperi_sakset import KiviPaperiSakset
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        super().__init__()
        self.tekoaly = TekoalyParannettu(10)
        self.eka_siirto_tehty = False

    def _toisen_siirto(self, ensimmaisen_siirto):
        toisen_siirto = self.tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {toisen_siirto}")

        if self.eka_siirto_tehty:
            self.tekoaly.aseta_siirto(ensimmaisen_siirto)

        self.eka_siirto_tehty = True

        return toisen_siirto
