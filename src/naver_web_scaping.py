import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. 웹 페이지 요청
url = "https://news.naver.com/section/105"  # 스크래핑할 웹 페이지 URL
response = requests.get(url)

# 2. 응답 상태 확인
if response.status_code == 200:  # HTTP 상태 코드 200은 요청 성공을 의미
    print("페이지를 성공적으로 가져왔습니다!")
else:
    print(f"페이지를 가져오는 데 실패했습니다. 상태 코드: {response.status_code}")
    exit()
    
# 3. HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')    

# print(soup)

# 헤드라인 뉴스기사의 html을 가져오기
print(soup.select('.as_headline .sa_text_strong'))

head_line_news_title = []
head_line_news_el = soup.select('.as_headline .sa_text_strong')

# html을 순회해서 뉴스기사 제목만 추출
for idx, title_el in enumerate(head_line_news_el):
  head_line_news_title.append(title_el.get_text())
  print(f"{idx} : {title_el.get_text()}")
  
print(head_line_news_title)  
print("== 헤드라인 뉴스 기사 출력 ==")
for idx, title in enumerate(head_line_news_title):  
  print(f"{idx + 1} : {title}")

print("== 키워드를 기반으로 뉴스기사 출력 ==")
keyword = "AI"

# title.find(keyword)
# - 키워드가 포함되어 있으면 0을 반환
# - 키워드가 포함되어 있지 않으면 -1을 반환

find_keyword_news_title = []

for idx, title in enumerate(head_line_news_title):  
  if title.find(keyword) != -1:
    find_keyword_news_title.append(title)
    
print(find_keyword_news_title)    
    

  