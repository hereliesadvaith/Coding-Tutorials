import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        # get books
        books = response.css("article.product_pod")
        # get single book
        for book in books:
            yield {
                "name": book.css("h3 a::text").get(),
                "price": book.css("div p.price_color::text").get(),
                "url": book.css("h3 a").attrib["href"],
            }
        pass
