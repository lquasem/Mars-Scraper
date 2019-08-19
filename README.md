# Mars-Scraper
# Mission to Mars

A web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines the steps.

## Step 1 - Scraping

Complete initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Creating a Jupyter Notebook file called `mission_to_mars.ipynb` and use this to complete all of the scraping and analysis tasks. The following outlines what was scraped.

### NASA Mars News

1)	From [NASA Mars News Site] (https://mars.nasa.gov/news/):
latest News Title and Paragraph Text was scraped 

2)From [JPL Mars Space Imagehttps://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) the featured image was scraped

3) Mars Weather: the latest Mars weather tweet from (https://twitter.com/marswxreport?lang=en)
4) Mars Facts webpage (https://space-facts.com/mars/) was scraped to get the facts table
5) From (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)
high resolution images for each of Mar's hemispheres was scraped


## Step 2 - MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Jupyter notebook converted into a Python script called `scrape_mars.py` with a function called `scrape` that  executed the scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, created a route called `/scrape` that imports  `scrape_mars.py` script and call `scrape` function.

  * Store the return value in Mongo as a Python dictionary.

* Created a root route `/` that queries Mongo database and pass the mars data into an HTML template to display the data.

* Created a template HTML file called `index.html` that takes the mars data dictionary and display all of the data in the appropriate HTML elements. 
