# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:37:43 2017

@author: behzad
"""

import numpy as np
import pandas as pd
from os.path import join

from pylab import rcParams
import matplotlib.pyplot as plt#%matplotlib inline
rcParams['figure.figsize'] = (16, 8)

import nilmtk
from nilmtk import DataSet, TimeFrame, MeterGroup, HDFDataStore
from nilmtk.disaggregate import CombinatorialOptimisation
from nilmtk.utils import print_dict
from nilmtk.metrics import f1_score
import nilmtk.stats as bstats

import warnings
warnings.filterwarnings("ignore")



data_dir = 'C:/Users/MANOJ/Dropbox/Manoj Thesis/NILMTK DataSets/Pecan Street (Wiki Energy)/notebook'
we = DataSet(join(data_dir, '6636_july_2013.h5'))
print('loaded ' + str(len(we.buildings)) + ' buildings')

elec = we.buildings[1].elec
elec.get_timeframe()


we.store.window = elec.get_timeframe()

building_number = 1
elec = we.buildings[building_number].elec

elec.plot();

fraction = elec.submeters().fraction_per_meter().dropna()


# Create convenient labels
labels = elec.get_labels(fraction.index)
plt.figure(figsize=(8,8))
fraction.plot(kind='pie', labels=labels);


# Train
co = CombinatorialOptimisation()
co.train(elec)


elec.mains().plot()


disag_filename = join(data_dir, 'pecan_6636_July-disag.h5')
output = HDFDataStore(disag_filename, 'w')
co.disaggregate(elec.mains(), output)
output.close()

disag = DataSet(disag_filename)
disag_elec = disag.buildings[building_number].elec
disag_elec.plot()
plt.xlabel("Time")
disag.store.close()


disag = DataSet(disag_filename)
disag_elec = disag.buildings[building_number].elec
#disag_elec.power_series().next()

f1 = f1_score(disag_elec, elec)
"""
f1.index = disag_elec.get_labels(f1.index)
f1.plot(kind='bar')
plt.xlabel('appliance');
plt.ylabel('f-score');

disag.store.close()

"""
