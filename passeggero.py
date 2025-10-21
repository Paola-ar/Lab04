class Passeggero:
    def __init__(self, codicePasseggero, nome, cognome):
        self._codicePasseggero = codicePasseggero
        self._nome = nome
        self._cognome = cognome
        self._cabina = None

    @property
    def codicePasseggero(self):
        return self._codicePasseggero
    @property
    def nome(self):
        return self._nome
    @property
    def cognome(self):
        return self._cognome
    @property
    def cabina(self):
        return self._cabina

    @cabina.setter
    def cabina(self, cabina):
        self._cabina = cabina


    def __str__(self):
        if self._cabina:
            return f"{self._codicePasseggero}, {self._cognome} {self._nome}, CABINA PRENOTATA: {self._codice_cabina}"
        else:
            return f"{self._codicePasseggero}, {self._cognome} {self._nome}, CABINA PRENOTATA: Nessuna"
