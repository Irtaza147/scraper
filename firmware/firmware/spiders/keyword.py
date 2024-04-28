import scrapy
import pandas as pd
from classroom.models import ScrapedData
class MySpider(scrapy.Spider):
    name = 'myspider'

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'FEED_FORMAT': 'csv',  # Save the scraped data in CSV format
        'FEED_URI': 'D:/University/FYP/ISPR-main/ISPR-main/ISPR_front_end/scrap_data.csv',  # Specify the file path to store the scraped data
        'FEED_EXPORT_ENCODING': 'utf-8'  # Specify encoding for the CSV file
    }
    
    def __init__(self, keyword=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.keyword = str(keyword) if keyword else None
        
        # Initialize an empty list to store scraped data
        self.data = []

        # Read URLs from Excel file
        self.start_urls = pd.read_excel('D:/University/FYP/links.xlsx')['Links'].tolist()

    def parse(self, response):
        # Check if the response body is text (HTML or similar)
        if not isinstance(response.text, str):
            return
        
        # Convert response text to lowercase for case-insensitive matching
        response_text = response.text.lower()
        
        # Check if the keyword exists in the response text
        if self.keyword and self.keyword.lower() in response_text:
            print(f"Keyword '{self.keyword}' found on page: {response.url}")
            if '#Firmware' in response.url:
                yield from self.parse_page_with_fragment(response)
            else:
                yield from self.parse_page(response)
        else:
            print(f"Keyword '{self.keyword}' not found on page: {response.url}")
        
        

    def parse_page(self, response):
        # Your parsing logic here
        model_name = response.xpath('//em[@id="model-version-name"]/text()').get()
        firmware_version = response.xpath('//span[@class="current-version"]/text()').get()
        download_link = response.css('a.tp-dialog-btn-white.ga-click::attr(href)').get()
        version_xpath = response.xpath('//h2[contains(@class, "featurette-heading")]/text()').get()
        tenda_download_link = response.css('a.btnDown::attr(href)').get()

        # Construct absolute download link
        absolute_download_link = response.urljoin(tenda_download_link) if tenda_download_link else None
        
        data = {
            'model_name': model_name,
            'firmware_version': firmware_version,
            'download_link': download_link,
            'version_xpath': version_xpath,
            'absolute_download_link': absolute_download_link,
            'source_url': response.url
}

         # Save data into Django model
        ScrapedData.objects.create(
            model_name=model_name,
            firmware_version=firmware_version,
            source_url=response.url,
            download_link=download_link,
            tenda_download_link=absolute_download_link,
        )

        print(data)  # Print the scraped data to the console
        self.data.append(data)  # Append data to self.data list
        yield data
    
    def parse_page_with_fragment(self, response):
        # Your parsing logic here
        firmware_details = response.css('table.download-resource-table th.download-resource-name p::text').get()
        download_link = response.css('a.tp-dialog-btn-white.ga-click::attr(href)').get()

        data = {
            'firmware_details': firmware_details,
            'download_link': download_link,
            'source_url': response.url
        }
        
        print(data)  # Print the scraped data to the console
        self.data.append(data)  # Append data to self.data list
        yield data
