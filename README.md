
# Was macht dieser Ehren Kampfhelikopter?

Der Bot trackt die Ehre der unterschiedlichen Nutzer, kann von diesen verändert werden und enthält weitere tools.

# Setup

Die benötigten Module aus **requirements.txt** installieren.
In **Einstellungen/admins.txt** die Benutzer IDs der gewünschten admins eintragen, pro Zeile eine ID.
In **Einstellungen/command_prefix.txt** kann der Präfix zum ansprechen des Bots festgelegt werden (standardmäßig auf **.**).
In **Einstellungen/status_liste.txt** können unterschiedliche Sätze (einer pro Zeile) eingegeben werden, welche vom Bot angezeigt werden.
In **Einstellungen/token.txt** kommt der Token des Bots.
Beim starten des Bots werden automatisch alle Erweiterungen in **cogs/** geladen.

# Zur Benutzung:

Der Bot ist darauf ausgelegt auf nur einen Server verwendet zu werden, ansonsten werden die Ehre-Counter der unterschiedlichen Server zusammen gelegt und eventuell unbekannte Nutzer referenziert.

# Wie speichert der Bot Daten?

Unter **data/** wird bei jedem speicher eine neue json Datei erstellt, mit dem Muster: 0.json, 1.json, 2.json,... Die älteren Dateien können Problemlos gelöscht werden. Jedoch **nicht amount.json**.

# Commands

## Für alle

### ehre

#### ehre *@user* *nummer*

Addiert nummer zu der Ehre vom user, ist nummer negativ verringrt sich die Ehre. Man kann sich nicht selber Ehre nehmen oder geben. Man kann nur Ehre nehmen oder geben wenn man auch selber mitmacht. Man kann nur Leuten Ehre geben oder nehmen welche auch mitmachen.

#### neuer_ehren_kampfhelikopter *@user*

Fügt einen Nutzer hinzu, er kann jetzt Ehre nehmen oder geben und ihm kann Ehre gegeben oder genommen werden.

#### alle_ehre

Gibt die Ehre aller Nutzer aus, welche mitmachen. Auch von denen auf anderern Servern.

### lilgadgets

Probier einfach mal aus!

## Für admins

Admin Commands werden nicht im **help** Command angezeigt.

### main

#### load *Erweiterung*

Lädt eine erweiterung, ist sie bereits geladen wird in der Konsole ein Fehler ausgegeben, über Discord kann man jedoch nichts sehen.

#### unload *Erweiterung*

Entlädt eine erweiterung, ist sie bereits entladen wird in der Konsole ein Fehler ausgegeben, über Discord kann man jedoch nichts sehen.

#### reload *Erweiterung*

Entlädt eine Erweiterung und lädt sie danach wieder. Tritt ein Fehler auf ist das nur über die Konsole zu erkennen, nicht über Discord.

### ehre

#### ehre_for_ever

Speichert die jetzigen Daten in einer neuen json Datei.

### update

#### update *Erweiterung*

Lädt die Bestimmte Bestimmte Erweiterung aus diesem Github Repo herunter und ersetzt die lokale Kopie.
