from SATInstanz_Musterlösung import SATInstanz

dateiname = input("Welche Datei soll eingelesen werden? (z.B. Beispiel1): ")
sat_solver = SATInstanz.from_file(dateiname+".txt")
for loesung in sat_solver.loese(False):
    print(sat_solver.belegung_zu_string(loesung, False))
    
    