# Nim
Spiele-KI-Entwicklung in Python

Nim ist ein Spiel für zwei Personen, bei welchem abwechselnd eine Anzahl von Gegenständen(wie z.B. Streichhölzer) weggenommen werden. Dabei darf jede Person, wenn sie am Zug ist, eine beliebige Anzahl von Hölzern in einer Reihe wegnehmen. Sie darf allerdings nicht aus verschiedenen Reihen im gleichen Zug Hölzer wegnehmen. In diesem Projekt wird in der Misère-Variante gespielt, sodass derjenige verliert, der das letzte Hölzchen wegnimmt.

# Ausführen des Spiels
Um das Spiel starten zu können, muss die Datei `startGame.py` mit einer kompatiblen Python Umgebung ausgeführt werden. (z.B. `python startGame.py`)

## Settings
In diesem Bereich hat man mehrere Möglichkeiten, das Spiel einzustellen.

### Spielertyp

Der Spielertyp ist für jeden Spieler individuell einstellbar. Hierfür ist es notwendig, den entsprechenden Spieler(z.B. Player 1) auszuwählen und diesem dann im nachfolgenden Untermenü einen Spielertyp zuzuweisen und mit **Save** bestätigen. Für den Spielertyp gibt es folgende Auswahlmöglichkeiten:

#### Manueller Spieler
Beim manuellen Spieler(wie der Name schon sagt) muss man selbst die Züge durch Anklicken der Spielsteine vornehmen.
 
#### Zufälliger Spieler
Beim zufälligen Spieler werden durch die KI pro Zug zufällige Spielsteine ausgewählt, welche man im Nachhinein  auch nicht mehr verändern kann.

#### Perfekter Spieler
Der perfekte Spieler spielt stets nach einer Gewinnstrategie und macht keinen falschen Zug, außer er selber ist bereits von Anfang an in einer Verluststellung.
 
#### Q-Learning Spieler
**ACHTUNG**: Dieser Spieler ist von Anfang an nicht spielfähig, sondern muss erst 
"trainiert" werden(Siehe Abschnitt "How to train Q-Learning Player"). Sobald er trainiert wurde, ist er dem Perfekten Spieler gleichzusetzen, da er über einen komplexen und langwierigen Algorithmus trainiert wurde. (siehe Abschnitt Q-Learning). 

### Gamesize
Darüber hinaus hat man die Möglichkeit, die Spielfeldgröße anzupassen. Die Ziffern geben die Anzahl der Spielsteine pro Reihe(von oben nach unten) an. An dieser Stelle kann beispielsweise die Spielfeldgröße **[5, 4, 3]** gewählt und anschließend mit **save** bestätigt werden.
**ACHTUNG**: Tritt in dem darauf folgendem Spiel ein Q-Learning Spieler an, so muss darauf geachtet werden, dass man hier die selbe Spielfeldgröße wählt, die man ebenso beim Trainieren für den Q-Learning Spieler verwendet hat, da sonst die Größe der Q-Matrix nicht übereinstimmt.

Hat man alle Einstellungen vorgenommen, kann das Spiel beginnen!



## Spielbeginn & Spielablauf
Durch Klicken auf **Start Game** im Hauptfenster beginnt das Spiel. Die UI zeigt durch eine <span style="background-color:yellow">gelbe Markierung</span> an, welcher Spieler im Moment am Zug ist. Ein manueller Spieler muss zunächst seine Spielsteine auswählen und anschließend den Zug durch **make turn** bestätigen. Bei allen anderen Spielern reicht es jedoch aus, den nächsten Zug sofort mit **make turn** in die Wege zu leiten. Nimmt ein Spieler den letzten Spielstein, signalisiert die UI das Ende des Spiels und zeigt in einem Pop-Up-Fenster den Gewinner an.

# Training des Q-Learning Spielers
Für das Training des Q-Learning Spielers wird das Skript `QTrainer.py` über python gestartet (`python QTrainer.py`).
Nun kann die Größe des Spielfeldes eingegeben und der Trainingsprozess gestartet werden.
Die Dauer des Trainingsprozesses is abhängig von der Spielfeldgröße.

Nach Abschluss des Trainings befindet sich das zugehörige Savefile im Verzeichnis `q_learning/saveFile`.

Der Trainingsprozess kann darüberhinaus auch visualisiert werden. Dazu muss die Variable `ENABLE_VISU` im Skript `q_learning/Trainer.py` auf `True` gesetzt werden. Der Trainingsprozess wird dadurch allerdings stark verlangsamt.

# Abhängigkeiten
- python 3.6
- wxpython
- pillow
- numpy
- random
- matplotlib

## Installation mit anaconda
- conda install wxpython -c conda-forge
- conda install pillow -c conda-forge
- conda install numpy
- conda install matplotlib -c conda-forge

## Installation mit pip
- pip install wxpython
- pip install pillow
- pip install numpy
- pip install random
- pip install matplotlib

* * *

# Das Projekt ##
Das Nim-Projekt lässt sich in vier Unterkategorien unterteilen:

1. User Interface (UI)
2. Spiellogik & Manueller Spieler
3. Künstliche Intelligenz (KI) & Zufälliger Spieler
4. Q-Learning & Q-Learning Spieler

Nachfolgend wird jede Unterkategorie im Detail erläutert.

## User Interface (UI)

## Spiellogik & Manueller Spieler
Für die Implementierung von Nim muss zunächst der Spielzustand dargestellt werden. Basierend auf diesem können die verschiedenen Spieler agieren und es kann geprüft werden, ob ein Zug eines Spielers gültig ist oder ob er gewonnen hat.

### Implementierung
Die Komponenten der Spiellogik sind in dem Verzeichnis `logic` zu finden. Es handelt sich dabei um:
- `State.py` - Implementierung eines Spielzustands
- `GameLogic.py` - Implementierung der Methoden zur Prüfung eines Spielzugs

Im folgenden werden die Funktionalitäten für die Spiellogik beschrieben.

**`State.py`**
Die Klasse `State` stellt einen Spielzustand über eine `typing.List` von `numpy arrays` dar. Dabei steht jedes `array` für eine Reihe von Objekten, das genau soviele Elemente enthält wie es Objekte gibt. 
Der Startspielzustand initialisiert alle Elemente der `arrays` mit `1`. Wird ein Element entfernt, so wird an der entsprechenden Stelle der verschachtelten Liste eine `1` durch eine `0` ersetzt. Hierfür steht die Methode `toggle_pearl` zur Verfügung.
Für den perfekten Spieler wird die Umwandlung des Spielzustands in eine Binärdarstellung benötigt (siehe Gewinnstrategie nach Bouton). Dafür wurde die Methode `to_binary_representation` implementiert.

**`GameLogic.py`**
Die Spiellogik prüft, ob der Zug eines Spielers erlaub ist (`is_valid`) und ob ein Spieler gewonnen hat (`has_won`).

## Künstliche Intelligenz (KI) & Zufälliger Spieler
In diesem Abschnitt wird insbesondere auf die beiden Python-Files `ai/perfectPlayer.py` und `ai/randomPlayer.py` eingegangen. Das Ziel war es, einen perfekten Spieler nach einer vorgegeben Gewinnstrategie zu realisieren. Zusätzlich sollte noch ein zufälliger Spieler entwickelt werden, der rein zufällige, aber dennoch erlaubte Spielzüge vornimmt.

Beide Spieler beziehen sich das Interface *Player* aus `player/Player.py`, wodurch für jeden Spieler eine individuelle *step-Methode* bereitsteht, welche den nächsten Zustand des Spielfeldes übergibt. Als Zustand wird diesbezüglich die Spielsteine in Form eines Arrays aus Einsen und Nullen bezeichnet. Darüber hinaus werden die beiden Spieler über das *Dictionary* aus `player/PlayerDict.py` bei der Konstruktion automatisch richtig initialisiert.

### Der perfekte Spieler
Der perfekte Spieler folgt stets der sogenannten **Gewinnstrategie nach Bouton**.

#### Gewinnstrategie nach Bouton
In dieser Gewinnstrategie werden die Spielsteine pro Reihe binär dargestellt. Daraus werden wiederum Spaltensummen berechnet, wodurch sich  aus der erhaltenen "Spaltensummen-Reihe" anschließend eine Verlust-/Gewinnstellung erkennen lässt. Errechnet sich für den ziehenden Spieler eine Stellung mit nur geraden Spaltensummen, so ist dies eine Verluststellung. Dies würde für den ziehenden Spieler bedeuten, dass er bei einem perfekten Spiel des Gegners verlieren würde. Errechnet sich hingegen für den ziehenden Spieler eine Stellung mit mindestens einer ungeraden Spaltensumme, so ist dies eine Gewinnstellung. Der ziehende Spieler hat demnach die Möglichkeit, eine Stellung mit nur geraden Spaltensummen mit dem nächsten Zug zu erreichen, sodass bei einem eigenen perfekten Spiel der ziehende Spieler gewinnen würde. Nachfolgendes Beispiel veranschaulicht diese Gewinnstrategie:

    | | |
    
    | | | |
    
    | | | | |
Im obigen Beispiel sind fünf Reihen zu 3, 4 und 5 Streichhölzern zu sehen. Wandelt man nun diese Reihen in Binärzahlen um, so ergibt sich folgende Berechnung:

    0-1-1 (Binärzahl von 3)
    1-0-0 (Binärzahl von 4)
    1-0-1 (Binärzahl von 5)
	------------------------------------------
	2-1-2 (Spaltensummen der einzelnen Reihen)
 
Da nun die 1 eine ungerade Zahl darstellt, ist dies für den ziehenden Spieler eine Gewinnstellung. Er hat nun die Möglichkeit, mit einem Zug nur gerade Spaltensummen zu erzeugen. Daher nimmt er nun aus der obersten Reihe beispielsweise 2 Spielsteine weg. Man erhält also folgende Spielstellung:

    |
    
    | | | |
    
    | | | | |
Daraus lassen sich nun wieder die Spaltensummen errechnen:

    0-0-1 (Binärzahl von 1)
    1-0-0 (Binärzahl von 4)
    1-0-1 (Binärzahl von 5)
	------------------------------------------
	2-0-2 (Spaltensummen der einzelnen Reihen)

Der Gegner erhält also eine Stellung mit nur geraden Spaltensummen und bekommt demnach eine Verluststellung.

### Der zufällige Spieler
Wenn der zufällige Spieler am Zug ist, wählt er stets eine zufällige Reihe aus, in welcher noch Spielsteine vorhanden sind. Anschließend wählt er eine zufällige Anzahl an Spielsteinen in dieser Reihe aus und entfernt diese. Er folgt demnach keiner Strategie, sondern bezieht sich ausschließlich auf eine Zufallsfunktion während seinem Zug.

### Implementierung
Die für den perfekten/zufälligen Spieler relevanten Komponenten sind in dem Verzeichnis `ai` zu finden. Nachfolgend sind diese kurz vorgestellt:

- `perfectPlayer.py` - Implementierung des perfekten Spielers inkl. Gewinnstrategie
- `randomPlayer.py` - Implementierung des zufälligen Spielers

Diesbezüglich werden im Folgenden die wesentlichen Funktionen erläutert:

**`perfectPlayer.py`**

Der perfekte Spieler entscheidet zunächst, ob für ihn aktuell eine Gewinnstellung oder eine Verluststellung vorliegt. Diese Überprüfung erlangt er durch die Funktion `is_winning_sate`, welche die bereits erläuterte Gewinnstrategie enthält. Erhält der perfekte Spieler vor seinem Zug eine Gewinnstellung, so ist es ihm nicht möglich mit seinem nachfolgenden Zug ebenso eine Gewinnstellung zu erzeugen. Aus diesem Grund wählt er das Prinzip des "minimalen Schadens" an und entfernt einen einzigen Spielstein aus den verbliebenen Spielsteinen mit der Methode `get_next_best_possible_state`. Erhält er hingegen eine Verluststellung, so versucht er innerhalb der Funktion `get_next_perfect_state` aus den vorhandenen Spielsteinen eine Gewinnstellung zu erzeugen, um diese als nächsten Zustand zu übermitteln.

**`randomPlayer.py`**

Beim zufälligen Spieler wird lediglich in der Methode `pick_random_pearls` überprüft, an welchen Stellen noch verfügbare Spielsteine vorhanden sind. Anschließend wird per Zufallsprinzip eine Reihe ausgewählt und eine zufällige Anzahl der noch vorhandenen Spielsteine entfernt und somit als nächsten Zustand übermittelt.

## Q-Learning
In diesem Abschnitt wird auf das Verfahren Q-Learning und die umgesetzten Komponenten eingegangen. Das Ziel war es, einen Spieler mit dem Verfahren Q-Learning zu implementieren und diesen für das Spiel Nim zu trainieren.

### Q-Learning
Q-Learning ist ein modellfreies Verfahren des Reinforcement Learnings. Ziel ist es, eine optimale Verhaltensstrategie für einen Agenten in einer vorgegebenen Umgebung zu erlernen. Hierbei steht kein Modell dieser Umgebung bereit. Das heißt, das Verfahren muss die optimale Strategie durch die Interaktion mit der Umgebung erlernen. 

![Agent Umgebungsinteraktion](https://cdn-images-1.medium.com/max/1600/1*Z2yMvuQ1-t5Ol1ac_W4dOQ.png)

Im Rahmen einer Interaktion gibt das Q-Learning Verfahren eine Aktion vor, auf welche die Umgebung mit einem Feedback und dem neuen Zustand reagiert. Das Feedback kann dabei direkt jeden Interaktionsschritt bewerten oder diese als *neutral* einstufen und erst bei einem bestimmten Ereignis, z.B. im Falle von Nim, bei Gewinn oder Verlust, ein bedeutungsvolles Feedback übergeben. Somit lernt das Verfahren, ob die gewählte Aktion in dem entsprechenden Zustand positiv ist.

Nach und nach wird im Rahmen von vielen Interaktionen jede mögliche Aktion für jeden möglichen Zustand bewertet. Neben dem Feedback der Umgebung fließen außerdem die bereits erlernten Kentnisse in die Bewertung mit ein. Somit werden Aktionen besser eingestuft, welche nach dem eigenen Kenntnisstand, einen guten Nachfolgezustand bewirken. Das heißt, Aktionen werden besser bewertet, wenn diese direkt oder indirekt zu einem positiven Feedback führen. In einem iterativen Prozess wird durch die wiederholte Interaktion mit der Umgebung die optimale Strategie ausgehend von einem Gewinnzustand ermittelt und bis in die Anfangszustände zurückgeführt.

Die folgende Formel zeigt die beschriebene Lernstrategie auf:

![Q-Learning](http://latex.codecogs.com/gif.latex?Q%28state,%20action%29%20=%20Reward%28state,%20action%29%20+%20\gamma%20%5C%3Bmax%28Q%28nextState,%20*%29%29)

### Nichtdeterministische Umgebung
Da das Spiel Nim abwechselnd von zwei Spielern gespielt wird, ergibt sich ein nicht deterministisches Verhalten für das Q-Learning Verfahren. Die vom Q-Learning ausgewählte Aktion führt zwar deterministisch in einen Nachfolgezustand, allerdings ist dieser nur für den anderen Spieler, welcher nun am Zug ist, von Interesse. Erst die Aktion dieses zweiten Spielers bestimmt, welcher Zustand das Q-Learning Verfahren im nächsten Schritt erwartet. Der zweite Spieler und seine Aktionen sind aus der Sicht des Q-Learning Verfahrens somit Teil einer nichtdeterministischen Umgebung.

Statt der eben aufgezeigten Formel, kommt somit die folgende zum Einsatz:

![](http://latex.codecogs.com/gif.latex?Q%28state,%20action%29%20=%20Q%28state,action%29%20+%20\alpha%20%5b%20Reward%28state,%20action%29%20+%20\gamma%20\%5c%20max%28Q%28nextState,%20*%29%29%20-%20\alpha\%5c%20Q%28state,action%29%5d)

### Exploration vs. Exploitation
Beim Lernvorgang muss das Q-Learning für jede Interaktion eine Aktion wählen. Die Auswahl dieser Aktion ist für den Lernfortschritt von großer Bedeutung. Hierbei unterscheidet man zwischen Exploration und Exploitation.

Exploitation beschreibt eine Strategie, welche stets die bestmögliche Aktion auswählt. Diese Strategie ist für den Lernvorgang nur bedingt geeignet. Hat das Verfahren einmal eine Strategie gefunden, welche zum gewünschten Ziel führt, so wird anschließend immer nur diese Strategie verfolgt, auch wenn es andere, bessere Strategien gibt.

Die Exploration Strategie beschreibt die Auswahl zufälliger Aktionen. Somit werden, auch wenn bereits eine Strategie gefunden wurde, dennoch andere Aktionen ausgewählt und überprüft, ob diese eventuell zu einer besseren Strategie führen.

Eine Kombination aus Exploration und Exploitation ist somit für den Lernprozess ideal.

### Implementierung
Alle Komponentnen des Q-Learning sind in dem Verzeichiss `q_learning` zu finden. Im folgenden werden diese kurz vorgestellt:

- `QLearner.py` - Implementierung des Q-Learning Verfahrens
- `QPlayer.py` - Wrapper für die Verwendung als Nim-Spieler
- `Trainer.py` - Implementierung eines Trainers, welcher einen Q-Learning Spieler gegen den zufälligen Spieler trainiert
- `Evaluator.py` - Funktionen zur Evaluation des trainierten Spielers
- `Rewards.py` - Definition der Rewards für das Training
- `SaveFileManager.py` - Hilfsfunktionen zum Speichern und Laden von trainierten Spielern
- `Rewarder.py` - Hilfsfunktionen zum Training ohne GUI
- `Logger.py` - Hilfsfunktionen zum Loggen von Informationen

Im folgenden werden die wichtigsten Funktionalitäten für das Q-Learning beschrieben.

*`QLearner.py`*

Die Funktion `learnStep` wählt eine Aktion entsprechend der Exploration vs. Exploitation Strategie aus. Ist diese Aktion illegal oder führt sie zu einem direkten Sieg oder Verlust, so wird der entsprechende Reward über die Funktion `immediateReward` dem Q-Learning-Verfahren übergeben und in die Q-Matrix eingetragen. Ist dies eine Aktion ohne direktes Feedback, erfolgt die Aktualisierung der Q-Matrix, entsprechend der vorgestellten Formel über die Funktion `updateQ`.

*`QPlayer.py`*

Die QPlayer Klasse implementiert das Interface für die Kommunikation mit dem Spiel entsprechend `player/Player.py`. Die Funktion `step` ist dabei für die Auswahl der nächsten Aktion zuständig. Hierbei wird der aktuelle Zustand in eine Binärzahl konvertiert, welche den einfachen Zugriff auf die Q-Matrix erlaubt.

Beim Erstellen eines Q-Players kann außerdem ein Dateipfad, zu einer gespeicherten Q-Matrix angegeben werden. Somit kann der Q-Player mit vortrainierten Q-Matrizen initialisiert werden.

*`Trainer.py`*

Die Klasse Trainer ist für das Training eines Q-Players verantwortlich. Hierbei werden mehrere Episoden des Nim Spiels gegen den zufälligen Spieler ausgeführt. Die Parameter Learning Rate, Exploration Factor und Gamma können dabei variiert werden.

Die implementierte Trainingsstrategie beginnt mit hohen Werten für die Learning Rate (1.0) und den Exploration Factor (1.0). Sobald jedes Zustands-Aktions-Paar mindestens einmal ausprobiert wurde, werden beide Parameter verkleinert (Learning Rate = Exploration Factor = 0.3). Das Training ist beendet, sobald der Q-Player genauso gut wie der perfekte Spieler spielt.

*`Evaluator.py`*

Die Evaluation des Q-Players erfolgt durch die Klasse Evaluator. Hierbei tritt der Q-Player gegen den perfekten Spieler in mehreren Episoden an. Als Startzustand wird nach und nach jeder mögliche Zustand des Spielfeldes verwendet. Somit kann das Verhalten beider Spieler in allen möglichen Situationen verglichen werden.