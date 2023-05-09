# crawl through single book pages to get the description of books
import scrapy
from bookscraper.items import BookItem


class DescriptionSpider(scrapy.Spider):
    name = "descriptionspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        # get books from response html
        books = response.css("article.product_pod")
        for book in books:
            description_url = book.css("h3 a ::attr(href)").get()
            yield response.follow(description_url, callback=self.descrptionParse)
        next_page = response.css("li.next a ::attr(href)").get()
        if "catalogue" in next_page:
            next_page_url = "https://books.toscrape.com/" + next_page
        else:
            next_page_url = "https://books.toscrape.com/catalogue/" + next_page
        # recursion
        yield response.follow(next_page_url, callback=self.parse)

    def descrptionParse(self, response):
        table_rows = response.css("tabel tr")
        bookitem = BookItem()

        bookitem["name"] = (response.css("h1 ::text").get(),)
        bookitem["description"] = (
            response.css(
                # if the pargraph is directly under the divsion or use p:nth-of-type(2)
                # or x path
                # response.xpath("//div[@id='product_description]/following-siblilng::p/text()").get()
                "article.product_page > p:first-of-type::text"
            ).get(),
        )
        bookitem["availability"] = (table_rows[5].css("td ::text").get(),)
        yield bookitem
