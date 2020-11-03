from urllib.request import urlopen
from bs4 import BeautifulSoup as soup


class Amazon:
    def __init__(self, url, name, num):
        self.url = url
        self.name = name
        self.num = num
        self.f = open(f"{self.name}.csv", "a", encoding="utf-8")


    def search_website(self):
        try:
            while True:
                page = urlopen(self.url).read()
                products = soup(page, "html.parser").findAll("li", {"class": "product"})
                for i in products:
                    item = i.div.h5.text
                    link = i.div.a["href"]
                    self.output(page_num, item, link)
                    self.save(self.num, item, link)

                self.num += 1
                return item, link, self.num
        except UnboundLocalError:
            print("no more pages")

    def save(self, page, item, link):
        self.f.write(str(page) + "," + item.replace(",", "|") + "," + link + "\n")

    def output(self, page_num, item, link):
        print(f"{page_num},{item},{link},")

    def write_header(self):
        headers = "Page,Product,Link \n"
        self.f.write(headers)

page_num = 1
filename = input("What do you want to call the file\n>>>  ")
while True:
    amazon = Amazon(f"https://uk.testzon.com/?page={page_num}", filename, page_num)
    if page_num == 1:
        amazon.write_header()
        page_num +=1
    else:
        the_item, the_link, the_num = amazon.search_website()
        amazon.output(the_num, the_item, the_link)
        amazon.save(the_num, the_item, the_link)
        page_num += 1
