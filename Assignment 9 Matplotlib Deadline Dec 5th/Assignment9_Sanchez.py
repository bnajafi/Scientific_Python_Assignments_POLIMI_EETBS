import pandas as pd
import matplotlib.pyplot as plt

Walls=[105.8,0.458,1201.7,547.5]
Door=[2.2,1.694,94.4,43]
Roof=[200,0.25,1240,514.6]

Opaque_Surfaces=['Walls','Door','Roof']
Columns_names=["Area","U_factor","Heating_Load","Cooling_Load"]
Opaque_DF=pd.DataFrame(Opaque_Surfaces,index=Opaque_Surfaces,columns=Columns_names)

plt.figure()
plt.pie(Opaque_DF['Heating_Load'],labels=Opaque_Surfaces,colors=['r','g','b'],startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')

plt.figure()
plt.pie(Opaque_DF['Cooling_Load'],labels=Opaque_Surfaces,colors=['r','g','b'],startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')

New_U_Factor=range(0.458,4)
new=pd.Series(New_U_Factor)
Area=[105,2.2,200]

def calc(UFac):
    Heating_L=Area*UFac*24.8
    return Heating_L

new_heating_load=new.apply(calc)
    
plt.bar(new_heating_load,color="g")
plt.figure()
