import random   # 난수 사용을 위한 random 라이브러리 import.

yesorno = "y"   # 게임 진행 여부를 담은 변수

# 게임 반복을 위한 while
while yesorno == "y" :

    random_number = random.randint(1, 100)              # 1~100 사이 난수 생성, 변수에 담아 보관.

    guess_number = input("Guess between 1 and 100 :")   # 입력받은 수, 변수에 담아 보관.
    
    guess_count = 0                                     # 시도 횟수를 담을 변수.    

    # 두 변수가 일치하지 않으면 루핑.
    while int(guess_number) != random_number:   
        
        if int(guess_number) < random_number:                   # gusess_number가 더 작으면, 
            print("up")                                         # up 출력.
            guess_number = input("Guess between 1 and 100 :")   # 재입력.
            guess_count += 1                                    # 시도 횟수 증가
            continue                                            # while 함수 재실행
        
        elif int(guess_number) > random_number:                 # gusess_number가 더 크면, 
            print("down")                                       # down 출력.
            guess_number = input("Guess between 1 and 100 :")   # 재입력.
            guess_count += 1                                    # 시도 횟수 증가
            continue                                            # while 함수 재실행

    # 일치하면 시도 횟수와 게임 진행 여부 재확인
    else:                  
        print(f"correct after {guess_count} tries")
        yesorno = input("try again?(y/n)")

else:
    print("thanks for enjoying me!")





"""
1차 완성:
1차 코드를 작성해 보기 전에 같이 공부하던 사람의 부탁으로 그 분의 코드를 봐버렸다.
솔직히 자세한 코드는 기억이 안나서 큰 영향이 없었지만,
이상하게 try-except 구문을 사용했다는 것만은 기억이 나서 왠지 그것만은 사용하지 말고 해보자라는 오기를 부려봤다.

문제점:
- 1~100 이상의 숫자도 입력 가능.
- 숫자가 아닌 잘못된 입력값 입력 시 오류와 함께 종료됨.
- 게임 진행 여부 재확인 시 'Y' 나 'yes' 도 재진행 의사로 간주해야함.
"""


    