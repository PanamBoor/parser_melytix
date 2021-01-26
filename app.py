from tokenize import Comment

from bs4 import BeautifulSoup
import requests as req

url = "https://habr.com/ru/post/525638/"
resp = req.get(url)


# Получаем домен сайта +
def getDomen(url):
    print(url.split('/')[2])
    return (url.split('/')[2])


# Получаем все мета подключения на сайте +
def getMeta():
    soup = BeautifulSoup(resp.text, 'lxml')
    page_url = soup.find_all("meta")
    print(page_url)
    return page_url


# Кол-во тегов h1 +
def getTegH1Count():
    soup = BeautifulSoup(resp.text, 'lxml')
    col = 0
    for tag in soup.find_all("h1"):
        col += 1
    print("h1(кол-во) " + str(col))


# Кол-во тегов h2 +
def getTegH2Count():
    soup = BeautifulSoup(resp.text, 'lxml')
    col = 0
    for tag in soup.find_all("h2"):
        col += 1
    print("h2(кол-во) " + str(col) + " тег ")


# Кол-во тегов h3 +
def getTegH3Count():
    soup = BeautifulSoup(resp.text, 'lxml')
    col = 0
    for tag in soup.find_all("h3"):
        col += 1
    print("h3(кол-во) " + str(col) + " тег ")


# Кол-во тегов h4
def getTegH4Count():
    soup = BeautifulSoup(resp.text, 'lxml')
    col = 0
    for tag in soup.find_all("h4"):
        col += 1
    print("h4(кол-во) " + str(col) + " тег ")


# Кол-во тегов h5
def getTegH5Count():
    soup = BeautifulSoup(resp.text, 'lxml')
    col = 0
    for tag in soup.find_all("h5"):
        col += 1
    print("h5(кол-во) " + str(col) + " тег ")


# Кол-во тегов h6 +
def getTegH6Count():
    soup = BeautifulSoup(resp.text, 'lxml')
    col = 0
    for tag in soup.find_all("h6"):
        col += 1
    print("h6(кол-во) " + str(col) + " тег ")


# получаем текст тега h1
def getTegH1Txt():
    soup = BeautifulSoup(resp.text, 'lxml')
    for tag in soup.find_all("h1"):
        print("{0} txt- {1}".format(tag.name, tag.text))


# получаем текст тегов h2
def getTegH2Txt():
    soup = BeautifulSoup(resp.text, 'lxml')
    for tag in soup.find_all("h2"):
        print("{0} txt- {1}".format(tag.name, tag.text))


# получаем текст тегов h3
def getTegH3Txt():
    soup = BeautifulSoup(resp.text, 'lxml')
    for tag in soup.find_all("h3"):
        print("{0} txt- {1}".format(tag.name, tag.text))


# получаем текст тегов h4
def getTegH4Txt():
    soup = BeautifulSoup(resp.text, 'lxml')
    for tag in soup.find_all("h4"):
        print("{0} txt- {1}".format(tag.name, tag.text))


# получаем текст тегов h5
def getTegH5Txt():
    soup = BeautifulSoup(resp.text, 'lxml')
    for tag in soup.find_all("h5"):
        print("{0} txt- {1}".format(tag.name, tag.text))


# получаем текст тегов h6
def getTegH6Txt():
    soup = BeautifulSoup(resp.text, 'lxml')
    for tag in soup.find_all("h6"):
        print("{0} txt- {1}".format(tag.name, tag.text))


# получаем текст meta title
def getMetaTitle():
    soup = BeautifulSoup(resp.text, 'lxml')
    for tag in soup.find("meta", property="og:title"):
        title = soup.find("meta", property="og:title")
        print("meta title - " + title["content"] if title else "No meta title given")


# получаем текст meta description
def getMetaDescription():
    soup = BeautifulSoup(resp.text, 'lxml')
    title = soup.find("meta", property="og:description")
    print("meta description - " + title["content"] if title else "No meta description given")


# Выгружаем теги <iframe> кол-во
def getTagIframeCount():
    soup = BeautifulSoup(resp.text, 'lxml')
    col = 0
    for tag in soup.find_all("iframe"):
        col += 1
    print("iframe кол-во - " + str(col))


# получаем все текста тегов alt атрибутов изображения
def getAltTxt():
    soup = BeautifulSoup(resp.text, 'lxml')
    title = soup.find("alt", property="og:description")
    print("alt txt - " + title["content"] if title else "No alt txt given")


# получаем кол-во символов на странице, все заголовки
def getCountSymbol():
    soup = BeautifulSoup(resp.text, 'lxml')
    for tag in soup.find_all("p"):
        print("{0} txt- {1}".format(tag.name, tag.text))


# выгрузить весь текстов тегов href на сайте
def getHrefTxt():
    soup = BeautifulSoup(resp.text, 'lxml')
    title = soup.find("href")
    print("href txt - " + title["content"] if title else "No href txt given")


# Проверка есть ли кодировка utf на сайте
def getUtf():
    soup = BeautifulSoup(resp.text, 'lxml')
    page_url = soup.find_all('meta charset="UTF-8"')
    print ("+") if page_url else print("-")


if __name__ == "__main__":
    getDomen(url), getMeta(), getTegH1Count(), getTegH2Count(), getTegH3Count()
    getTegH4Count(), getTegH5Count(), getTegH6Count(), getTegH1Txt(), getTegH2Txt(), getTegH3Txt(),
    getTegH4Txt(), getTegH5Txt(), getTegH6Txt(), getMetaTitle(), getMetaDescription(), getTagIframeCount(), getAltTxt(),
    getCountSymbol(), getHrefTxt(), getUtf()
