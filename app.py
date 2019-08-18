from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# mongo = PyMongo(app)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_info")

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars = mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars 
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)





















# from flask import Flask, render_template, jsonify, redirect
# from flask_pymongo import PyMongo
# import scrape_mars

# app = Flask(__name__)




# # # connect to mongo db and collection

# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_info")

# # mongo = PyMongo(app)


# #initial route
# @app.route('/')
# def index():
#     # Find one record of data from the mongo database
#     mars = mongo.db.mars_info.find_one()
#     return render_template('index.html', mars = mars) 
    
# @app.route('/scrape')
# def scrape():


#     # mars = mongo.db.mars_db
   
#     # mongo.db.mars_info.update({}, data, upsert=True)


#     # Update the Mongo database using update and upsert=True
#     # mongo.db.collection.update({}, mars_data, upsert=True)
#     mars = mongo.db.mars 
#     mars_data = scrape_mar.scrape()

#     mars.update({}, mars_data, upsert=True)
#     return redirect("http://localhost:5000/", code=302)



#     # Redirect back to home page
#     return redirect("/")

    
    

# if __name__ == "__main__":
#     app.run(debug=True)
    