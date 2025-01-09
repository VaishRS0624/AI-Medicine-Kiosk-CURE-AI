import pandas as pd
class findmatrix():
    symptoms_combined = {
    'itching': ['skin rash', 'nodal skin eruptions', 'Feeling of skin irritation and a desire to scratch.'],
    'skin_rash': ['itching', 'nodal skin eruptions', 'Feeling of skin irritation and a desire to scratch.'],
    'nodal_skin_eruptions': ['itching', 'skin rash', 'Feeling of skin irritation and a desire to scratch.'],
    'continuous_sneezing': ['shivering', 'chills', 'Frequent and persistent sneezing.'],
    'shivering': ['continuous_sneezing', 'chills', 'Frequent and persistent sneezing.'],
    'chills': ['continuous_sneezing', 'shivering', 'Frequent and persistent sneezing.'],
    'joint_pain': ['stomach pain', 'acidity', 'Discomfort or aching in the joints.'],
    'stomach_pain': ['joint_pain', 'acidity', 'Discomfort or pain in the abdominal area.'],
    'acidity': ['joint_pain', 'stomach_pain', 'Discomfort or pain in the stomach related to digestion.'],
    'ulcers_on_tongue': ['muscle wasting', 'vomiting', 'Presence of sores or open lesions on the tongue.'],
    'muscle_wasting': ['ulcers_on_tongue', 'vomiting', 'Presence of sores or open lesions on the tongue.'],
    'vomiting': ['ulcers_on_tongue', 'muscle_wasting', 'Presence of sores or open lesions on the tongue.'],
    'burning_micturition': ['spotting urination', 'fatigue',
                            'Experiencing pain or a burning sensation during urination.'],
    'spotting_urination': ['burning_micturition', 'fatigue',
                           'Experiencing pain or a burning sensation during urination.'],
    'fatigue': ['burning_micturition', 'spotting urination',
                'Experiencing pain or a burning sensation during urination.'],
    'weight_gain': ['anxiety', 'cold hands and feets', 'An increase in body weight.'],
    'anxiety': ['weight_gain', 'cold hands and feets', 'An increase in body weight.'],
    'cold_hands_and_feets': ['weight_gain', 'anxiety', 'An increase in body weight.'],
    'mood_swings': ['weight_loss', 'restlessness', 'Sudden and intense changes in mood.'],
    'weight_loss': ['mood_swings', 'restlessness', 'Sudden and intense changes in mood.'],
    'restlessness': ['mood_swings', 'weight_loss', 'Sudden and intense changes in mood.'],
    'lethargy': ['patches in throat', 'irregular sugar level', 'Feeling of tiredness and lack of energy.'],
    'patches_in_throat': ['lethargy', 'irregular sugar level', 'Feeling of tiredness and lack of energy.'],
    'irregular_sugar_level': ['lethargy', 'patches in throat', 'Feeling of tiredness and lack of energy.'],
    'cough': ['high fever', 'sunken eyes', 'Expelling air from the lungs with a sudden sharp sound.'],
    'high_fever': ['cough', 'sunken eyes', 'Expelling air from the lungs with a sudden sharp sound.'],
    'sunken_eyes': ['cough', 'high fever', 'Expelling air from the lungs with a sudden sharp sound.'],
    'breathlessness': ['sweating', 'dehydration', 'Difficulty in breathing or shortness of breath.'],
    'sweating': ['breathlessness', 'dehydration', 'Difficulty in breathing or shortness of breath.'],
    'dehydration': ['breathlessness', 'sweating', 'Difficulty in breathing or shortness of breath.'],
    'indigestion': ['headache', 'yellowish skin', 'Discomfort or pain in the stomach related to digestion.'],
    'headache': ['indigestion', 'yellowish skin', 'Discomfort or pain in the head.'],
    'yellowish_skin': ['indigestion', 'headache', 'Skin coloration turning yellow.'],
    'dark_urine': ['nausea', 'loss of appetite', 'Urine that is darker in color than usual.'],
    'nausea': ['dark_urine', 'loss of appetite', 'Feeling of wanting to vomit.'],
    'loss_of_appetite': ['dark_urine', 'nausea', 'Reduction in the desire to eat.'],
    'pain_behind_the_eyes': ['back pain', 'constipation', 'Discomfort or ache located at the back of the eyes.'],
    'back_pain': ['pain_behind_the_eyes', 'constipation', 'Discomfort or pain in the back.'],
    'constipation': ['pain_behind_the_eyes', 'back pain', 'Difficulty in passing stool.'],
    'abdominal_pain': ['diarrhoea', 'mild fever', 'Discomfort or pain in the abdominal area.'],
    'diarrhoea': ['abdominal_pain', 'mild fever', 'Frequent and loose bowel movements.'],
    'mild_fever': ['abdominal_pain', 'diarrhoea', 'A slight increase in body temperature.'],
    'yellow_urine': ['acute liver failure', 'fluid overload', 'Urine that has a yellowish color.'],
    'yellowing_of_eyes': ['acute liver failure', 'fluid overload', 'Yellowing of the eyes.'],
    'acute_liver_failure': ['yellow_urine', 'yellowing_of_eyes', 'A sudden, severe liver dysfunction.'],
    'fluid_overload': ['swelling of stomach', 'swelled lymph nodes', 'Excess accumulation of fluid in the body.'],
    'swelling_of_stomach': ['fluid_overload', 'swelled lymph nodes','Abnormal enlargement or puffiness of the stomach.'],
    'swelled_lymph_nodes': ['fluid_overload', 'swelling of stomach', 'Enlarged and tender lymph nodes.'],
    'malaise': ['blurred and distorted vision', 'phlegm', 'A general feeling of discomfort, illness, or uneasiness.'],
    'blurred_and_distorted_vision': ['malaise', 'phlegm', 'Visual impairment with unclear and distorted images.'],
    'phlegm': ['malaise', 'blurred and distorted vision', 'Thick, sticky mucus in the throat or lungs.'],
    'throat_irritation': ['malaise', 'blurred and distorted vision', 'Scratchiness or discomfort in the throat.'],
    'redness_of_eyes': ['malaise', 'blurred and distorted vision', 'Eyes that appear red in color.'],
    'sinus_pressure': ['malaise', 'blurred and distorted vision', 'Feeling of pressure or fullness in the sinuses.'],
    'runny_nose': ['malaise', 'blurred and distorted vision', 'Excessive nasal discharge.'],
    'congestion': ['chest pain', 'weakness in limbs', 'Blockage or accumulation of fluid in the nasal passages.'],
    'chest_pain': ['congestion', 'weakness in limbs', 'Discomfort or pain in the chest area.'],
    'weakness_in_limbs': ['congestion', 'chest pain', 'Lack of strength or energy in the arms or legs.'],
    'fast_heart_rate': ['congestion', 'chest pain', 'Abnormally rapid heartbeat.'],
    'pain_during_bowel_movements': ['pain in anal region', 'bloody stool', 'Discomfort or pain while passing stool.'],
    'pain_in_anal_region': ['pain_during_bowel_movements', 'bloody stool', 'Discomfort or ache in the anal area.'],
    'bloody_stool': ['pain_during_bowel_movements', 'pain_in_anal_region', 'Presence of blood in the stool.'],
    'irritation_in_anus': ['pain_in_anal_region', 'bloody stool', 'Discomfort or inflammation in the anus.'],
    'neck_pain': ['dizziness', 'cramps', 'Discomfort or pain in the neck.'],
    'dizziness': ['neck_pain', 'cramps', 'Sensation of lightheadedness or unsteadiness.'],
    'cramps': ['neck_pain', 'dizziness', 'Painful muscle contractions.'],
    'bruising': ['obesity', 'swollen legs', 'Injury or discoloration of the skin due to impact.'],
    'obesity': ['bruising', 'swollen legs', 'Excessive body weight or fat accumulation.'],
    'swollen_legs': ['bruising', 'obesity', 'Abnormal enlargement or puffiness of the legs.'],
    'swollen_blood_vessels': ['bruising', 'obesity', 'Enlarged or distended blood vessels.'],
    'puffy_face_and_eyes': ['bruising', 'obesity', 'Swelling or puffiness of the face and eyes.'],
    'enlarged_thyroid': ['brittle nails', 'swollen extremities', 'Abnormal enlargement of the thyroid gland.'],
    'brittle_nails': ['enlarged_thyroid', 'swollen extremities', 'Nails that are easily broken or cracked.'],
    'swollen_extremities': ['enlarged_thyroid', 'brittle nails',
                            'Abnormal enlargement of the extremities (hands or feet).'],
    'excessive_hunger': ['drying and tingling lips', 'slurred speech', 'Unusual or extreme hunger.'],
    'extra_marital_contacts': ['excessive_hunger', 'drying and tingling lips',
                               'Engaging in intimate relationships outside of marriage.'],
    'drying_and_tingling_lips': ['excessive_hunger', 'slurred speech', 'Feeling of dryness and tingling in the lips.'],
    'slurred_speech': ['excessive_hunger', 'drying and tingling lips', 'Impaired or unclear speech.'],
    'knee_pain': ['slurred speech', 'hip joint pain', 'Discomfort or pain in the knees.'],
    'hip_joint_pain': ['knee_pain', 'muscle weakness', 'Discomfort or pain in the hip joint.'],
    'muscle_weakness': ['knee_pain', 'hip joint pain', 'Lack of strength or endurance in the muscles.'],
    'stiff_neck': ['muscle_weakness', 'spinning movements', 'Difficulty in moving the neck due to stiffness.'],
    'swelling_joints': ['muscle_weakness', 'movement stiffness', 'Abnormal enlargement or puffiness of the joints.'],
    'movement_stiffness': ['stiff_neck', 'swelling_joints', 'Difficulty in moving the body with stiffness.'],
    'spinning_movements': ['loss of balance', 'unsteadiness', 'Sensation of spinning or dizziness.'],
    'loss_of_balance': ['spinning_movements', 'unsteadiness',
                        'Inability to maintain an upright posture or equilibrium.'],
    'unsteadiness': ['spinning_movements', 'loss_of_balance', 'Lack of stability or steadiness.'],
    'weakness_of_one_body_side': ['loss_of_balance', 'unsteadiness',
                                  'Reduced strength or control on one side of the body.'],
    'loss_of_smell': ['bladder discomfort', 'foul smell of urine', 'Impaired or complete loss of the sense of smell.'],
    'bladder_discomfort': ['loss_of_smell', 'foul smell of urine', 'Discomfort or pain in the bladder.'],
    'foul_smell_of_urine': ['loss_of_smell', 'bladder discomfort', 'Unpleasant odor in the urine.'],
    'continuous_feel_of_urine': ['loss_of_smell', 'passage of gases', 'Persistent sensation of needing to urinate.'],
    'passage_of_gases': ['loss_of_smell', 'continuous_feel_of_urine',
                         'Excretion of air or gas from the digestive tract.'],
    'internal_itching': ['loss_of_smell', 'toxic_look_(typhos)', 'Itching sensation inside the body.'],
    'toxic_look_(typhos)': ['internal_itching', 'loss_of_smell',
                            'Appearance of a toxic or ill look associated with typhoid fever.'],
    'depression': ['muscle pain', 'altered sensorium', 'Persistent feeling of sadness or hopelessness.'],
    'irritability': ['depression', 'muscle pain', 'Tendency to become easily annoyed or angered.'],
    'muscle_pain': ['irritability', 'depression', 'Discomfort or ache in the muscles.'],
    'altered_sensorium': ['irritability', 'depression', 'Changes in consciousness or mental awareness.'],
    'red_spots_over_body': ['belly pain', 'abnormal menstruation', 'Reddish spots or markings on the skin.'],
    'belly_pain': ['red_spots_over_body', 'abnormal menstruation', 'Discomfort or pain in the abdominal area.'],
    'abnormal_menstruation': ['red_spots_over_body', 'belly pain', 'Irregular or abnormal menstrual bleeding.'],
    'dischromic_patches': ['watering from eyes', 'increased appetite', 'Abnormal discoloration or patches on the skin.'],
    'watering_from_eyes': ['dischromic_patches', 'increased appetite', 'Excessive production of tears from the eyes.'],
    'increased_appetite': ['dischromic_patches', 'watering from eyes', 'An abnormal or excessive desire for food.'],
    'polyuria': ['family history', 'mucoid sputum', 'Excessive production of urine.'],
    'family_history': ['polyuria', 'mucoid sputum', 'A record of illnesses in the patient\'s family.'],
    'mucoid_sputum': ['polyuria', 'family history', 'Thick, viscous mucus expelled from the respiratory tract.'],
    'rusty_sputum': ['lack of concentration', 'visual disturbances', 'Sputum with a rusty or brownish color.'],
    'lack_of_concentration': ['rusty_sputum', 'visual disturbances', 'Difficulty focusing or paying attention.'],
    'visual_disturbances': ['rusty_sputum', 'lack of concentration', 'Problems with vision or seeing clearly.'],
    'receiving_blood_transfusion': ['receiving unsterile injections', 'coma', 'Process of receiving blood from a donor.'],
    'receiving_unsterile_injections': ['receiving_blood_transfusion', 'coma', 'Receiving injections in an unsterile environment.'],
    'coma': ['receiving_blood_transfusion', 'receiving_unsterile_injections', 'A state of unconsciousness in which a person cannot be awakened.'],
    'stomach_bleeding': ['distention of abdomen', 'history of alcohol consumption', 'Bleeding that occurs in the stomach.'],
    'distention_of_abdomen': ['stomach_bleeding', 'history of alcohol consumption', 'Abnormal enlargement or swelling of the abdomen.'],
    'history_of_alcohol_consumption': ['stomach_bleeding', 'distention of abdomen', 'Record of past alcohol consumption by the patient.'],
    'fluid overload': ['blood in sputum', 'prominent veins on calf', 'Excess accumulation of fluid in the body.'],
    'blood_in_sputum': ['fluid_overload', 'prominent veins on calf', 'Presence of blood in the sputum.'],
    'prominent_veins_on_calf': ['fluid_overload', 'blood in sputum', 'Enlarged or visible veins on the calf.'],
    'palpitations': ['painful walking', 'pus-filled pimples', 'Perception of rapid, strong, or irregular heartbeats.'],
    'painful_walking': ['palpitations', 'pus-filled pimples', 'Discomfort or pain while walking.'],
    'pus_filled_pimples': ['palpitations', 'painful walking', 'Pimples filled with pus on the skin.'],
    'blackheads': ['scurring', 'skin peeling', 'Small dark bumps on the skin, especially the face.'],
    'scurring': ['blackheads', 'skin peeling', 'Formation of flakes or scales on the skin.'],
    'skin_peeling': ['blackheads', 'scurring', 'Shedding of the outer layer of skin in flakes.'],
    'silver_like_dusting': ['small dents in nails', 'inflammatory nails', 'Appearance of silver-like dust on the skin or nails.'],
    'small_dents_in_nails': ['silver_like_dusting', 'inflammatory nails', 'Tiny indentations or depressions in the nails.'],
    'inflammatory_nails': ['silver_like_dusting', 'small dents in nails', 'Nails showing signs of inflammation or infection.'],
    'blister': ['red sore around nose', 'yellow crust ooze', 'A small, raised area of skin filled with fluid.'],
    'red_sore_around_nose': ['blister', 'yellow crust ooze', 'Red and sore area around the nose.'],
    'yellow_crust_ooze': ['blister', 'red sore around nose', 'Yellowish crust or discharge oozing from the skin.']

}

    def createdf(self):
        max_length = max(len(self.symptoms_combined[key]) for key in self.symptoms_combined)
        for key in self.symptoms_combined:
            self.symptoms_combined[key] += [''] * (max_length - len(self.symptoms_combined[key]))
        #Create DataFrame

    def predictionmatrix(self,user_symptoms):
        count=132
        list1 = [0 for i in range(count)]
        # print(list1)
        df = pd.DataFrame(self.symptoms_combined)
        # print(df.columns)
        for symptoms in user_symptoms:
            # print(symptoms)
            for columns1 in df.columns:
                count=0
                # print(columns1)
                for sym in df[columns1]:
                    # print(sym)
                    if symptoms == sym:
                        count+=1
                if symptoms==columns1 or count>0:
                    column_index = df.columns.get_loc(columns1)
                    list1[column_index]=1

        return list1
#
# a=findmatrix()
# a.createdf()
# b1="itching red_sore_around_nose"
# words=b1.split()
# # print(words[0])
# b=a.predictionmatrix(words)
# count=0
# for i in b:
#     count+=1
# print(count)
# print(b)