class Room:
    def __init__(self, capacity):
        self.songs = []
        self.guests = []
        self.capacity = capacity
        self.tab = 0
        self.entry_fee = 5.00

    def add_and_remove_cash(self, amount):
        self.tab += amount

    def add_guest(self, guest):
        if len(self.guests) < self.capacity and guest.wallet >= self.entry_fee:
            guest.remove_cash(self.entry_fee)
            self.add_and_remove_cash(self.entry_fee)
            self.guests.append(guest)

    def remove_guest(self, guest):
        self.guests.remove(guest)

    def clear(self):
        self.guests = []

    def add_song(self, song):
        self.songs.append(song)
        for guest in self.guests:
            if song.name == guest.favourite_song:
                return guest.cheer()

    def add_songlist(self, songlist):
        [self.songs.append(song) for song in songlist]

    def remove_song(self, song):
        self.songs.remove(song)

    def clear_songlist(self):
        self.songs = []

    def find_song_by_name(self, name):
        for song in self.songs:
            if song.name == name:
                return song

    def find_songs_by_artist(self, artist):
        return [song for song in self.songs if artist == song.artist]

    def find_songs_by_year_released(self, year):
        return [song for song in self.songs if year == song.year_released]