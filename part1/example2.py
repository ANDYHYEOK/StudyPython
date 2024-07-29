# 클래스를 만들어보자!

# 구조적으로 클래스를 만들만한 상황을 클래스로 만들어보자!

# 격투기 선수 두명 김동현 vs 은가누 <= 격투기선수()

import random
--------------------------------------------------
class fighterClass:
  
    def __init__(self):
        pass

    def userInput(self):
        userName = input("user name: ")
        return userName

    def statusInput(self):
        h = float(input("height: "))
        w = float(input("weight: "))
        return h + w

    def attack(self, x):
        y = random.randint(1, 100)
        return x - y
--------------------------------------------------
def main():
    f = fighterClass()
  
    print("user status: ")
    username = f.userInput
    userlife = f.statusInput
  
    print("enemy status: ")
    enemyname = f.userInput
    enemylife = f.statusInput

    while True:
        user = f.attack(0)
        enemy = f.attack(0)
        if user < enemy:
            print(f"damage: {enemy * (-1)}")
            print(f"user life: {f.attack(userlife)}")
        else:
            print(f"damage: {user * (-1)}")
            print(f"enemy life: {f.attack(enemylife)}")
        c = input("continue? (yes/no): ")
        if c.lower() == 'no':
            break
--------------------------------------------------
if __name__ == "__main__":
    main()
