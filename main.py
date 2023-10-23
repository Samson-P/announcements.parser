import os.path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

ANNOUNCEMENTS_URL = 'https://announcements.bybit.com/en-US/?category=&page=1'
FILENAME_OUTPUT = 'out.csv'
PROFILE_PATH = r'D:\\Users\\samsonp\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\sqc33wdh.default-release'


def get_title(element):
    title_element = element.find_element(By.CLASS_NAME, "article-item-title")
    title = title_element.find_element(By.TAG_NAME, "span")

    return title.text


def get_datetime(element):
    datetime_element = element.find_element(By.CLASS_NAME, "article-item-date")

    return datetime_element.text


def get_link(element):
    return element.get_attribute('href')


class News:
    last_new = None
    news: list

    def __init__(self):
        self.browser = webdriver.Firefox()
        # Проверяем если файл FILENAME_OUTPUT существует, читаем последнюю новость, и записываем в last_new
        if os.path.exists(FILENAME_OUTPUT):
            with open(FILENAME_OUTPUT, 'r') as file:
                lines = file.readlines()
                # Если есть хоть 1 запись ( + \n )
                if len(lines) >= 1:
                    # Минимальная длина записи о новости - 2 символа (разделителя ; )
                    if len(lines[-1]) > 2:
                        datetime, title, link = lines[-1].split(';')
                        self.last_new = {
                            "title": title,
                            "datetime": datetime,
                            "link": link[:-1],
                        }

    def get_news(self):
        # Делаем GET запрос на страничку
        self.browser.get(ANNOUNCEMENTS_URL)
        # Очищаем список новостей
        self.news = []
        # Новости обернуты в tag a, class no-style. Забираем все новости с первой страницы
        news_elements = self.browser.find_elements(By.CLASS_NAME, "no-style")

        # Пробегаемся по списку новостей на первой странице, записываем каждый в список news
        for element in news_elements:
            data = {
                "title": get_title(element),
                "datetime": get_datetime(element),
                "link": get_link(element),
            }
            self.news.append(data)

        self.verify()

        return self.news

    # Проверяем, если новость не похожа на последнюю новость из предыдущей итерации,
    # тогда обновляем last_new и записываем в файл
    def verify(self):
        # Последнюю новость записываем в атрибут класса last_new
        if self.last_new != self.news[0]:
            self.last_new = self.news[0]
            self.write()

    # Записываем новость в файл FILENAME_OUTPUT
    def write(self):
        with open(FILENAME_OUTPUT, 'a+') as file:
            title, datetime, link = self.last_new.values()
            line = f'{datetime};{title};{link}\n'
            file.write(line)


if __name__ == "__main__":

    news = News()

    while True:
        news.get_news()
        time.sleep(1)
