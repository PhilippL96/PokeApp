# Pokemon-Scraper

Mit diesem Projekt wird über die Bibliothek Streamlit eine simple App erstellt, die es ermöglicht, nach jedem beliebigen Pokemon zu suchen und so verschiedene Informationen über dieses Pokemon zu erhalten. Verwendet dafür wird die [PokeAPI](https://pokeapi.co/api/v2/pokemon/).

## Skripte

**`api.py`**: Enthält verschiedene Funktionen, um:
- das JSON Skript für ein Pokemon aus der API zu scrapen
- Informationen zu Fähigkeiten des Pokemons aus der JSON zu filtern
- Informationen zu den Maßen des Pokemons aus der JSON zu filtern
- das Bild des Pokemons aus der JSON zu erhalten


**`main.py`**: Implementiert die Logik in einer Streamlit App.



## Verwendung

Starte die Streamlit App mit dem Befehl `streamlit run Predicter_App.py`.

## Installation

Stelle sicher, dass Python installiert ist. Installiere die benötigten Python-Abhängigkeiten mit `pip install -r requirements.txt`.
