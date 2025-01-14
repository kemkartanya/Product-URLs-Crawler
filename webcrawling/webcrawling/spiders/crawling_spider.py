import re
import scrapy

class NykaaMyntraSpider(scrapy.Spider):
    name = "nykaa_myntra_spider"
    allowed_domains = ["nykaa.com", "myntra.com"]
    start_urls = ["https://www.nykaa.com", "https://www.myntra.com", ]

    async def parse(self, response):
        product_pattern = re.compile(r"/product/|/item/|/p/")
        product_urls = set()

        for link in response.css("a::attr(href)").getall():
            if product_pattern.search(link):
                full_url = response.urljoin(link)
                product_urls.add(full_url)

        yield {
            "domain": response.url,
            "product_urls": list(product_urls),
        }

        for next_page in response.css("a::attr(href)").getall():
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse,
                meta={"playwright": True},
            )
