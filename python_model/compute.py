import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def compute(input1, input2,input3,input4,input5):
   
#    num_companies = 50
#    profession_options = ['Film and television', 'Visual arts', 'Fashion and beauty', 'Architect', 'Interior designer']
#    num_hashtags_per_profession = 10
#    companies = pd.DataFrame(columns=['username', 'hashtags', 'profession', 'experience_level', 'location'])

#    for i in range(num_companies):
#     # Randomly choose up to two professions for the company
#         professions = np.random.choice(profession_options, size=np.random.randint(1, 3), replace=False)
#         professions_str = ', '.join(professions)
#         # Generate a hashtag vector with 50 bits
#         hashtags = np.zeros(50)
#         for profession in professions:
#             # Find the index of the profession in the profession_options list
#             profession_index = profession_options.index(profession)
#             # Set the corresponding 10 bits to 1 for the profession
#             hashtags[profession_index*num_hashtags_per_profession:(profession_index+1)*num_hashtags_per_profession] = 1
#         companies.loc[i] = ['company' + str(i), hashtags.astype(int).tolist(), professions_str,
#                             np.random.randint(1, 6), 'location' + str(np.random.randint(1, 6))]

    hashtags = ['#filmmaking', '#television', '#cinema', '#filmproduction', '#acting', '#screenwriting','#act','#direct','#shortfilm','#cinematography',
            '#design', '#graphicdesign', '#drawing', '#sculpture', '#photography', '#printmaking', '#visualarts','#mixedmedia','#gallery','#illustrations','#sketch',
            '#fashion', '#beauty', '#style', '#modeling', '#makeup', '#designer', '#fashionista','#streetstyle','#accessories','#nails',
            '#architecture', '#construction', '#building', '#architecturaldesign', '#urbanplanning','#modern' ,'#historic','#landscape','#monument',
            '#interiordesign', '#homedecor', '#homeimprovement', '#furniture','#homecolor','#homestyling','#interiorforall','#roomdecor']

    # input_list = ['#cinema', '#acting', '#graphicdesign', '#fashion', '#architecture']
    input_list = []
    # input_list.apprnd()
    my_list.append(var1)
    my_list.append(var2)
    my_list.append(var3)
    result = []

    for i in range(0,len(hashtags)):
        if(hashtags[i] in input_list):
            result.append(1)
        else:
            result.append(0)

    return result