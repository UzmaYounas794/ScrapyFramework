import scrapy


class ScrapbotSpider(scrapy.Spider):
    name = "scrapBot"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Web_scraping"]
    base_url = "https://en.wikipedia.org"
    custom_settings = {"DEPTH_LIMIT": 1}

    def parse(self, response):

        for next_page in response.css("div.mw-parser-output > p > a"):
            yield response.follow(next_page, self.parse)

        for quote in response.css("#firstHeading::text"):
            yield {"quote": quote.extract()}
