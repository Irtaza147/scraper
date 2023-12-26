import scrapy

class FirmwareSpider(scrapy.Spider):
    name = 'router'
    start_urls = [
    'https://www.tp-link.com//us/support/download/archer-be900/',
    'https://www.tp-link.com//us/support/download/archer-be800/',
    'https://www.tp-link.com//us/support/download/archer-be550/',
    'https://www.tp-link.com//us/support/download/archer-be9300/',
    'https://www.tp-link.com//us/support/download/archer-axe5400/',
    'https://www.tp-link.com//us/support/download/archer-axe300/',
    'https://www.tp-link.com//us/support/download/archer-axe95/',
    'https://www.tp-link.com//us/support/download/archer-axe75/',
    'https://www.tp-link.com//us/support/download/archer-ax55/',
    'https://www.tp-link.com//us/support/download/archer-ax10000/',
    'https://www.tp-link.com//us/support/download/archer-gx90/',
    'https://www.tp-link.com//us/support/download/archer-ax11000/',
    'https://www.tp-link.com//us/support/download/archer-ax6000/',
    'https://www.tp-link.com//us/support/download/archer-ax50/',
    'https://www.tp-link.com//us/support/download/archer-ax10/',
    'https://www.tp-link.com//us/support/download/archer-ax21/',
    'https://www.tp-link.com//us/support/download/archer-ax1500/',
    'https://www.tp-link.com//us/support/download/archer-ax1450/',
    'https://www.tp-link.com//us/support/download/archer-ax3000/',
    'https://www.tp-link.com//us/support/download/archer-ax3200/',
    'https://www.tp-link.com//us/support/download/archer-a8/',
    'https://www.tp-link.com//us/support/download/archer-ac1900/',
    'https://www.tp-link.com//us/support/download/archer-a54/',
    'https://www.tp-link.com//us/support/download/archer-ax80/',
    'https://www.tp-link.com//us/support/download/archer-ax90/',
    'https://www.tp-link.com//us/support/download/archer-ax75/',
    'https://www.tp-link.com//us/support/download/archer-ax5400-pro/',
    'https://www.tp-link.com//us/support/download/archer-ax73/',
    'https://www.tp-link.com//us/support/download/archer-ax72-pro/',
    'https://www.tp-link.com//us/support/download/archer-ax55-pro/',
    'https://www.tp-link.com//us/support/download/archer-ax4400/',
    'https://www.tp-link.com//us/support/download/archer-ax1800/',
    'https://www.tp-link.com//us/support/download/archer-ax20/',
    'https://www.tp-link.com//us/support/download/archer-ax3000-pro/',
    'https://www.tp-link.com//us/support/download/archer-c80/',
    'https://www.tp-link.com//us/support/download/archer-c2700/',
    'https://www.tp-link.com//us/support/download/archer-c5400/',
    'https://www.tp-link.com//us/support/download/archer-c4000/',
    'https://www.tp-link.com//us/support/download/archer-c3200/',
    'https://www.tp-link.com//us/support/download/archer-c5400x/',
    'https://www.tp-link.com//us/support/download/tl-wr842nd/',
    'https://www.tp-link.com//us/support/download/archer-a20/',
    'https://www.tp-link.com//us/support/download/archer-c3150/',
    'https://www.tp-link.com//us/support/download/archer-c54/',
    'https://www.tp-link.com//us/support/download/archer-a10/',
    'https://www.tp-link.com//us/support/download/archer-c2600/',
    'https://www.tp-link.com//us/support/download/ad7200/',
    'https://www.tp-link.com//us/support/download/archer-c2300/',
    'https://www.tp-link.com//us/support/download/archer-c90/',
    'https://www.tp-link.com//us/support/download/archer-a9/',
    'https://www.tp-link.com//us/support/download/tl-wr842n/',
    'https://www.tp-link.com//us/support/download/archer-c9/',
    'https://www.tp-link.com//us/support/download/archer-a7/',
    'https://www.tp-link.com//us/support/download/tl-wr700n/',
    'https://www.tp-link.com//us/support/download/archer-c1900/',
    'https://www.tp-link.com//us/support/download/archer-c6/',
    'https://www.tp-link.com//us/support/download/archer-c8/',
    'https://www.tp-link.com//us/support/download/archer-c7/',
    'https://www.tp-link.com//us/support/download/archer-a6/',
    'https://www.tp-link.com//us/support/download/archer-c1200/',
    'https://www.tp-link.com//us/support/download/archer-c20/',
    'https://www.tp-link.com//us/support/download/archer-c59/',
    'https://www.tp-link.com//us/support/download/touch-p5/',
    'https://www.tp-link.com//us/support/download/archer-a5/',
    'https://www.tp-link.com//us/support/download/archer-c50/',
    'https://www.tp-link.com//us/support/download/archer-c900/',
    'https://www.tp-link.com//us/support/download/archer-c2/',
    'https://www.tp-link.com//us/support/download/tl-wr902ac/',
    'https://www.tp-link.com//us/support/download/tl-wr743nd/',
    'https://www.tp-link.com//us/support/download/tl-wr710n/',
    'https://www.tp-link.com//us/support/download/tl-wr740n/',
    'https://www.tp-link.com//us/support/download/tl-wr1043n/',
    'https://www.tp-link.com//us/support/download/tl-wr1043nd/',
    'https://www.tp-link.com//us/support/download/tl-wr940n/',
    'https://www.tp-link.com//us/support/download/tl-wr720n/',
    'https://www.tp-link.com//us/support/download/tl-wr802n/',
    'https://www.tp-link.com//us/support/download/tl-wdr3500/',
    'https://www.tp-link.com//us/support/download/tl-wr702n/',
    'https://www.tp-link.com//us/support/download/tl-wdr4300/',
    'https://www.tp-link.com//us/support/download/tl-wr810n/',
    'https://www.tp-link.com//us/support/download/tl-wdr3600/',
    'https://www.tp-link.com//us/support/download/tl-wr1042nd/',
    'https://www.tp-link.com//us/support/download/tl-wr941nd/',
    'https://www.tp-link.com//us/support/download/tl-wr841nd/',
    'https://www.tp-link.com//us/support/download/tl-wr841n/',
    'https://www.tp-link.com//us/support/download/tl-wr741nd/',
    'https://www.tp-link.com//us/support/download/archer-c5200/',
    'https://www.tp-link.com//us/support/download/archer-c3000/',
    'https://www.tp-link.com//us/support/download/archer-a2300/',
    'https://www.tp-link.com//us/support/download/ap9670/',
    'https://www.tp-link.com//us/support/download/ap9650/',
    'https://www.tp-link.com//us/support/download/ap9635/',
    'https://www.tp-link.com//us/support/download/ap8635-i/',
    'https://www.tp-link.com//us/support/download/ap7650/',
    
]

    custom_settings = {
        'FEEDS': {
            'file:///D:/University/FYP/Scraper/firmware/router.csv': {
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
            # Extract download link using a more general CSS selector
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


        


