from bs4 import BeautifulSoup

html = """

<div class="item tp-ada-mouseactivate" data-class="" data-id="21320" data-ids="|353|">
                      <h2 class="">
                        <span class="tp-m-hide">WiFi</span>
                        <span class="tp-m-show">WiFi</span>
                        <i class="tp-dropdown-icon tp-active"></i>
                      </h2>
                      <div class="item-box" style="display: block;">
                                                  <span>
                            <a class="ga-click" data-vars-event-category="Support-Download_AP9670" href="/us/support/download/ap9670/" target="_blank" aria-label="AP9670">AP9670</a>
                          </span>
                                                  <span>
                            <a class="ga-click" data-vars-event-category="Support-Download_AP9650" href="/us/support/download/ap9650/" target="_blank" aria-label="AP9650">AP9650</a>
                          </span>
                                                  <span class="">
                            <a class="ga-click" data-vars-event-category="Support-Download_AP9635" href="/us/support/download/ap9635/" target="_blank" aria-label="AP9635">AP9635</a>
                          </span>
                                                  <span>
                            <a class="ga-click" data-vars-event-category="Support-Download_AP8635-I" href="/us/support/download/ap8635-i/" target="_blank" aria-label="AP8635-I">AP8635-I</a>
                          </span>
                                                  <span>
                            <a class="ga-click" data-vars-event-category="Support-Download_AP7650" href="/us/support/download/ap7650/" target="_blank" aria-label="AP7650">AP7650</a>
                          </span>
                                              </div>
                    </div>

"""


soup = BeautifulSoup(html, 'html.parser')

# Find all anchor tags with class 'ga-click' inside the div with class 'item-box'
link_anchors = soup.select('div.item-box a.ga-click')

# Extract href attributes from the anchor tags
base_url = "https://www.tp-link.com/"
links = [base_url + anchor['href'] for anchor in link_anchors]

start_urls = [f"'{link}'" for link in links]

# Print the start_urls list
print("start_urls = [")
for start_url in start_urls:
    print(f"    {start_url},")
print("]")