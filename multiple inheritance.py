class Human:
    def eat(self):
        print("human can eat")

    def smell(self):
        print("human can smell")

    def need(self):
        print("basic need of human food shelter and cloths")

class Male(Human) :
    def loudVoice(self):
        print("male has loud voice")

    def beard(self):
        print("male has beard")

class Female(Human):
    def voice(self):
        print("female has sweet voice")

    def hair(self):
        print("female has long hair ")


h1=Male()
h1.eat()
h1.beard()
h1.need()
h1.smell()

h2=Female()
h2.need()
h2.voice()
h2.eat()