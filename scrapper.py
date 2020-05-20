import requests
from bs4 import BeautifulSoup

key_word = "python"
LIMIT = 50

# word를 검색어로 한 검색결과 페이지 개수 반환
def get_count_page(url):
    count_page = 1

    # 페이지 하단 리스트 추출
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pages_list = soup.find("ul", {"class":"pagination-list"})
    pages = pages_list.find_all("li")
    
    # list가 존재하지 않을 경우 1개의 페이지 개수 반환
    # 다음 버튼 제외 한 개수
    if pages is not None: count_page = len(pages)-1
    
    return count_page

def extract_job_detail(job_card):
    #print(job_card)
    title = job_card.find_all("a")
    print(len(title))

    for ti in title:
        print(ti)
    

def extract_jobs(word):
    url = f"https://kr.indeed.com/jobs?q={word}&limit=50"
    jobs = []
    count_page = get_count_page(url)

    #for page in range(last_page):
    page = 0
    result = requests.get(f"{url}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})

    for result in results:
        job = extract_job_detail(result)
        jobs.append(job)
        break

extract_jobs(key_word)