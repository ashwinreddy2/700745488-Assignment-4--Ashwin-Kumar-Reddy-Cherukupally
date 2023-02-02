# 700745488-Assignment-4--Ashwin-Kumar-Reddy-Cherukupally

Here is the video recording which describes the information.
https://drive.google.com/file/d/1uiVsDFTzDwgMIRV--NDH9kXalJnmaxs-/view?usp=sharing

1. Data Manipulation
   a. Read the provided CSV file ‘data.csv’.
   b. https://drive.google.com/drive/folders/1h8C3mLsso-R-sIOLsvoYwPLzy2fJ4IOF?usp=sharing
   c. Show the basic statistical description about the data.
   d. Check if the data has null values.
   i. Replace the null values with the mean
   e. Select at least two columns and aggregate the data using: min, max, count, mean.
   f. Filter the dataframe to select the rows with calories values between 500 and 1000.
   g. Filter the dataframe to select the rows with calories values > 500 and pulse < 100.
   h. Create a new “df_modified” dataframe that contains all the columns from df except for
      “Maxpulse”.
   i. Delete the “Maxpulse” column from the main df dataframe
   j. Convert the datatype of Calories column to int datatype.
   k. Using pandas create a scatter plot for the two columns (Duration and Calories).
   
   
   A) Here In this program we need to import pandas as pd and matpotlib functions as plt because pandas are used for data cleaning and analysis whereas matpotlib is uased for data visulaization and graphical plotting and then reading data.csv file and storing in the data variable which contains attributes like maxpulse, calories,duration and pulse and we are using .head function used to return first n rows and also using .describe function beacause it returns the data in the dataframe in the form of mean, average, standard deviation and using fillna method we are replacing null values with mean and then printing the data. Now we are selecting attributes maxpulse and calories from the data.csv file for aggregation and then finding the minimum,maximum,count and mean for 2 attributes and filtering the dataframe to select the values of calories and maxpulse between a specific range and then using .drop function for droping maxpulse attribute and then converting the datatype of calories into integer data type using astype function and finally plotting a graph using 2 attributes namely Duration and Calories.
   
   
2. Linear Regression
a) Import the given “Salary_Data.csv”
b) Split the data in train_test partitions, such that 1/3 of the data is reserved as test subset.
c) Train and predict the model.
d) Calculate the mean_squared error
e) Visualize both train and test data using scatter plot


In this program we are using pandas module for data cleaning and data analysis and reading salary.data csv file and storing it into salariesdata variable and we are using .iloc function mainly for selecting a specific row and column from a given data set and we are splitting the data into training data and testing data by using train_test_split function and we are using an algorithm known as linear Regression for prediction of the data and calculating the mean_squared error from A_test and B_test data and we are importing matpotlib library to plot a graph for both training data and testing data and highlighting them with green and orange colors respectively and labelling the graph with the tittle as Salary data and assigning the X and Y axis names as Experience(Years) and Salary and using .show function to display the graph.
