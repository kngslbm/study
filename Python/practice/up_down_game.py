# import random   # 난수 사용을 위한 random 라이브러리 import.

# yesorno = "y"   # 게임 진행 여부를 담은 변수

# # 게임 반복을 위한 while
# while yesorno == "y" :

#     random_number = random.randint(1, 100)              # 1~100 사이 난수 생성, 변수에 담아 보관.

#     guess_number = input("Guess between 1 and 100 :")   # 입력받은 수, 변수에 담아 보관.
    
#     guess_count = 0                                     # 시도 횟수를 담을 변수.    

#     # 두 변수가 일치하지 않으면 루핑.
#     while int(guess_number) != random_number:   
        
#         if int(guess_number) < random_number:                   # gusess_number가 더 작으면, 
#             print("up")                                         # up 출력.
#             guess_number = input("Guess between 1 and 100 :")   # 재입력.
#             guess_count += 1                                    # 시도 횟수 증가
#             continue                                            # while 함수 재실행
        
#         elif int(guess_number) > random_number:                 # gusess_number가 더 크면, 
#             print("down")                                       # down 출력.
#             guess_number = input("Guess between 1 and 100 :")   # 재입력.
#             guess_count += 1                                    # 시도 횟수 증가
#             continue                                            # while 함수 재실행

#     # 일치하면 시도 횟수 출력과 게임 진행 여부 재확인
#     else:                  
#         print(f"correct after {guess_count} tries")
#         yesorno = input("try again?(y/n)")

# # 게임(루핑) 종료 시 출력
# print("thanks for enjoying me!")



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



import random   # 난수 사용을 위한 random 라이브러리 import.

yesorno = "Y"   # 게임 진행 여부를 담은 변수

# 게임 반복을 위한 while
while yesorno == "Y" or yesorno == "YES" :             # 대문자로 "Y", "YES" 모두 루프 실행

    guess_number = input("Guess between 1 and 100 :")  # 입력받은 수, 변수에 담아 보관.
    random_number = random.randint(1, 100)               # 1~100 사이 난수 생성, 변수에 담아 보관.
    guess_count = 1                                    # 시도 횟수를 담을 변수.

    # 입력값이 0~100 사이 숫자임을 확인
    if guess_number.isdigit() and 0 < int(guess_number) < 101:      # .isgigit() 함수는 문자열이 숫자로만 이루어져 있으면 True 를 반환

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
            
        # 일치하면 시도 횟수 출력과 게임 진행 여부 재확인
        else:                  
            print(f"correct after {guess_count} tries")
            yorn = input("try again?(y/n)")               
            yesorno = yorn.upper()    # 소문자 입력도 대문자로 변경.
    else:
        print("Just the number between 1 and 100, plz :) ")

# 게임(루핑) 종료 시 출력
print("thanks for enjoying me!")



"""
2차 수정:
1차 문제점들 모두 보완. 추가로 게임 최고기록을 알려주는 기능 필요.
시도 횟수 0 이 아닌 1로 시작하는 걸로 수정.(첫 시도도 카운트)
"Just the number between 1 and 100, plz :) " 출력 시, 다시 "Guess between 1 and 100 :" 출력 안하고 바로 입력값 받고 다시 시작할 수 있으면 좋을 듯.
문제점을 발견했는데 try-except 안쓰려고 하니 방법이 안떠오른다. 좀 더 고민해보고 안되면 써야할 듯.

문제점
- 첫 시도 숫자입력 이후 문자 입력 시 오류
"""
    


import random   # 난수 사용을 위한 random 라이브러리 import.

yesorno = "Y"   # 게임 진행 여부를 담은 변수

# 게임 반복을 위한 while
while yesorno.upper() == "Y" or yesorno.upper() == "YES":   # .upper() 함수로 대소문자 모두 입력 허용
    random_number = random.randint(1, 100)             # 1~100 사이 난수 생성, 변수에 담아 보관.
    guess_count = 0                                    # 시도 횟수를 담을 변수.

    # guess_number 입력 루프
    while True: 
        guess_number = input("Guess between 1 and 100 :")  # 입력받은 수, 변수에 담아 보관.
        guess_count += 1                                   # 시도 횟수 증가

        # 입력값이 숫자가 아니거나, 1 부터 100 사이 숫자가 아닐 경우
        if not guess_number.isdigit() or not 1 <= int(guess_number) <= 100:   # .isgigit() 함수는 문자열이 숫자로만 이루어져 있으면 True 를 반환
            print("Just the number between 1 and 100, plz :) ")
            continue 
        
        elif int(guess_number) < random_number:                   # gusess_number가 더 작으면, 
            print("up")                                         # up 출력.
            print(random_number)                                          
        
        elif int(guess_number) > random_number:                 # gusess_number가 더 크면, 
            print("down")                                       # down 출력.
            print(random_number)                                      
            
        # 일치하면 시도 횟수 출력하고 루프 탈출
        else:                 
            print(f"correct after {guess_count} tries")
            break

    # 게임 진행 여부 재확인        
    yesorno = input("try again?(y/n)")          

# 게임(루핑) 종료 시 출력
print("thanks for enjoying me!")

"""
3차 수정:
불필요한 중첩 반복문들을 삭제했다.
유효한 입력값을 검증하기 위한 조건문과 숫자의 업다운 기능의 조건문을 너무 따로따로 생각했었다.
그러다보니 순차적으로 해결해야 되겠다는 생각에 갇혀있었던 것 같다. 
그리고 그 결과 입력값을 받을 때 한번 검증하고,
입력값을 받은 후에 업다운을 알려주고 다시 입력값을 받으면 또 검증하는 절차가 필요하게 된 것이다.

처음으로 돌아간다는 생각으로 다시 작성해 나갔다.
입력값을 받고 시도 횟수가 증가하는 하나의 과정을 while 로 묶어 루프를 돌리고,
그 반복 속에서 검증과 업다운, 그리고 정답을 맞춘 경우 전부 한번에 나누어 조건화 했다.
정답을 맞추면 루프를 탈출한다. 

코드는 훨씬 간단한데 문제점들은 모두 해결되었다. 기쁘다^^
"""