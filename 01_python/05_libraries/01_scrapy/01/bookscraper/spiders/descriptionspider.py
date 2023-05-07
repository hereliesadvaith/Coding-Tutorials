# crawl through single book pages to get the description of books
import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        # get books from response html
        books = response.css("article.product_pod")
        for book in books:
            next_page = response.css("li.next a ::attr(href)").get()
            if "catalogue" in next_page:
                next_page_url = "https://books.toscrape.com/" + next_page
            else:
                next_page_url = "https://books.toscrape.com/catalogue/" + next_page
            # recursion
            yield response.follow(next_page_url, callback=self.parse)
