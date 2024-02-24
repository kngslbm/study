import random   # 난수 사용을 위한 random 라이브러리 import.

yesorno = "y"   # 게임 진행 여부를 담은 변수

# 게임 반복을 위한 while
while yesorno == "y":

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
        yesorno = input("try again?")

   
            

    