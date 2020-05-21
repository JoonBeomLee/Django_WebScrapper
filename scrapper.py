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
    title = job_card.find("h2", {"class":"title"}).find("a").text.strip()
    link = job_card["data-jk"]
    company = job_card.find("span", {"class":"company"}).text.strip()
    location = job_card.find("div", {"class":"recJobLoc"})["data-rc-loc"].rstrip()
    
    return {
        'title': title,
        'company': company,
        'location': location,
        "link": f"https://kr.indeed.com/viewjob?jk={link}"
    }



def extract_jobs(word):
    url = f"https://kr.indeed.com/jobs?q={word}&limit=50"
    jobs = []
    count_page = get_count_page(url)

    for page in range(count_page):
        result = requests.get(f"{url}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})

        for result in results:
            job = extract_job_detail(result)
            jobs.append(job)

    return jobs

result = extract_jobs(key_word)
print(result)