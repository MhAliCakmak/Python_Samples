class Athlete:
    def __init__(self, name, surname, branch, bronze, silver, gold):
        self.name = name
        self.surname = surname
        self.branch = branch
        self.bronze = bronze  # Public and anyone who want can see this info # Go to 47 line
        self._silver = silver  # This is protected info so anyone can see only private can see # Go to 48 line
        self.__gold = gold  # This is private info for me  . Nobody but you can see # Go to 49 line

    def __str__(self):
        return f"{self.name} {self.surname}  {self.branch} "

    @property
    def athlete_info(self):
        return f"{self.name} {self.surname} {self.branch} {self.bronze} {self._silver}"

    @athlete_info.setter
    def athlete_info(self, sinfo):
        name, surname, branch, bronze, silver = sinfo.split(" ")
        self.name = name
        self.surname = surname
        self.branch = branch
        self.bronze = bronze
        self._silver = silver

    @athlete_info.deleter
    def athelete_info(self):
        self.name = None
        self.surname = None
        self.branch = None
        self.silver = None
        self.bronze = None

        print("USER DELETED")

    @property
    def gold_madal(self):
        return self.__gold


athlete1 = Athlete("Mehmet Ali", "Cakmak", "Boxing", "6", "8", "2")

print(athlete1.athlete_info)
athlete1.athlete_info = "Mahir Çamdalı Wrest 4 3"
print(athlete1.athlete_info)
# del athlete1.athelete_info
print(athlete1)

print(athlete1.bronze)
print(athlete1._silver)
print(athlete1.gold_madal)
