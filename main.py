class Team:
    name = ""
    capt = ""
    Win = 0

    def won_Csk(self):
        if self.name == "CSK":
         return "Whistle Podu"
        elif self.name == "RCB":
         return "We are Chuthiyas"

t1 = Team()
t1.name = "CSK"
t1.capt = "MSD"


  t2 = Team()
t2.name = "RCB"
t2.capt = "VK"

print(t2.won_Csk())
