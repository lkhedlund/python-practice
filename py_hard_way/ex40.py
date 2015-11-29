class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

    def shout_song(self):
        for ch in self.lyrics:
            print ch.upper()
"""
    def user_song(self):
        lines = int(raw_input("How many lines in the song? "))
        for i in range(0, lines, 1):
            user = raw_input("> ")
            self.lyrics[i: user]
"""

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there."])

bulls_on_parade = Song(["They really around the family",
                        "With pockets full of shells"])

new_lyrics = ["""
Stole a key
Took a car downtown to where the lost boys meet
Took a car downtown and took what they offered me
To set me free
I saw the lights go down at the end of the scene
Saw the lights go down and standing in front of me
"""]

charlie_brown = Song(new_lyrics)

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
charlie_brown.sing_me_a_song()

charlie_brown.shout_song()

# new_song = []
# new_song.user_song()
