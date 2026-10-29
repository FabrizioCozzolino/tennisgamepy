import unittest
from src.game import Game
from src.errors import DuplicatedPlayerError, GameHasAlreadyBeenWonError

class TestGame(unittest.TestCase):

    def setUp(self):
        """Inizializza una partita base prima di ogni test."""
        self.game = Game("Federer", "Nadal")

    # --- TEST COSTRUTTORE E NOMI ---

    def test_get_player1_name(self):
        """Verifica la lettura del nome del primo giocatore."""
        self.assertEqual(self.game.get_player1_name(), "Federer")

    def test_get_player2_name(self):
        """Verifica la lettura del nome del secondo giocatore."""
        self.assertEqual(self.game.get_player2_name(), "Nadal")

    def test_init_raises_duplicated_player_error(self):
        """Verifica che venga sollevata Un'eccezione se i due giocatori hanno lo stesso nome."""
        with self.assertRaises(DuplicatedPlayerError):
            Game("Federer", "Federer")

    # --- TEST STATO INIZIALE E PUNTEGGI STANDARD ---

    def test_initial_game_status(self):
        """Verifica che lo stato iniziale sia 'Player1 love - Player2 love'."""
        self.assertEqual(self.game.get_game_status(), "Federer love - Nadal love")

    def test_increment_player1_score(self):
        """Verifica l'aggiornamento dello stato incrementando il punteggio del giocatore 1."""
        self.game.increment_player_score("Federer")
        self.assertEqual(self.game.get_game_status(), "Federer fifteen - Nadal love")

    def test_increment_player2_score(self):
        """Verifica l'aggiornamento dello stato incrementando il punteggio del giocatore 2."""
        self.game.increment_player_score("Nadal")
        self.assertEqual(self.game.get_game_status(), "Federer love - Nadal fifteen")

    def test_game_status_fifteen_all(self):
        """Verifica lo stato sul 15-15."""
        self.game.increment_player_score("Federer")
        self.game.increment_player_score("Nadal")
        self.assertEqual(self.game.get_game_status(), "Federer fifteen - Nadal fifteen")

    def test_game_status_thirty_all(self):
        """Verifica lo stato sul 30-30."""
        for _ in range(2):
            self.game.increment_player_score("Federer")
            self.game.increment_player_score("Nadal")
        self.assertEqual(self.game.get_game_status(), "Federer thirty - Nadal thirty")

    def test_increment_non_existing_player_does_nothing(self):
        """Verifica che la chiamata con un nome non valido non modifichi il punteggio."""
        self.game.increment_player_score("Djokovic")
        self.assertEqual(self.game.get_game_status(), "Federer love - Nadal love")

    # --- TEST DEUCE (PARITÀ A 40 O PIÙ) ---

    def test_game_status_deuce_at_forty_all(self):
        """Verifica lo stato Deuce quando entrambi i giocatori hanno 3 punti (40-40)."""
        for _ in range(3):
            self.game.increment_player_score("Federer")
            self.game.increment_player_score("Nadal")

        self.assertEqual(self.game.get_game_status(), "Deuce")

    def test_game_status_deuce_after_advantage_lost(self):
        """Verifica il ritorno allo stato Deuce dopo la perdita del vantaggio."""
        for _ in range(3):
            self.game.increment_player_score("Federer")
            self.game.increment_player_score("Nadal")

        # Vantaggio Federer (4-3) e poi pareggio Nadal (4-4)
        self.game.increment_player_score("Federer")
        self.game.increment_player_score("Nadal")

        self.assertEqual(self.game.get_game_status(), "Deuce")

    # --- TEST ADVANTAGE (VANTAGGIO) ---

    def test_game_status_advantage_player1(self):
        """Verifica lo stato Advantage quando il giocatore 1 passa in vantaggio da Deuce."""
        for _ in range(3):
            self.game.increment_player_score("Federer")
            self.game.increment_player_score("Nadal")

        self.game.increment_player_score("Federer")
        self.assertEqual(self.game.get_game_status(), "Advantage Federer")

    def test_game_status_advantage_player2(self):
        """Verifica lo stato Advantage quando il giocatore 2 passa in vantaggio da Deuce."""
        for _ in range(3):
            self.game.increment_player_score("Federer")
            self.game.increment_player_score("Nadal")

        self.game.increment_player_score("Nadal")
        self.assertEqual(self.game.get_game_status(), "Advantage Nadal")

    # --- TEST VITTORIA ---

    def test_game_status_winner_player1_direct(self):
        """Verifica la vittoria del giocatore 1 con vittoria diretta (40-0 -> 4-0)."""
        for _ in range(4):
            self.game.increment_player_score("Federer")

        self.assertEqual(self.game.get_game_status(), "Federer wins")

    def test_game_status_winner_player2_direct(self):
        """Verifica la vittoria del giocatore 2 con vittoria diretta (0-40 -> 0-4)."""
        for _ in range(4):
            self.game.increment_player_score("Nadal")

        self.assertEqual(self.game.get_game_status(), "Nadal wins")

    def test_game_status_winner_player1_after_advantage(self):
        """Verifica la vittoria del giocatore 1 dopo la gestione dei vantaggi (5-3)."""
        for _ in range(3):
            self.game.increment_player_score("Federer")
            self.game.increment_player_score("Nadal")

        self.game.increment_player_score("Federer")
        self.game.increment_player_score("Federer")

        self.assertEqual(self.game.get_game_status(), "Federer wins")

    def test_game_status_winner_player2_after_advantage(self):
        """Verifica la vittoria del giocatore 2 dopo la gestione dei vantaggi (3-5)."""
        for _ in range(3):
            self.game.increment_player_score("Federer")
            self.game.increment_player_score("Nadal")

        self.game.increment_player_score("Nadal")
        self.game.increment_player_score("Nadal")

        self.assertEqual(self.game.get_game_status(), "Nadal wins")

    def test_increment_score_raises_game_has_already_been_won_error(self):
        """Verifica che incrementare il punteggio a partita finita sollevi GameHasAlreadyBeenWonError."""
        # Vittoria rapida di Federer (4-0)
        for _ in range(4):
            self.game.increment_player_score("Federer")

        # Tentativo di un quinto punto
        with self.assertRaises(GameHasAlreadyBeenWonError):
            self.game.increment_player_score("Federer")


if __name__ == "__main__":
    unittest.main()