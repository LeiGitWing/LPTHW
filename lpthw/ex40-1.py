class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_baby = Song(["Happy birthday to you", 
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family", 
                        "With pockets full of shells"])

old_town_road = Song(["I miss the cat in my home",
                      "I miss the paint in my bedroom",
                      "I miss the photo hang on the wall",
                      "When can I go back to my home",
                      "My sweet home and lovely parent"])

happy_baby.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

old_town_road.sing_me_a_song()