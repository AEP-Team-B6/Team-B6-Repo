## Hinweis für externe Prüfer:innen

Dieses Repository dokumentiert die vollständige Umsetzung unseres Projekts im Rahmen des Moduls *Anwendungsentwicklung mit Python* an der FHNW.

Das Projekt basiert auf vorgegebenen User Stories rund um ein Hotelreservierungssystem. Ziel war es, technische Konzepte wie objektorientierte Programmierung, saubere Datenbankanbindung und eine strukturierte Architektur mit Python umzusetzen.

Die Codebasis folgt einem mehrschichtigen Aufbau (`model`, `data_access`, `business_logic`, `ui`) und wurde als textbasierte Anwendung umgesetzt. Ergänzend sind Diagramme, eine Dokumentation auf Deepnote, ein Präsentationsvideo sowie ein Projektboard auf GitHub vorhanden.

Wir haben generative Tools wie ChatGPT gezielt zur Problemanalyse, Strukturierung von Lösungswegen, Fehlersuche und Validierung eingesetzt – insbesondere in frühen Phasen, um Verständnisfragen zu klären und Einstiegspunkte für die Codeumsetzung zu finden. Die Umsetzung erfolgte stets eigenständig und mit Fokus auf das eigene Lernen.

---

## Anleitung für Prüfer:innen – Projekt testen & nachvollziehen

### A. Nutzung über Deepnote (empfohlen)

Öffnen Sie den Deepnote-Link:  
[Zum Projekt auf Deepnote](https://deepnote.com/workspace/DBUA-Team-C-c18e3c8f-25c5-4be0-bb77-bb8f6a66300d/project/AEP-B6-9cb1cc5b-60cb-4063-9234-00e840489c38/notebook/AEP-B6-a186cbbb02284c55b13524202bbe26ed)

Dort findet ihr:
- Ausführbare Projekt-Notebooks
- SQL-Abfragen mit Resultaten
- Visualisierungen (Charts)
- Kommentierte Codeabschnitte zur Erklärung

---

### B. Lokale Ausführung (für Python-Nutzer:innen)

#### Voraussetzungen
- Python 3.11 oder höher
- Optional: Visual Studio Code als IDE

#### Ausführungsschritte
1. Repository klonen:
   ```bash
   git clone https://github.com/AEP-Team-B6/Team-B6-Repo.git
   ```

2. In das Projektverzeichnis wechseln und sicherstellen, dass sich die Datei  
   `hotel_reservation_sample.db` im Ordner `/database` befindet.

3. Projekt starten:
   ```bash
   python main.py
   ```

4. Die Anwendung läuft in der Konsole. Navigieren Sie durch die Menüs, um Hotels zu suchen, Zimmer zu buchen oder Stammdaten zu verwalten.

---

### Architekturüberblick

Unser Projekt basiert auf einem mehrschichtigen Modell mit folgenden Layern:

- `model`: Datenklassen (Hotel, Guest, Room etc.)
- `data_access`: SQL-Operationen, getrennt vom Businesscode
- `business_logic`: Anwendung der Regeln & Steuerung des Ablaufs
- `ui`: Konsoleninterface für Eingabe & Ausgabe

Diese Struktur erlaubt eine klare Trennung von Zuständigkeiten und erleichtert Wartung & Erweiterung.

---

### Wichtige Hinweise

- Das Projekt nutzt **ausschliesslich Python-Standardbibliotheken** – keine externen Libraries erforderlich.
- In der Anwendung wird die ursprüngliche Datenbank hotel_reservation_sample.db zu Testzwecken kopiert und als current_db.db  gespeichert. Alle Änderungen erfolgen ausschliesslich auf dieser Kopie, sodass die Originaldatenbank erhalten bleibt.
- Der Quellcode ist kommentiert und folgt den Prinzipien von **KISS** und **DRY**.
- Testdatensätze sind in der Datenbank bereits enthalten.

---

Vielen Dank für eure Zeit und die Bewertung unserer Arbeit!
