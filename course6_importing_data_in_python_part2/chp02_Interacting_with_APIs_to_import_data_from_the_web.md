# Chapter 02: Interacting with APIs to import data from the web

## Pop quiz: What exactly is a JSON?
Which of the following is NOT true of the JSON file format?

### Possible Answers
JSONs consist of key-value pairs.  &emsp;&emsp; press 1
JSONs are human-readable. &emsp;&emsp; press 2
The JSON file format arose out of a growing need for real-time server-to-browser communication.  &emsp;&emsp;  press 3
The function json.load() will load the JSON into Python as a list.    &emsp;&emsp;   press 4
The function json.load() will load the JSON into Python as a dictionary.    &emsp;&emsp;   press 5

## Loading and exploring a JSON
Now that you know what a JSON is, you'll load one into your Python environment and explore it yourself. Here, you'll load the JSON 'a_movie.json' into the variable json_data, which will be a dictionary. You'll then explore the JSON contents by printing the key-value pairs of json_data to the shell.

### Instructions
* Load the JSON 'a_movie.json' into the variable json_data within the context provided by the with statement. To do so, use the function json.load() within the context manager.
* Use a for loop to print all key-value pairs in the dictionary json_data. Recall that you can access a value in a dictionary * using the syntax: dictionary[key].

### Script
```{python}
# Load JSON: json_data
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])
```

#### Output:
```
<script.py> output:
    Plot:  Harvard student Mark Zuckerberg creates the social networking site that would become known as Facebook, but is later sued by two brothers who claimed he stole their idea, and the co-founder who was later squeezed out of the business.
    Title:  The Social Network
    imdbRating:  7.7
    Response:  True
    Genre:  Biography, Drama
    BoxOffice:  $96,400,000
    Released:  01 Oct 2010
    Awards:  Won 3 Oscars. Another 165 wins & 168 nominations.
    Type:  movie
    Language:  English, French
    imdbID:  tt1285016
    Website:  http://www.thesocialnetwork-movie.com/
    Poster:  https://m.media-amazon.com/images/M/MV5BMTM2ODk0NDAwMF5BMl5BanBnXkFtZTcwNTM1MDc2Mw@@._V1_SX300.jpg
    Production:  Columbia Pictures
    Director:  David Fincher
    Ratings:  [{'Value': '7.7/10', 'Source': 'Internet Movie Database'}, {'Value': '96%', 'Source': 'Rotten Tomatoes'}, {'Value': '95/100', 'Source': 'Metacritic'}]
    imdbVotes:  546,709
    Rated:  PG-13
    Metascore:  95
    DVD:  11 Jan 2011
    Runtime:  120 min
    Country:  USA
    Writer:  Aaron Sorkin (screenplay), Ben Mezrich (book)
    Year:  2010
    Actors:  Jesse Eisenberg, Rooney Mara, Bryan Barter, Dustin Fitzsimons
```
##### Comment:
Awesome!

## Pop quiz: Exploring your JSON
Load the JSON 'a_movie.json' into a variable, which will be a dictionary. Do so by copying, pasting and executing the following code in the IPython Shell:
```
import json
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)
```
Print the values corresponding to the keys 'Title' and 'Year' and answer the following question about the movie that the JSON describes:

Which of the following statements is true of the movie in question?

### Instructions:
Possible Answers
* The title is 'Kung Fu Panda' and the year is 2010.  &emsp;&emsp;  press 1
* The title is 'Kung Fu Panda' and the year is 2008. &emsp;&emsp;  press 2
* The title is 'The Social Network' and the year is 2010.   &emsp;&emsp;  press 3
* The title is 'The Social Network' and the year is 2008.  &emsp;&emsp;  press 4

#### Output:
```
In [5]: with open('a_movie.json') as json_file:
...    json_data = json.load(json_file)
...    print("Title = {} and Year = {}".format(json_data['Title'], json_data['Year']))
Title = The Social Network and Year = 2010
```
##### Answer:
3

##### Comment:
Correct

## Pop quiz: What's an API?
Which of the following statements about APIs is NOT true?

### Possible Answers
* An API is a set of protocols and routines for building and interacting with software applications. &emsp;&emsp; press 1
* API is an acronym and is short for Application Program interface. &emsp;&emsp press 2
* It is common to pull data from APIs in the JSON file format. &emsp;&emsp press 3
* All APIs transmit data only in the JSON file format. &emsp;&emsp  press 4
* An API is a bunch of code that allows two software programs to communicate with each other.  &emsp;&emsp  press 5

#### Answer:
4

## API requests
Now it's your turn to pull some movie data down from the Open Movie Database (OMDB) using their API. The movie you'll query the API about is The Social Network. Recall that, in the video, to query the API about the movie Hackers, Hugo's query string was 'http://www.omdbapi.com/?t=hackers' and had a single argument t=hackers.

Note: recently, OMDB has changed their API: you now also have to specify an API key. This means you'll have to add another argument to the URL: apikey=ff21610b.

### Instructions:
* Import the requests package.
* Assign to the variable url the URL of interest in order to query 'http://www.omdbapi.com' for the data corresponding to the movie The Social Network. The query string should have two arguments: apikey=ff21610b and t=the+social+network. You can combine them as follows: apikey=ff21610b&t=the+social+network.
* Print the text of the reponse object r by using its text attribute and passing the result to the print() function.

#### Script:
```
# Import requests package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=ff21610b&t=the+social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)
```

#### Output:
```
<script.py> output:
    {"Title":"The Social Network","Year":"2010","Rated":"PG-13","Released":"01 Oct 2010","Runtime":"120 min","Genre":"Biography, Drama","Director":"David Fincher","Writer":"Aaron Sorkin (screenplay), Ben Mezrich (book)","Actors":"Jesse Eisenberg, Rooney Mara, Bryan Barter, Dustin Fitzsimons","Plot":"Harvard student Mark Zuckerberg creates the social networking site that would become known as Facebook, but is later sued by two brothers who claimed he stole their idea, and the co-founder who was later squeezed out of the business.","Language":"English, French","Country":"USA","Awards":"Won 3 Oscars. Another 165 wins & 168 nominations.","Poster":"https://m.media-amazon.com/images/M/MV5BMTM2ODk0NDAwMF5BMl5BanBnXkFtZTcwNTM1MDc2Mw@@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"7.7/10"},{"Source":"Rotten Tomatoes","Value":"96%"},{"Source":"Metacritic","Value":"95/100"}],"Metascore":"95","imdbRating":"7.7","imdbVotes":"546,709","imdbID":"tt1285016","Type":"movie","DVD":"11 Jan 2011","BoxOffice":"$96,400,000","Production":"Columbia Pictures","Website":"http://www.thesocialnetwork-movie.com/","Response":"True"}
```
##### Comment:
Awesome!

## JSON–from the web to Python
Wow, congrats! You've just queried your first API programmatically in Python and printed the text of the response to the shell. However, as you know, your response is actually a JSON, so you can do one step better and decode the JSON. You can then print the key-value pairs of the resulting dictionary. That's what you're going to do now!

### Instructions
* Pass the variable url to the requests.get() function in order to send the relevant request and catch the response, assigning the resultant response message to the variable r.
* Apply the json() method to the response object r and store the resulting dictionary in the variable json_data.
* Hit Submit Answer to print the key-value pairs of the dictionary json_data to the shell.

#### Script:
```
# Import package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=ff21610b&t=social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])

```
##### Output:
```
<script.py> output:
    imdbRating:  7.7
    Actors:  Jesse Eisenberg, Rooney Mara, Bryan Barter, Dustin Fitzsimons
    Awards:  Won 3 Oscars. Another 165 wins & 168 nominations.
    Website:  http://www.thesocialnetwork-movie.com/
    Released:  01 Oct 2010
    imdbVotes:  546,709
    Year:  2010
    Poster:  https://m.media-amazon.com/images/M/MV5BMTM2ODk0NDAwMF5BMl5BanBnXkFtZTcwNTM1MDc2Mw@@._V1_SX300.jpg
    Ratings:  [{'Source': 'Internet Movie Database', 'Value': '7.7/10'}, {'Source': 'Rotten Tomatoes', 'Value': '96%'}, {'Source': 'Metacritic', 'Value': '95/100'}]
    Production:  Columbia Pictures
    Writer:  Aaron Sorkin (screenplay), Ben Mezrich (book)
    Genre:  Biography, Drama
    Response:  True
    Runtime:  120 min
    DVD:  11 Jan 2011
    Plot:  Harvard student Mark Zuckerberg creates the social networking site that would become known as Facebook, but is later sued by two brothers who claimed he stole their idea, and the co-founder who was later squeezed out of the business.
    Country:  USA
    Rated:  PG-13
    BoxOffice:  $96,400,000
    Language:  English, French
    Type:  movie
    Metascore:  95
    Title:  The Social Network
    imdbID:  tt1285016
    Director:  David Fincher
```

##### Comment:
Awesome!

## Checking out the Wikipedia API
You're doing so well and having so much fun that we're going to throw one more API at you: the Wikipedia API (documented here). You'll figure out how to find and extract information from the Wikipedia page for Pizza. What gets a bit wild here is that your query will return nested JSONs, that is, JSONs with JSONs, but Python can handle that because it will translate them into dictionaries within dictionaries.

The URL that requests the relevant query from the Wikipedia API is
```
https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza
```

### Instructions:
* Assign the relevant URL to the variable url.
* Apply the json() method to the response object r and store the resulting dictionary in the variable json_data.
* The variable pizza_extract holds the HTML of an extract from Wikipedia's Pizza page as a string; use the function print() to print this string to the shell.

```{python}
# Import package
import requests

# Assign URL to variable: url
url = "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza"

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)

```

#### Output:
```
<script.py> output:
    <p class="mw-empty-elt">
    </p>
    <p>A savoury dish of Italian origin, <b>pizza</b>—a term  first recorded in the 10th century in a Latin manuscript from the Southern Italian town of Gaeta in Lazio, on the border with Campania—consists of a usually round, flattened base of leavened wheat-based dough topped with tomatoes, cheese, and various other ingredients (anchovies, olives, meat, etc.) baked at a high temperature in a traditionally wood-fired oven. In formal settings, like a restaurant, pizza is  eaten with knife and fork, but in casual settings it is cut into wedges to be eaten while held in the hand. Small pizzas are sometimes called pizzettas.   
    </p><p>Popular in many countries, pizza is a common fast food item in Europe and North America, available at any pizzeria (a restaurant specializing in pizza) or other restaurants offering Mediterranean cuisine, which usually offer pizza delivery.   Many companies sell ready-baked frozen pizzas to be reheated in an ordinary home oven. 
    </p><p>Modern pizza was invented in Naples.  The <i>Associazione Verace Pizza Napoletana</i> (True Neapolitan Pizza Association), a non-profit organization founded in 1984 with headquarters in Naples, aims to "promote and protect... the true Neapolitan pizza". In 2009, upon Italy's request, Neapolitan pizza was registered with the European Union as a Traditional Speciality Guaranteed dish.</p>
```

##### Comment:
Awesome!
