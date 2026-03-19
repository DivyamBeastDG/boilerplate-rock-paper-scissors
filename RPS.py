# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
from RPS_game import quincy, kris, abbey, mrugesh

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    beat = {'R': 'P', 'P': 'S', 'S': 'R'}
    recent = opponent_history[-10:] or ['R']
    return beat[max('RPS', key=recent.count)]
    
