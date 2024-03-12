
## Hr 1 - Introducing

* Self-Introduction: Use one sentence to introduce yourself. Also, share with us your favourite thing about programming and why.
Post on the padlet. We will share with the group

* Specify at least one type of computing project that interested you the most (software app, data visualisation, an AI application, robotics, cybersecurity, design, etc) Then post on the padlet ( Likes and comments on each other posts! )

* Introduction to the unit (objectives and goals for this session) and intro to data collection, exploring data and hands-on mapping exercise

## Hr 2 - In class activity

### Discovering Geographic Data with OpenStreetMap APIs

Today, we're going on a digital adventure to learn how we can explore the use of open maps. 
We're going to use something called the OpenStreetMap (OSM) API and the Overpass API. These are tools that allow us to dive into a global map and pull out exactly the information we want. 
Imagine being able to find every coffee shop in London or all the parks in New York City with just a few lines of code!

**What is OpenStreetMap (OSM)?**

OpenStreetMap is like Wikipedia but for maps. It's a massive project where people all around the world work together to create a free and editable map of the entire globe. That's right, free! This means you can use it to find places, create routes, or even add new information.

**Why Use the OSM API?**

The OSM API is a way for us to talk to the OpenStreetMap database. Here's what we can do with it:

    *Read Data:* Grab map data like locations, roads, and buildings.
    *Edit Data:* Add new places or update existing ones.
    *User Authentication:* Log in and contribute to the map.

It's perfect for building apps that need map data or for creating your own customized maps.

**The Power of Overpass API**

While the OSM API is fantastic, the Overpass API is where the magic really happens for data queries. It's a read-only API, which means it's all about pulling data out in clever ways, but you can't change the map with it.

*What's Overpass API?*

Think of the Overpass API as a super-search engine for map data. 
It uses its own language, Overpass QL, to let you ask very specific questions. 

Want to find all the cafes in London? Or how about every public swimming pool in London? 

The Overpass API can help you find these answers.

**Finding Coffee Shops in London**

Let's put this into practice with a real example. We're going to find coffee shops in a specific area of London called "Holborn." Here's how we do it:

*Understanding the Query*

We start with a query that looks for places tagged as `"London,`" then zoom in on the `"Holborn"` area within 500 meters, and finally, we look for locations tagged as "cafes."

Here's the query we use:


```json
area[name="London"]->.searchArea;
node(area.searchArea)["place"="suburb"]["name"="Holborn"]->.holborn;
node(around.holborn:500)["amenity"="cafe"];
out;
```

*Breaking It Down*

    Find London: We define an area named "London" and store it as .searchArea.

 

```json
area[name="London"]->.searchArea;
```

Zoom in on Holborn: Next, we find the suburb "Holborn" within our London area.


```json
node(area.searchArea)["place"="suburb"]["name"="Holborn"]->.holborn;
```

Find Cafes: Finally, we look for nodes tagged as "cafes" around Holborn, within 500 meters.


  ```json
    node(around.holborn:500)["amenity"="cafe"];
    out;
  ```

*What's Happening Here?*

    *Filtering by London:* This makes sure we only look at places in London.
    *Narrowing Down to Holborn:* We get even more specific by focusing on a single suburb.
    *Selecting Cafes:* We find all the coffee shops in this area.


## Hr 3 - Data Collection activity

1. Form teams of two
2. Give yourself a group name and post your group name on the padlet here. This will be your reference for the two-week mapping project
3. Go around Holborn and collect data on various places: coffee shops, fast food restaurants, offices, hotels, etc.
5. Record any data you think is relevant (think about ethics).
5. [Data collection journal](https://demo.hedgedoc.org/s/3uc1GbiDx#)

