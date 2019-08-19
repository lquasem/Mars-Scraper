#import dependencies
from bs4 import BeautifulSoup
import pandas as pd
from splinter import Browser
import time
import lxml


def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
  
    browser = init_browser()

    # visit nasa's mars news site
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(1)
    # scrape latest article title/para

    
    time.sleep(2)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


    title = soup.find("div", class_="content_title").get_text()
    news_p = soup.find("div", class_="rollover_description_inner").get_text()





    # visit jpl's mars images site 
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    time.sleep(1)
    browser.find_by_css('div.carousel_items a.fancybox').click()
    time.sleep(1)
    # scrape featured image url
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    featured_image = soup.find('img', class_='fancybox-image')
    featured_image_url = "https://www.jpl.nasa.gov" + \
        str(featured_image).split(" ")[2].split('"')[1]

    # scrape tweet from mars weather twitter account
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    time.sleep(1)
    mars_weather = browser.find_by_css(
        'div.js-tweet-text-container p.tweet-text').text


    # scrape table from mars facts
       # Get Mars Facts
    
    url = "https://space-facts.com/mars/"
    browser.visit(url)
    
    time.sleep(2)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    

    mars_facts_df = pd.read_html(url)[0]
    mars_facts_df = mars_facts_df.rename(index=str, columns={0: "Description", 1: "Value"})
    mars_table = mars_facts_df.to_html(index='False')


    
    return mars_table

     # hemisphere URLs
    hemis_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemis_url)
    time.sleep(2)
    
    mars_hemis= []

    for i in range (4):
        time.sleep(5)
        images = browser.find_by_tag('h3')
        images[i].click()
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        partial = soup.find("img", class_="wide-image")["src"]
        img_title = soup.find("h2",class_="title").text
        img_url = 'https://astrogeology.usgs.gov'+ partial
        dictionary={"title":img_title,"img_url":img_url}
        mars_hemis.append(dictionary)
        browser.back()

   
    #     {"title1" : "Cerberus Hemisphere", "img_url" : "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg" },
    #     {"title2" : "Schiaparelli Hemisphere", "img_url" : "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    #     {"title3" : "Syrtis Major Hemisphere", "img_url" : "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    #     {"title4" : "Valles Marineris Hemisphere", "img_url" : "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"}]

    return mars_hemis

    mars_data = {
        "news_title": title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "mars_facts": mars_table,
        "hemisphere_urls": mars_hemis
        
    }

    return mars_data