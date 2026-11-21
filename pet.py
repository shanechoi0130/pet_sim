class Pet:
    def __init__(self, name, pet_type):
        self.name = name
        self.pet_type = pet_type

        self.energy = 80
        self.hunger = 30
        self.happiness = 70
        self.mood = ("Normal", "🙂")

    def feed(self):
        self.hunger = max(0, self.hunger - 10)
        self.happiness = min(100, self.happiness + 5)

    def play(self):
        self.happiness = min(100, self.happiness + 10)
        self.hunger = self.hunger + 10
        self.energy = self.energy - 10

    def sleep(self):
        self.energy = min(100, self.energy + 25)
        self.hunger = min(100, self.hunger + 10)

    def is_alive(self):
        if self.energy < 0:
            return False
        if self.hunger > 100:
            return False
        return True

    def get_mood(self):
        self.update_mood()
        return self.mood

    def update_mood(self):
        if self.happiness >= 80 and self.hunger <= 50 and self.energy >= 50:
            self.mood = ("Super Happy", "😍")
            return self.mood
        if self.hunger >= 70:
            self.mood = ("Very Hungry", "😠")
            return self.mood
        if self.energy <= 30:
            self.mood = ("Very Tired", "🫩")
            return self.mood
        if self.happiness <= 30:
            self.mood = ("Sad and Lonely", "🥺")
            return self.mood
        if self.happiness >= 80:
            self.mood = ("Super Happy", "😍")
            return self.mood
        else:
            self.mood = ("Normal", "🙂")
            return self.mood

    def pass_time(self):
        self.energy = self.energy - 3
        self.hunger = self.hunger + 5
        self.happiness = self.happiness - 2
        self.update_mood()
