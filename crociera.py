from cabina import Cabina
from persona import Passeggero

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.listaPasseggeri = []
        self.listaCabine = []

    """Aggiungere setter e getter se necessari"""
    # TODO

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
                    prezzo = int(campo[3])
                    #if int(campo[4]) == True:

                    cabina = Cabina(codice_cabina, num_posti, ponte, prezzo)
                    self.listaCabine.append(cabina)
                elif str(campo[0]).startswith("P"):
                    codice_passeggeri = campo[0]
                    nome = campo[1]
                    cognome = campo[2]
                    passeggero = Passeggero(codice_passeggeri, nome, cognome)
                    self.listaPasseggeri.append(passeggero)
        except FileNotFoundError:
            raise FileNotFoundError


    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO
        self.listaCabine.sort( key = lambda cabina: cabina.prezzo )
        return self.listaCabine


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

