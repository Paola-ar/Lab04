class Cabina:
    def __init__(self, codice_cabina, num_posti, ponte, prezzoBase):
        self._codice_cabina = codice_cabina
        self._num_posti = num_posti
        self._ponte = ponte
        self._prezzoBase = prezzoBase
        self._prenotata = False
        self._passeggero = None

    @property
    def codice_cabina(self):
        return self._codice_cabina
    @property
    def num_posti(self):
        return self._num_posti
    @property
    def ponte(self):
        return self._ponte
    @property
    def prezzoBase(self):
        return self._prezzoBase
    @property
    def prenotata(self):
        return self._prenotata


    def assegna_passeggero(self, passeggero):
        if self._prenotata:
            raise Exception('Cabina già prenotata.')
        self._passeggero = passeggero
        self._prenotata = True

    def __str__(self):
        if self._prenotata:
            stato = "Occupata"
        else:
            stato = "Libera"
        return f"Codice cabina STANDARD: {self.codice_cabina}, Posti Letto:{self.num_posti}, Numero Ponte: {self.ponte}, Prezzo: {self.prezzoBase:.2f}€,{stato}"

    def __lt__(self, other):
        return self.prezzo < other.prezzo




class CabinaAnimale(Cabina):
    def __init__(self, codice_cabina, num_posti, ponte, prezzoBase, maxAnimali):
        super().__init__(codice_cabina,num_posti,ponte,prezzoBase)
        self._maxAnimali = maxAnimali

    @property
    def prezzo(self):
        return self._prezzoBase * (1 + 0.10 *self._maxAnimali)

    def __str__(self):
        if self._prenotata:
            stato = "Occupata"
        else:
            stato = "Libera"
        return (f"Codice Cabina ANIMALI: {self._codice_cabina}, Posti Letto:{self.num_posti}, Numero Ponte: {self.ponte}, Prezzo: {self.prezzo:.2f}€, Max Animali: {self._maxAnimali}, {stato}")


class CabinaDeluxe(Cabina):
    def __init__(self, codice_cabina, num_posti, ponte, prezzoBase, stile):
        super().__init__(codice_cabina, num_posti, ponte, prezzoBase)
        self._stile = stile

    @property
    def prezzo(self):
        return self._prezzoBase * 1.20

    def __str__(self):
        if self._prenotata:
            stato = "Occupata"
        else:
            stato = "Libera"
        return (f"Codice Cabina DELUXE {self._stile}: {self._codice_cabina}, Posti Letto:{self.num_posti}, Numero Ponte: {self.ponte}, Prezzo: {self.prezzo:.2f}€, {stato}")

