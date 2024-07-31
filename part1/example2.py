# 클래스를 만들어보자!

# 구조적으로 클래스를 만들만한 상황을 클래스로 만들어보자!

# 격투기 선수 두명 김동현 vs 은가누 <= 격투기선수()

import random
class Fighter:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    def attack(self, enemy):
        damage = random.randint(1, self.weight)
        enemy.height -= damage
        print(f"{self.name} attacks {enemy.name}")
        print(f"damage: {damage}")
        print(f"{enemy.name} life: {enemy.height}")
    def winner(user, enemy):
        if user.height <= 0:
            print(f"winner: {enemy.name}")
        if enemy.height <= 0:
            print(f"winner: {user.name}")
def main():
    print("User status")
    name_user = input("User name: ")
    height_user = float(input("User height: "))
    weight_user = float(input("User weight: "))
    print("Enemy status")
    name_enemy = input("Enemy name: ")
    height_enemy = float(input("Enemy height: "))
    weight_enemy = float(input("Enemy weight: "))
    user_fighter = Fighter(name_user, height_user, weight_user)
    enemy_fighter = Fighter(name_enemy, height_enemy, weight_enemy)
    round= 1
    while user_fighter.height > 0 and enemy_fighter.height > 0:
        print(f"Round {round}")
        user_fighter.attack(enemy_fighter)
        if enemy_fighter.height <= 0:
            Fighter.winner(user_fighter, enemy_fighter)
            break
        enemy_fighter.attack(user_fighter)
        if user_fighter.height <= 0:
            Fighter.winner(user_fighter, enemy_fighter)
            break
        round += 1
if __name__ == "__main__":
    main()
