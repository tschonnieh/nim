# nim
Game-AI-Development in Python

Nim ist ein Spiel für zwei Personen, bei welchem abwechselnd eine Anzahl von Gegenständen(wie z.B. Streichhölzer) weggenommen werden. Dabei darf jede Person, wenn sie am Zug ist, eine beliebige Anzahl von Hölzern in einer Reihe wegnehmen. Sie darf allerdings nicht aus verschiedenen Reihen im gleichen Zug Hölzer wegnehmen. In diesem Projekt wird in der Misère-Variante gespielt, sodass derjenige verliert, der das letzte Hölzchen wegnimmt.

# How to start the game
Just run the python file 'startGame.py' with a compatible python environment.
e.G. "python startGame.py"

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

### Game-Size
Darüber hinaus hat man die Möglichkeit, die Spielfeldgröße anzupassen. Die Ziffern geben die Anzahl der Spielsteine pro Reihe(von oben nach unten) an. An dieser Stelle kann beispielsweise die Spielfeldgröße **[5, 4, 3]** gewählt und anschließend mit **save** bestätigt werden.
**ACHTUNG**: Tritt in dem darauf folgendem Spiel ein Q-Learning Spieler an, so muss darauf geachtet werden, dass man hier die selbe Spielfeldgröße wählt, die man ebenso beim Trainieren für den Q-Learning Spieler verwendet hat, da sonst die Größe der Q-Matrix nicht übereinstimmt.

Hat man alle Einstellungen vorgenommen, kann das Spiel beginnen!



## Spielbeginn & Spielablauf
Durch Klicken auf **Start Game** im Hauptfenster beginnt das Spiel. Die UI zeigt durch eine <span style="background-color:yellow">gelbe Markierung</span> an, welcher Spieler im Moment am Zug ist. Ein manueller Spieler muss zunächst seine Spielsteine auswählen und anschließend den Zug durch **make turn** bestätigen. Bei allen anderen Spielern reicht es jedoch aus, den nächsten Zug sofort mit **make turn** in die Wege zu leiten. Nimmt ein Spieler den letzten Spielstein, signalisiert die UI das Ende des Spiels und zeigt in einem Pop-Up-Fenster den Gewinner an.

# How to train Q-Learning Player
Run the python file 'QTrainer.py' with a compatible python environment.
e.G. "python QTrainer.py"
Here you can set the size of the game board.
The training process may take some time.

After the training is finished, the corresponding savefiles
can be found under 'q_learning/saveFile'.

In order to activate the Visualization of the q-learning process, you can set 
the variable ENABLE_VISU in the file 'q_learning/Trainer.py' to True.
This will greatly increase the duration of the training process.

# Dependencies
- python 3.6
- wxpython
- pillow
- numpy
- random
- matplotlib

## How to install with anaconda
- conda install wxpython -c conda-forge
- conda install pillow -c conda-forge
- conda install numpy
- conda install matplotlib -c conda-forge

## How to install with pip
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

## Künstliche Intelligenz (KI) & Zufälliger Spieler
In diesem Abschnitt wird insbesondere auf die beiden Python-Files `ai/perfectPlayer.py` und `ai/randomPlayer.py` eingegangen. Das Ziel war es, einen perfekten Spieler nach einer vorgegeben Gewinnstrategie zu realisieren. Zusätzlich sollte noch ein zufälliger Spieler entwickelt werden, der rein zufällige, aber dennoch erlaubte Spielzüge vornimmt.

Beide Spieler beziehen sich das Interface *Player* aus `player/Player.py`, wodurch für jeden Spieler eine individuelle *step-Methode* bereitsteht, welche den nächsten Zustand des Spielfeldes übergibt. Als Zustand wird diesbezüglich die Spielsteine in Form eines Arrays aus Einsen und Nullen bezeichnet. Darüber hinaus werden die beiden Spieler über das *Dictionary* aus `player/PlayerDict.py` bei der Konstruktion automatisch richtig initialisiert.

### Der perfekte Spieler
Der perfekte Spieler folgt stets der sogenannten **Gewinnstrategie nach Bouton**.

####Gewinnstrategie nach Bouton
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
## Q-Learning & Q Learning Spieler