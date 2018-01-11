# nim
Game-AI-Development in Python

# How to start the game
Just run the python file 'startGame.py' with a compatible python environment.
e.G. "python startGame.py"

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
