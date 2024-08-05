# 1. 클래스를 여러개 만드는 것인지?

# 2. 서브 클래스를 여러개 만들고, 메인 클래스 하나로 다 통합되게 만드는 것인지?

# 그때 말해주셨지만, 조금 더 명확하게 이해하고자 다시 한번 더 여쭈어 봅니다. 

# 클래스를 만들어보자!

# 구조적으로 클래스를 만들만한 상황을 클래스로 만들어보자!

# 격투기 선수 두명 김동현 vs 은가누 <= 격투기선수()
import random

class Attack:
    def __init__(self, user, target):
        print(f"{user.name} attacked! {target.name}")

class Weaving:
    def __init__(self, user, target):
        damage = random.randint(1, int(user.weight))
        if 10 <= damage:
            target.height -= damage
            print(f"{target.name} received {damage} damage! / {target.name} has {target.height} health remaining!")
        else:
            print(f"{target.name} weaving! / {target.height} health remaining!")

class Fighter:
    def __init__(self):
        self.name = input("name: ")
        self.height = float(input("height: "))
        self.weight = float(input("weight: "))
      
    def Fight(self, target):
        if self.height <= 0:
            print(f"winner: {target.name}")
            return "break"
        if target.height <= 0:
            print(f"winner: {self.name}")
            return "break"
          
        self.Attack = Attack(self, target)
        self.Weaving = Weaving(self, target)

def main():
    print("User status")
    UserFighter = Fighter()
  
    print("Enemy status")
    EnemyFighter = Fighter()
  
    round = 1
  
    while UserFighter.height > 0 and EnemyFighter.height > 0:
      
        print(f"Round {round}!")
      
        if UserFighter.Fight(EnemyFighter) == "break":
            break
        if EnemyFighter.Fight(UserFighter) == "break":
            break
          
        round += 1
        
if __name__ == "__main__":
    main()
