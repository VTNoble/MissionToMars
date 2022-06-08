from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

# importing our scrape_mars script
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection, URI (uniform resource identifier) = connection string
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
# pass in app into PyMongo
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# create a home route
@app.route("/")

# create a function
def index():
    # find one document from our mongo db and return it.
    mars_dict = mongo.db.collection.find_one()
    # pass that listing to render_template
    return render_template("index.html", mars_dict=mars_dict)

# set our path to /scrape
@app.route("/scrape")

# define a function
def scraper():

    # create a listings database
    # mars_dict = mongo.db.mars_dict

    # call the scrape function in our scrape_mars file. This will scrape and save to mongo.
    scraped_mars = scrape_mars.scrape()

    # update our mars_dict with the data that is being scraped.
    mongo.db.collection.update_one({}, {"$set": scraped_mars}, upsert=True)

    # return a message to our page so we know it was successful.
    return redirect("/", code=302)

# BOILERPLATE
if __name__ == "__main__":
    app.run(debug=True)
