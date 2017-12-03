# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
<<<<<<< HEAD
os.chdir("C:/Users/behzad/Dropbox/_2_Teaching Activities/_0_EETBS- On-going/git_fork_clone/Scientific_Python_Assignments_POLIMI_EETBS/Assignment 7 Pandas B DeadLine Nov 8th 2017/__Guidelines__")
=======
os.chdir ("C:\Users\Marica\Desktop\Scientific_Python_Assignments_POLIMI_EETBS\Assignment 7 Pandas B DeadLine Nov 8th 2017\__Guidelines__")
>>>>>>> e6c3439b3e8e67251c7895875b304c4f164ff375



# Here is what we did for reading windows.csv

windows_DF = pd.read_csv("windows.csv",sep=";",index_col=0)
# Let's see what the columns are!
print windows_DF.columns
print windows_DF.index

windows_DF["width"]["west"]
windows_DF.loc["west","width"]
windows_DF["Area"]=windows_DF["Height"]*windows_DF["width"]

# How to write the modified Table to a new file.
windows_DF.to_csv("windows_completed1.csv",sep=";")
windows_DF.to_html("windows_completed1.html")


# How to read IAC_cl.csv file


DF_IAC_cl = pd.read_csv("IAC_cl.csv",sep = ";",index_col=1)

# How to extract a value:

IAC_cl_value= DF_IAC_cl["DrapesLightOpen"]["5c"]

# or taking the inputs from the windows_DF
index="east"
windowID= windows_DF["Window_ID"][index]
IntShadingID=windows_DF["IntShading_ID"][index]
IAC_cl_value= DF_IAC_cl[IntShadingID][windowID]


windows_DF["IAC_cl"] = np.array([IAC_cl_value,0,0,0])


# How to write the modified Table to a new file.
windows_DF.to_csv("windows_completedWithIAC.csv",sep=";")
windows_DF.to_html("windows_completedWithIAC.html")
    

# you should go through a similar procedure to find the PXI for the "east" window and update the Table accordingly!

    
