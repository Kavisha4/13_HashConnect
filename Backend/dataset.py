# -*- coding: utf-8 -*-
"""Dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1woj4k5uLtckcft2YzB6DGTBSjZuCX_mV
"""

# !pip install faker
# from faker import Faker
# import random

# fake = Faker()

# # Define lists of possible values for the other columns
# company_names = [
#     "Indeed", 
#     "Dribble", 
#     "Behance", 
#     "Creative hotist", 
#     "Art jobs", 
#     "Talent zoo", 
#     "Vymo", 
#     "BigBasket", 
#     "Lenskart", 
#     "Jumbotail"
# ]

# job_names = ['Film and television', 'Visual arts', 'Fashion and beauty', 'Architect', 'Interior designer']
# #experience_levels = ['Entry Level', 'Mid Level', 'Senior Level']
# locations = ['Mumbai', 'Banaglore', 'Remote', 'Hyderabad', 'Chennai']

# # Define a dictionary that maps job names to relevant hashtags
# # job_hashtags_old = {
# #     'Film and television': ['#filmmaking', '#television', '#cinema', '#filmproduction', '#acting', '#screenwriting'],
# #     'Visual arts': ['#design', '#graphicdesign', '#drawing', '#sculpture', '#photography', '#printmaking', '#visualarts'],
# #     'Fashion and beauty': ['#fashion', '#beauty', '#style', '#modeling', '#makeup', '#designer', '#fashionista'],
# #     'Architect': ['#architecture', '#design', '#construction', '#building', '#architecturaldesign', '#urbanplanning'],
# #     'Interior designer': ['#interiordesign', '#homedecor', '#designer', '#decorating', '#homeimprovement', '#furniture']
# # }

# job_hashtags = {
#     'Film and television': ['#filmmaking', '#television', '#cinema', '#filmproduction', '#acting', '#screenwriting','designer','planning','#photography','#style','#makeup'],
#     'Visual arts': ['#design', '#graphicdesign', '#drawing', '#sculpture', '#photography', '#printmaking', '#visualarts','#style'],
#     'Fashion and beauty': ['#fashion', '#beauty', '#style', '#modeling', '#makeup', '#designer', '#fashionista','#design'],
#     'Architect': ['#architecture', '#design', '#construction', '#building', '#architecturaldesign', '#urbanplanning','planning','#style','#homeimprovement','#drawing'],
#     'Interior designer': ['#interiordesign', '#homedecor', '#designer', '#decorating', '#homeimprovement', '#furniture','#style','#design','#drawing']
# }


# # Generate random data
# num_rows = 100  # number of rows to generate
# data = []
# for i in range(num_rows):
#     company = random.choice(company_names)
#     job_name = random.choice(job_names)
#     hashtags = random.sample(job_hashtags[job_name], 3)  # select 3 random hashtags from the list of hashtags for this job name
#     experience_level = fake.random_int(min=1, max=10)
#     location = random.choice(locations)
#     row = (company, job_name, hashtags, experience_level, location)
#     data.append(row)

# # Print the generated data
# for row in data:
#     print(row)





# # Save the data to a CSV file
# import csv

# with open('jobs.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Company', 'Job Name', 'hashtags', 'Experience Level', 'Location'])
#     for row in data:
#         writer.writerow(row)





"""User dataset generation

"""

# import random
# import string
# from faker import Faker

# fake = Faker()

# # List of possible experience levels
# #experience_levels = ['Beginner', 'Intermediate', 'Advanced']

# # List of possible locations
# locations = ['Mumbai', 'Banaglore', 'Remote', 'Hyderabad', 'Chennai']

# # Dictionary of possible professions and their associated hashtags
# # professions = {
# #     'Film and television': ['#filmmaking', '#television', '#cinema', '#filmproduction', '#acting', '#screenwriting'],
# #     'Visual arts': ['#design', '#graphicdesign', '#drawing', '#sculpture', '#photography', '#printmaking', '#visualarts'],
# #     'Fashion and beauty': ['#fashion', '#beauty', '#style', '#modeling', '#makeup', '#designer', '#fashionista'],
# #     'Architect': ['#architecture', '#design', '#construction', '#building', '#architecturaldesign', '#urbanplanning'],
# #     'Interior designer': ['#interiordesign', '#homedecor', '#designer', '#decorating', '#homeimprovement', '#furniture']
# # }

# professions = {
#     'Film and television': ['#filmmaking', '#television', '#cinema', '#filmproduction', '#acting', '#screenwriting','designer','planning','#photography','#style','#makeup','#architecture'],
#     'Visual arts': ['#design', '#graphicdesign', '#drawing', '#sculpture', '#photography', '#printmaking', '#visualarts','#style'],
#     'Fashion and beauty': ['#fashion', '#beauty', '#style', '#modeling', '#makeup', '#designer', '#fashionista','#design'],
#     'Architect': ['#architecture', '#design', '#construction', '#building', '#architecturaldesign', '#urbanplanning','planning','#style','#homeimprovement','#drawing'],
#     'Interior designer': ['#interiordesign', '#homedecor', '#designer', '#decorating', '#homeimprovement', '#furniture','#style','#design','#drawing']
# }

# # Generate a random username
# def generate_username():
#     return ''.join(random.choice(string.ascii_lowercase) for i in range(6))

# # Generate a random profession and associated hashtags
# def generate_profession():
#     profession = random.choice(list(professions.keys()))
#     hashtags = professions[profession]
#     return profession, hashtags

# # Generate a random list of relevant hashtags from a given profession
# def generate_hashtags(profession_hashtags):
#     hashtags = []
#     for i in range(random.randint(1, 5)):
#         hashtag = random.choice(profession_hashtags) 
#         hashtags.append(hashtag)
#     return ' '.join(hashtags)

# # Generate a random experience level
# # def generate_experience_level():
# #     return random.choice(experience_levels)

# # Generate a random location
# def generate_location():
#     return random.choice(locations)

# data = []
# # Generate 100 rows of random data
# for i in range(100):
#     profession, profession_hashtags = generate_profession()
#     username = generate_username()
#     hashtags = generate_hashtags(profession_hashtags)
#     #experience_level = generate_experience_level()
#     experience_level = fake.random_int(min=1, max=10)
#     location = generate_location()
#     row = (username, hashtags, profession, experience_level, location)
#     data.append(row)

# # Save the data to a CSV file
# import csv

# with open('users.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['username', 'hashtags', 'profession', 'experience_level', 'location'])
#     for row in data:
#         writer.writerow(row)

"""Matrix bana"""

# import pandas as pd

# # Load the user and company CSV files into Pandas DataFrames
# users_df = pd.read_csv('/content/users.csv')
# companies_df = pd.read_csv('/content/jobs.csv')

# # Merge the users and companies DataFrames on the 'hashtags' column
# merged_df = pd.merge(users_df, companies_df, on='hashtags', how='outer')

# # Create a pivot table of the merged DataFrame, with users as rows and companies as columns,
# # and the values as the number of hashtags in common between each user and company
# pivot_table = pd.pivot_table(merged_df, values='hashtags', index='username', columns='Company', aggfunc=len)

# # Fill any NaN values in the pivot table with 0
# pivot_table = pivot_table.fillna(0)

# # Print the pivot table
# print(pivot_table)

# import pandas as pd

# # Load data from CSV files
# jobs_df = pd.read_csv('/content/jobs.csv')
# users_df = pd.read_csv('/content/users.csv')

# # Create a new empty DataFrame to store recommendations
# recommendations_df = pd.DataFrame(columns=['User', 'Company'])

# # Loop over each row in the users DataFrame
# for _, user_row in users_df.iterrows():
#     user_hashtags = user_row['hashtags'].split()  # Get user's hashtags as a list
#     matched_jobs = set()  # Set to store matched jobs to avoid duplicates
    
#     # Loop over each row in the jobs DataFrame
#     for _, job_row in jobs_df.iterrows():
#         job_hashtags = job_row['hashtags'].split()  # Get job's hashtags as a list
        
#         # Check if there are 2 or 3 matching hashtags
#         matching_hashtags = set(user_hashtags).intersection(job_hashtags)
#         if len(matching_hashtags) == 3 or len(matching_hashtags) == 4:
#             matched_jobs.add(job_row['Company'])  # Add company to matched_jobs set
    
#     # Combine matched companies into a comma-separated string and add to recommendations DataFrame
#     if len(matched_jobs) > 0:
#         recommendations_df = recommendations_df.append({
#             'User': user_row['username'],
#             'Company': ', '.join(matched_jobs)
#         }, ignore_index=True)
        
# # Print recommendations
# print(recommendations_df)



# import pandas as pd
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.feature_extraction.text import CountVectorizer

# # Load user and company data from CSV files
# users_df = pd.read_csv('users.csv')
# companies_df = pd.read_csv('jobs.csv')

# # Extract hashtags from user and company data
# user_hashtags = users_df['hashtags'].tolist()
# company_hashtags = companies_df['hashtags'].tolist()

# # Use CountVectorizer to transform the hashtags into a feature vector
# vectorizer = CountVectorizer(tokenizer=lambda x: x.split(','))
# hashtags_matrix = vectorizer.fit_transform(user_hashtags + company_hashtags)

# # Compute the cosine similarity between user and company vectors
# user_vectors = hashtags_matrix[:len(user_hashtags)]
# company_vectors = hashtags_matrix[len(user_hashtags):]
# similarity_matrix = cosine_similarity(user_vectors, company_vectors)

# # Convert the similarity matrix into a DataFrame
# similarity_df = pd.DataFrame(similarity_matrix, index=users_df['username'], columns=companies_df['Company'])

# # Print the similarity between users and companies
# print(similarity_df)



"""# **Making recommender system**"""

# import pandas as pd 
# import numpy as np 
# df1=pd.read_csv('/content/jobs.csv')
# df2=pd.read_csv('/content/users.csv')

# df1.columns = ['Company','Job Name','hashtags','Experience Level','Location']
# df2= df2.merge(df1,on='hashtags')

# df2.head(5)

# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer

# # Load data into a pandas dataframe
# data = pd.read_csv("/content/users.csv")

# # Create a tfidf vectorizer object
# tfidf = TfidfVectorizer()

# # Fit and transform the hashtags column into a tfidf matrix
# tfidf_matrix = tfidf.fit_transform(data["hashtags"])

# # Print out the tfidf matrix
# print(tfidf_matrix.toarray())

# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer


# jobs_df = pd.read_csv('/content/jobs.csv')
# user_df = pd.read_csv('/content/users.csv')

# # Creating a TF-IDF vectorizer and transforming user data based on hashtags
# tfidf = TfidfVectorizer()
# hashtags_tfidf = tfidf.fit_transform(user_df['hashtags'])

# # Converting the transformed data to a pandas DataFrame and joining with the original user data
# hashtags_tfidf_df = pd.DataFrame(hashtags_tfidf.toarray(), columns=tfidf.get_feature_names_out())
# user_df = user_df.join(hashtags_tfidf_df)

# print(jobs_df)
# print(user_df)



# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# # Load data into a pandas dataframe
# data = pd.read_csv("/content/users.csv")

# # Create a tfidf vectorizer object
# tfidf = TfidfVectorizer()

# # Fit and transform the hashtags column into a tfidf matrix
# tfidf_matrix = tfidf.fit_transform(data["hashtags"])

# # Compute cosine similarities between all users based on their hashtags
# cosine_similarities = cosine_similarity(tfidf_matrix)

# # Find the top 5 most similar users for each user
# similar_users = {}
# for i in range(len(data)):
#     similar_users[data.iloc[i]["username"]] = list(data.iloc[cosine_similarities[i].argsort()[-6:-1]]["username"])

# # Print out the results
# for user in similar_users:
#     print(f"Users similar to {user}: {', '.join(similar_users[user])}")



"""Linear kernel: Cosine similariy



"""

# # Import linear_kernel
# from sklearn.metrics.pairwise import linear_kernel

# # Compute the cosine similarity matrix
# cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)



"""Reverse Index



"""

# #Construct a reverse map of indices and movie titles
# indices = pd.Series(df2.index, index=df2['hashtags']).drop_duplicates()

"""Get the index of the movie given its title.
Get the list of cosine similarity scores for that particular movie with all movies. Convert it into a list of tuples where the first element is its position and the second is the similarity score.
Sort the aforementioned list of tuples based on the similarity scores; that is, the second element.
Get the top 10 elements of this list. Ignore the first element as it refers to self (the movie most similar to a particular movie is the movie itself).
Return the titles corresponding to the indices of the top elements.
"""

# # Function that takes in movie title as input and outputs most similar movies
# def get_recommendations(hashtag, cosine_sim=cosine_sim):
#     # Get the index of the movie that matches the title
#     idx = indices[hashtag]

#     # Get the pairwsie similarity scores of all movies with that movie
#     sim_scores = list(enumerate(cosine_sim[idx]))

#     # Sort the movies based on the similarity scores
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

#     # Get the scores of the 10 most similar movies
#     sim_scores = sim_scores[1:11]

#     # Get the movie indices
#     movie_indices = [i[0] for i in sim_scores]

#     # Return the top 10 most similar movies
#     return df2['hashtags'].iloc[movie_indices]

"""Generate 50 bit ka array

"""

import pandas as pd
import numpy as np

# Set the number of users in the database
num_users = 100

# Define the possible profession options
profession_options = ['Film and television', 'Visual arts', 'Fashion and beauty', 'Architect', 'Interior designer']

# Create an empty DataFrame for the user database
users = pd.DataFrame(columns=['username', 'hashtags', 'profession', 'experience_level', 'location'])

# Generate random bit vectors for the hashtags field
hashtags = [np.random.randint(0, 2, size=50) for i in range(num_users)]

# Populate the user database with random data
for i in range(num_users):
    users.loc[i] = ['user' + str(i), hashtags[i], np.random.choice(profession_options),
                    np.random.randint(1, 6), 'location' + str(np.random.randint(1, 6))]

# Print the user database
print(users)

users.to_csv('user_data.csv', index=False)

# # Save the data to a CSV file
# import csv

# with open('users_final.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['username', 'hashtags', 'profession', 'experience_level', 'location'])
#     for row in users:
#         print(row)
#         writer.writerow(row)



"""Generation for companies"""



"""company

"""

# Companies final

import pandas as pd
import numpy as np

# Set the number of companies in the database
num_companies = 50

# Define the possible profession options
profession_options = ['Film and television', 'Visual arts', 'Fashion and beauty', 'Architect', 'Interior designer']

# Define the number of hashtags per profession
num_hashtags_per_profession = 10

# Create an empty DataFrame for the company database
companies = pd.DataFrame(columns=['Job Name', 'hashtags', 'profession', 'experience_level', 'location'])

# Populate the company database with random data
for i in range(num_companies):
    # Randomly choose up to two professions for the company
    professions = np.random.choice(profession_options, size=np.random.randint(1, 3), replace=False)
    professions_str = ', '.join(professions)
    # Generate a hashtag vector with 50 bits
    hashtags = np.zeros(50)
    for profession in professions:
        # Find the index of the profession in the profession_options list
        profession_index = profession_options.index(profession)
        # Set the corresponding 10 bits to 1 for the profession
        hashtags[profession_index*num_hashtags_per_profession:(profession_index+1)*num_hashtags_per_profession] = 1
    companies.loc[i] = ['company' + str(i), hashtags.astype(int).tolist(), professions_str,
                        np.random.randint(1, 6), 'location' + str(np.random.randint(1, 6))]
companies.to_csv('jobs_data.csv', index=False)

# # Save the data to a CSV file
# import csv

# with open('jobs_final.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Company','hashtags', 'Job Name', 'experience_level', 'location'])
#     for row in companies:
#         print(data)
#         writer.writerow(row)



import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# load the company and user data into Pandas dataframes
company_df = pd.read_csv("/content/jobs_data.csv")
user_df = pd.read_csv("/content/user_data.csv")

# extract the hashtags from the dataframes as strings
hashtags_company_str = company_df['hashtags'].str[1:-1]
hashtags_user_str = user_df['hashtags'].str[1:-1]

#print(hashtags_company_str)

# convert the hashtags strings to numpy arrays of integers
hashtags_company_vec = np.array([list(map(int, hashtags.split(','))) for hashtags in hashtags_company_str])
hashtags_user_vec = np.array([list(map(int, hashtags.split(' '))) for hashtags in hashtags_user_str])

# calculate the cosine similarity between each company and user
cosine_similarities = cosine_similarity(hashtags_user_vec, hashtags_company_vec)

# create a dataframe to store the results
result_df = pd.DataFrame(cosine_similarities, columns=company_df['Job Name'], index=user_df['username'])

# display the dataframe
#print(hashtags_company_vec)
print(result_df)

import pandas as pd
import numpy as np

# Set the number of companies in the database
num_companies = 50

# Define the possible profession options
profession_options = ['Film and television', 'Visual arts', 'Fashion and beauty', 'Architect', 'Interior designer']

# Define the number of hashtags per profession
num_hashtags_per_profession = 10

# Create an empty DataFrame for the company database
companies = pd.DataFrame(columns=['username', 'hashtags', 'profession', 'experience_level', 'location'])

# Populate the company database with random data
for i in range(num_companies):
    # Randomly choose up to two professions for the company
    professions = np.random.choice(profession_options, size=np.random.randint(1, 3), replace=False)
    professions_str = ', '.join(professions)
    # Generate a hashtag vector with 50 bits
    hashtags = np.zeros(50)
    for profession in professions:
        # Find the index of the profession in the profession_options list
        profession_index = profession_options.index(profession)
        # Set the corresponding 10 bits to 1 for the profession
        hashtags[profession_index*num_hashtags_per_profession:(profession_index+1)*num_hashtags_per_profession] = 1
    companies.loc[i] = ['company' + str(i), hashtags.astype(int).tolist(), professions_str,
                        np.random.randint(1, 6), 'location' + str(np.random.randint(1, 6))]



import re

def generate_skills(jobs_skills, paragraph):
    # Create a new list to store the generated skills
    generated_skills = []
    # Split the paragraph into words while ignoring punctuation marks
    words = re.findall(r'\b\w+\b', paragraph)
    hashtag_words = ['#' + word for word in words]
    # Iterate over the jobs and their skills
    for job, skills in jobs_skills.items():
        # Iterate over the skills for this job
        for skill in skills:
            # Check if the skill is mentioned in the paragraph
            if skill in hashtag_words:
                # Add the skill to the list of generated skills
                generated_skills.append(skill)
    return generated_skills

jobs_skills = {
    'Film and television': ['#filmmaking', '#television', '#cinema', '#filmproduction', '#acting', '#screenwriting'],
    'Visual arts': ['#design', '#graphic', '#design', '#drawing', '#sculpture', '#photography', '#printmaking', '#visualarts'],
    'Fashion and beauty': ['#fashion', '#beauty', '#style', '#modeling', '#makeup', '#designer', '#fashionista'],
    'Architect': ['#architecture', '#design', '#construction', '#building', '#architecturaldesign', '#urbanplanning'],
    'Interior designer': ['#interiordesign', '#homedecor', '#designer', '#decorating', '#homeimprovement', '#furniture']
}

#paragraph = "I am a programmer. I excel in Python, C++, Java."
paragraph = input('Enter a paragraph: ')
generated_skills = generate_skills(jobs_skills, paragraph)
print('Generated skills:', generated_skills)