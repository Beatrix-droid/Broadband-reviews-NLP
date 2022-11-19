#A Machine Learning Project on NLP
This will become a machine learning project on natural language processing (NLP). The Idea is that given a set of reviews, both positive and negative from customers, build a model that can predict the average scores of the review.

The dataset (contained in raw_data.csv)using the scrape.py script  was scraped off of the internet and is a collection of the most recent reviews for an unnamed company.
These reviews were scraped using the scrape.py script. 

*srape.py scrapes the data off of the internet

*scraped_to_csv.py collects the raw data scraped by scrape.py and puts it into a csv 9raw_data.csv) 

preprocessing_part 1.ipynb is the jupiter notebook that does the initial preprocessing of the data contained in raw_data.csv. String numbers are converted to floats, dates are converted to datetime objects and missing values are handled. It spits out a fiel called preprocessed_data.csv

preprocessing_part2.ipynb takes the data from the preprocessed_data.csv, adds a new column called "Average Score" that displays the average score per each review and eliminates the "date column" as that is unneeded for this machine learning project.

model_creation.ipynb is where the neural network is actually built. Processed data from preprocessing_part2.ipynb is taken and used to build and train a text classifier model that will read the comments in the datatable and try to predict its average score.