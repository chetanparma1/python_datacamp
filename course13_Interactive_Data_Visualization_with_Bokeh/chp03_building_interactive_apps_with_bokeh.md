# Chapter 03: Building Interactive Apps with Bokeh

## 01. Understanding Bokeh apps
The main purpose of the Bokeh server is to synchronize python objects with web applications in a browser, so that rich, interactive data applications can be connected to powerful PyData libraries such as NumPy, SciPy, Pandas, and scikit-learn.

What sort of properties can the Bokeh server automatically keep in sync?

### Possible Answers
* Only data source objects.
** press 1
* Only glyph properties.
** press 2
* Any property of any Bokeh object.
** press 3

#### Answer:
3

#### Comment:
Correct. Bokeh server will automatically keep every property of any Bokeh object in sync.

## 02. Using the current document
Let's get started with building an interactive Bokeh app. This typically begins with importing the curdoc, or "current document", function from bokeh.io. This current document will eventually hold all the plots, controls, and layouts that you create. Your job in this exercise is to use this function to add a single plot to your application.

In the video, Bryan described the process for running a Bokeh app using the bokeh serve command line tool. In this chapter and the one that follows, the DataCamp environment does this for you behind the scenes. Notice that your code is part of a script.py file. When you hit 'Submit Answer', you'll see in the IPython Shell that we call bokeh serve script.py for you.

Remember, as in the previous chapters, that there are different options available for you to interact with your plots, and as before, you may have to scroll down to view the lower portion of the plots.

### Instructions:
* Import curdoc from bokeh.io and figure from bokeh.plotting.
* Create a new plot called plot using the figure() function.
* Add a line to the plot using [1,2,3,4,5] as the x coordinates and [2,5,4,6,7] as the y coordinates.
* Add the plot to the current document using curdoc().add_root(). It needs to be passed in as an argument to add_root().

#### Script:
```
# Perform necessary imports
from bokeh.io import curdoc
from bokeh.plotting import figure

# Create a new plot: plot
plot = figure(x_axis_label = 'x', y_axis_label = 'y')

# Add a line to the plot
plot.line([1,2,3,4,5], [2,5,4,6,7])

# Add the plot to the current document
curdoc().add_root(plot)
```
#### Output:
![Alt text](./curdoc.png)

#### Comment:
Great work! In the next exercise, you'll practice adding a single slider to a current document.

## 03. Add a single slider
In the previous exercise, you added a single plot to the "current document" of your application. In this exercise, you'll practice adding a layout to your current document.

Your job here is to create a single slider, use it to create a widgetbox layout, and then add this layout to the current document.

The slider you create here cannot be used for much, but in the later exercises, you'll use it to update your plots!

### Instructions:
* Import curdoc from bokeh.io, widgetbox from bokeh.layouts, and Slider from bokeh.models.
* Create a slider called slider by using the Slider() function and specifying the parameters title, start, end, step, and value.
* Use the slider to create a widgetbox layout called layout.
* Add the layout to the current document using curdoc().add_root(). It needs to be passed in as an argument to add_root().

#### Script:
```
# Perform the necessary imports
from bokeh.io import curdoc
from bokeh.layouts import widgetbox
from bokeh.models import Slider

# Create a slider: slider
slider = Slider(title='my slider', start=0, end=10, step=0.1, value=2)

# Create a widgetbox layout: layout
layout = widgetbox(slider)

# Add the layout to the current document
curdoc().add_root(layout)
```
#### Output:
![Alt text](./slider1.gif)

#### Comment:
Good job! You'll build on this in the next exercise by adding another slider to the current document!

## 04. Multiple sliders in one document
Having added a single slider in a widgetbox layout to your current document, you'll now add multiple sliders into the current document.

Your job in this exercise is to create two sliders, add them to a widgetbox layout, and then add the layout into the current document.

### Instructions:
* Create the first slider, slider1, using the Slider() function. Give it a title of 'slider1'. Have it start at 0, end at 10, with a step of 0.1 and initial value of 2.
* Create the second slider, slider2, using the Slider() function. Give it a title of 'slider2'. Have it start at 10, end at 100, with a step of 1 and initial value of 20.
* Use slider1 and slider2 to create a widgetbox layout called layout.
* Add the layout to the current document using curdoc().add_root(). This has already been done for you.

#### Script:
```
# Perform necessary imports
from bokeh.io import curdoc
from bokeh.layouts import widgetbox
from bokeh.models import Slider

# Create first slider: slider1
slider1 = Slider(title='slider1', start=0, end=10, step=0.1, value=2)

# Create second slider: slider2
slider2 = Slider(title='slider2', start=10, end=100, step=1, value=20)

# Add slider1 and slider2 to a widgetbox
layout = widgetbox(slider1, slider2)

# Add the layout to the current document
curdoc().add_root(layout)
```
#### Output:
![Alt text](./slider2.gif)

#### Comment:
Excellent! The next step now is to learn how to connect these sliders to plots.
