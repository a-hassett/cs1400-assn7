class Artomat:
    def __init__(self, money=0, hopper=0, bin1=10, bin2=10, bin3=10, bin4=10, text1="", text2="", text3="", text4=""):
        # define all properties of the class
        self.money = money
        self.hopper = hopper
        self.bin1 = bin1
        self.bin2 = bin2
        self.bin3 = bin3
        self.bin4 = bin4
        self.text1 = text1
        self.text2 = text2
        self.text3 = text3
        self.text4 = text4

    def printStatus(self):
        # print amount of each photo and amount of money in hopper and machine
        print("\n1:", self.bin1, "packs of", self.text1)
        print("2:", self.bin2, "packs of", self.text2)
        print("3:", self.bin3, "packs of", self.text3)
        print("4:", self.bin4, "packs of", self.text4)
        print("There is $", format(self.money/4, ".2f"), "in the machine.")
        print("There is $", format(self.hopper/4, ".2f"), "in the hopper.\n")

    def dropQuarter(self):
        # increase money in hopper when quarters are dropped
        print("ching")
        self.hopper += 1

    def pullKnob(self, photoNum):
        if self.hopper >= 3:
            # if there is enough money to pay for a photo, pick a photo and remove it from machine
            # release all quarters from hopper into machine
            self.money = self.money + self.hopper
            self.hopper = 0
            if photoNum == 1:
                print("A pack of", self.text1, "slides into view.")
                self.bin1 -= 1
            elif photoNum == 2:
                print("A pack of", self.text2, "slides into view.")
                self.bin2 -= 1
            elif photoNum == 3:
                print("A pack of", self.text3, "slides into view.")
                self.bin3 -= 1
            elif photoNum == 4:
                print("A pack of", self.text4, "slides into view.")
                self.bin4 -= 1
        else:
            print("(nothing happens)")

    def restock(self):
        # reset bin amounts and hopper and machine money amounts to default
        print("A grouchy-looking attendant shows up, opens the back, fiddles around a bit, closes it, and leaves.")
        self.bin1 = 10
        self.bin2 = 10
        self.bin3 = 10
        self.bin4 = 10
        self.hopper = 0
        self.money = 0


def main():
    photoMachine = Artomat(text1="Adams", text2="Arbus", text3="Dali", text4="Lange")
    portraitMachine = Artomat(money=212, hopper=2, bin1=1, bin2=0, bin3=8, bin4=10, text1="Picasso", text2="Rembrandt", text3="Van Gogh", text4="Monet")

    photoMachine.printStatus()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.pullKnob(1)
    photoMachine.pullKnob(2)
    photoMachine.dropQuarter()
    photoMachine.pullKnob(2)
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.pullKnob(2)
    photoMachine.printStatus()
    photoMachine.restock()
    photoMachine.printStatus()
    print("----")
    portraitMachine.printStatus()
    portraitMachine.dropQuarter()
    portraitMachine.pullKnob(1)
    portraitMachine.printStatus()


main()
