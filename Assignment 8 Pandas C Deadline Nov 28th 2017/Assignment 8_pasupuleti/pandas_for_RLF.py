import os
import pandas as pd
import numpy as np
os.chdir("C:/Users/behzad/Dropbox/_2_Teaching Activities/_0_EETBS- On-going/EETBS 2017-2018 POLIMI-PIACENZA/3 Python Files and Guidelines/Numpy - Pandas/RLF Method")
windows_DF = pd.read_csv("windows.csv",sep=";",index_col=0)
# Let's see what the columns are!
print windows_DF.columns
print windows_DF.index

windows_DF["width"]["west"]
windows_DF.loc["west","width"]
windows_DF["Area"]=windows_DF["Height"]*windows_DF["width"]
windows_DF.to_csv("windows_completed1.csv",sep=";")
windows_DF.to_html("windows_completed1.html")