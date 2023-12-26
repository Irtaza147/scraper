import scrapy

class FirmwareSpider(scrapy.Spider):
    name = 'modem'
    start_urls = [
     'https://www.tp-link.com//us/support/download/tc-7620/',
    'https://www.tp-link.com//us/support/download/tc-7610/',
    'https://www.tp-link.com//us/support/download/tc7650/',
    
]

    custom_settings = {
        'FEEDS': {
            'file:///D:/University/FYP/Scraper/firmware/cable_modem.csv': {
                'format': 'csv',
                'overwrite': True,
            },
        },
    }

    def parse(self, response):
        # Extract firmware version using XPath
        version_xpath = response.xpath('//span[@class="current-version"]/text()').get()

        # Extract model name using XPath
        model_name_xpath = response.xpath('//em[@id="model-version-name"]/text()').get()

        # Extract download link with text "_V1.6_Datasheet" using XPath
        download_link_xpath = response.xpath('//a[@class="ga-click" and contains(@data-vars-event-category, "Download-Datasheet")]/@href').get()

        # Print the extracted version, model name, and download link
        print(f'Firmware Version: {version_xpath}')
        print(f'Model Name: {model_name_xpath}')
        print(f'Datasheet download_link: {download_link_xpath}')
        print(f'URL: {response.url}')

        # You can further process or yield the extracted data as needed
        yield {
            'model_name': model_name_xpath,
            'firmware_version': version_xpath,
            'Datasheet download_link': download_link_xpath,
            'Visited URL': response.url,
        }


