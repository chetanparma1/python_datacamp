# Chapter 01: Classification

## 01. Which of these is a classification problem?
Once you decide to leverage supervised machine learning to solve a new problem, you need to identify whether your problem is better suited to classification or regression. This exercise will help you develop your intuition for distinguishing between the two.

Provided below are 4 example applications of machine learning. Which of them is a supervised classification problem?

### Possible Answers
* Using labeled financial data to predict whether the value of a stock will go up or go down next week.
** press 1
* Using labeled housing price data to predict the price of a new house based on various features.
** press 2
* Using unlabeled data to cluster the students of an online education company into different categories based on their learning styles.
** press 3
* Using labeled financial data to predict what the value of a stock will be next week.
** press 4

#### Answer:
1

#### Comment:
Exactly! In this example, there are two discrete, qualitative outcomes: the stock market going up, and the stock market going down. This can be represented using a binary variable, and is an application perfectly suited for classification.

## 02. Numerical EDA
In this chapter, you'll be working with a dataset obtained from the <a href="https://archive.ics.uci.edu/ml/datasets/Congressional+Voting+Records">UCI Machine Learning Repository</a> consisting of votes made by US House of Representatives Congressmen. Your goal will be to predict their party affiliation ('Democrat' or 'Republican') based on how they voted on certain key issues. Here, it's worth noting that we have preprocessed this dataset to deal with missing values. This is so that your focus can be directed towards understanding how to train and evaluate supervised learning models. Once you have mastered these fundamentals, you will be introduced to preprocessing techniques in Chapter 4 and have the chance to apply them there yourself - including on this very same dataset!

Before thinking about what supervised learning models you can apply to this, however, you need to perform Exploratory data analysis (EDA) in order to understand the structure of the data. For a refresher on the importance of EDA, check out the first two chapters of <a href="https://www.datacamp.com/courses/statistical-thinking-in-python-part-1">Statistical Thinking in Python (Part 1)</a>.

Get started with your EDA now by exploring this voting records dataset numerically. It has been pre-loaded for you into a DataFrame called df. Use pandas' .head(), .info(), and .describe() methods in the IPython Shell to explore the DataFrame, and select the statement below that is not true.

### Possible Answers
* The DataFrame has a total of 435 rows and 17 columns.
* Except for 'party', all of the columns are of type int64.
* The first two rows of the DataFrame consist of votes made by Republicans and the next three rows consist of votes made by Democrats.
* There are 17 predictor variables, or features, in this DataFrame.
* The target variable in this DataFrame is 'party'.

#### Answer:
4

#### Comment:
Great work! The number of columns in the DataFrame is not equal to the number of features. One of the columns - 'party' is the target variable.

## 03. Visual EDA
The Numerical EDA you did in the previous exercise gave you some very important information, such as the names and data types of the columns, and the dimensions of the DataFrame. Following this with some visual EDA will give you an even better understanding of the data. In the video, Hugo used the scatter_matrix() function on the Iris data for this purpose. However, you may have noticed in the previous exercise that all the features in this dataset are binary; that is, they are either 0 or 1. So a different type of plot would be more useful here, such as Seaborn's countplot.

Given on the right is a countplot of the 'education' bill, generated from the following code:
```
plt.figure()
sns.countplot(x='education', hue='party', data=df, palette='RdBu')
plt.xticks([0,1], ['No', 'Yes'])
plt.show()
```
In sns.countplot(), we specify the x-axis data to be 'education', and hue to be 'party'. Recall that 'party' is also our target variable. So the resulting plot shows the difference in voting behavior between the two parties for the 'education' bill, with each party colored differently. We manually specified the color to be 'RdBu', as the Republican party has been traditionally associated with red, and the Democratic party with blue.

It seems like Democrats voted resoundingly against this bill, compared to Republicans. This is the kind of information that our machine learning model will seek to learn when we try to predict party affiliation solely based on voting behavior. An expert in U.S politics may be able to predict this without machine learning, but probably not instantaneously - and certainly not if we are dealing with hundreds of samples!

In the IPython Shell, explore the voting behavior further by generating countplots for the 'satellite' and 'missile' bills, and answer the following question: Of these two bills, __for which ones do Democrats vote resoundingly in favor of, compared to Republicans?__ Be sure to begin your plotting statements for each figure with plt.figure() so that a new figure will be set up. Otherwise, your plots will be overlayed onto the same figure.

### Possible Answers
* 'satellite'.
* 'missile'.
* Both 'satellite' and 'missile'.
* Neither 'satellite' nor 'missile'.

#### Answer:
3

#### Script & Output for Satellite & Missile
```
In [1]: plt.figure()
... sns.countplot(x='satellite', hue='party', data=df, palette='RdBu')
... plt.xticks([0,1], ['No', 'Yes'])
... plt.show()

In [2]: plt.figure()
... sns.countplot(x='missile', hue='party', data=df, palette='RdBu')
... plt.xticks([0,1], ['No', 'Yes'])
... plt.show()
```
__satellite__
![Alt text](./satellite.svg)
__missile__
![Alt text](./missile.svg)

#### Comment:
Correct! Democrats voted in favor of both 'satellite' and 'missile'
