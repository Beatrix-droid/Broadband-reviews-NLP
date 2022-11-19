import pandas as pd
from scrape import customer_service_reviews, comments, dates, satisfaction_reviews, speed_reviews, reliability_reviews, customer_service_reviews
df_dict={"Dates": dates, "Comments": comments, "Customer Service": customer_service_reviews, "Satisfaction Reviews": satisfaction_reviews, "Speed Reviews": speed_reviews, "Reliability Reviews": reliability_reviews}

#as certain columns are shorter than others use a trick to create a df with unequal arrays:https://stackoverflow.com/questions/19736080/creating-dataframe-from-a-dictionary-where-entries-have-different-lengths
df = pd.DataFrame.from_dict(df_dict, orient='index')
df=df.transpose()

#convert the dates columns from string to datetime object:
df["Dates"]= pd.to_datetime(df["Dates"])

#save date to csv:
df.to_csv('./data/raw_data.csv')
