import requests
from bs4 import BeautifulSoup

# 1. 웹 페이지 요청
url = "https://www.naver.com/"  # 스크래핑할 웹 페이지 URL
response = requests.get(url)

# 2. 응답 상태 확인
if response.status_code == 200:  # HTTP 상태 코드 200은 요청 성공을 의미
    print("페이지를 성공적으로 가져왔습니다!")
else:
    print(f"페이지를 가져오는 데 실패했습니다. 상태 코드: {response.status_code}")
    exit()
    
# 3. HTML 파싱
'''
soup = BeautifulSoup(response.text, 'html.parser')    

print(soup)
'''
# 테스트용 html
html = """
<nav class="menu-box-1" id="menu-box">
  <ul>
    <li>
      <a class="naver a b c" href="https://www.naver.com">네이버로 이동</a>      
    </li>
    <li>
      <a class="google" href="https://www.google.com">구글로 이동</a>
    </li>
    <li>
      <a class="daum" href="https://www.daum.net">다음으로 이동</a>
    </li>
  </ul>
</nav>
<nav id="hello">어서와</nav>
"""  

soup = BeautifulSoup(html, 'html.parser')    

print("== find 사용법 ==")

# html 상에 있는 nav를 검색
# 그 중에 첫 번째 nav를 검색
print(soup.find('nav')) 

# html 상에 첫 번째 a엘리먼트를 검색
print(soup.find('a')) 

# html 상에 a를 검색하는데, class 이름이 google인 대상을 검색
print(soup.find('a', class_="google"))

# html 상에 nav를 검색하는데, id가 hello인 녀석을 검색
print(soup.find('nav', id="hello"))

print("== find_all 사용법 ==")
print(soup.find_all('a')) 

a_el = soup.find_all('a')

for idx, a in enumerate(a_el):
  # print(f"{idx} : {a}")
  # print(f"{idx} : {a.get_text()}") # a.get_text() : 엘리먼트를 제외한 텍스트만 추출
  # print(f"{idx} : {a.get('href')}") # a.get('href') : href 속성 값만 출력
  print(f"{idx} : {a.get('class')}") # a.get('class') : class 값만 출력(클래스는 리스트 객체로 출력)