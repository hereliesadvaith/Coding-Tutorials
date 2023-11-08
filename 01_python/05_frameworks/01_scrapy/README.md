# Scrapy

Scrapy is an open-source Python web crawling framework that helps developers extract structured data from websites. It is designed to efficiently handle large amounts of data and is widely used for web scraping, data mining, information processing, and automation tasks.

Scrapy works by sending HTTP requests to websites, downloading the HTML response, and parsing the data using a set of rules defined by the developer. It provides a powerful and flexible way to extract data from websites, and allows developers to easily define the data they want to scrape and how it should be extracted.

Some of the key features of Scrapy include:

- Built-in support for handling HTTP requests and responses
- Ability to handle cookies and session management
- Customizable request and response middleware
- Support for multiple concurrent requests
- Built-in support for parsing HTML, XML, and JSON data
- Ability to export scraped data to various formats, such as CSV, JSON, or XML
- Support for distributed crawling and data processing
- Integration with other Python libraries, such as Pandas and NumPy

Scrapy is a popular choice for web scraping and data mining projects, and is widely used in industries such as e-commerce, finance, and media. It is a powerful and versatile tool that can help developers extract valuable insights from large amounts of data available on the web.

## Configuration

Scrapy installation
```bash
pip install scrapy
```
You can start the project 'bookscraper' by command
```bash
scrapy startproject bookscraper
```
To generate spider with name 'bookspider' to scrape the website with url 'books.toscrape.com' navigate to spiders folder and use command
```bash
scrapy genspider bookspider books.toscrape.com
```
We can use the shell feature of scrapy to find the css elements of the web page we want to scrape. Go to 'scrapy.cfg' and add your preferred shell inside configuration. Now we can run scrapy shell by command
```bash
scrapy shell
```
Now we can see the available scrapy objects inside the shell. We can use 'fetch' command to fetch the data from a url.
```bash
fetch('https://books.toscrape.com')
```
This command will put all the html page details inside a variable called 'response'. So we can get the details of element. For example if we want to get the elements with tag 'article' and class 'product_pod' we can use the command
```bash
response.css('article.product_pod')
```
It will gieve a list of elements with tag 'article' and class 'product_pod' in that page. After confirming the css of the data we want to scrape exit scrapy shell and navigate to 'bookspider' folder to run our bookspider spider using the command
```bash
scrapy crawl bookspider
```
You can save the scraped data to csv by command
```bash
scrapy crawl bookspider -O bookdata.csv
```