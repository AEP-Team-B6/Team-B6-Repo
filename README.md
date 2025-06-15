# Team-B6-Repo  
This is the repository of **Team B6**  
Module Application Development with Python  
Akishan Arichchandran  
Nils Strehle  
Noah Rolli  
Thiemo Frei  
Fachhochschule Nordwestschweiz  
Business Artificial Intelligence  

## SCRUM Project Management:  
https://github.com/orgs/AEP-Team-B6/projects/1  

## Link to Deepnote Documentation  
https://deepnote.com/workspace/DBUA-Team-C-c18e3c8f-25c5-4be0-bb77-bb8f6a66300d/project/AEP-B6-9cb1cc5b-60cb-4063-9234-00e840489c38/notebook/AEP-B6-a186cbbb02284c55b13524202bbe26ed?utm_content=9cb1cc5b-60cb-4063-9234-00e840489c38  

## Rollen der Projektmitglieder
### Thiemo Frei:
* Aufsetzen von Github
* Aufsetzen der Projektstruktur
* Implementierung Github in Deepnote
* Implementierung aller Importe im Deepnote und in Main
* Erstellen des Projekt-Boards und der Iterationen
* Erstellen und Verwalten der Tasks
* Unterstützen der Teammitglieder bei Fragen zu VS-Code, OOP und US
* Implementierung US 1.1-1.5, 2.1, 2.2, DB 2, DB 2.1, 7, Vis 1
* Erweitern der Datenbank mit weiteren Instanzen für besseres Testing
* Aufsetzen der Dokumentationsstruktur

### Nils Strehle
* Erstellen des Class Diagram
* Aufsetzen der VS Code Struktur
    * OOP-Struktur: Aufbau des gesamten Datenmodells (Model Klassen mit Getter und Setter)
    * Modularisierung: Trennung in model, data_access und business_logic für sauberes Layer-Modell
* Unterstützen der Teammitglieder bei Fragen zu VS-Code, OOP und US
* Implementierung der US 1.6, 4, 8, 9, 10
* Erweitern der Datenbank mit weiteren Instanzen für besseres Testing
* Fehleranalyse und Debugging: Laufende Fehlerbehebung im Livebetrieb
* Finaler Code-Clean-Up mit folgenden Tätigkeiten über den gesamten Code
    * Fehlerbehandlung: Konsistente Exception-Logik, u.a. in Eingabefeldern, Datumskontrollen und DB-Logik
    * DB-Debugging: Analyse und Fix von Tabelleninkonsistenzen
    * Validierung: Absicherung gegen doppelte Buchungen, falsche Eingaben, Vergangenheitstermine, ungültige IDs etc.
    * Docstrings & Kommentare: Einheitliche deutschsprachige Dokumentation und Kommentare im Code
    * Strukturierung & Übersicht: Umfassende Refactorings zur Einhaltung von Clean Code-Prinzipien
* Präsentationsvorbereitung: Skriptarbeit und Struktur für Video-Demo, inkl. Fokus auf zentrale Stories

### Akishan Arichchandran 
* 
* 
* 

### Noah Rolli
* Erstellen der Klassen
* US 3.1, 3.2; 3.3 zu 10 hinzugefügt  
* Dokumentation Deepnote
* README

## Projekt Struktur
Dieses Projekt folgt einer mehrschichtigen Architektur, bei der jede Schicht (Layer) eine klar abgegrenzte Aufgabe erfüllt. Dadurch wird das System übersichtlich, wartbar und leicht erweiterbar. Im Folgenden wird jede Schicht erläutert:

### .model
Der model-Layer enthält die zentralen Datenstrukturen (z. B. Hotel, Room, Address). Diese Klassen definieren, welche Eigenschaften ein Objekt besitzt und dienen als gemeinsame Schnittstelle zwischen Datenbank, Logik und UI. Sie ermöglichen eine strukturierte und typisierte Datenverarbeitung. Durch die Trennung von Struktur und Verarbeitung bleibt der Code übersichtlich.

### .database
Dieser Layer ist für die technische Anbindung der Datenbank zuständig. Hier befinden sich Konfigurationsdateien und Methoden zur Initialisierung der Verbindung. Auch die Datenbankengine oder -pfade sind hier definiert. Diese Schicht liegt direkt an der Datenquelle und wird vom data_access-Layer genutzt. Die Datei __init__.py macht das Verzeichnis als Modul importierbar.

### .data_access
Der data_access-Layer kümmert sich um den konkreten Zugriff auf Datenobjekte: Hotels lesen, Adressen erstellen, Buchungen löschen usw. Er nutzt die Modelle aus dem model-Layer und arbeitet mit dem database-Layer zusammen. Hier wird definiert, wie Daten per SQL gelesen, geschrieben oder gelöscht werden. 
Ein grosser Vorteil dieser Struktur: Möchte man auf einen anderen Datenbanktyp umstellen, muss nur der data_access-Layer angepasst werden – model, business_logic und ui können unverändert bleiben. Damit trennt dieser Layer technische Datenoperationen sauber von der fachlichen Logik.

### .business_logic
Dieser Layer dient als Connektor "Proxy". Funktionen wie z. B. ob ein Hotel gelöscht werden darf oder wie Preise berechnet werden, haben wir aus praktischen Gründen direkt im main.py implementiert. Dies entspricht nicht vollständig objektorientierten Prinzipien, orientiert sich jedoch am Referenzprojekt und wurde bewusst so umgesetzt.

### .ui
Die ui-Schicht enthält mit input_helper.py Hilfsfunktionen zur Eingabevalidierung und Fehlerbehandlung. Die zentrale Benutzerlogik und alle User Stories sind direkt in main.py umgesetzt. Die UI dient somit als technische Unterstützung und nicht als eigenständige Interaktionsschicht. Die Benutzerinteraktion erfolgt direkt über das Deepnote.

### main.py
Die Datei main.py enthält alle Benutzerinteraktionen und ruft die benötigten Funktionen zur ausfürung der User Stories auf. Eine Trennung in eine separate UI-Schicht erfolgt hier nicht, was hier jedoch beabsichtigt ist. Die zusammenarbeit im Team war für uns so am unkomplizierstesten. 

## Anwendung von KISS

**KISS** steht für *Keep It Simple, Stupid* – ein Prinzip der Softwareentwicklung, das besagt, dass Systeme möglichst einfach, verständlich und wartbar gestaltet werden sollen. Komplexität soll nur dort entstehen, wo sie notwendig ist.

**Angewendet bei uns:**
- **Modularisierung:** Jede Klasse erfüllt eine klar definierte Aufgabe (z. B. `Address`, `Room`, `Booking`). Die Aufteilung in `model`, `data_access`, `business_logic` etc. reduziert Abhängigkeiten und hält jede Schicht fokussiert.
- **Einfache UI:** Statt ein komplexes GUI zu bauen, setzen wir auf eine klar strukturierte **Konsolenanwendung** mit einem zentralen `main.py` und der Hilfsklasse `input_helper`, die Eingaben validiert.
- **Wenige externe Libraries:** Wir haben bewusst auf Drittbibliotheken verzichtet (ausser SQLite), um Abhängigkeiten gering zu halten.

**Verbesserungspotenzial:**
- Einige Methoden (z. B. in `BookingManager`) könnten weiter aufgeteilt werden, um sie einfacher test- und wiederverwendbar zu machen.
- In der `main.py` sind einige Logiken noch leicht verschachtelt – eine zusätzliche Aufteilung in logische Blöcke oder Funktionen würde die Lesbarkeit weiter verbessern.


## Anwendung von DRY
**DRY** steht für *Don't Repeat Yourself* – also die Vermeidung von Redundanzen im Code.

**Angewendet bei:**
- Gemeinsame Eingabevalidierung durch `input_helper.py`
- Getter-/Setter-Struktur zur Wiederverwendung von Logik
- Gemeinsame Methoden für Datenbankzugriffe in `base_data_access.py`

**Verbesserungspotenzial:**
- Wiederholte SQL-Statements könnten in Hilfsmethoden ausgelagert werden


## Klassendiagram

![Logo](/images/Class_Diagram_v3.png) 


Address
Funktion: Repräsentiert die Adresse eines Hotels oder Gastes.
Attribute: Strasse, PLZ, Stadt, ID.
Getter/Setter: vorhanden z. B. street(), zip_code(), city().
Besonderheit: Wird als eigene Klasse eingebunden, um Redundanz zu vermeiden (1:n-Beziehung zu Hotel und Guest)

Guest
Funktion: Enthält persönliche Daten eines Gasts und referenzierte Buchungen.
Wichtige Attribute: first_name, last_name, email, address
Getter/Setter: vorhanden für alle Attribute.
Besonderheit: Enthält eine Liste von Buchungen (bookings), sowie Methoden um Buchungen hinzuzufügen und zu entfernen.

Booking
Funktion: Beschreibt eine einzelne Buchung zwischen Gast und Zimmer.
Wichtige Attribute: check_in_date, check_out_date, is_cancelled
Getter/Setter: vorhanden.
Besonderheit: Enthält zusätzlich das Attribut is_cancelled zur Stornierungskennzeichnung. Sowie eine Methode um Review zu verknüpfen.

Invoice
Funktion: Repräsentiert die Rechnung zu einer Buchung.
Wichtige Attribute: issue_date, total_amount
Getter/Setter: vorhanden, z. B. total_amount()
Besonderheit: Composition und 1:1-Verknüpfung mit einer Buchung.
Das Attribut "invoice_status" wurde der DB ergänzt, um einzusehen, ob die Rechnung "Offen", "Bezahlt" oder "Storniert" ist.

Hotel
Funktion: Repräsentiert ein Hotel mit Name, Adresse und Zimmern.
Wichtige Attribute: name, stars, address, rooms, reviews
Getter/Setter: vollständig vorhanden.
Abweichung:
    Referenziert Liste von Room-Objekten
    Reviews als Liste zum Hotel zugehörig mit einer Methode diese zu referenzieren

Room
Funktion: Beschreibt ein konkretes Zimmer eines Hotels.
Wichtige Attribute: room_number, price_per_night, price_per_night_ls, type
Getter/Setter: vorhanden.
Abweichung:
    price_per_night_ls wurde hinzugefügt (z. B. für Nebensaisonpreise)
    room_facility als Liste um direkt über die Facilities pro Room zu referenzieren

Room_Facility
Funktion: Verknüpfungstabelle zwischen Room und Facility (n:m-Beziehung).
Wichtige Attribute: room, facility
Getter/Setter: vorhanden.
Besonderheit: Ermöglicht flexible Zuordnung beliebiger Ausstattungen pro Zimmer.

Facility
Funktion: Repräsentiert eine Ausstattung wie WLAN, TV etc.
Wichtige Attribute: facility_name
Getter/Setter: vorhanden.
Besonderheit: Wird über Room_Facility zugeordnet.

Room_Type
Funktion: Definiert Zimmerkategorien (Einzelzimmer, Suite etc.).
Wichtige Attribute: description, max_guests
Getter/Setter: vorhanden.
Besonderheit: Wird als Fremdschlüssel in Room verwendet.

Review (neu hinzugefügt)
Funktion: Repräsentiert Bewertungen durch Gäste für Hotels oder Zimmer.
Wichtige Attribute: rating, comment
Getter/Setter: vorhanden.
Besonderheit: Wird mit Hotel und Booking verknüpft, sodass das Review korrekt zugeordnet wird.

Abweichungen & Ergänzungen zusammengefasst:
- price_per_night_ls in Room: Zweiter Preis für Nebensaison/Sondertarife
- Review-Klasse: Neue Entität zur Qualitätsbewertung
- Referenzierte Attribute aus anderen Klassen ergänzt um Zugriff zu erleichtern.
- Testinstanzen: Zusätzliche Datensätze zum manuellen oder automatisierten Test

Hinweis zu Getter/Setter:
Alle Klassen verwenden klassische Getter- und Setter-Methoden zur sicheren Kapselung von Attributen, z. B. get_name(), set_name(name: str), wie im OOP-Stil üblich.


## Projektmanagement und Planung
Unser Projekt wurde nach der agilen Methodik SCRUM organisiert. Ziel war es, das Hotelbuchungssystem schrittweise in funktionalen Inkrementen zu entwickeln, mit regelmässiger Abstimmung im Team. Dabei haben wir bewusst auf iteratives Arbeiten und kurze Kommunikationswege gesetzt.

Zur Aufgabenplanung und Fortschrittsverfolgung haben wir das GitHub Project Board genutzt. Alle Aufgaben wurden dort in Form von Issues und Cards gepflegt, priorisiert und einzelnen Teammitgliedern zugewiesen.
Wir haben darauf geachtet, nach jedem abgeschlossenen Codeblock regelmässig zu committen, um die Nachvollziehbarkeit und Versionskontrolle zu gewährleisten.

Die Codequalität wurde durch Code Reviews und manuelle sowie automatische Tests sichergestellt. Vor der Integration grösserer Features wurde der Code von anderen Teammitgliedern geprüft, wodurch Fehler frühzeitig erkannt und beseitigt werden konnten.

Obwohl wir nach dem SCRUM-Vorgehen gearbeitet haben, konnten wir aufgrund des engen Zeitrahmens keine vollständigen Sprint-Zyklen mit schriftlichen Retrospektiven durchführen. Stattdessen fanden regelmässige Abgleichsmeetings statt, in denen wir Aufgaben abgestimmt, Probleme diskutiert und Anpassungen vorgenommen haben.

Diese agile, pragmatische Vorgehensweise hat es uns ermöglicht, das Projekt fokussiert, kollaborativ und flexibel umzusetzen.


## Fazit
### Was haben wir gelernt?

Im Verlauf des Moduls „Anwendungsentwicklung mit Python“ haben wir zentrale Konzepte der Softwareentwicklung kennengelernt und direkt im Projekt angewendet:

- **Grundlagen von Python:** Wir starteten mit Variablen, Datentypen, Benutzerinteraktion (Input), Bedingungen (if-else) und unveränderlichen Strukturen wie Tuples.
- **Objektorientierte Programmierung (OOP):** Wir lernten Klassen, Objekte, Kapselung (Getter/Setter), Vererbung, sowie Beziehungen wie Assoziation, Aggregation und Komposition kennen – alles essentielle Bausteine für wartbaren Code.
- **Mehrschichtige Architektur:** Durch die Layer `model`, `data_access`, `business_logic` und `ui` konnten wir klare Verantwortlichkeiten definieren und eine robuste Projektstruktur umsetzen.
- **Datenbankintegration:** Wir haben SQLite über Python angebunden und gelernt, Datenbankoperationen sicher (mit `cursor`, `fetchall()` etc.) und gekapselt über DataAccess-Klassen umzusetzen.
- **Clean Code Prinzipien:** Mit den Konzepten **DRY** und **KISS** sowie gezieltem Error Handling haben wir gelernt, unseren Code lesbar, wartbar und fehlertolerant zu gestalten.

Diese Kompetenzen haben uns befähigt, ein reales Softwareprojekt zu planen, umzusetzen und in einem Team erfolgreich abzuschliessen.

### Hürden und Lernprozess

Wie bei jedem echten Projekt standen auch wir vor Herausforderungen – insbesondere in der Anfangsphase. Zu Beginn galt es, die neuen Konzepte aus dem Unterricht zu verarbeiten und eine geeignete technische Struktur für das Projekt zu finden. Statt mit einer festen Rollenverteilung zu starten, entschieden wir uns bewusst dafür, individuell zu lernen, zu experimentieren und erste Bausteine eigenständig zu entwickeln.

Diese Phase war wichtig, um ein gemeinsames Grundverständnis für Python und OOP aufzubauen. Unterstützung fanden wir dabei sowohl im Unterricht als auch durch externe Plattformen wie Codefinity. Als die Klassenattribute und -beziehungen im Unterricht behandelt wurden, hatten wir unseren inhaltlichen Anker gefunden – ab da konnten wir strukturiert und zielgerichtet arbeiten.

### Zusammenarbeit im Team

Unser Team hatte sich bereits im ersten Semester bewährt – deshalb war schnell klar, dass wir die Zusammenarbeit fortsetzen wollten. Auch wenn wir diesmal anfangs mit einem etwas lockereren Setup starteten, gelang es uns, die Stärken jedes Einzelnen optimal zu nutzen.

Besonders in der Schlussphase haben wir gezielt Aufgaben verteilt: Zwei Mitglieder konzentrierten sich auf die finalen Features und den Code-Feinschliff, während die anderen beiden die Dokumentation und Präsentation verantworteten. Diese pragmatische, rollenbasierte Arbeitsweise hat sich bewährt und unsere Effizienz deutlich gesteigert.

### Abschluss

Das Projekt hat uns gezeigt, wie viel man durch eigenständiges Arbeiten, Teamkommunikation und konsequente Strukturierung erreichen kann. Wir konnten viele Konzepte aus dem ersten Semester weiterentwickeln – insbesondere unser lösungsorientiertes Vorgehen und die Fähigkeit, unter Zeitdruck produktiv und fokussiert zusammenzuarbeiten. Dieses Projekt hat nicht nur unser technisches Verständnis, sondern auch unsere Teamkompetenz gestärkt.


## Quellen & Tools

- Moodle-Unterlagen (FHNW Modul Anwendungsentwicklung)
- Codefinity (Python Tutorials)
- Visual Paradigm (UML-Modellierung)
- SQLiteOnline (SQL-Testing)
- Deepnote (Cloud IDE & Visualisierung)
- GitHub (Versionierung & Kollaboration)
- Visual Studio Code (lokale Entwicklung, Debugging, Git-Integration)
- ChatGPT (Fehleranalyse, Optimierungsvorschläge)