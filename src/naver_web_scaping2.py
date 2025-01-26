import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

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
head_line_news_info = []
head_line_news_a_el = soup.select('.as_headline .sa_text_title')

# html을 순회해서 뉴스기사 제목만 추출
for idx, title_el in enumerate(head_line_news_a_el):  
  title = title_el.select('.sa_text_strong')[0].get_text()  
  link = title_el.get('href')
  head_line_news_info.append({'뉴스 제목': title, '링크': link})

# 3. pandas DataFrame으로 변환
df = pd.DataFrame(head_line_news_info)
save_path = 'C:\work\python_projects\뉴스_기사.xlsx'

# 4. 엑셀 파일로 저장
df.to_excel(save_path, index=False, engine='openpyxl')
print("뉴스 기사가 엑셀 파일로 저장되었습니다!")