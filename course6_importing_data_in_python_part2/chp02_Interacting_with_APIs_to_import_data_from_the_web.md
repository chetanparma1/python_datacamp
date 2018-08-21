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
