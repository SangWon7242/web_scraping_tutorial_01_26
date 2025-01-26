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
