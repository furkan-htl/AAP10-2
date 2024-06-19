# Eingabe vom Benutzer
satz = input("Gib einen Satz ein: ")

# Wörter zählen
woerter = satz.split()
anzahl_woerter = len(woerter)

# Ergebnis ausgeben
print("Die Anzahl der Wörter in dem Satz ist:", anzahl_woerter)
