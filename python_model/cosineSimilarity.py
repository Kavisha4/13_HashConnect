import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

company_df = pd.read_csv("jobs_data.csv")
user_df = pd.read_csv("user_data.csv")
hashtags_company_str = company_df['hashtags'].str[1:-1]
hashtags_user_str = user_df['hashtags'].str[1:-1]
hashtags_company_vec = np.array([list(map(int, hashtags.split(','))) for hashtags in hashtags_company_str])
hashtags_user_vec = np.array([list(map(int, hashtags.split(' '))) for hashtags in hashtags_user_str])

cosine_similarities = cosine_similarity(hashtags_user_vec, hashtags_company_vec)

result_df = pd.DataFrame(cosine_similarities, columns=company_df['Job Name'], index=user_df['username'])
result_df.to_csv('cosineSimilarity.csv', index=False)
