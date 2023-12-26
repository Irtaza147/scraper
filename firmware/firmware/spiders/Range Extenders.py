import scrapy

class FirmwareSpider(scrapy.Spider):
    name = 'range'
    start_urls = [
    'https://www.tp-link.com//us/support/download/re220/',
    'https://www.tp-link.com//us/support/download/re315/',
    'https://www.tp-link.com//us/support/download/re550/',
    'https://www.tp-link.com//us/support/download/re715x/',
    'https://www.tp-link.com//us/support/download/re700x/',
    'https://www.tp-link.com//us/support/download/re815xe/',
    'https://www.tp-link.com//us/support/download/re500x/',
    'https://www.tp-link.com//us/support/download/re505x/',
    'https://www.tp-link.com//us/support/download/re815x/',
    'https://www.tp-link.com//us/support/download/re650/',
    'https://www.tp-link.com//us/support/download/re600x/',
    'https://www.tp-link.com//us/support/download/re603x/',
    'https://www.tp-link.com//us/support/download/re105/',
    'https://www.tp-link.com//us/support/download/re605x/',
    'https://www.tp-link.com//us/support/download/re705x/',
    'https://www.tp-link.com//us/support/download/re615x/',
    'https://www.tp-link.com//us/support/download/re450/',
    'https://www.tp-link.com//us/support/download/re330/',
    'https://www.tp-link.com//us/support/download/re215/',
    'https://www.tp-link.com//us/support/download/re500/',
    'https://www.tp-link.com//us/support/download/re580d/',
    'https://www.tp-link.com//us/support/download/re400/',
    'https://www.tp-link.com//us/support/download/re300/',
    'https://www.tp-link.com//us/support/download/re355/',
    'https://www.tp-link.com//us/support/download/re350k/',
    'https://www.tp-link.com//us/support/download/re305/',
    'https://www.tp-link.com//us/support/download/re230/',
    'https://www.tp-link.com//us/support/download/re360/',
    'https://www.tp-link.com//us/support/download/tl-wa855re/',
    'https://www.tp-link.com//us/support/download/re380d/',
    'https://www.tp-link.com//us/support/download/re350/',
    'https://www.tp-link.com//us/support/download/re205/',
    'https://www.tp-link.com//us/support/download/re210/',
    'https://www.tp-link.com//us/support/download/re200/',
    'https://www.tp-link.com//us/support/download/tl-wa860re/',
    'https://www.tp-link.com//us/support/download/tl-wa850re/',
    'https://www.tp-link.com//us/support/download/tl-wa854re/',
    'https://www.tp-link.com//us/support/download/tl-wa750re/',
    'https://www.tp-link.com//us/support/download/tl-wa830re/',
    'https://www.tp-link.com//us/support/download/tl-wa730re/',
    
]

    custom_settings = {
        'FEEDS': {
            'file:///D:/University/FYP/Scraper/firmware/range.csv': {
                'format': 'csv',
                'overwrite': True,
            },
        },
    }

    def parse(self, response):
       # Add "#Firmware" to the URL
        firmware_url = response.urljoin("#Firmware")

        if "#Firmware" in response.urljoin(firmware_url):
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


