import pandas as pd
df  = pd.read_stata(data_filepath + "individual_characteristics.dta")
df1 = df.loc[df.village == 1]
df2 = df.loc[df.village == 2]
df1.head()