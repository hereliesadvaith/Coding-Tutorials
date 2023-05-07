# crawl through pages to get the name, price of all the books
import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        # get books from response html
        books = response.css("article.product_pod")
        # get single book
        for book in books:
            yield {
                "name": book.css("h3 a::text").get(),
                "price": book.css("div p.price_color::text").get(),
                "url": book.css("h3 a").attrib["href"],
            }
        next_page = response.css("li.next a ::attr(href)").get()
        if next_page is not None:
            if "catalogue" in next_page:
                next_page_url = "https://books.toscrape.com/" + next_page
            else:
                next_page_url = "https://books.toscrape.com/catalogue/" + next_page
            # recursion
            yield response.follow(next_page_url, callback=self.parse)
