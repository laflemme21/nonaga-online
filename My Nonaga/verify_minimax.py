from AI import AI
from nonaga_logic import NonagaLogic
from nonaga_constants import RED, BLACK
import sys
print("starting verify_minimax.py")


def test_minimax_decisions():
    print("Starting test...")
    # 1. Initialize a specific game state
    game_state = NonagaLogic()

    print("State initialized")
    # 2. Initialize your AI with some parameters
    # Set depth=1 and depth=2 to compare behaviors
    ai_depth_1 = AI(parameter=[1, 1, 1, 1, 1, 1, 1, 1], depth=1, color=BLACK)
    ai_depth_2 = AI(parameter=[1, 1, 1, 1, 1, 1, 1, 1], depth=2, color=BLACK)
    print("AI initialized")

    # 3. Test Depth 1 Focus (Myopic)
    # The AI should purely pick the move with the highest immediate cost_function
    best_piece, best_tile = ai_depth_1.get_best_move(game_state)
    print("Depth 1 Best Move:", best_piece, best_tile)

    # 4. Test Depth 2 Focus (Tactical)
    # The AI should avoid moves that leave it vulnerable to a punishing response by the opponent
    best_piece_2, best_tile_2 = ai_depth_2.get_best_move(game_state)
    print("Depth 2 Best Move:", best_piece_2, best_tile_2)

    # 5. Overriding the cost function to trace it
    # You can monkey-patch cost_function to print out the values being evaluated at the leaf nodes
    original_cost = AI.cost_function

    def tracing_cost_function(self, state, is_max, max_c, params):
        score = original_cost(self, state, is_max, max_c, params)
        print(f"Eval Leaf -> MaxPlayer Turn: {is_max}, Score: {score}")
        return score

    AI.cost_function = tracing_cost_function
    ai_depth_2.get_best_move(game_state)


if __name__ == "__main__":
    test_minimax_decisions()
