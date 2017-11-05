# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 15:47:41 2017

@author: edoua
"""

#Assignment 2 with Panda
#

import pandas as pd

#namelist= pd.Series ([type, h, k, L, area,Rvalue])
Rf_list = (["condser",None, 0.026,0.03,0.25,0])
Rp1_list = (["condser",None,0.22,0.02,0.25,0])
Rp2_list = (["condser",None,0.22,0.02,0.25,0])
Rpc1_list = (["condpara",None,0.22,0.16,0.015,0])
Rpc2_list = (["condpara",None,0.22,0.16,0.015,0])
Rb_list = (["condpara",None,0.72,0.16,0.22,0])
R1_list = (["conv",10,None,None,0.25,0])
R2_list = (["conv",20,None,None,0.25,0])

resistance_index = ["Rf","Rp1","Rp2","Rpc1","Rpc2","Rb","R1","R2"]
columns_name = ["type","h","k","L","area","R"]

Resistance_DF=pd.DataFrame([Rf_list,Rp1_list,Rp2_list,Rpc1_list,Rpc2_list,
                            Rb_list,R1_list,R2_list], index = resistance_index,
                             columns = columns_name)

Resistance_DF["R"][ Resistance_DF ["type"]=="condser" ] =  Resistance_DF["L"][Resistance_DF["type"]=="condser" ] / (Resistance_DF["k"][Resistance_DF["type"]=="condser" ] * Resistance_DF["area"][Resistance_DF["type"]=="condser" ])
Resistance_DF["R"][ Resistance_DF ["type"]=="condpara" ] =  Resistance_DF["L"][Resistance_DF["type"]=="condpara" ] / (Resistance_DF["k"][Resistance_DF["type"]=="condpara" ] * Resistance_DF["area"][Resistance_DF["type"]=="condpara" ])
Resistance_DF["R"][ Resistance_DF ["type"]=="conv" ] = 1 / (Resistance_DF["h"][Resistance_DF["type"]=="conv" ] * Resistance_DF["area"][Resistance_DF["type"]=="conv" ])

#y = Resistance_DF["L"][Resistance_DF["type"]=="condser" ]
#z= (Resistance_DF["k"][Resistance_DF["type"]=="condser" ] * Resistance_DF["area"][Resistance_DF["type"]=="condser" ])
#
#x=y/z
Rcondser = Resistance_DF["R"][ Resistance_DF ["type"]=="condser" ].sum()
#Rinvcondpara = 1/Resistance_DF["R"][ Resistance_DF ["type"]=="condpara" ].sum()
Rcondpara = 1/ ((1/Resistance_DF["R"][ Resistance_DF ["type"]=="condpara" ]).sum())
Rconv = Resistance_DF["R"][ Resistance_DF ["type"]=="conv" ].sum()
Rtot = Rcondser + Rcondpara + Rconv

print "The value of the total resistance across the wall is: " + str(Rtot) + " °C/W"

#import numpy as np
#
#
#Rnames =np.array (["Rf","Rp1","Rp2","Rpc1","Rpc2","Rb","R1","R2"] )     #list of all resistances
#Rtype = np.array (["condser","condser","condser","condpara","condpara","condpara","conv","conv"])
#R_h = np.array ([None, None, None, None, None, None, 10.0, 20.0])
#R_k = np.array ([0.026, 0.22, 0.22, 0.22, 0.22, 0.72, None, None])
#Rlength = np.array([0.03, 0.02, 0.02, 0.16, 0.16, 0.16, None, None])
#Rarea = np.array ([0.25, 0.25, 0.25, 0.015, 0.015, 0.22, 0.25, 0.25])
#
#Rvalues = np.array (np.zeros(8))
#Rvalues [Rtype == "condser"] = Rlength[Rtype=="condser"]/(R_k[Rtype=="condser"]*Rarea[Rtype=="condser"])
#Rvalues [Rtype == "condpara"] = Rlength[Rtype=="condpara"]/(R_k[Rtype=="condpara"]*Rarea[Rtype=="condpara"])
#Rvalues [Rtype == "conv"] = 1/(R_h[Rtype=="conv"]*Rarea[Rtype=="conv"])
#
#Rparainv = np.array (np.zeros(8))
#Rparainv [Rtype == "condpara"] = 1/Rvalues [Rtype == "condpara"]
#Rcondpara = 1/Rparainv [Rtype == "condpara"].sum()
#
#Rcondser = Rvalues [Rtype == "condser"].sum()
#Rconv = Rvalues [Rtype == "conv"].sum()
#Rtot = Rcondser + Rcondpara + Rconv
#
#
#print "The value of the total resistance across the wall is: " + str(Rtot) + " °C/W"