import pandas as pd
import re
class get_prescription_from_medicine():

       df=pd.read_csv("assets/medicine_data.csv")

       def createcsv(self):
              self.df.drop(['product_manufactured', 'medicine_desc', 'side_effects',
       'drug_interactions'],axis=1,inplace=True, errors='ignore')
              self.df['product_price'] = self.df['product_price'].str.replace('₹', '')
              self.df['product_price'] = self.df['product_price'].astype(float)
              self.df['salt'] = self.df['salt_composition'].str.lower()
              self.df.drop(['salt_composition'],axis=1,inplace=True)
              # print(self.df.isna().sum())
              self.df.dropna(inplace=True)
              # print(self.df.isna().sum())
              # self.df['Cleaned_Medication'] = self.df['salt'].apply(lambda x: re.sub(r'[^a-zA-Z]', '', x.lower()))
              # print(self.df.head())

       def prepare_prescription(self,pri_medicine):
              result = self.df[self.df['salt'].str.contains(pri_medicine.lower())]
              df1 = pd.DataFrame(result)
              df1 = df1.sort_values(by='product_price')

              if not df1.empty:
                     product_names_df = pd.DataFrame(df1.product_name)
                     product_name = product_names_df.product_name.iloc[0]
                     # print(product_name)
                     return product_name
              else:
                     # print("No matching prescriptions found.")
                     return None
#
# a=get_prescription_from_medicine()
# a.createcsv()
# list1=['Humalog', 'Lantus', 'Novolog', 'insulin lispro', 'insulin aspart', 'Lantus SoloStar', 'Lyumjev', 'insulin detemir', 'Levemir', 'insulin aspart/insulin aspart protamine', 'Humalog KwikPen', 'NovoLog FlexPen', 'Apidra', 'insulin glargine', 'Basaglar', 'Tresiba', 'Toujeo SoloStar', 'Humulin N', 'Humulin R', 'Afrezza', 'Novolin R', 'Symlin', 'Humulin 70/30', 'insulin regular', 'Novolin N', 'Admelog', 'Fiasp', 'Novolin 70/30', 'Humalog Mix 75/25', 'insulin glulisine', 'Rezvoglar', 'Semglee', 'Toujeo Max SoloStar', 'Humulin R U-500 (Concentrated)', 'NovoLog Mix 70/30', 'NovoLog PenFill', 'octreotide', 'pramlintide', 'insulin inhalation, rapid acting', 'insulin isophane', 'NovoLog Mix 70/30 FlexPen', 'Humulin N Pen', 'Humulin R U-500 KwikPen', 'insulin degludec', 'insulin isophane / insulin regular', 'Myxredlin', 'Humalog Mix 50/50', 'Humalog Mix 75/25 KwikPen', 'insulin lispro/insulin lispro protamine', 'Symlin Pen', 'SymlinPen 60', 'SymlinPen 120', 'Humalog Mix 50/50 KwikPen', 'Humulin 50/50', 'Humulin 70/30 Pen', 'ReliOn/Novolin 70/30', 'Tzield', 'metformin', 'Farxiga', 'Trulicity', 'Rybelsus', 'dapagliflozin', 'dulaglutide', 'insulin aspart', 'insulin detemir', 'insulin lispro', 'Lyumjev', 'semaglutide', 'Soliqua', 'insulin aspart/insulin aspart protamine', 'insulin glargine / lixisenatide', 'Januvia', 'Mounjaro', 'Victoza', 'glipizide', 'glimepiride', 'Amaryl', 'Invokana', 'Lantus', 'Actos', 'Jardiance', 'Levemir', 'Janumet', 'Glucotrol', 'Byetta', 'Ozempic', 'Glumetza', 'liraglutide', 'pioglitazone', 'Tradjenta', 'Bydureon', 'Humalog', 'Lantus SoloStar', 'sitagliptin', 'Novolog', 'glyburide', 'metformin / sitagliptin', 'Onglyza', 'Riomet', 'GlipiZIDE XL', 'insulin glargine', 'NovoLog FlexPen', 'Prandin', 'Tresiba', 'canagliflozin', 'chromium picolinate', 'empagliflozin', 'exenatide', 'Humulin R', 'repaglinide', 'acarbose', 'alogliptin', 'Avandia', 'Basaglar', 'glimepiride / pioglitazone', 'Glucotrol XL', 'glyburide / metformin', 'Humalog KwikPen', 'Humulin N', 'Kombiglyze XR', 'linagliptin', 'Toujeo SoloStar', 'Welchol', 'Xigduo XR', 'Adlyxin', 'Admelog', 'Apidra', 'bromocriptine', 'colesevelam', 'Cycloset', 'dapagliflozin / metformin', 'DiaBeta', 'empagliflozin / metformin', 'glipizide / metformin', 'Glucovance', 'Glycron', 'Glynase', 'Glyset', 'Humulin 70/30', 'insulin regular', 'Janumet XR', 'Jentadueto', 'lixisenatide', 'metformin / pioglitazone', 'metformin / saxagliptin', 'miglitol', 'Nesina', 'Novolin 70/30', 'Novolin N', 'Novolin R', 'pramlintide', 'saxagliptin', 'Synjardy', 'Toujeo Max SoloStar', 'Xultophy', 'ActoPlus Met', 'Afrezza', 'albiglutide', 'alogliptin / metformin', 'alogliptin / pioglitazone', 'Bydureon BCise', 'canagliflozin / metformin', 'Cr-GTF', 'CRM', 'dapagliflozin / saxagliptin', 'Duetact', 'empagliflozin / linagliptin / metformin', 'empagliflozin / linagliptin', 'ertugliflozin / metformin', 'ertugliflozin / sitagliptin', 'ertugliflozin', 'Fiasp', 'Glynase PresTab', 'Glyxambi', 'Humalog Mix 50/50', 'Humalog Mix 50/50 KwikPen', 'Humalog Mix 75/25', 'Humalog Mix 75/25 KwikPen', 'Humulin 50/50', 'Humulin 70/30 Pen', 'Humulin N Pen', 'Humulin R U-500 (Concentrated)', 'Humulin R U-500 KwikPen', 'insulin degludec / liraglutide', 'insulin degludec', 'insulin glulisine', 'insulin inhalation, rapid acting', 'insulin isophane / insulin regular', 'insulin isophane', 'insulin lispro/insulin lispro protamine', 'Invokamet', 'Invokamet XR', 'Jentadueto XR', 'Kazano', 'linagliptin / metformin', 'Myxredlin', 'nateglinide', 'NovoLog Mix 70/30', 'NovoLog Mix 70/30 FlexPen', 'NovoLog PenFill', 'Oseni', 'Qtern', 'ReliOn/Novolin 70/30', 'Rezvoglar', 'rosiglitazone', 'Segluromet', 'Semglee', 'Starlix', 'Steglatro', 'Steglujan', 'Symlin', 'Symlin Pen', 'SymlinPen 60', 'SymlinPen 120', 'Synjardy XR', 'Tanzeum', 'tirzepatide', 'Trijardy XR']
#
# # for i in list1:
# b=a.prepare_prescription(i)
# print(b)
