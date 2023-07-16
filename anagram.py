class Anagram():
    def __init__(self,s1,s2):
        self.s1 = s1
        self.s2 = s2

    def replace(self):
        self.s1 = self.s1.replace(" ","").lower()
        self.s2 = self.s2.replace(" ","").lower()

    def chk(self):
        self.replace()
        if sorted(self.s1) == sorted(self.s2):
            return True
        else:
            return False
        
ang = Anagram("Emperor Octavian","Captain over Rome")
print(ang.chk())

