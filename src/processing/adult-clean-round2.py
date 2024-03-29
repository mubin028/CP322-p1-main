import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('adult_clean.csv')

# Convert binary classifications to 0 and 1
df['sex'] = df['sex'].map({' Male': 1, ' Female': 0})
df['income'] = df['income'].map({' <=50K': 0, ' >50K': 1})

# Replace 'True' with 1 and 'False' with 0 in the entire DataFrame
df = df.replace({True: 1, False: 0})

df = df[['age', 'education-num', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week',
         'workclass_ Local-gov', 'workclass_ Never-worked', 'workclass_ Private', 'workclass_ Self-emp-inc',
         'workclass_ Self-emp-not-inc', 'workclass_ State-gov', 'workclass_ Without-pay', 'education_ 11th',
         'education_ 12th', 'education_ 1st-4th', 'education_ 5th-6th', 'education_ 7th-8th', 'education_ 9th',
         'education_ Assoc-acdm', 'education_ Assoc-voc', 'education_ Bachelors', 'education_ Doctorate',
         'education_ HS-grad', 'education_ Masters', 'education_ Preschool', 'education_ Prof-school',
         'education_ Some-college', 'marital-status_ Married-AF-spouse', 'marital-status_ Married-civ-spouse',
         'marital-status_ Married-spouse-absent', 'marital-status_ Never-married', 'marital-status_ Separated',
         'marital-status_ Widowed', 'occupation_ Armed-Forces', 'occupation_ Craft-repair', 'occupation_ Exec-managerial',
         'occupation_ Farming-fishing', 'occupation_ Handlers-cleaners', 'occupation_ Machine-op-inspct',
         'occupation_ Other-service', 'occupation_ Priv-house-serv', 'occupation_ Prof-specialty',
         'occupation_ Protective-serv', 'occupation_ Sales', 'occupation_ Tech-support', 'occupation_ Transport-moving',
         'relationship_ Not-in-family', 'relationship_ Other-relative', 'relationship_ Own-child', 'relationship_ Unmarried',
         'relationship_ Wife', 'race_ Asian-Pac-Islander', 'race_ Black', 'race_ Other', 'race_ White'] +
        ['native-country_ Canada', 'native-country_ China', 'native-country_ Columbia', 'native-country_ Cuba',
         'native-country_ Dominican-Republic', 'native-country_ Ecuador', 'native-country_ El-Salvador',
         'native-country_ England', 'native-country_ France', 'native-country_ Germany', 'native-country_ Greece',
         'native-country_ Guatemala', 'native-country_ Haiti', 'native-country_ Holand-Netherlands', 'native-country_ Honduras',
         'native-country_ Hong', 'native-country_ Hungary', 'native-country_ India', 'native-country_ Iran',
         'native-country_ Ireland', 'native-country_ Italy', 'native-country_ Jamaica', 'native-country_ Japan',
         'native-country_ Laos', 'native-country_ Mexico', 'native-country_ Nicaragua', 'native-country_ Outlying-US(Guam-USVI-etc)',
         'native-country_ Peru', 'native-country_ Philippines', 'native-country_ Poland', 'native-country_ Portugal',
         'native-country_ Puerto-Rico', 'native-country_ Scotland', 'native-country_ South', 'native-country_ Taiwan',
         'native-country_ Thailand', 'native-country_ Trinadad&Tobago', 'native-country_ United-States', 'native-country_ Vietnam',
         'native-country_ Yugoslavia', 'income']]

df.to_csv('adult_clean_updated.csv', index=False)
