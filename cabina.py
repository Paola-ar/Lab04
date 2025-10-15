class Cabina:
    def __init__(self, codice_cabina, num_posti, ponte, prezzo):
        self.codice_cabina = codice_cabina
        self.num_posti = num_posti
        self.ponte = ponte
        self.prezzo = prezzo
        self.prenotata = False

    def __str__(self):
        return f"{self.codice_cabina},{self.num_posti},{self.ponte},{self.prezzo},{self.prenotata}"

#class CabinaAnimale(cabina):
#   def __init__(self, codice_cabina, num_posti, ponte, prezzo):

