# --- Python scrapy bot ---

## Scrap site: quotes.toscrape.com

### Install steps: 
- Install python -> https://www.python.org/
- Create virtual environment -> python -m virtualenv quotes
- Activate virutal environment -> source ./Scripts/activate
- Install Scrapy -> install Scrapy
- Start project -> startproject quotes
- Change directory to scrapy project -> cd quotes
- Start scrapy -> scrapy crawl quotes

### Useful commands
- Save data in JSON file -> scrapy crawl quotes -o file.json
- Shell -> sprapy shell quotes.toscrape.com
- Css selectors - class "." - id "#" -> response.css('.text::text').extract()
- Return a list with extracted data -> .extract()
- Extract first -> response.css('.text::text')[0].extract()
- Extract first -> response.css('.text::text').extract_first()
- w/ XPATH -> response.xpath("//span[@class='text']/text()").extract()
