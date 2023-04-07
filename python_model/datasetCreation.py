import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

num_users = 100

profession_options = ['Film and television', 'Visual arts', 'Fashion and beauty', 'Architect', 'Interior designer']

users = pd.DataFrame(columns=['username', 'hashtags', 'profession', 'experience_level', 'location'])

hashtags = [np.random.randint(0, 2, size=50) for i in range(num_users)]


for i in range(num_users):
    users.loc[i] = ['user' + str(i), hashtags[i], np.random.choice(profession_options),
                    np.random.randint(1, 6), 'location' + str(np.random.randint(1, 6))]


users.to_csv('user_data.csv', index=False)

num_companies = 50

profession_options = ['Film and television', 'Visual arts', 'Fashion and beauty', 'Architect', 'Interior designer']

num_hashtags_per_profession = 10
companies = pd.DataFrame(columns=['Job Name', 'hashtags', 'profession', 'experience_level', 'location'])

for i in range(num_companies):
    professions = np.random.choice(profession_options, size=np.random.randint(1, 3), replace=False)
    professions_str = ', '.join(professions)
    hashtags = np.zeros(50)
    for profession in professions:
        profession_index = profession_options.index(profession)
        hashtags[profession_index*num_hashtags_per_profession:(profession_index+1)*num_hashtags_per_profession] = 1
    companies.loc[i] = ['company' + str(i), hashtags.astype(int).tolist(), professions_str,
                        np.random.randint(1, 6), 'location' + str(np.random.randint(1, 6))]
companies.to_csv('jobs_data.csv', index=False)

