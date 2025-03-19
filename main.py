class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атаковал {other.name} и нанес {self.attack_power} урона!")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        print("Начало игры!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.computer.name} побежден! {self.player.name} победил!")
                break
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} побежден! {self.computer.name} победил!")
                break
            print(f"У {self.player.name} осталось {self.player.health} здоровья.")
            print(f"У {self.computer.name} осталось {self.computer.health} здоровья.")


# Пример использования
player = Hero(name="Игрок")
computer = Hero(name="Компьютер")
game = Game(player, computer)
game.start()