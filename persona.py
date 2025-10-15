class Passeggero:
    def __init__(self, codice_passeggeri, nome, cognome):
        self.codice_passeggeri = codice_passeggeri
        self.nome = nome
        self.cognome = cognome

    def __str__(self):
        return f"{self.codice_passeggeri},{self.nome},{self.cognome}"

