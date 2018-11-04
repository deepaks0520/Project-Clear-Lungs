import os 
import pandas as pd
import matplotlib.pyplot as plt
import tsfresh.feature_extraction.feature_calculators as tf
from tsfresh import extract_features
import openpyxl
import glob

def main():
    dirname = os.path.realpath('.')
    excelF = dirname + '\\Summary.xlsx'
    myworkbook = openpyxl.load_workbook(excelF)
    worksheet = myworkbook['SummaryPatients']

   

    file = 1
    for filename in glob.glob(dirname + "\*.txt"):  
  
        data = open(filename, 'r')

        totalData = {}
        
        time = []
        totalForceL = []
        totalForceR = []
        id = []
        for line in data:
            tempForce = line.split()
            id.append(1)
            time.append(float(tempForce[0]))
            totalForceL.append(float(tempForce[17]))
            totalForceR.append(float(tempForce[18]))

        totalData["id"] = id
        totalData["time"] = time
        totalData["totalForceL"] = totalForceL
        totalData["totalForceR"] = totalForceR

        dataPandas = pd.DataFrame.from_dict(totalData)

        extracted_features = {}
        #extract_featuresL = extract_features(dataPandas, column_id="id", column_kind=None, column_value=None)

        worksheet ['A' + str(file+1)] = file
        if 'Pt' in filename:
            worksheet['B' + str(file+1)] = 1
        else:
            worksheet['B' + str(file+1)] = 0

        worksheet ['C' + str(file+1)] = tf.abs_energy(totalData["totalForceL"])
        worksheet ['D' + str(file+1)] = tf.abs_energy(totalData["totalForceR"])
        worksheet ['E' + str(file+1)] = tf.kurtosis(totalData["totalForceL"])
        worksheet ['F' + str(file+1)] = tf.kurtosis(totalData["totalForceR"])
        worksheet ['G' + str(file+1)] = tf.skewness(totalData["totalForceL"])
        worksheet ['H' + str(file+1)] = tf.skewness(totalData["totalForceR"])
        worksheet ['I' + str(file+1)] = tf.median(totalData["totalForceL"])
        worksheet ['J' + str(file+1)] = tf.median(totalData["totalForceR"])
        worksheet ['K' + str(file+1)] = tf.mean(totalData["totalForceL"])
        worksheet ['L' + str(file+1)] = tf.mean(totalData["totalForceR"])
        worksheet ['M' + str(file+1)] = tf.variance(totalData["totalForceL"])
        worksheet ['N' + str(file+1)] = tf.variance(totalData["totalForceR"])

        temp = tf.fft_aggregated(totalData["totalForceL"], [{"aggtype": "centroid"}, {"aggtype": "variance"}, {"aggtype":"skew"}, {"aggtype":"kurtosis"}])
        int = 0
        for list in temp:
            if int == 0:
                worksheet ['O' + str(file+1)] = list[1]
            if int == 1:
                worksheet ['P' + str(file+1)] = list[1]
            if int == 2:
                worksheet ['Q' + str(file+1)] = list[1]
            if int == 3:
                worksheet ['R' + str(file+1)] = list[1]
            int += 1
        
        temp2 = tf.fft_aggregated(totalData["totalForceR"], [{"aggtype": "centroid"}, {"aggtype": "variance"}, {"aggtype":"skew"}, {"aggtype":"kurtosis"}])
        int = 0
        for list in temp2:
            if int == 0:
                worksheet ['S' + str(file+1)] = list[1]
            if int == 1:
                worksheet ['T' + str(file+1)] = list[1]
            if int == 2:
                worksheet ['U' + str(file+1)] = list[1]
            if int == 3:
                worksheet ['V' + str(file+1)] = list[1]
            int += 1

        file += 1

    myworkbook.save(excelF)

    
if __name__ == "__main__":
    main()