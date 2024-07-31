# 클래스를 만들어보자!
import random

class Fighter:
    def __init__(self):
        self.name = input("name: ")
        self.height = float(input("height: "))
        self.weight = float(input("weight: "))

    def attack(self, target):
        damage = random.randint(1, int(self.weight))
        target.height -= damage
        print(f"{self.name} attacked! / {target.name} received {damage} damage! / {target.name} has {target.height} health remaining!")

    def winner(self, target):
        if self.height <= 0:
            print(f"winner: {target.name}")
        if target.height <= 0:
            print(f"winner: {self.name}")

def main():
    print("User status")
    UserFighter = Fighter()

    print("Enemy status")
    EnemyFighter = Fighter()

    round = 1

    while UserFighter.height > 0 and EnemyFighter.height > 0:

        print(f"Round {round}!")

        UserFighter.attack(EnemyFighter)
        if EnemyFighter.height <= 0:
            UserFighter.winner(EnemyFighter)
            break

        EnemyFighter.attack(UserFighter)
        if UserFighter.height <= 0:
            EnemyFighter.winner(UserFighter)
            break

        round += 1
        
if __name__ == "__main__":
    main()
