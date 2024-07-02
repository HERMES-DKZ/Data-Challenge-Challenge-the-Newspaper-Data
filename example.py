import pandas as pd


zeitungen = pd.read_pickle('newspapers/newspapers_example')                      # Import des Beispieldatensatzes, besteht aus den ersten 10.000 Einträgen des Pakets aus dem Jahre 1914 Part 1


print(zeitungen.head())                                 # Ausgabe der ersten 10 Einträge des Dataframes
print(zeitungen.iloc[0])                                # Ausgabe des ersten Eintrags
print(zeitungen.info())

# Unique Values
# Beispielausgabe von bestimmten, relevanten Infos für eine Analyse:
print(len(zeitungen['provider'].unique()))              # Aus wie vielen und welchen Institutionen stammen die Zeitungen?
print(zeitungen['provider'].unique())
print(len(zeitungen['paper_title'].unique()))           # Wie viele Zeitungen und welche sind enthalten?
print(zeitungen['paper_title'].unique())



print(zeitungen.iloc[0].plainpagefulltext)              # Ausgabe des OCR-Scans der ersten Zeitschrift im Datensatz