# A Machine Learning Project on NLP
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://beatrix-droid-broadband-reviews-nlp-frontend-deployment-mmuqk0.streamlit.app/)
 

This will become a machine learning project on natural language processing (NLP). The Idea is that given a set of reviews, both positive and negative from customers, build a model that can predict the average scores of the review.

The dataset (contained in raw_data.csv)using the scrape.py script  was scraped off of the internet and is a collection of the most recent reviews for an unnamed company.
These reviews were scraped using the scrape.py script. 

the structure of the files in the project is the following:

* /data contains all the data in forms of csv files in all its different stages of processing

* scrape.py scrapes the data off of the internet, and puts it into a csv called "raw_data.csv" 

* preprocessing_part 1.ipynb is the jupiter notebook that does the initial preprocessing of the data contained in raw_data.csv. String numbers are converted to floats, dates are converted to datetime objects and missing values are handled. It spits out a file called preprocessed_data.csv

* preprocessing_part2.ipynb takes the data from the preprocessed_data.csv, adds a new column called "Average Score" that displays the average score per each review and eliminates the "date column" as that is unneeded for this machine learning project. It creates a file suitable for the model to take as an  imput called "data_ready_for_model.csv".

* model_creation.ipynb is where the neural network is actually built. Processed data from preprocessing_part2.ipynb is taken and used to build and train a text classifier model that will read the comments in the datatable and try to predict its average score.

* Saved_model is the folder that contains the model

* frontend.py serves the streamlit web app with which the user can interact with the model
./streamlit/config.toml contains the styling configurations of the application of the frontend streamlit app.


The deployment branch contains only the scripts required to run the web application live on streamlit which viewers can check out [here]("https://beatrix-droid-broadband-reviews-nlp-frontend-deployment-mmuqk0.streamlit.app/").
This means that only the saved model, frontend.py and helper.py along with the requirements.txt and the README.md are present in that branch.
