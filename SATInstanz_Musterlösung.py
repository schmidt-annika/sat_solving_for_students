class SATInstanz():
    def __init__(self):
        self.variablen = []
        self.variablen_indizes = dict()
        self.klauseln = []
        
    def klausel_parsen(self, zeile):
        klausel = []
        for literal in zeile.split():
            if literal.startswith("~"):
                negiert = 1
            else:
                negiert = 0
            variable = literal[negiert:]
            if variable not in self.variablen_indizes:
                self.variablen_indizes[variable] = len(self.variablen)
                self.variablen.append(variable)
            encodiertes_literal = self.variablen_indizes[variable] << 1 | negiert
            klausel.append(encodiertes_literal)
        self.klauseln.append(tuple(set(klausel)))

    @classmethod
    def from_file(cls, dateiname):
        instanz = cls()
        with open(dateiname, 'r') as datei:
            for zeile in datei:
                zeile = zeile.strip()
                if len(zeile) > 0 and not zeile.startswith('#'):
                    instanz.klausel_parsen(zeile)
        return instanz


    def literal_zu_string(self, literal):
        if literal & 1:
            vorzeichen = "~"
        else:
            vorzeichen = ""
        return vorzeichen + self.variablen[literal >> 1]

    def klausel_zu_string(self, klausel):
        return ' '.join(self.literal_zu_string(literal) for literal in klausel)

    def belegung_zu_string(self, belegung, nur_wahre_variablen = False, startet_mit = ""):
        literale = []
        for b, v in zip(belegung, self.variablen):
            if not v.startswith(startet_mit):
                continue
            if b == 0 and not nur_wahre_variablen:
                literale.append(v + "=false")
            elif b:
                literale.append(v + "=true")
        return " ".join(literale)
    
    def initialisiere_watchlist_set(self):
        watchlist = [set() for _ in range(2 * len(self.variablen))]
        for klausel in self.klauseln:
            watchlist[klausel[0]].add(klausel)
        return watchlist
    
    def update_watchlist(self, watchlist, falsches_literal, belegung):
        for klausel in list(watchlist[falsches_literal]):
            alternative_gefunden = False
            for alternative in klausel:
                variable = alternative >> 1
                vorzeichen = alternative & 1
                if belegung[variable] is None or belegung[variable] == vorzeichen ^ 1:
                    alternative_gefunden = True
                    watchlist[falsches_literal].remove(klausel)
                    watchlist[alternative].add(klausel)
                    break
            if not alternative_gefunden:
                return False 
        return True
        
    
    def loese(self, ausfuehrlich=True):
        return self.loese_rekursiv(self.initialisiere_watchlist_set(), [None]*len(self.variablen), 0, ausfuehrlich)
    
    def loese_rekursiv(self, watchlist, belegung, akt_variable, ausfuehrlich):
        if akt_variable == len(self.variablen):
            yield list(belegung)
            return

        for b in [0, 1]:
            if ausfuehrlich:
                print(f"Prüfe {self.variablen[akt_variable]} = {b}")

            belegung[akt_variable] = b
            
            wl = [s.copy() for s in watchlist]
            if self.update_watchlist(wl, (akt_variable << 1) | b, belegung):
                yield from self.loese_rekursiv(wl, belegung, akt_variable + 1, ausfuehrlich)

            belegung[akt_variable] = None
        
        
   