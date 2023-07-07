import scrapy
from ..items import QuotesItem

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class QuoteSpider(scrapy.Spider):

    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def __init__(self):
        self.data = []

    def parse(self, response):

        items = QuotesItem()

        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:

            title = quotes.css('span.text::text').extract_first()
            author = quotes.css('.author::text').extract_first()
            tags = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tags'] = tags
            
            self.data.append({
                'title': title, 
                'author': author, 
                'tags': tags
            })

            yield items

        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)
        else:
            self.sendEmail()

    def sendEmail(self):
        
        print('\n******* Total quotes = ' + str(len(self.data)) + ' ********\n')

        # Email details
        sender_email = ''
        receiver_email = ''
        subject = 'Quotes'
        message = 'Quotes \n\n'
        for item in self.data:
            print(item)
            message += f"\nTitle: {item['title']}\n Author: {item['author']}\n Tags: {', '.join(item['tags'])}\n"

        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        
        # Attach the message to the email
        msg.attach(MIMEText(message, 'plain'))
        
        # SMTP server details (for Outlook)
        smtp_server = 'smtp.office365.com'
        smtp_port = 587
        smtp_username = sender_email
        smtp_password = ''
        
        # Create a secure connection to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
            print('\n***** Email sent successfully *****\n')