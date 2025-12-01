import pandas as pd
Rankholders = {
    'Name': ["Deepak", "Karthick", "Vinoth", "Ganesh", "Faruk", "Vignesh", "Harish", "Kanagavel"],
    'Top_Subjects': ["Physics", "Maths", "Engineering Graphics", "Chemistry", "Geography", "UHV", "Python", "Java"],
    'CGPA': [9, 8, 7, 8, 9, 8, 7, 7]
}
Rank = pd.DataFrame(Rankholders)
print(Rank.loc[[0, 2, 4, 6, 7]])
