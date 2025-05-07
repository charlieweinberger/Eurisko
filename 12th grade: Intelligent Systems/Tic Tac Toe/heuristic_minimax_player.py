from tic_tac_toe import *
from reduced_search_game_tree import *

class HeuristicMinimaxPlayer():
    
    def __init__(self, ply):
        self.player_number = None
        self.ply = ply
    
    def set_player_number(self, player_number):
        self.player_number = player_number
        self.game = ReducedSearchTree([[None for _ in range(3)] for _ in range(3)], self.player_number, self.ply)
        self.game.build_tree()
        self.game.root.set_score()

    def choose_move(self, state):

        for node in self.game.root.children:
            if node.score == max(node.score for node in self.game.root.children):  

                for i in range(3):
                    for j in range(3):
                        if self.game.root.state[i][j] != node.state[i][j]:
                            return (i, j)
        
    def update_state(self, state):

        for child in self.game.root.children:
            if child.state == state:

                self.game.root = child
                self.game.root.depth = 0
                
                self.game.player_number = self.player_number
                self.game.current_nodes = [self.game.root]
                self.game.all_nodes = {str(state):self.game.root}
                
                self.game.build_tree()
                self.game.root.set_score()
                
                break