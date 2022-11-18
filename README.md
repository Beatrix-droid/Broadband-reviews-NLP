#A Machine Learning Project on NLP
This will become a machine learning project on natural language processing (NLP). The Idea is that given a set of reviews, both positive and negative from customers, build a model that can predict the average scores of the review.

The dataset (contained in raw_data.csv) was scraped off of the internet and is a collection of the most recent Virgin media reviews.
These reviews were scraped off of https://www.broadband.co.uk/broadband/providers/virgin-media/reviews using the scrape.py script. 


preprocessing_part 1.ipynb is the jupiter notebook that retrieves all of this data from teh scrape.py script, stores it into a csv (raw_data.csv) and does the initial preprocessing of the data. String numbers are converted to floats, dates are converted to datetime objects and missing values are handled. It spits out a preprocessed_data.csv

preprocessing_part2.ipynb takes the data from the preprocessed_data.csv, adds a new column called "Average Score" that displays the average score per each review and eliminates the "date column" as that is unneeded for this machine learning project.
