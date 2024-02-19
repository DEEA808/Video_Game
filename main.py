from src.service.game_service import GameService
from src.domain.board import board
from src.ui.console import UI

board=board()
game_service=GameService(board)
console=UI(game_service)
console.start_game()
