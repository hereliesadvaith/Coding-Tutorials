import scrapy
from bookscraper.items import BookscraperItem


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        # function will get called once we get the response.
        books = response.css("article.product_pod")
        # Go to each book's page to retrieve data
        for book in books:
            relative_url = book.css("h3 a::attr(href)").get()
            if relative_url:
                if "catalogue" in relative_url:
                    book_url = "https://books.toscrape.com/" + relative_url
                else:
                    book_url = "https://books.toscrape.com/catalogue/" + relative_url
                yield response.follow(book_url, callback=self.parse_book_page)
        # Then going to next page
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            if "catalogue" in next_page:
                next_page_url = "https://books.toscrape.com/" + next_page
                yield response.follow(next_page_url, callback=self.parse)
            else:
                next_page_url = "https://books.toscrape.com/catalogue/" + next_page
                yield response.follow(next_page_url, callback=self.parse)

    def parse_book_page(self, response):
        bookitem = BookscraperItem()

        bookitem["name"] = response.css(".product_main h1 ::text").get()
        bookitem["category"] = response.xpath(
            "//ul[@class='breadcrumb']/li")[2].css("a::text").get()
        bookitem["price"] = response.xpath(
            "//table/tr")[3].css("td ::text").get()[1:]
        bookitem["availability"] = response.xpath(
            "//table/tr")[5].css("td ::text").get().split('(')[1].split(' ')[0]

        yield bookitem
