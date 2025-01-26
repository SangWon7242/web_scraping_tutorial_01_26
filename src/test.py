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
      <a class="naver" href="https://www.naver.com">네이버로 이동</a>      
    </li>
    <li>
      <a class="google" href="https://www.google.com">구글로 이동</a>
    </li>
    <li>
      <a class="daum" href="https://www.daum.net">다음으로 이동</a>
    </li>
  </ul>
</nav>
"""  

soup = BeautifulSoup(html, 'html.parser')    