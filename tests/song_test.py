import unittest

from src.song import Song

class TestSong (unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Wannabe", "The Spice Girls", 1996)
        self.song2 = Song("Song 2", "Blur", 1997)
        self.song3 = Song("Three Times a Lady", "Commodores", 1978)

        self.songlist = [self.song1, self.song2, self.song3]

    def test_song_has_name(self):
        self.assertEqual("Wannabe", self.song1.name)

    def test_song_has_artist(self):
        self.assertEqual("Blur", self.song2.artist)

    def test_song_has_year_released(self):
        self.assertEqual(1978, self.song3.year_released)

