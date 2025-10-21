from cabina import Cabina, CabinaDeluxe, CabinaAnimale
from passeggero import Passeggero

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self._nome = nome
        self._listaPasseggeri = []
        self._listaCabine = []

    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nuovo_nome):
        self._nome = nuovo_nome

    @property
    def listaPasseggeri(self):
        return self._listaPasseggeri
    @property
    def listaCabine(self):
        return self._listaCabine

    def aggiorna_nome(self,nuovo_nome):
        self.nome = nuovo_nome

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        try:
            file = open(file_path, "r", encoding = "utf-8")
            for riga in file:
                riga = riga.strip()
                campo = riga.split(",")
                if str(campo[0]).startswith("C"):
                    codice_cabina = campo[0]
                    num_posti = int(campo[1])
                    ponte = int(campo[2])
                    prezzoBase = int(campo[3])
                    #if int(campo[4]) == True:

                    cabina = Cabina(codice_cabina, num_posti, ponte, prezzoBase)
                    self.listaCabine.append(cabina)
                elif str(campo[0]).startswith("P"):
                    codicePasseggero = campo[0]
                    nome = campo[1]
                    cognome = campo[2]
                    passeggero = Passeggero(codicePasseggero, nome, cognome)
                    self.listaPasseggeri.append(passeggero)
        except FileNotFoundError:
            raise FileNotFoundError


    def assegna_passeggero_a_cabina(self, codice_cabina, codicePasseggero):
        """Associa una cabina a un passeggero"""
        # TODO
        cabina = None
        for c in self._listaCabine:
            if c.codice_cabina == codice_cabina:
                cabina = c
                break
        if cabina is None:
            raise Exception (f"Cabina {codice_cabina} non trovata")

        passeggero = None
        for p in self._listaPasseggeri:
            if p.codicePasseggero == codicePasseggero:
                passeggero = p
                break

        if passeggero is None:
            raise Exception (f"Passeggero {codicePasseggero} non trovato")

        if cabina.prenotata:
            raise Exception (f"Cabina {codice_cabina} già prenotata")
        if passeggero.cabina is not None:
            raise Exception (f"Passeggero {codicePasseggero} ha già una cabina assegnata")

        cabina.assegna_passeggero(passeggero)
        passeggero.cabina = cabina


    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO
        self.listaCabine.sort(key = lambda cabina: getattr(cabina,"prezzo",cabina._prezzoBase))
        return self.listaCabine


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO
        for p in self._listaPasseggeri:
            if p.cabina:
                codice_cabina = p.cabina.codice_cabina
            else:
                codice_cabina = "Nessuna"
            print (f"{p.codicePasseggero},{p.cognome} {p.nome}, CABINA PRENOTATA: {codice_cabina}")
