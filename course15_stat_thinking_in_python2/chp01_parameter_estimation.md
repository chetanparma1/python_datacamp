# Chapter 01: Parameter Estimation by Optimization

## 01. How often do we get no-hitters?
The number of games played between each no-hitter in the modern era (1901-2015) of Major League Baseball is stored in the array nohitter_times.

If you assume that no-hitters are described as a Poisson process, then the time between no-hitters is Exponentially distributed. As you have seen, the Exponential distribution has a single parameter, which we will call τ, the typical interval time. The value of the parameter τ that makes the exponential distribution best match the data is the mean interval time (where time is in units of number of games) between no-hitters.

Compute the value of this parameter from the data. Then, use np.random.exponential() to "repeat" the history of Major League Baseball by drawing inter-no-hitter times from an exponential distribution with the τ you found and plot the histogram as an approximation to the PDF.

NumPy, pandas, matlotlib.pyplot, and seaborn have been imported for you as np, pd, plt, and sns, respectively.

### Instructions:
* Seed the random number generator with 42.
* Compute the mean time (in units of number of games) between no-hitters.
* Draw 100,000 samples from an Exponential distribution with the parameter you computed from the mean of the inter-no-hitter times.
* Plot the theoretical PDF using plt.hist(). Remember to use keyword arguments bins=50, normed=True, and histtype='step'. Be sure to label your axes.
* Show your plot.

#### Script:
```
# Seed random number generator
np.random.seed(42)

# Compute mean no-hitter time: tau
tau = np.mean(nohitter_times)

# Draw out of an exponential distribution with parameter tau: inter_nohitter_time
inter_nohitter_time = np.random.exponential(tau, 100000)

# Plot the PDF and label axes
_ = plt.hist(inter_nohitter_time,
             bins=50, normed=True, histtype='step')
_ = plt.xlabel('Games between no-hitters')
_ = plt.ylabel('PDF')

# Show the plot
plt.show()

```

#### Output:
```
In [1]: nohitter_times
Out[1]: 
array([ 843, 1613, 1101,  215,  684,  814,  278,  324,  161,  219,  545,
        715,  966,  624,   29,  450,  107,   20,   91, 1325,  124, 1468,
        104, 1309,  429,   62, 1878, 1104,  123,  251,   93,  188,  983,
        166,   96,  702,   23,  524,   26,  299,   59,   39,   12,    2,
        308, 1114,  813,  887,  645, 2088,   42, 2090,   11,  886, 1665,
       1084, 2900, 2432,  750, 4021, 1070, 1765, 1322,   26,  548, 1525,
         77, 2181, 2752,  127, 2147,  211,   41, 1575,  151,  479,  697,
        557, 2267,  542,  392,   73,  603,  233,  255,  528,  397, 1529,
       1023, 1194,  462,  583,   37,  943,  996,  480, 1497,  717,  224,
        219, 1531,  498,   44,  288,  267,  600,   52,  269, 1086,  386,
        176, 2199,  216,   54,  675, 1243,  463,  650,  171,  327,  110,
        774,  509,    8,  197,  136,   12, 1124,   64,  380,  811,  232,
        192,  731,  715,  226,  605,  539, 1491,  323,  240,  179,  702,
        156,   82, 1397,  354,  778,  603, 1001,  385,  986,  203,  149,
        576,  445,  180, 1403,  252,  675, 1351, 2983, 1568,   45,  899,
       3260, 1025,   31,  100, 2055, 4043,   79,  238, 3931, 2351,  595,
        110,  215,    0,  563,  206,  660,  242,  577,  179,  157,  192,
        192, 1848,  792, 1693,   55,  388,  225, 1134, 1172, 1555,   31,
       1582, 1044,  378, 1687, 2915,  280,  765, 2819,  511, 1521,  745,
       2491,  580, 2072, 6450,  578,  745, 1075, 1103, 1549, 1520,  138,
       1202,  296,  277,  351,  391,  950,  459,   62, 1056, 1128,  139,
        420,   87,   71,  814,  603, 1349,  162, 1027,  783,  326,  101,
        876,  381,  905,  156,  419,  239,  119,  129,  467])
```

![Alt text](./nohitter_hist.svg)

#### Comment:
Nice work! We see the typical shape of the Exponential distribution, going from a maximum at 0 and decaying to the right.

## 02. Do the data follow our story?
You have modeled no-hitters using an Exponential distribution. Create an ECDF of the real data. Overlay the theoretical CDF with the ECDF from the data. This helps you to verify that the Exponential distribution describes the observed data.

It may be helpful to remind yourself of the <a href="https://campus.datacamp.com/courses/statistical-thinking-in-python-part-1/graphical-exploratory-data-analysis?ex=12">function you created in the previous course</a> to compute the ECDF, as well as the code you wrote to <a href="https://campus.datacamp.com/courses/statistical-thinking-in-python-part-1/graphical-exploratory-data-analysis?ex=13">plot it</a>.

### Instructions:
* Compute an ECDF from the actual time between no-hitters (nohitter_times). Use the ecdf() function you wrote in the prequel course.
* Create a CDF from the theoretical samples you took in the last exercise (inter_nohitter_time).
* Plot x_theor and y_theor as a line using plt.plot(). Then overlay the ECDF of the real data x and y as points. To do this, you have to specify the keyword arguments marker = '.' and linestyle = 'none' in addition to x and y inside plt.plot().
* Set a 2% margin on the plot.
* Show the plot.

#### Script:
```
# Create an ECDF from real data: x, y
x, y = ecdf(nohitter_times)

# Create a CDF from theoretical samples: x_theor, y_theor
x_theor, y_theor = ecdf(inter_nohitter_time)

# Overlay the plots
plt.plot(x_theor, y_theor)
plt.plot(x, y, marker='.', linestyle='none')

# Margins and axis labels
plt.margins(0.02)
plt.xlabel('Games between no-hitters')
plt.ylabel('CDF')

# Show the plot
plt.show()

```
#### Output:
![Alt text](./nohitter_ecdf.svg)

#### Comment:
It looks like no-hitters in the modern era of Major League Baseball are Exponentially distributed. Based on the story of the Exponential distribution, this suggests that they are a random process; when a no-hitter will happen is independent of when the last no-hitter was.

## 03. How is this parameter optimal?
Now sample out of an exponential distribution with τ being twice as large as the optimal τ. Do it again for τ half as large. Make CDFs of these samples and overlay them with your data. You can see that they do not reproduce the data as well. Thus, the τ you computed from the mean inter-no-hitter times is optimal in that it best reproduces the data.

Note: In this and all subsequent exercises, the random number generator is pre-seeded for you to save you some typing.

### Instructions:
* Take 10000 samples out of an Exponential distribution with parameter τ1/2 = tau/2.
* Take 10000 samples out of an Exponential distribution with parameter τ2 = 2*tau.
* Generate CDFs from these two sets of samples using your ecdf() function.
* Add these two CDFs as lines to your plot. This has been done for you, so hit 'Submit Answer' to view the plot!

#### Script:
```
# Plot the theoretical CDFs
plt.plot(x_theor, y_theor)
plt.plot(x, y, marker='.', linestyle='none')
plt.margins(0.02)
plt.xlabel('Games between no-hitters')
plt.ylabel('CDF')

# Take samples with half tau: samples_half
samples_half = np.random.exponential(tau/2, 10000)

# Take samples with double tau: samples_double
samples_double = np.random.exponential(2*tau, 10000)

# Generate CDFs from these samples
x_half, y_half = ecdf(samples_half)
x_double, y_double = ecdf(samples_double)

# Plot these CDFs as lines
_ = plt.plot(x_half, y_half)
_ = plt.plot(x_double, y_double)

# Show the plot
plt.show()
```

#### Output:
```
In [1]: tau
Out[1]: 763.0358565737051
```
![Alt text](./half_double.svg)

#### Comment:
Great work! Notice how the value of tau given by the mean matches the data best. In this way, tau is an optimal parameter.

## 04. EDA of literacy/fertility data
In the next few exercises, we will look at the correlation between female literacy and fertility (defined as the average number of children born per woman) throughout the world. For ease of analysis and interpretation, we will work with the illiteracy rate.

It is always a good idea to do some EDA ahead of our analysis. To this end, plot the fertility versus illiteracy and compute the Pearson correlation coefficient. The Numpy array illiteracy has the illiteracy rate among females for most of the world's nations. The array fertility has the corresponding fertility data.

Here, it may be useful to refer back to the <a href=https://campus.datacamp.com/courses/statistical-thinking-in-python-part-1/quantitative-exploratory-data-analysis?ex=15">function you wrote in the previous course</a> to compute the Pearson correlation coefficient.
  
### Instructions:
* Plot fertility (y-axis) versus illiteracy (x-axis) as a scatter plot.
* Set a 2% margin.
* Compute and print the Pearson correlation coefficient between illiteracy and fertility.

#### Script:
```
# Plot the illiteracy rate versus fertility
_ = plt.plot(illiteracy, fertility, marker='.', linestyle='none')

# Set the margins and label axes
plt.margins(0.02)
_ = plt.xlabel('percent illiterate')
_ = plt.ylabel('fertility')

# Show the plot
plt.show()

# Show the Pearson correlation coefficient
print(pearson_r(illiteracy, fertility))

```
#### Output:
```
<script.py> output:
    0.8041324026815344
```
![Alt text](./illifer.svg)

#### Comment:
You can see the correlation between illiteracy and fertility by eye, and by the substantial Pearson correlation coefficient of 0.8. It is difficult to resolve in the scatter plot, but there are many points around near-zero illiteracy and about 1.8 children/woman.

## 05. Linear regression
We will assume that fertility is a linear function of the female illiteracy rate. That is, f=ai+b, where a is the slope and b is the intercept. We can think of the intercept as the minimal fertility rate, probably somewhere between one and two. The slope tells us how the fertility rate varies with illiteracy. We can find the best fit line using np.polyfit().

Plot the data and the best fit line. Print out the slope and intercept. (Think: what are their units?)

### Instructions:
* Compute the slope and intercept of the regression line using np.polyfit(). Remember, fertility is on the y-axis and illiteracy on the x-axis.
* Print out the slope and intercept from the linear regression.
* To plot the best fit line, create an array x that consists of 0 and 100 using np.array(). Then, compute the theoretical values of y based on your regression parameters. I.e., y = a * x + b.
* Plot the data and the regression line on the same plot. Be sure to label your axes.
* Hit 'Submit Answer' to display your plot.

#### Script:
```
# Plot the illiteracy rate versus fertility
_ = plt.plot(illiteracy, fertility, marker='.', linestyle='none')
plt.margins(0.02)
_ = plt.xlabel('percent illiterate')
_ = plt.ylabel('fertility')

# Perform a linear regression using np.polyfit(): a, b
a, b = np.polyfit(illiteracy, fertility, 1)

# Print the results to the screen
print('slope =', a, 'children per woman / percent illiterate')
print('intercept =', b, 'children per woman')

# Make theoretical line to plot
x = np.array([0, 100])
y = a * x + b

# Add regression line to your plot
_ = plt.plot(x, y)

# Draw the plot
plt.show()

```
#### Output:
```
<script.py> output:
    slope = 0.04979854809063423 children per woman / percent illiterate
    intercept = 1.888050610636557 children per woman
```
![Alt text](./polyfit.svg)

#### Comment:
Great work!

## 06 How is it optimal?
The function np.polyfit() that you used to get your regression parameters finds the optimal slope and intercept. It is optimizing the sum of the squares of the residuals, also known as RSS (for residual sum of squares). In this exercise, you will plot the function that is being optimized, the RSS, versus the slope parameter a. To do this, fix the intercept to be what you found in the optimization. Then, plot the RSS vs. the slope. Where is it minimal?

### Instructions:
* Specify the values of the slope to compute the RSS. Use np.linspace() to get 200 points in the range between 0 and 0.1. For example, to get 100 points in the range between 0 and 0.5, you could use np.linspace() like so: np.linspace(0, 0.5, 100).
* Initialize an array, rss, to contain the RSS using np.empty_like() and the array you created above. The empty_like() function returns a new array with the same shape and type as a given array (in this case, a_vals).
* Write a for loop to compute the sum of RSS of the slope. Hint: the RSS is given by np.sum((y_data - a * x_data - b)**2). The variable b you computed in the last exercise is already in your namespace. Here, fertility is the y_data and illiteracy the x_data.
* Plot the RSS (rss) versus slope (a_vals).
* Hit 'Submit Answer' to see the plot!

#### Script:
```
# Specify slopes to consider: a_vals
a_vals = np.linspace(0, 0.1, 200)

# Initialize sum of square of residuals: rss
rss = np.empty_like(a_vals)

# Compute sum of square of residuals for each value of a_vals
for i, a in enumerate(a_vals):
    rss[i] = np.sum((fertility - a*illiteracy - b)**2)

# Plot the RSS
plt.plot(a_vals, rss, '-')
plt.xlabel('slope (children per woman / percent illiterate)')
plt.ylabel('sum of square of residuals')

plt.show()

```

#### Output:
```
In [2]: a_vals
Out[2]: 
array([0.        , 0.00050251, 0.00100503, 0.00150754, 0.00201005,
       0.00251256, 0.00301508, 0.00351759, 0.0040201 , 0.00452261,
       0.00502513, 0.00552764, 0.00603015, 0.00653266, 0.00703518,
       0.00753769, 0.0080402 , 0.00854271, 0.00904523, 0.00954774,
       0.01005025, 0.01055276, 0.01105528, 0.01155779, 0.0120603 ,
       0.01256281, 0.01306533, 0.01356784, 0.01407035, 0.01457286,
       0.01507538, 0.01557789, 0.0160804 , 0.01658291, 0.01708543,
       0.01758794, 0.01809045, 0.01859296, 0.01909548, 0.01959799,
       0.0201005 , 0.02060302, 0.02110553, 0.02160804, 0.02211055,
       0.02261307, 0.02311558, 0.02361809, 0.0241206 , 0.02462312,
       0.02512563, 0.02562814, 0.02613065, 0.02663317, 0.02713568,
       0.02763819, 0.0281407 , 0.02864322, 0.02914573, 0.02964824,
       0.03015075, 0.03065327, 0.03115578, 0.03165829, 0.0321608 ,
       0.03266332, 0.03316583, 0.03366834, 0.03417085, 0.03467337,
       0.03517588, 0.03567839, 0.0361809 , 0.03668342, 0.03718593,
       0.03768844, 0.03819095, 0.03869347, 0.03919598, 0.03969849,
       0.04020101, 0.04070352, 0.04120603, 0.04170854, 0.04221106,
       0.04271357, 0.04321608, 0.04371859, 0.04422111, 0.04472362,
       0.04522613, 0.04572864, 0.04623116, 0.04673367, 0.04723618,
       0.04773869, 0.04824121, 0.04874372, 0.04924623, 0.04974874,
       0.05025126, 0.05075377, 0.05125628, 0.05175879, 0.05226131,
       0.05276382, 0.05326633, 0.05376884, 0.05427136, 0.05477387,
       0.05527638, 0.05577889, 0.05628141, 0.05678392, 0.05728643,
       0.05778894, 0.05829146, 0.05879397, 0.05929648, 0.05979899,
       0.06030151, 0.06080402, 0.06130653, 0.06180905, 0.06231156,
       0.06281407, 0.06331658, 0.0638191 , 0.06432161, 0.06482412,
       0.06532663, 0.06582915, 0.06633166, 0.06683417, 0.06733668,
       0.0678392 , 0.06834171, 0.06884422, 0.06934673, 0.06984925,
       0.07035176, 0.07085427, 0.07135678, 0.0718593 , 0.07236181,
       0.07286432, 0.07336683, 0.07386935, 0.07437186, 0.07487437,
       0.07537688, 0.0758794 , 0.07638191, 0.07688442, 0.07738693,
       0.07788945, 0.07839196, 0.07889447, 0.07939698, 0.0798995 ,
       0.08040201, 0.08090452, 0.08140704, 0.08190955, 0.08241206,
       0.08291457, 0.08341709, 0.0839196 , 0.08442211, 0.08492462,
       0.08542714, 0.08592965, 0.08643216, 0.08693467, 0.08743719,
       0.0879397 , 0.08844221, 0.08894472, 0.08944724, 0.08994975,
       0.09045226, 0.09095477, 0.09145729, 0.0919598 , 0.09246231,
       0.09296482, 0.09346734, 0.09396985, 0.09447236, 0.09497487,
       0.09547739, 0.0959799 , 0.09648241, 0.09698492, 0.09748744,
       0.09798995, 0.09849246, 0.09899497, 0.09949749, 0.1       ])
```
```
In [3]: rss
Out[3]: 
array([6.95184592e-310, 2.74076395e-316, 2.74076395e-316, 2.74076395e-316,
       4.94065646e-324, 2.74322677e-316, 4.94065646e-324, 2.74321531e-316,
       1.38338381e-322, 6.95182908e-310, 6.95165821e-310, 6.95165821e-310,
       2.47032823e-323, 1.38338381e-322, 6.95184427e-310, 6.95165821e-310,
       4.94065646e-324, 1.27319747e-313, 1.90979621e-313, 2.74321729e-316,
       6.95184414e-310, 6.95165821e-310, 1.27319747e-313, 4.94065646e-324,
       2.74322203e-316, 1.38338381e-322, 6.95182908e-310, 4.94065646e-324,
       5.39043801e-317, 4.24399158e-313, 0.00000000e+000, 0.00000000e+000,
       7.90505033e-323, 2.74321926e-316, 2.74322124e-316, 2.74322401e-316,
       1.27319747e-313, 2.96439388e-323, 2.74321452e-316, 2.74322480e-316,
       8.39911598e-323, 6.15378779e-313, 0.00000000e+000, 2.47032823e-323,
       6.15378779e-313, 2.74321373e-316, 2.74322124e-316, 2.74322875e-316,
       1.90979621e-313, 1.90979621e-313, 2.74321452e-316, 2.74322954e-316,
       2.74322993e-316, 0.00000000e+000, 0.00000000e+000, 9.88131292e-324,
       4.94065646e-324, 2.74321373e-316, 2.74323547e-316, 1.38338381e-322,
       6.95182908e-310, 9.88131292e-324, 0.00000000e+000, 2.47032823e-323,
       1.38338381e-322, 6.95184427e-310, 4.94065646e-324, 0.00000000e+000,
       1.27319747e-313, 1.23516411e-322, 2.74323744e-316, 6.95184414e-310,
       4.94065646e-324, 1.27319747e-313, 4.94065646e-324, 2.74324298e-316,
       0.00000000e+000, 0.00000000e+000, 1.38338381e-322, 6.95182908e-310,
       4.94065646e-324, 2.84581812e-321, 4.24399158e-313,             nan,
       2.74323942e-316, 2.74324140e-316, 2.74324219e-316, 1.27319747e-313,
       2.96439388e-323, 2.74323468e-316, 2.74324495e-316, 0.00000000e+000,
       0.00000000e+000, 0.00000000e+000, 2.47032823e-323, 4.94065646e-324,
       2.74321373e-316, 0.00000000e+000, 0.00000000e+000, 0.00000000e+000,
       0.00000000e+000, 0.00000000e+000, 0.00000000e+000, 0.00000000e+000,
       0.00000000e+000, 0.00000000e+000, 0.00000000e+000, 0.00000000e+000,
       0.00000000e+000, 0.00000000e+000, 0.00000000e+000, 0.00000000e+000,
       0.00000000e+000, 0.00000000e+000, 0.00000000e+000, 0.00000000e+000,
       6.95178976e-310, 3.04344438e-321, 5.43472210e-323, 6.95178976e-310,
       2.34801754e-316,             nan, 1.48219694e-322,             nan,
       6.95184414e-310, 6.95165821e-310, 4.62445445e-321, 4.44659081e-323,
       6.95178976e-310, 2.34802248e-316, 4.94065646e-324, 6.95184425e-310,
       6.95184416e-310, 6.95178975e-310, 6.95165821e-310, 4.98018171e-321,
       1.48219694e-323, 6.95178976e-310, 2.34802267e-316, 6.95184419e-310,
       6.95184440e-310, 4.47593816e-091, 9.00083904e+223, 1.27803567e-152,
       1.06758000e+224, 2.59345433e+161, 3.94646008e+180, 3.58511268e+246,
       6.01099947e+175, 2.64519874e+185, 1.23797299e-259, 6.97283586e+228,
       1.03474381e-028, 1.81667905e-152, 4.83245960e+276, 6.97283586e+228,
       3.58511268e+246, 6.01099947e+175, 2.64519874e+185, 1.23797299e-259,
       1.91610942e+214, 1.94860694e-153, 7.21910206e+159, 1.96086585e+243,
       1.45913393e-152, 2.64519874e+185, 8.73983158e+183, 1.10638849e+200,
       5.55603592e+180, 9.32166862e+218, 1.17521328e+180, 2.96036207e+222,
       7.27461249e+199, 4.24976375e+175, 1.23875453e-259, 7.17236781e+252,
       2.47379808e-091, 6.01334512e-154, 3.32234062e+257, 2.03199083e+174,
       7.20104168e+252, 1.78935395e+161, 3.17095857e+180, 3.94814797e+180,
       3.35910140e-022, 2.35341934e+251, 1.39515159e-258, 1.14572647e+243,
       2.29751664e+156, 3.94658617e+180, 9.78305794e-153, 3.27842382e-085,
       4.82670362e+276, 2.04736976e+190, 8.75013230e+183, 1.46923330e+195,
       2.30908182e+251, 4.45197005e+252, 1.71898014e+161, 4.91437031e+252])
```
```
In [4]: b
Out[4]: 1.888050610636557
```
![Alt text](./avals_rss.svg)

#### Comment:
Great work! Notice that the minimum on the plot, that is the value of the slope that gives the minimum sum of the square of the residuals, is the same value you got when performing the regression.

## 07. The importance of EDA
Why should exploratory data analysis be the first step in an analysis of data (after getting your data imported and cleaned, of course)?

### Possible Answers
* You can be protected from misinterpretation of the type demonstrated by Anscombe's quartet.
** press 1
* EDA provides a good starting point for planning the rest of your analysis.
** press 2
* EDA is not really any more difficult than any of the subsequent analysis, so there is no excuse for not exploring the data.
** press 3
* All of these reasons!
** press 4

#### Answer:
4

#### Comment:
Yes! Always do EDA as you jump into a data set.
