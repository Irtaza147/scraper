import scrapy

class FirmwareSpider(scrapy.Spider):
    name = 'access'
    start_urls = [
    'https://www.tp-link.com//us/support/download/pharos-control/',
    'https://www.tp-link.com//us/support/download/cpe710/',
    'https://www.tp-link.com//us/support/download/cpe610/',
    'https://www.tp-link.com//us/support/download/cpe510/',
    'https://www.tp-link.com//us/support/download/cpe210/',
    'https://www.tp-link.com//us/support/download/wbs510/',
    'https://www.tp-link.com//us/support/download/wbs210/',
    'https://www.tp-link.com//us/support/download/tl-wa7510n/',
    'https://www.tp-link.com//us/support/download/tl-wa7210n/',
    'https://www.tp-link.com//us/support/download/tl-wa5210g/',
    
]

    custom_settings = {
        'FEEDS': {
            'file:///D:/University/FYP/Scraper/firmware/access.csv': {
                'format': 'csv',
                'overwrite': True,
            },
        },
    }

    def parse(self, response):
        # Extract firmware version using XPath
        version_xpath = response.xpath('//h2[contains(@class, "featurette-heading")]/text()').get().strip()

        # Extract model name using XPath
        model_name_xpath = response.xpath('//p[contains(strong, "Hardware Version")]/text()').get().strip().split(':')[-1]

        # Extract download link using XPath
        download_link_xpath = response.xpath('//a[contains(@class, "btnDown")]/@href').get()

        # Print the extracted version, model name, and download link
        self.log(f'Firmware Version: {version_xpath}')
        self.log(f'Model Name: {model_name_xpath}')
        self.log(f'Download Link: {download_link_xpath}')
        self.log(f'URL: {response.url}')

        # You can further process or yield the extracted data as needed
        yield {
            'model_name': model_name_xpath,
            'firmware_version': version_xpath,
            'download_link': download_link_xpath,
            'visited_url': response.url,
        }


