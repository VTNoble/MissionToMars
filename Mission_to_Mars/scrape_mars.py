# Automates browser actions
from splinter import Browser

# Parses the HTML
from bs4 import BeautifulSoup
import pandas as pd
import time

# For scraping with Chrome
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    # Setup splinter
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Set an empty dict for scraped data that we can save to Mongo
    mars_dict = {}

    # The url we want to scrape
    url = "https://redplanetscience.com/"
    
    # Call visit on our browser and pass in the URL we want to scrape   
    browser.visit(url)

    # Let it sleep for 1 second
    time.sleep(1)

    # Return all the HTML on our page
    html = browser.html
    
    # Create a Beautiful Soup object, pass in our HTML, and call 'html.parser'
    soup = BeautifulSoup(html, "html.parser")

    # scrape the titles
    titles = soup.find_all('div', class_='content_title')

    # grab latest title and assign to variable
    news_title = titles[0].text

    # scrape the paragraphs
    pars = soup.find_all('div', class_='article_teaser_body')

    # grab latest paragraph and assign to variable
    news_p = pars[0].text

    # Build our dictionary for the news_title and news_p from our scraped data
    mars_dict["news_title"] = news_title
    mars_dict["news_p"] = news_p

    # url to scrape
    url = 'https://spaceimages-mars.com'

    # visit the url in the headless browser
    browser.visit(url)

    # Let it sleep for 1 second
    time.sleep(1)

    # grab the html
    html = browser.html

    # create the soup
    soup = BeautifulSoup(html, 'html.parser')

    # find featured image and assign to variable
    featured_image = soup.find(class_='headerimage', src=True)

    # extract src from image, build and assign url to variable
    featured_image_url = url + '/' + featured_image.get('src')

    # Build our dictionary for the featured_image-url from our scraped data
    mars_dict["featured_image_url"] = featured_image_url

    # url to scrape
    url = 'https://galaxyfacts-mars.com'

    # use pandas read_html to parse the url
    tables = pd.read_html(url)

    # assign desired table to 'df'
    df = tables[0]

    # format df
    # assign columns
    df.columns = ['Description', 'Mars', 'Earth']

    # drop row that is no longer needed
    df.drop([0], inplace=True)

    # set index to 'Description' column
    df.set_index('Description', inplace=True)

    # Build our dictionary for the df (as html) from our scraped data
    mars_dict["mars_table"] = df.to_html()

    # url to scrape
    url = 'https://marshemispheres.com/'

    # create hemispheres list
    hemispheres = ['cerberus', 'schiaparelli', 'syrtis', 'valles']

    # loop through hemispheres and build dictionary
    hemisphere_image_urls = []
    for hemisphere in hemispheres:
        
        # visit url
        browser.visit(url + hemisphere + '.html')
        
        # Let it sleep for 1 second
        time.sleep(1)

        # grab the html
        html = browser.html
        
        # create the soup
        soup = BeautifulSoup(html, 'html.parser')
        
        # grab title
        title = soup.find('h2', class_='title').text
        
        # grab url
        div_w = soup.find('div', class_='wrapper')
        div_c = div_w.find('div', class_='container')
        div_wi = div_c.find('div', class_='wide-image-wrapper')
        div_d = div_wi.find('div', class_='downloads')
        link = div_d.find('a')
        img_url = url + link['href']
        
        # create dictionary and append to list
        hemisphere_image_urls.append({'title': title, 'img_url': img_url})

    # Build our dictionary for the hemisphere_image_urls from our scraped data
    mars_dict["hemisphere_image_urls"] = hemisphere_image_urls
    
    # Quit the browser
    browser.quit()

    # Return our dictionary
    return mars_dict
