# web-scraping-challenge
Unit 12 Homework: Mission to Mars

In this assignment, web scraping was performed in a jupyter notebook to compile various components to ultimately be incorporated into a web page. Splinter was used to navigate web pages and BeautifulSoup was used to find and parse out the necessary data. Pandas scraping was also utilized to scrape a table.

After the data was scraped in a jupyter notebook, the notebook was then converted into a Python Script by using a function called 'scrape'. This function executes all scraping code from the jupyter notebook and returns it into one Python dictionary.

A Flask App was created that connects, fetches, and inserts data to and from MongoDB, which was then rendered into a template. Bootstrap was used to style the webpage.

The Mission_to_Mars folder includes the following:
* mission_to_mars.ipynb: jupyter notebook used to initially scrape all data
* scrape_mars.py: python script with converted jupyter notebook code
* app.py: Flask app to set up home and scrape routes and build mongo database
* templates folder: holds index.html file with Bootstrap styling

A screenshot of the final application is also included in the repository.