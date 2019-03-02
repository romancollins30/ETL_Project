from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mlb

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/baseball_db")

@app.route("/")
def home():

    # Find one record of data from the mongo database
    data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", scraped=data)



@app.route("/scrape")
def scrape():

    # Run the scrape function
    baseball_data = scrape_mlb.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, baseball_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
