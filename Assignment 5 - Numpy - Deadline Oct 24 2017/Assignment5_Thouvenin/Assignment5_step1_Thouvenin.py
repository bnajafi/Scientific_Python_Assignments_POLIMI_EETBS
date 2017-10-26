# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 18:18:27 2017
@author: edoua
"""
#assignment 2

import numpy as np


Rnames =np.array (["Rf","Rp1","Rp2","Rpc1","Rpc2","Rb","R1","R2"] )     #list of all resistances
Rtype = np.array (["condser","condser","condser","condpara","condpara","condpara","conv","conv"])
R_h = np.array ([None, None, None, None, None, None, 10.0, 20.0])
R_k = np.array ([0.026, 0.22, 0.22, 0.22, 0.22, 0.72, None, None])
Rlength = np.array([0.03, 0.02, 0.02, 0.16, 0.16, 0.16, None, None])
Rarea = np.array ([0.25, 0.25, 0.25, 0.015, 0.015, 0.22, 0.25, 0.25])

Rvalues = np.array (np.zeros(8))
Rvalues [Rtype == "condser"] = Rlength[Rtype=="condser"]/(R_k[Rtype=="condser"]*Rarea[Rtype=="condser"])
Rvalues [Rtype == "condpara"] = Rlength[Rtype=="condpara"]/(R_k[Rtype=="condpara"]*Rarea[Rtype=="condpara"])
Rvalues [Rtype == "conv"] = 1/(R_h[Rtype=="conv"]*Rarea[Rtype=="conv"])

Rparainv = np.array (np.zeros(8))
Rparainv [Rtype == "condpara"] = 1/Rvalues [Rtype == "condpara"]
Rcondpara = 1/Rparainv [Rtype == "condpara"].sum()

Rcondser = Rvalues [Rtype == "condser"].sum()
Rconv = Rvalues [Rtype == "conv"].sum()
Rtot = Rcondser + Rcondpara + Rconv


print "The value of the total resistance across the wall is: " + str(Rtot) + " °C/W"