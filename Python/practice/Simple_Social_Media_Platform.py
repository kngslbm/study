# ------ 코드 정의 ------

# member 클래스
class Member:
    def __init__(self, name, user_id, password):
        self.name = name
        self.user_id = user_id
        self.password = password

    def display(self):
        print(f"Name:{self.name}  ID:{self.user_id}")   # method 'display' : member 의 이름과 id 를 출력해준다.

# post 클래스
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
    if post.author == "user_id":  # 원하는 멤버 user_id 입력
        print(f"<{post.title}> by {post.author}")

# 특정 단어가 포함된 post 모두 출력
for post in posts:
    if "특정단어" in post.content:   # 원하는 단어 "특정단어"에 입력
        print(f"<{post.title}> by {post.author}")



"""
1차 완성:
클래스와 객체 개념을 이해하고 활용해보기 위해 member 들이 post 를 등록할 수 있는 단순한 소셜 미디어 플랫폼을 작성해봤음.
추가로 terminal 에서 클래스를 활용해 인스턴스를 생성할 수 있는 기능 필요
'비밀번호 해싱'에 대해 공부하고 적용시킬 것.
"""