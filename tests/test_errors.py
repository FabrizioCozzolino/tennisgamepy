import unittest
from src.errors import DuplicatedPlayerError, GameHasAlreadyBeenWonError


class TestErrors(unittest.TestCase):

    # --- TEST DUPLICATED PLAYER ERROR ---

    def test_duplicated_player_error_inheritance(self):
        """Verifica che DuplicatedPlayerError sia una sottoclasse di Exception."""
        err = DuplicatedPlayerError()
        self.assertIsInstance(err, Exception)

    def test_duplicated_player_error_can_be_raised(self):
        """Verifica che DuplicatedPlayerError possa essere sollevata e catturata correttamente."""
        with self.assertRaises(DuplicatedPlayerError):
            raise DuplicatedPlayerError()

    def test_duplicated_player_error_message(self):
        """Verifica la creazione dell'errore con un messaggio personalizzato facoltativo."""
        err_msg = "I giocatori non possono avere lo stesso nome"
        err = DuplicatedPlayerError(err_msg)
        self.assertEqual(str(err), err_msg)

    # --- TEST GAME HAS ALREADY BEEN WON ERROR ---

    def test_game_has_already_been_won_error_inheritance(self):
        """Verifica che GameHasAlreadyBeenWonError sia una sottoclasse di Exception."""
        err = GameHasAlreadyBeenWonError()
        self.assertIsInstance(err, Exception)

    def test_game_has_already_been_won_error_can_be_raised(self):
        """Verifica che GameHasAlreadyBeenWonError possa essere sollevata e catturata correttamente."""
        with self.assertRaises(GameHasAlreadyBeenWonError):
            raise GameHasAlreadyBeenWonError()

    def test_game_has_already_been_won_error_message(self):
        """Verifica la creazione dell'errore con un messaggio personalizzato facoltativo."""
        err_msg = "La partita è già stata vinta"
        err = GameHasAlreadyBeenWonError(err_msg)
        self.assertEqual(str(err), err_msg)


if __name__ == "__main__":
    unittest.main()