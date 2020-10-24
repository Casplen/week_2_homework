import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestRoom (unittest.TestCase):
    def setUp(self):
        self.room1 = Room(8)
        self.room2 = Room(6)
        self.room3 = Room(4)
        self.room4 = Room(3)

        self.rooms = [self.room1, self.room2, self.room3, self.room4]

        self.song1 = Song("Wannabe", "The Spice Girls", 1996)
        self.song2 = Song("Song 2", "Blur", 1997)
        self.song3 = Song("Three Times a Lady", "Commodores", 1978)
        self.song4 = Song("For Free", "Joni Mitchell", 1970)
        self.song5 = Song("Spice Up Your Life", "The Spice Girls", 1997)

        self.songlist = [self.song1, self.song2, self.song3]

        self.guest1 = Guest("Bob", 10.00, "Wannabe")
        self.guest2 = Guest("Tina", 15.00, None)
        self.guest3 = Guest("Linda", 8.00, None)
        self.guest4 = Guest("Louise", 5.00, None)
        self.guest5 = Guest("Ted", 2.00, None)

    def test_room_has_songs_attribute(self):
        self.assertEqual([], self.room1.songs)

    def test_room_has_guests_attribute(self):
        self.assertEqual([], self.room1.guests)

    def test_room_has_capacity(self):
        self.assertEqual(8, self.room1.capacity)

    def test_add_guest_to_room(self):
        self.room1.add_guest(self.guest1)
        self.assertEqual(1, len(self.room1.guests))

    def test_remove_guest_from_room(self):
        self.room1.add_guest(self.guest1)
        self.room1.remove_guest(self.guest1)
        self.assertEqual(0, len(self.room1.guests))

    def test_clear_room_of_guests(self):
        self.room1.add_guest(self.guest1)
        self.room1.add_guest(self.guest2)
        self.room1.add_guest(self.guest3)
        self.room1.clear()
        self.assertEqual(0, len(self.room1.guests))

    def test_add_song_to_room(self):
        self.room1.add_song(self.song1)
        self.assertEqual(1, len(self.room1.songs))

    def test_remove_song_from_room(self):
        self.room1.add_song(self.song1)
        self.room1.remove_song(self.song1)
        self.assertEqual(0, len(self.room1.songs))

    def test_add_list_of_songs(self):
        self.room1.add_songlist(self.songlist)
        self.assertEqual(3, len(self.room1.songs))

    def test_songs_can_be_added_individually_and_from_list(self):
        self.room1.add_songlist(self.songlist)
        self.room1.add_song(self.song4)
        self.assertEqual(4, len(self.room1.songs))

    def test_clear_songlist(self):
        self.room1.add_songlist(self.songlist)
        self.room1.clear_songlist()
        self.assertEqual(0, len(self.room1.songs))

    def test_find_song_by_name(self):
        self.room1.add_songlist(self.songlist)
        song = self.room1.find_song_by_name("Wannabe")
        self.assertEqual("Wannabe", song.name)

    def test_room_has_guest_add_limit(self):
        self.room4.add_guest(self.guest1)
        self.room4.add_guest(self.guest2)
        self.room4.add_guest(self.guest3)
        self.room4.add_guest(self.guest4)
        self.assertEqual(3, len(self.room4.guests))

    def test_room_has_tab(self):
        self.assertEqual(0, self.room1.tab)

    def test_guest_entry_fee(self):
        self.room1.add_guest(self.guest1)
        self.room1.add_guest(self.guest2)
        self.assertEqual(10.00, self.room1.tab)
        self.assertEqual(5.00, self.guest1.wallet)
        self.assertEqual(10.00, self.guest2.wallet)
    
    def test_rejects_guests_who_cannot_afford_fee(self):
        self.room1.add_guest(self.guest5)
        self.assertEqual(0, len(self.room1.guests))

    def test_find_songs_by_artist(self):
        self.room1.add_song(self.song1)
        self.room1.add_song(self.song2)
        self.room1.add_song(self.song5)
        songs = self.room1.find_songs_by_artist("The Spice Girls")
        self.assertEqual(2, len(songs))
        self.assertEqual("Spice Up Your Life", songs[1].name)

    def test_find_songs_by_year_released(self):
        self.room1.add_song(self.song1)
        songs = self.room1.find_songs_by_year_released(1996)
        self.assertEqual("Wannabe", songs[0].name)
    
    def test_favourite_song_response(self):
        self.room1.add_guest(self.guest1)
        self.assertEqual("Woo!", self.room1.add_song(self.song1))


