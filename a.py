import pandas as pd

class get_disease_from_symptoms:
    mapping = {
        "Acne": "Fungal infection",
        "ADHD": "Drug Reaction",
        "Allergies": "Allergy",
        "Alzheimer's": "AIDS",
        "Angina": "Heart attack",
        "Anxiety": "Drug Reaction",
        "Asthma": "Bronchial Asthma",
        "Bipolar Disorder": "Drug Reaction",
        "Bronchitis": "Common Cold",
        "Cancer": "Drug Reaction",
        "Cholesterol": "Drug Reaction",
        "Colds & Flu": "Common Cold",
        "Constipation": "Gastroenteritis",
        "COPD": "Bronchial Asthma",
        "Covid 19": "Common Cold",  # Placeholder; replace with appropriate mapping
        "Depression": "Drug Reaction",
        "Diabetes (Type 1)": "Diabetes",
        "Diabetes (Type 2)": "Diabetes",
        "Diarrhea": "Gastroenteritis",
        "Eczema": "Psoriasis",
        "Erectile Dysfunction": "Drug Reaction",
        "Gastrointestinal": "Gastroenteritis",
        "GERD (Heartburn)": "GERD",
        "Gout": "Drug Reaction",
        "Hair Loss": "Drug Reaction",
        "Hayfever": "Allergy",
        "Herpes": "Drug Reaction",
        "Hypertension": "Hypertension",
        "Hypothyroidism": "Hypothyroidism",
        "IBD (Bowel)": "Gastroenteritis",
        "Incontinence": "Drug Reaction",
        "Insomnia": "Drug Reaction",
        "Menopause": "Drug Reaction",
        "Migraine": "Migraine",
        "Osteoarthritis": "Osteoarthristis",
        "Osteoporosis": "Drug Reaction",
        "Pain": "Drug Reaction",
        "Pneumonia": "Pneumonia",
        "Psoriasis": "Psoriasis",
        "Rheumatoid Arthritis": ""
        # ... (your mapping dictionary remains the same)
    }

    df = pd.read_csv('assets/drugs_for_common_treatments.csv')

    def createcsv(self):
        self.df = pd.read_csv('assets/drugs_for_common_treatments.csv')
        self.df = self.df.drop(['medical_condition_url', 'drug_link', 'medical_condition_description', 'rx_otc', 'csa', 'alcohol',
                      'no_of_reviews'], axis=1)
        self.df['medical_cond'] = self.df['medical_condition'].str.lower()
        self.df['activity'] = self.df['activity'].str.replace('%', '')
        self.df['activity'] = self.df['activity'].astype(float)
        self.df.drop('medical_condition', axis=1, inplace=True)
        self.df = self.df.set_index('medical_cond')


    def illness_mapping(self, illnesses):
        matched_illnesses = []
        for i in illnesses:
            for illness1 in self.mapping.keys():
                if i in self.mapping[illness1]:
                    illness2 = illness1
                    matched_illnesses.append(illness2)
        return matched_illnesses

    def get_medicine(self, illness):
        row_by_index = self.df.loc[illness]
        df2 = pd.DataFrame(row_by_index)
        # return df2
        return df2['drug_name']


# Create an instance of the class
a = get_disease_from_symptoms()

# Load data and preprocess it
a.createcsv()

# Get matched illnesses from mapping
illnesses = a.illness_mapping(['Fungal infection'])

list1=[]
# Get medicine for each matched illness
for illness in illnesses:
    medicine_data = a.get_medicine(illness.lower())
    print(medicine_data)