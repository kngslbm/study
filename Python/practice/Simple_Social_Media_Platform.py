# ------ 코드 정의 ------

import hashlib

# Member 클래스
class Member:
    def __init__(self, name, user_id, password):
        self.name = name
        self.user_id = user_id
        self.password = password

    def display(self):
        print(f"Name:{self.name}  ID:{self.user_id}")   # method 'display' : member 의 이름과 id 를 출력해준다.

# Post 클래스
class Post:
    def __init__(self, title, content, author): 
        self.title = title
        self.content = content
        self.author = author.user_id   # Member 클래스로 만든 인스턴스에서 user_id 를 가져옴

# member 정보와 post 정보를 담을 변수
members = [] 
posts = []

# Member 인스턴스
member1 = Member("seulbeom","sb","1234")
member2 = Member("mehtap","tabi","1234")
member3 = Member("yasemin","ysm","1234")
member4 = Member("rukiye","ruki","1234")

# members list에 정보 추가
members.append(member1)
members.append(member2)
members.append(member3)
members.append(member4)

# Post 인스턴스
post1 = Post("Hi","It's my first post", member1)
post2 = Post("Hi","It's my first post", member2)
post3 = Post("Hi","It's my first post", member3)
post4 = Post("Hi","It's my first post", member4)

# posts list에 정보 추가
posts.append(post1)
posts.append(post2)
posts.append(post3)
posts.append(post4)


# ------ 코드 실행 ------

# method 'display' 호출
member?.display() # ?에 원하는 member 번호 입력

# member 전원 이름 출력
for member in members:
    print(member.name)

# post 전체 title, author 출력
for post in posts:
    print(f"<{post.title}> by {post.author}")

# 특정 member의 전체 post 출력
for post in posts:
    if post.author == "user_id":  # 원하는 멤버 user_id 입력s
        print(f"<{post.title}> by {post.author}")

# 특정 단어가 포함된 post 모두 출력
for post in posts:
    if "특정단어" in post.content:   # 원하는 단어 "특정단어"에 입력
        print(f"<{post.title}> by {post.author}")


# ---terminal 에서 member 추가---
new_member_name = input("What's your name? ")
new_member_id = input("Set up your ID :")
new_member_pw = input("Set up your Password :")

#  hash(sha256) 사용
hashed_pw = hashlib.sha256(new_member_pw.encode('utf-8'))

# Member 생성
new_member = Member(new_member_name, new_member_id, hashed_pw)

# member list에 추가
members.append(new_member)


# ---terminal 에서 post 추가---
new_post_id = input("What's your ID? ")

# 회원임을 확인
for member in members:
    if member.user_id == new_post_id:
        new_post_author = member

# post 입력
new_post_title = input("Please write the title : ")
new_post_content = input("Please write the content : ")

# Post 생성
new_post = Post(new_post_title, new_post_content, new_post_author)

# posts list에 추가
posts.append(new_post)



"""
1차 수정:
클래스와 객체 개념을 이해하고 활용해보기 위해 member 들이 post 를 등록할 수 있는 단순한 소셜 미디어 플랫폼을 작성해봤음.
추가로 terminal 에서 클래스를 활용해 인스턴스를 생성할 수 있는 기능 필요
'비밀번호 해싱'에 대해 공부하고 적용시킬 것.
"""

"""
2차 수정:
terminal 에서 Member 클래스와 Post 클래스의 인스턴스를 생성할 수 있는 기능을 구현해봤다.
hashlib 모듈을 사용하여 새로운 member를 등록할 때 비밀번호를 해싱하여 보관할 수 있도록 했다.

이번에 Hash 를 공부하다가 어쩌다보니 조금 깊이 들어가버려서 단순히 비밀번호처럼 민감한 데이터를 보관하기 위해 사용되는 Hash 말고도,
컴퓨터 공학에서 말하는 큰 개념의 Hash 부터 자료구조로써 활용되는 Hash, 그리고 암호학에서의 Hash의 의미까지 모두 공부하였다.
블로그에 개념도 정리하고 하다보니 이틀이 순식간에 사라져서 막상 코드 작성에 쓸 시간이 부족했다.

그래도 기본적인 개념을 잘 쌓아가는게 나중에 도움이 될거라고 생각하련다~
"""