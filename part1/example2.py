# 클래스를 만들어보자!

# 구조적으로 클래스를 만들만한 상황을 클래스로 만들어보자!

# 격투기 선수 두명 김동현 vs 은가누 <= 격투기선수()

import random
class Fighter:
    def Attack(Name, Height, Weight):
        Damage = random.randint(1, Weight)
        life = Height - Damage
        print("attack: " + Damage + "/" + Name + "life: " + life)
    def Winner(User, Enemy):
        if User < Enemy:
            print("winner: " + NameEnemy)
        else:
            print("winner: " + NameUser)
def main():
    print("user status: ")
    NameUser = input("user name: ")
    HeightUser = float(input("user height: "))
    WeightUser = float(input("user weight: "))
    print("enemy status: ")
    NameEnemy = input("enemy name: ")
    HeightEnemy = float(input("enemy height: "))
    WeightEnemy = float(input("enemy weight: "))
    Round = 1
    while True:
        UserFighter = Fighter()
        EnemyFighter = Fighter()
        print("round" +  Round)
        UserFighter.Attack(NameEnemy, HeightUser, WeightUser)
        EnemyFighter.Attack(NameUser, HeightEnemy, WeightEnemy)
        if HeightUser = 0 or HeightEnemy = 0:
            UserFighter.Winner(HeightUser, HeightEnemy)
            break
        else:
            Round++
if __name__ == "__main__":
    main()
