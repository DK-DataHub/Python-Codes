import pandas as pd
Rankholders = {
    'Name': ["Deepak", "Karthick", "Vinoth"],
    'Top_Subjects': ["Physics", "Maths", "Engineering Graphics"],
    'CGPA': [9, 8, 7]
}
Rank = pd.DataFrame(Rankholders)
print(Rank)
