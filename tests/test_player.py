import unittest
from player import Player  # Sostituisci 'player' con il nome del file in cui si trova la tua classe


class TestPlayer(unittest.TestCase):

    def setUp(self):
        """Inizializza oggetti di test primari prima di ogni metodo di test."""
        self.player1 = Player("Nadal")
        self.player2 = Player("Federer", 2)

    def test_initialization(self):
        """Verifica la corretta inizializzazione di un oggetto Player."""
        self.assertEqual(self.player1.get_name(), "Nadal")
        self.assertEqual(self.player1.get_score(), 0)
        self.assertEqual(self.player2.get_name(), "Federer")
        self.assertEqual(self.player2.get_score(), 2)

    def test_get_name(self):
        """Verifica la lettura del nome del giocatore tramite get_name."""
        player = Player("Sinner")
        self.assertEqual(player.get_name(), "Sinner")

    def test_set_name(self):
        """Verifica la modifica del nome del giocatore tramite set_name."""
        self.player1.set_name("Alcaraz")
        self.assertEqual(self.player1.get_name(), "Alcaraz")

    def test_get_score(self):
        """Verifica la lettura del punteggio del giocatore tramite get_score."""
        player = Player("Djokovic", 3)
        self.assertEqual(player.get_score(), 3)

    def test_set_score(self):
        """Verifica la modifica del punteggio del giocatore tramite set_score."""
        self.player1.set_score(3)
        self.assertEqual(self.player1.get_score(), 3)

    def test_increment_score(self):
        """Verifica l'incremento del punteggio di un'unità."""
        self.player1.increment_score()
        self.assertEqual(self.player1.get_score(), 1)

        self.player1.increment_score()
        self.assertEqual(self.player1.get_score(), 2)

    def test_get_score_as_string(self):
        """Verifica la traduzione dei punteggi numerici nella notazione del tennis."""
        test_cases = [
            (0, "love"),
            (1, "fifteen"),
            (2, "thirty"),
            (3, "forty"),
            (4, None),   # Punteggi superiori a 3 restituiscono None secondo il codice
            (-1, None)   # Punteggi negativi restituiscono None
        ]

        for score, expected_string in test_cases:
            with self.subTest(score=score):
                self.player1.set_score(score)
                self.assertEqual(self.player1.get_score_as_string(), expected_string)

    def test_is_tied_with(self):
        """Verifica la parità tra due giocatori."""
        p1 = Player("P1", 2)
        p2 = Player("P2", 2)
        p3 = Player("P3", 3)

        self.assertTrue(p1.is_tied_with(p2))
        self.assertFalse(p1.is_tied_with(p3))
        self.assertFalse(p3.is_tied_with(p1))

    def test_has_at_least_forty_points(self):
        """Verifica se il giocatore ha almeno 3 punti ('forty')."""
        self.player1.set_score(2)
        self.assertFalse(self.player1.has_at_least_forty_points())

        self.player1.set_score(3)
        self.assertTrue(self.player1.has_at_least_forty_points())

    def test_has_less_than_forty_points(self):
        """Verifica se il giocatore ha meno di 3 punti ('forty')."""
        self.player1.set_score(2)
        self.assertTrue(self.player1.has_less_than_forty_points())

        self.player1.set_score(3)
        self.assertFalse(self.player1.has_less_than_forty_points())

    def test_has_more_than_forty_points(self):
        """Verifica se il giocatore ha più di 3 punti ('forty')."""
        self.player1.set_score(3)
        self.assertFalse(self.player1.has_more_than_forty_points())

        self.player1.set_score(4)
        self.assertTrue(self.player1.has_more_than_forty_points())

    def test_has_one_point_advantage_on(self):
        """Verifica il vantaggio di esattamente 1 punto rispetto all'avversario."""
        p1 = Player("P1", 4)
        p2 = Player("P2", 3)
        p3 = Player("P3", 4)

        self.assertTrue(p1.has_one_point_advantage_on(p2))   # 4 - 3 = 1
        self.assertFalse(p1.has_one_point_advantage_on(p3))  # 4 - 2 = 2
        self.assertFalse(p2.has_one_point_advantage_on(p1))  # 3 - 4 = -1

    def test_has_at_least_two_points_advantage_on(self):
        """Verifica il vantaggio di almeno 2 punti rispetto all'avversario."""
        p1 = Player("P1", 4)
        p2 = Player("P2", 2)  # Diff: 2
        p3 = Player("P3", 1)  # Diff: 3
        p4 = Player("P4", 3)  # Diff: 1

        self.assertTrue(p1.has_at_least_two_points_advantage_on(p2))
        self.assertTrue(p4.has_at_least_two_points_advantage_on(p3))
        self.assertFalse(p1.has_at_least_two_points_advantage_on(p4))


if __name__ == "__main__":
    unittest.main()