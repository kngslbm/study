import random   # 무작위 선택을 위한 random import

yesorno = "y"   # 게임 진행 여부를 담은 변수
win_cnt = 0     # 승리수 카운트
lose_cnt = 0    # 패배수 카운트
tie_cnt = 0     # 무승부 카운트

# 게임 반복
while yesorno.lower() == "y" or yesorno.lower() == "yes":   # .lower() 함수로 대소문자 모두 입력 허용
    rps_list = ["rock", "paper", "scissors"]   # 가위 바위 보 리스트
    com = random.choice(rps_list)   # .choice() 함수로 리스트에서 무작위 선택
    user = input("Rock, Paper, Scissors!")   # 사용자 입력값을 담을 변수
    
    # 입력값이 유효한지 검증
    if user.lower() not in rps_list:  
        print("Pick again out of 'Rock', 'Paper', 'Scissors'. :) ")
        continue
    
    # 게임 결과를 위한 다중 if 문
    elif user.lower() == "rock":
        if com == "rock":
            print("Tie!")
            tie_cnt += 1
        
        elif com == "paper":
            print("You lose")
            win_cnt += 1 

        elif com == "scissors":
            print("You win!")
            lose_cnt += 1

    elif user.lower() == "paper":
        if com == "rock":
            print("You win!")
            lose_cnt += 1
        
        elif com == "paper":
            print("Tie!")
            tie_cnt += 1

        elif com == "scissors":
            print("You lose")
            win_cnt += 1 
    
    elif user.lower() == "scissors":
        if com == "rock":
            print("You lose")
            win_cnt += 1 
        
        elif com == "paper":
            print("You win!")
            lose_cnt += 1

        elif com == "scissors":
            print("Tie!")
            tie_cnt += 1

    # 게임 진행 여부 재확인
    yesorno = input("Try again? (Y/N)")

# 게임 종료 시 출력
print("Thanks for enjoying me!")
print(f"Win:{win_cnt}  Ties:{tie_cnt}  Losses:{lose_cnt}")



"""
1차 완성:
부족한게 많지만 up down game 을 만들어 봐서인지 비교적 술술 써진 느낌.
게임 결과를 위한 다중 if 문은 반복이 많아서 분명 더 간결하개 바꿀 수 있어 보임. 고민해보자
"""