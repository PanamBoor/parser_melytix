from bs4 import BeautifulSoup
import requests as req
import re


class MainSiteParser(object):
    def __init__(self, site_ulr):
        self.__site_url = site_ulr
        resp = req.get(site_ulr)
        if resp.status_code == 200:
            self.soup = BeautifulSoup(resp.text, 'lxml')
        else:
            domain = site_ulr.split('/')[2]
            raise ConnectionError(f"Could not fetch domain {domain}")

    def parse(self) -> dict:
        attributes = [attr for attr in dir(self) if attr != 'parse' and not attr.startswith('__')]
        return {property: getattr(self, property, '') for property in attributes}

    # Получаем домен главного сайта
    @property
    def domain(self):
        return dict(self.__site_url.split('/')[2])

    # Получаем все мета подключения на главном сайте
    @property
    def meta_main(self):
        return self.soup.find_all("meta")

    # Получаем кол-во тегов h1
    @property
    def h1_count(self):
        return len(self.soup.find_all("h1"))

    # Получаем текст тегов h1
    @property
    def h1_txt(self):
        answer = []
        for tag in self.soup.find_all("h1"):
            answer.append("{0} txt- {1}".format(tag.name, tag.text))
        return answer

    # получаем кол-во тегов h2
    @property
    def h2_count(self):
        return len(self.soup.find_all("h2"))

    # получаем текст тегов h2
    @property
    def h2_txt(self):
        answer = []
        for tag in self.soup.find_all("h2"):
            answer.append("{0} txt- {1}".format(tag.name, tag.text))
        return answer

    # получаем кол-во тегов h3
    @property
    def h3_count(self):
        return len(self.soup.find_all("h3"))

    # получаем текст тегов h3
    @property
    def h3_txt(self):
        answer = []
        for tag in self.soup.find_all("h3"):
            answer.append("{0} txt- {1}".format(tag.name, tag.text))
        return answer

    # получаем кол-во тегов h4
    @property
    def h4_count(self):
        return len(self.soup.find_all("h4"))

    # получаем текст тегов h4
    @property
    def h4_txt(self):
        answer = []
        for tag in self.soup.find_all("h4"):
            answer.append("{0} txt- {1}".format(tag.name, tag.text))
        return answer

    # получаем кол-во тегов h5
    @property
    def h5_count(self):
        return len(self.soup.find_all("h5"))

    # получаем текст тегов h5
    @property
    def h5_txt(self):
        answer = []
        for tag in self.soup.find_all("h5"):
            answer.append("{0} txt- {1}".format(tag.name, tag.text))
        return answer

    # получаем кол-во тегов h6
    @property
    def h6_count(self):
        return len(self.soup.find_all("h6"))

    # получаем текст тегов h6
    @property
    def h6_txt(self):
        answer = []
        for tag in self.soup.find_all("h6"):
            answer.append("{0} txt- {1}".format(tag.name, tag.text))
        return answer

    # получаем текст meta title
    @property
    def meta_title(self):
        return self.soup.find("meta", property="og:title").get('content', '')

    # получаем текст meta description
    @property
    def meta_description(self):
        return self.soup.find("meta", property="og:description").get('content', '')

    # Выгружаем теги <iframe> кол-во
    @property
    def iframe_count(self):
        return len(self.soup.find_all("iframe"))

    # получаем все текста тегов alt атрибутов изображения
    @property
    def alt_txt(self):
        return self.soup.find("alt", property="og:description").get('content', '')

    # получаем кол-во символов на странице, все заголовки
    @property
    def count_symbol(self):
        return len(self.soup.find_all("p"))

    # выгрузить весь текстов тегов href на сайте
    @property
    def href_txt(self):
        return self.soup.find("href").get('content', '')

    # Проверка есть ли кодировка utf на сайте
    @property
    def is_utf(self) -> bool:
        answer = []
        if self.soup.find_all('meta charset="utf-8"'):
            answer = "True"
        else:
            answer = "False"

    # Выгружаем все мета линки сайта
    @property
    def meta_links(self):
        links_urls = []
        for i in self.soup.findAll('a'):
            links_urls.append(str(i.get('href')))
        links_urls = list(filter(lambda x: x.startswith('https'), links_urls))
        new_links = list(set(links_urls))
        domain = self.__site_url.split('/')[2]
        links = []
        for i in new_links:
            try:
                match = re.search(fr'(https:(..{domain}(.*)?))', i).group(1)
                links.append(match)
            except:
                pass

        return list(links)


class SiteUrls(object):
    def __init__(self, site_urls):
        self.__site_urls = site_urls
        for j in site_urls:
            resp = req.get(j)
            if resp.status_code == 200:
                self.soup = BeautifulSoup(resp.text, 'lxml')
                print(j)
            else:
                domain = j.split('/')[2]
                raise ConnectionError(f'could not fetch domain {domain} html')

    def parse(self) -> dict:
        attributes = [attr for attr in dir(self) if attr != 'parse' and not attr.startswith('__')]
        return {property: getattr(self, property, '') for property in attributes}

    @property
    def meta_urls(self):
        answer = {}
        for i in self.__site_urls:
            answer[i] = self.soup.find_all("meta")
        return answer

    # Кол-во тегов h1 +
    @property
    def h1_counts(self):
        answer = {}
        for i in self.__site_urls:
            answer[i] = len(self.soup.find_all("h1"))
        return answer

    # Получаем текст тегов h1
    @property
    def h1_txt(self):
        answer = {}
        for i in self.__site_urls:
            answer[i] = self.soup.find_all("h1")
        return answer

    # Кол-во тегов h2
    @property
    def h2_counts(self):
        answer = {}
        for i in self.__site_urls:
            answer[i] = len(self.soup.find_all("h2"))
        return answer

    # Получаем текст тегов h2
    @property
    def h2_txt(self):
        answer = {}
        for i in self.__site_urls:
            answer[i] = self.soup.find_all("h2")
        return answer

    # Кол-во тегов h3
    @property
    def h3_counts(self):
        answer = {}
        for i in self.__site_urls:
            answer[i] = len(self.soup.find_all("h3"))
        return answer

    # Получаем текст тегов h3
    @property
    def h3_txt(self):
        answer = {}
        for i in self.__site_urls:
            answer[i] = self.soup.find_all("h3")
        return answer

    # Кол-во тегов h4
    @property
    def h4_counts(self):
        answer = {}
        for i in self.__site_urls:
            answer[i] = len(self.soup.find_all("h4"))
        return answer

    # Получаем текст тегов h3
    @property
    def h4_txt(self):
        answer = {}
        for i in self.__site_urls:
            answer[i] = self.soup.find_all("h4")
        return answer

    # Кол-во тегов h5
    @property
    def h5_counts(self):
        answer = {}
        for i in self.__site_urls:
            answer[i] = len(self.soup.find_all("h5"))
        return answer

    # Получаем текст тегов h5
    @property
    def h5_txt(self):
        answer = {}
        for i in self.__site_urls:
            answer[i] = self.soup.find_all("h5")
        return answer

    # Кол-во тегов h6
    @property
    def h6_counts(self):
        answer = {}
        for i in self.__site_urls:
            answer[i] = len(self.soup.find_all("h6"))
        return answer

    # Получаем текст тегов h6
    @property
    def h6_txt(self):
        answer = {}
        for i in self.__site_urls:
            answer[i] = self.soup.find_all("h6")
        return answer

    # получаем текст meta title
    @property
    def meta_title(self):
        answer = {}
        for i in self.__site_urls:
            answer[i] = self.soup.find("meta", property="og:title").get('content', '')
        return answer

    # получаем текст meta description
    @property
    def meta_description(self):
        answer = {}
        for i in self.__site_urls:
            answer[i] = self.soup.find("meta", property="og:description").get('content', '')
        return answer

    # Выгружаем теги <iframe> кол-во
    @property
    def iframe_count(self):
        answer = {}
        for i in self.__site_urls:
            answer[i] = len(self.soup.find_all("iframe"))
        return answer

    # получаем все текста тегов alt атрибутов изображения
    @property
    def alt_txt(self):
        answer = {}
        for i in self.__site_urls:
            answer[i] = self.soup.find("alt", property="og:description").get('content', '')
        return answer

    # получаем кол-во символов на странице, все заголовки
    @property
    def count_symbol(self):
        answer = {}
        for i in self.__site_urls:
            answer[i] = len(self.soup.find_all("p"))
        return answer

    # выгрузить весь текстов тегов href на сайте
    @property
    def href_txt(self):
        answer = {}
        for i in self.__site_urls:
            answer[i] = self.soup.find("href").get('content', '')
        return answer

    # Проверка есть ли кодировка utf на сайте
    @property
    def is_utf(self):
        answer = {}
        for i in self.__site_urls:
            if self.soup.find_all('meta charset="utf-8"'):
                answer[i] = "True"
            else:
                answer[i] = "False"
        return answer


if __name__ == "__main__":
    url = 'https://kith2kin.com.ua/'
    urls = MainSiteParser(url).meta_links
    # print(SiteUrls(urls).meta_urls)
    print(SiteUrls(urls).meta_urls)

    # нужно залить на гит и отправить максу на проверку

