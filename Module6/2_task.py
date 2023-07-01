import scrapy
from scrapy.crawler import CrawlerProcess
import csv


class SteamSpider(scrapy.Spider):
    name = "steam_spider"
    start_urls = ["https://store.steampowered.com/search/?tags=4182&filter=topsellers&page=1"]
    game_count = 0

    def parse(self, response):
        num_pages = 45
        for page_num in range(1, num_pages + 1):
            url = f"https://store.steampowered.com/search/?filter=topsellers&page={page_num}"
            if self.game_count < 1000:
                yield scrapy.Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        games = response.css("a.search_result_row")
        for game in games:
            href = game.xpath('@href').get()
            title = game.css("span.title::text").get()
            if self.game_count < 1000:
                yield scrapy.Request(url=href, callback=self.parse_tags, meta={'title': title})

    def parse_tags(self, response):
        is_game = response.css('.game_area_purchase_game::attr(style)').get() is None
        title = response.meta.get("title")
        if is_game:
            game_tags = response.css('.app_tag::text').getall()
            if game_tags:
                game_tags = [tag.strip() for tag in game_tags if tag != "+"]
                with open('game_tags.csv', 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    if self.game_count < 1000:
                        writer.writerow([title, *game_tags])
                        self.game_count += 1


process = CrawlerProcess()
process.crawl(SteamSpider)
process.start()
