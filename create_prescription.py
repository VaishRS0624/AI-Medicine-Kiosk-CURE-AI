import pandas as pd
class create():
        df = pd.read_csv('assets/empy_stomach.csv')
        df['empty stomach'] = df['empty stomach'].str.lower()
        def method1(self,salt,prescribed_medicine):
            result = self.df[self.df['empty stomach'].str.contains(salt)]
            # print(result)
            if result.empty:
                 str=prescribed_medicine+" 1 - 0 - 1 after food"
                 return str
            else:
                str = prescribed_medicine + " 1 - 0 - 1 before food"
                return str
