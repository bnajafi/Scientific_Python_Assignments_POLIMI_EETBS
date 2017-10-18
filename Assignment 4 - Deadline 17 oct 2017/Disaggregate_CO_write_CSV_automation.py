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

from nilmtk import *
from nilmtk import DataSet, TimeFrame, MeterGroup, HDFDataStore
from nilmtk.disaggregate import combinatorial_optimisation, fhmm_exact
from nilmtk.utils import print_dict
from nilmtk.metrics import f1_score
import nilmtk.stats as bstats


import warnings
warnings.filterwarnings("ignore")

import os    

def get_files_by_file_size(dirname, reverse=True):
    """ Return list of file paths in directory sorted by file size """

    # Get list of files
    filepaths = []
    for basename in os.listdir(dirname):
        filename = os.path.join(dirname, basename)
        if os.path.isfile(filename):
            filepaths.append(filename)

    # Re-populate list with filename, size tuples
    for i in xrange(len(filepaths)):
        filepaths[i] = (filepaths[i], os.path.getsize(filepaths[i]))

    # Sort list by file size
    # If reverse=True sort from largest to smallest
    # If reverse=False sort from smallest to largest
    filepaths.sort(key=lambda filename: filename[1], reverse=reverse)

    # Re-populate list with just filenames
    for i in xrange(len(filepaths)):
        filepaths[i] = filepaths[i][0]

    return filepaths
'''search for a string in between 2 string'''
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
def builds_dictionary(house_list_dir):
    buildings_list = []
    buildings = {}
    list_of_buildings = pd.read_csv(join(house_list_dir,'house_list_latest.csv'))
    for index,row in list_of_buildings.iterrows():
        buildings = {
                     "dataid":int(row['dataid']),
                    "start_period":row['date_enrolled'],
                    "end_period":row['date_withdrawn']}
        buildings_list.append(buildings)
    return buildings_list

def select_top_meters(train_elec):
    
    top_5_train_elec = train_elec.submeters().select_top_k(k=4)
    '''---------SELECTING TOP K AND AIR CONDITIONER--------'''
    
    applist = []
    appliance = top_5_train_elec.all_meters()
    
    for app in appliance:
        string = str(app)
        device_name = find_between(string,"type='","', instance")
        applist.append(device_name)
    new_list = []
    new_list = list(set(applist))
    if 'air conditioner' in new_list:
        top_5_train_elec = train_elec.submeters().select_using_appliances(type=new_list)
    else:
        new_list.insert(0,'air conditioner')
        try:
            top_5_train_elec = train_elec.submeters().select_using_appliances(type=new_list)
        except KeyError:
            top_5_train_elec = []
            print "\nNo Air conditioner here"
    return top_5_train_elec

house_list_dir = 'C:/Users/MANOJ/Dropbox/Manoj Thesis/NILMTK DataSets/Pecan Street (Wiki Energy)/notebook/base disaggregation codes'
disagg_dir = 'D:/DOCUMENTS/thesis/PECAN-Dataport/nilmtk format data/Automated_download_2014 - whole year/disaggregated_short_training'

list_of_houses_downloaded = get_files_by_file_size('D:/DOCUMENTS/thesis/PECAN-Dataport/nilmtk format data/Automated_download_2014 - whole year')
buildings_dict = builds_dictionary(house_list_dir)


buildings_list = []
for build in buildings_dict:
    buildings_list.append(build['dataid'])

buildings_list = [9929,5545,5949,160,3504,1681]

for build in buildings_list:
    print'started'
    file_name_CO = "CO_{}1week_2014.csv".format(str(build))
    file_name_output = "CO_{}1week_2014.h5".format(str(build))
    file_name_gt = "gt_{}1week_2014.csv".format(str(build))
#    build = 1714
    if os.path.isfile(join(disagg_dir,file_name_CO)) ==False:
        
        b_2013 = "\\"+str(build)+"_2013"
        file_2013=[b for b in list_of_houses_downloaded if b_2013 in str(b)]
        b_2014 = "\\"+str(build)+"_2014"
        file_2014=[b for b in list_of_houses_downloaded if b_2014 in str(b)]
        
        if not file_2013 or not file_2014:
            print "house {} not in downloaded list".format(build)
            pass
        else:
            file_2013_size = int(os.path.getsize(file_2013[0]))/1000000
            file_2014_size = int(os.path.getsize(file_2014[0]))/1000000
            print "what ?"
            if file_2013_size >1.5 and file_2014_size >1.5:
                try:
                    we_train = DataSet(file_2013[0])
                    we_test = DataSet(file_2014[0])
                except AttributeError:
                    continue
                print "loaded successfully\n",file_2013[0],'\n',file_2014[0],'\n'
                we_train.set_window(start="07-03-2013")
                we_train.set_window(end="07-10-2013")
                train_elec = we_train.buildings[1].elec
                test_elec = we_test.buildings[1].elec
                print("Training range"+str(train_elec.get_timeframe()))
                print("Testing range"+str(test_elec.get_timeframe()))
                top_5_train_elec = select_top_meters(train_elec)
                if not top_5_train_elec:
                    
                    continue
                else:
                    from datetime import datetime
                    print("\nTraining started at "+str(datetime.now()))
                    
                    
                    # train
                    import time
                    start = time.time()
                    co = combinatorial_optimisation.CombinatorialOptimisation()
                    try:
                        co.train(top_5_train_elec, sample_period=60)
                    except (AttributeError,RuntimeError,ValueError): #the meters may contain nothing
                        continue
                    end = time.time()
                    print("Runtime =", end-start, "seconds.")
                    
                    print("Disaggregation started at "+str(datetime.now()))
                    start_disag_time = time.time()
                    
                    pred = {}
                    gt = {}
                    
                    try:
                        
                        for i, chunk in enumerate(test_elec.mains().load(sample_period=60)):
                            chunk_drop_na = chunk.dropna()
                            pred[i] = co.disaggregate_chunk(chunk_drop_na)
                            gt[i] = {}
                           
                            for meter in test_elec.submeters().meters:
                                gt[i][meter] = meter.load(sample_period=60).next()     
                            gt[i] = pd.DataFrame({k:v.squeeze() for k,v in gt[i].iteritems()},index=gt[i].values()[0].index).dropna()
#                        disagg_output = pd.HDFStore(join(disagg_dir,file_name_output),mode='w')
##                       disagg_output['Prediction'] = pred[0] ###### check this i have asked the question in github
#                        disagg_output.append('df', pred[0], data_columns=['Prediction'], index=False)
#                        disagg_output.put('df/image',pd.DataFrame(pred,index=pred[0].index))
#                        disagg_output.close()
                    except AttributeError:
                        print "Test and train data applaince mismatch"
                        continue
                    end_disag_time = time.time()
                    print("Disaggregation time =", end_disag_time-start_disag_time, "seconds.") 
                        
                    # If everything can fit in memory
                    gt_overall = pd.concat(gt)
                    gt_overall.index = gt_overall.index.droplevel()
                    pred_overall = pd.concat(pred)
                    pred_overall.index = pred_overall.index.droplevel()
                    ''' This pred_overall is the predicted individual consumptions of the test data'''
                    
                    
                    
                    #gt_overall.plot();
                    #pred_overall.plot();
                    try:
                        # Having the same order of columns
                        gt_overall = gt_overall[pred_overall.columns]
                        pred_overall = pred_overall.ix[gt_overall.index]
                        gt_overall = gt_overall.ix[pred_overall.index]
                    except KeyError:
                        continue
                
#                from sklearn.metrics import mean_squared_error
#                
#                rmse={}
#                for col in pred_overall.columns:
#                    rmse[col] = np.sqrt(mean_squared_error(gt_overall[col], pred_overall[col]))
                
                #pd.Series(rmse).plot(kind="barh")
                

                
                    pred_overall.to_csv(join(disagg_dir,file_name_CO),sep=',')
#                    gt_overall.to_csv(join(disagg_dir,file_name_gt),sep=',')
                
                


        

##we_train.set_window(start="04-01-2013")
##we_train.set_window(end="07-30-2013")
####
##we_test.set_window(start="04-01-2014")
#
#
##train_elec.plot()
#
#
#
## Create convenient labels
##fraction = train_elec.submeters().fraction_per_meter().dropna()
##labels = train_elec.get_labels(fraction.index)
##plt.figure(figsize=(8,8))
##fraction.plot(kind='pie', labels=labels);
#
##top_5_train_elec = train_elec.submeters().select_top_k(k=5)
#
#print(train_elec)
#
##top_5_train_elec = train_elec.submeters().select_using_appliances(type=['air conditioner','dish washer','spin dryer','electric furnace','waste disposal unit','microwave','washing machine','oven'])
#
#'''-------------------------------------------------------'''
#
#from datetime import datetime
#print("\nTraining started at "+str(datetime.now()))
#
#
## train
#import time
#start = time.time()
#co = combinatorial_optimisation.CombinatorialOptimisation()
#co.train(top_5_train_elec, sample_period=60)
#end = time.time()
#print("Runtime =", end-start, "seconds.")
#
#print("Disaggregation started at "+str(datetime.now()))
#start_disag_time = time.time()
#
#pred = {}
#gt = {}
#
#for i, chunk in enumerate(test_elec.mains().load(sample_period=60)):
#    chunk_drop_na = chunk.dropna()
#    pred[i] = co.disaggregate_chunk(chunk_drop_na)
#    gt[i] = {}
#    
#    for meter in test_elec.submeters().meters:
#        gt[i][meter] = meter.load(sample_period=60).next()     
#    gt[i] = pd.DataFrame({k:v.squeeze() for k,v in gt[i].iteritems()},index=gt[i].values()[0].index).dropna()
#
#end_disag_time = time.time()
#print("Disaggregation time =", end_disag_time-start_disag_time, "seconds.") 
#    
## If everything can fit in memory
#gt_overall = pd.concat(gt)
#gt_overall.index = gt_overall.index.droplevel()
#pred_overall = pd.concat(pred)
#pred_overall.index = pred_overall.index.droplevel()
#''' This pred_overall is the predicted individual consumptions of the test data'''
#
## Having the same order of columns
#gt_overall = gt_overall[pred_overall.columns]
#
##gt_overall.plot();
##pred_overall.plot();
#
#pred_overall = pred_overall.ix[gt_overall.index]
#gt_overall = gt_overall.ix[pred_overall.index]
#
#from sklearn.metrics import mean_squared_error
#
#rmse={}
#for col in pred_overall.columns:
#    rmse[col] = np.sqrt(mean_squared_error(gt_overall[col], pred_overall[col]))
#
##pd.Series(rmse).plot(kind="barh")
#
#
#pred_overall.to_csv(join(disagg_dir,"CO_2335_2014April-November_top3.csv"),sep=',')
#gt_overall.to_csv(join(disagg_dir,"gt_CO_2335_2014April-November_top3.csv"),sep=',')

'''
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
'''

"""
f1.index = disag_elec.get_labels(f1.index)
f1.plot(kind='bar')
plt.xlabel('appliance');
plt.ylabel('f-score');

disag.store.close()

"""
