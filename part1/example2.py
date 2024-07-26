# 클래스를 만들어보자!

# 구조적으로 클래스를 만들만한 상황을 클래스로 만들어보자!

# 격투기 선수 두명 김동현 vs 은가누 <= 격투기선수()
import random

class FighterClass:
  
    def __init__(self):
        pass

    def kim_punch(self, x, y):
        return x - y

    def kim_kick(self, x, y):
        return x - y

    def sliver_punch(self, x, y):
        return x - (3 * y)

    def sliver_kick(self, x, y):
        return x - y

def main():
    fight = FighterClass()
    
    print("Select operation:")
    print("1. 김동현 주먹!")
    print("2. 김동현 발차기")
    print("3. 은가누 주먹!")
    print("4. 은가누 발차기!")

    while True:
        choice = input("Enter choice (1/2/3/4): ")
        num1 = 100
        num2 = random.randint(1, 10)
        if choice in ['1', '2', '3', '4']:
            if 0 < num1 :
                if choice == '1':
                    print(f"Damage: {num1} sliver life: {fight.kim_punch(num1, num2)}")
                elif choice == '2':
                    print(f"Damage: {num1} sliver life: {fight.kim_kick(num1, num2)}")
                elif choice == '3':
                    print(f"Damage: {num1} kim life: {fight.sliver_punch(num1, num2)}")
                elif choice == '4':
                    print(f"Damage: {num1} kim life: {fight.sliver_kick(num1, num2)}")
            else :
                print("--Done--")

        else:
            print("Invalid choice! Please select from 1, 2, 3, or 4.")

        num3 = input("Do you want to perform another calculation? (yes/no): ")
        
        if num3.lower() == 'no':
            break

if __name__ == "__main__":
    main()
