import scrapy

class FirmwareSpider(scrapy.Spider):
    name = 'camera'
    start_urls = [
    'https://www.tp-link.com//us/support/download/tc85/',
    'https://www.tp-link.com//us/support/download/tapo-c120/',
    'https://www.tp-link.com//us/support/download/tapo-c125/',
    'https://www.tp-link.com//us/support/download/tapo-c325wb/',
    'https://www.tp-link.com//us/support/download/tc73/',
    'https://www.tp-link.com//us/support/download/tapo-c420s2/',
    'https://www.tp-link.com//us/support/download/tapo-c425-%252b-tapo-a200/',
    'https://www.tp-link.com//us/support/download/tapo-c500/',
    'https://www.tp-link.com//us/support/download/tapo-c520ws/',
    'https://www.tp-link.com//us/support/download/tapo-c510w/',
    'https://www.tp-link.com//us/support/download/tapo-c420s1/',
    'https://www.tp-link.com//us/support/download/tapo-c111/',
    'https://www.tp-link.com//us/support/download/tapo-c211/',
    'https://www.tp-link.com//us/support/download/tapo-c425/',
    'https://www.tp-link.com//us/support/download/tapo-c400s2/',
    'https://www.tp-link.com//us/support/download/tapo-c210/',
    'https://www.tp-link.com//us/support/download/kc310s2/',
    'https://www.tp-link.com//us/support/download/tapo-c200/',
    'https://www.tp-link.com//us/support/download/kc110/',
    'https://www.tp-link.com//us/support/download/tapo-a100/',
    'https://www.tp-link.com//us/support/download/tapo-a200/',
    'https://www.tp-link.com//us/support/download/tapo-c100/',
    'https://www.tp-link.com//us/support/download/tapo-c110/',
    'https://www.tp-link.com//us/support/download/ec71/',
    'https://www.tp-link.com//us/support/download/tapo-c310/',
    'https://www.tp-link.com//us/support/download/ec60/',
    'https://www.tp-link.com//us/support/download/tapo-c225/',
    'https://www.tp-link.com//us/support/download/tapo-c320ws/',
    'https://www.tp-link.com//us/support/download/kd110/',
    'https://www.tp-link.com//us/support/download/kc420ws/',
    'https://www.tp-link.com//us/support/download/kc400/',
    'https://www.tp-link.com//us/support/download/kc410s/',
    'https://www.tp-link.com//us/support/download/kc105/',
    'https://www.tp-link.com//us/support/download/kc401/',
    'https://www.tp-link.com//us/support/download/kc411s/',
    'https://www.tp-link.com//us/support/download/kc300s2/',
    'https://www.tp-link.com//us/support/download/tl-nc450/',
    'https://www.tp-link.com//us/support/download/kc200/',
]

    custom_settings = {
        'FEEDS': {
            'file:///D:/University/FYP/Scraper/firmware/smart_cameras.csv': {
                'format': 'csv',
                'overwrite': True,
            },
        },
    }

    def parse(self, response):
         # Add "#Firmware" to the URL
        firmware_url = response.urljoin("#Firmware-Release-Notes")

        if "#Firmware-Release-Notes" in response.urljoin(firmware_url):
            # Parse firmware details from the table with class "download-resource-table"
            firmware_details = response.css('table.download-resource-table th.download-resource-name p::text').get()
            
            # Extract download link from the "Download" button
            download_link = response.css('a.tp-dialog-btn-white.ga-click::attr(href)').get()

            # Print and yield the extracted firmware details
            self.log(f'Firmware Details: {firmware_details}')
            self.log(f'Download Link: {download_link}')

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

            # You can further process or yield the extracted data as needed
            yield {
               
                'model_name': model_name_xpath,
                'firmware_version': version_xpath,
                'Datasheet download_link': download_link_xpath,
                'Visited URL': firmware_url,
                'firmware_details': firmware_details,
                'download_link': download_link,
                'source_url': response.url,
                
            }
        else:
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

            # You can further process or yield the extracted data as needed
            yield {
                'model_name': model_name_xpath,
                'firmware_version': version_xpath,
                'Datasheet download_link': download_link_xpath,
                'Visited URL': firmware_url,
            }

