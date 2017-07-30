import bs4 as bs
import urllib.request

sauce_1 = urllib.request.urlopen("https://www.indeed.com/resumes?q=java&l=")
sauce_2 = urllib.request.urlopen("https://www.indeed.com/resumes?q=java&co=IN&start=50")

soup_1 = bs.BeautifulSoup(sauce_1, 'lxml')
soup_2 = bs.BeautifulSoup(sauce_2, 'lxml')

first_50 = soup_1.find_all(class_='app_name')
next_50 = soup_2.find_all(class_='app_name')

# for names_1 in first_50:
#     print(names_1.text)
#
# for names_2 in next_50:
#     print(names_2.text)

def main():
    resume_links = soup_1.find_all('a', class_='app_link', limit=10)

    # for i in resume_sauce:
    #     print(i['href'])

    for urls in resume_links:
        x = urls['href']
        # print(x)

        resume_url = urllib.request.urlopen("https://www.indeed.com"+x)
        # print(resume_url)

        resume_soup = bs.BeautifulSoup(resume_url, 'lxml')

        work_title = resume_soup.find_all(class_='work_title')
        dates = resume_soup.find_all(class_='work_dates')

        for w in work_title:
            print(w.text)
        for d in dates:
            print(d.text)

        print("-------------------------------------------------------------")




main()