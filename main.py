'''Now this was some task, i did learn alot doing it thanks... Abeg mark me well o, i be newbie'''


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks=[], score=0):
        self.name = str(name)
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)

    def change_name(self, name):
        self.name = name
        # return self.name
        print(self.name)

    def change_age(self, age):
        self.age = age
        # return self.age
        print(self.age)

    def add_track(self, track):
        self.tracks.append(track)
        # return self.tracks
        print(self.tracks)

    def get_score(self):
        # return float(self.score)
        print(self.score)


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)
# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
