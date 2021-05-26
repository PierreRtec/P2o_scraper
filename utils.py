""""Ce module contient des fonctions utilitaires qui permettent de réaliser mon programme de scraping."""

import requests
import csv
from slugify import slugify
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlretrieve


class Downloader:

    def get_info(self, url):
        response = requests.get(url)
        return BeautifulSoup(response.content, "html.parser")


class Page:
    
    def __init__(self):
        self.url = "https://books.toscrape.com/index.html"
        self.downloader = Downloader()
        self.soup = self.downloader.get_info(self.url)
        self.categories = self._get_categories()

    def _get_categories(self):
        categories = self.soup.select(".side_categories ul ul li a")
        return [Category(urljoin(self.url, cat['href'])) for cat in categories]

class Urls:

    def get_all_categories(self):
        menu = soup.find(class_="side_categories")
        links = menu.find_all("a")
        for link in links:
            link_urls.append(urljoin(url, link["href"]))
        return link_urls


class Category:
    
    def __init__(self, url):
        self.downloader = Downloader()
        self.soup = self.downloader.get_info(url)
        self.name = self._get_category_name()
        self.books = []

    def _get_category_name(self):
        return self.soup.select_one(".page-header > h1").text

    def __repr__(self):
        return self.name


class Book:
    
    def scraping_book(self):
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.select_one(".product_main h1").text.strip()
        description = product_description(soup)
        category = product_category(soup)
        upc = universal_product_code(soup)
        image_url = urljoin(url_book, product_image_url(soup))
        number = product_number_available(soup)
        including = product_price_including(soup)
        excluding = product_price_excluding(soup)
        review_rating = product_review_rating(soup)
        image_name = f"Images/{slugify(title[:100])}.jpg"
        return {
          "title": title,
          "description": description,
          "category": category,
          "upc": upc,
          "image_url": image_url,
          "including": including,
          "excluding": excluding,
          "review_rating": review_rating,
          "image_name": image_name
          }


class Description:

    def product_description(self):
        description_element = soup.select_one(".sub-header ~ p")
        if description_element is not None:
            description = description_element.text
        else:
            description = ""
            return description


class Upc:

    def get_product_code(self):
          upc = soup.find_all("td")[-0].text
          table = soup.find("table")
          table_rows = table.find_all("tr")
          return upc


def main():
    homepage = Page()
    link_urls = []
    print(homepage.categories)
    print(link_urls)
    print(title)
    print(upc)



main()