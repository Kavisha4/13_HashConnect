#generate hashtags
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
