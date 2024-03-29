#Dependencies
  
import os
import time
import requests
import pandas as pd #pandas 
from splinter import Browser 
from bs4 import BeautifulSoup 
from webdriver_manager.chrome import ChromeDriverManager


def scrape_info():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://redplanetscience.com/'

    browser.visit(url)  

    html = browser.html
    firstsoup = BeautifulSoup(html, 'html.parser')

    ## Step 1 - Scraping
    ### NASA Mars News

    results = firstsoup.find_all('div', class_='list_text')[0]
    latest_News_title = (results.find("div", class_='content_title').text)
    results

    results2 = firstsoup.find_all('div',  class_='list_text')
    Paragraphtext = (results.find('div',  class_='article_teaser_body').text)

    Paragraphtext

    soup = BeautifulSoup(html)
    soup.title.text.strip()

    soup.body.p.text

    browser.visit(url)

    paragrpahs = soup.body.find_all('p')

    paragrpahs[8].text

    paragraphs = soup.find_all('p')

    for paragraph in paragraphs:
        print(paragraph.text)

    title=soup.find_all('title')

    for title in title:
        print(title.text)

    

    ### JPL Mars Space Images - Featured Image

#              executable_path={
#                  'executable_path': ChromeDriverManager().install()}
#              browser=Browser('chrome', **executable_path, headless=False)

    url='https://spaceimages-mars.com'
    browser.visit(url)


    browser.links.find_by_partial_text('FULL IMAGE').click()
    featured_image_url='https://spaceimages-mars.com/image/featured/mars2.jpg'


    ### Mars Facts

    #import pandas as pd

    url='https://galaxyfacts-mars.com'
    table =pd.read_html(url)[0]  
    print(table)
    # You need to covert this table to html
    tables = table.to_html()
    ### Mars Hemispheres

    url='https://marshemispheres.com/'


    browser.visit(url)
    links=browser.find_by_css('a.product-item img')

    hemisphere_img_url=[]

    for i in range(len(links)):
            browser.find_by_css('a.product-item img')[i].click()
            # we are on the page finding the picture
            sample_elem=browser.links.find_by_text('Sample').first
            title=browser.find_by_css('h2.title').text


            # we found the picture, now we save it into our list (append)
            img_url=sample_elem['href']
            print(f' Page {i} image url: {img_url}')
            hemisphere_img_url.append({
                "title": title,
                "img_url": img_url
            })
            #we are done with this page, lets go back for the next page.
            browser.back()
    browser.quit()
    hemisphere_img_url

    scrape_data= {
        "news_title": latest_News_title,
        "news_paragraph":  Paragraphtext,
        "featured_image_url": featured_image_url,
        "html_table": tables,
        "hemisphere_img_urls": hemisphere_img_url
    }
    return scrape_data
# choclate cake to allow for imports not acting weird
if __name__ == '__main__':
    print(scrape_info())