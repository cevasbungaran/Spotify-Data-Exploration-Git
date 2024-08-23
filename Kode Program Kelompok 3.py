# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import re
from sklearn import preprocessing
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn import metrics

data = pd.DataFrame()

for i in range(1960,2005):
    dataname = str(i) + ".xlsx"
    df = pd.read_excel(dataname)
    df["year"] = i
    data = data.append(df)
    
for i in range(2006,2023):
    dataname = str(i) + ".xlsx"
    df = pd.read_excel(dataname)
    df["year"] = i
    data = data.append(df)
    
data = data.reset_index(drop=True)

# atribut dan tipe datanya
data.dtypes

# cari data yang duplicate
data.duplicated().sum()

# Pertanyaan No. 1
# by genre
genre = []
genreDict = {}
for i, rowArtists in data.iterrows():
    artistsList = json.loads(rowArtists['artists'])
    for artists in artistsList:
        genreList = eval(artists['genre'])
        for itemGenre in genreList:
            #print(itemGenre)
            if not itemGenre in genreDict.keys():
                genreDict[itemGenre]=[i]
            else:
                genreDict[itemGenre].append(i)

# mengelompokkan by genre
dataTotal = pd.DataFrame(data.groupby('year')['uri'].count())
dataTotal['proporsi'] = dataTotal['uri']/dataTotal['uri'].sum()
normalized_dataTotal = preprocessing.normalize([dataTotal['proporsi']])

thresholdLineplot = normalized_dataTotal.mean()
rata2 = data['popularity'].mean()
# genre jazz
jazz = re.compile(r'.*jazz.*')
dataJazz = pd.DataFrame()
for key in genreDict.keys():
    if jazz.match(key):
        dataJazz = dataJazz.append(data.iloc[genreDict[key]])
        dataJazz = dataJazz.reset_index(drop=True)
        
# genre electronic, edm, dsb
electronic = re.compile(r'.*electronic.*|.*edm.*|.*electric.*|.*electra.*|.*electro.*|.*techno.*|.*house.*')
dataElectronic = pd.DataFrame()
for key in genreDict.keys():
    if electronic.match(key):
        dataElectronic = dataElectronic.append(data.iloc[genreDict[key]])
        dataElectronic = dataElectronic.reset_index(drop=True)

# genre rock
rock = re.compile(r'.*rock.*|.*punk.*|.*folk.*|.*grunge.*|.*goth.*')
dataRock = pd.DataFrame()
for key in genreDict.keys():
    if rock.match(key):
        dataRock = dataRock.append(data.iloc[genreDict[key]])
        dataRock = dataRock.reset_index(drop=True)

# genre pop
pop = re.compile(r'.*pop.*')
dataPop = pd.DataFrame()
for key in genreDict.keys():
    if pop.match(key):
        dataPop = dataPop.append(data.iloc[genreDict[key]])
        dataPop = dataPop.reset_index(drop=True)

# genre hip hop = rap
hipHop = re.compile(r'.*hip hop.*|.*rap.*')
dataHipHop = pd.DataFrame()
for key in genreDict.keys():
    if hipHop.match(key):
        dataHipHop = dataHipHop.append(data.iloc[genreDict[key]])
        dataHipHop = dataHipHop.reset_index(drop=True)

# genre blues
blues = re.compile(r'.*blues.*|.*r&b.*|.*rhythm.*')
dataBlues = pd.DataFrame()
for key in genreDict.keys():
    if blues.match(key):
        dataBlues = dataBlues.append(data.iloc[genreDict[key]])
        dataBlues = dataBlues.reset_index(drop=True)

# genre indie, alternative 
alternative = re.compile(r'.*alternative.*|.*indie.*|.*punk.*')
dataAlternative = pd.DataFrame()
for key in genreDict.keys():
    if alternative.match(key):
        dataAlternative = dataAlternative.append(data.iloc[genreDict[key]])
        dataAlternative = dataAlternative.reset_index(drop=True)  
        
# genre country
country = re.compile(r'.*country.*|.*indie.*|.*cowboy.*|.*cowpunk.*')
dataCountry = pd.DataFrame()
for key in genreDict.keys():
    if country.match(key):
        dataCountry = dataCountry.append(data.iloc[genreDict[key]])
        dataCountry = dataCountry.reset_index(drop=True)
        
# genre classic
classic = re.compile(r'.*classic.*|.*opera.*|.*cowboy.*|.*cowpunk.*')
dataClassic = pd.DataFrame()
for key in genreDict.keys():
    if classic.match(key):
        dataClassic = dataClassic.append(data.iloc[genreDict[key]])
        dataClassic = dataClassic.reset_index(drop=True)

# genre metal
metal = re.compile(r'.*metal.*')
dataMetal = pd.DataFrame()
for key in genreDict.keys():
    if metal.match(key):
        dataMetal = dataMetal.append(data.iloc[genreDict[key]])
        dataMetal = dataMetal.reset_index(drop=True)
        
# Line Plot Genre Jazz
# seluruh lagu genre jazz
allJazz = pd.DataFrame(dataJazz.groupby('year')['uri'].count())
allJazz['proporsi'] = allJazz['uri']/dataTotal['uri']
allJazz['proporsi'].plot(kind='line', figsize=(20,5), marker='o', color='forestgreen')
plt.title('Lineplot seluruh lagu genre Jazz', fontsize=16)
plt.xlabel('Tahun', fontsize=14)
plt.ylabel('Proporsi', fontsize=14)
plt.axhline(y=thresholdLineplot, color='red', linestyle='--')
plt.show()

# hanya lagu populer genre jazz
JazzPopularity = pd.DataFrame(dataJazz.groupby('year')['popularity'].mean())
filterDataJazz = dataJazz[dataJazz['popularity'] > rata2]
dataPopularJazz = pd.DataFrame(filterDataJazz.groupby('year')['popularity'].count())
dataPopularJazz['proporsi'] = dataPopularJazz['popularity'] / dataTotal['uri']
dataPopularJazz['proporsi'].plot(kind='line', figsize=(20,5), marker='o', color='forestgreen')
plt.title('Lineplot lagu populer genre Electronic', fontsize=16)
plt.xlabel('Tahun', fontsize=14)
plt.ylabel('Proporsi', fontsize=14)
plt.axhline(y=thresholdLineplot, color='red', linestyle='--')
plt.show()

# Line Plot Genre Electronic
# seluruh lagu genre Electronic
allElectronic = pd.DataFrame(dataElectronic.groupby('year')['uri'].count())
allElectronic['proporsi'] = allElectronic['uri']/dataTotal['uri']
allElectronic['proporsi'].plot(kind='line', figsize=(20,5), marker='o', color='darkorange')
plt.title('Lineplot seluruh lagu genre Electronic', fontsize=16)
plt.xlabel('Tahun', fontsize=14)
plt.ylabel('Proporsi', fontsize=14)
plt.axhline(y=thresholdLineplot, color='red', linestyle='--')
plt.show()

# hanya lagu populer Electronic
ElectronicPopularity = pd.DataFrame(dataElectronic.groupby('year')['popularity'].mean())
filterDataElectronic = dataElectronic[dataElectronic['popularity'] > rata2]
dataPopularElectronic = pd.DataFrame(filterDataElectronic.groupby('year')['popularity'].count())
dataPopularElectronic['proporsi'] = dataPopularElectronic['popularity'] / dataTotal['uri']
dataPopularElectronic['proporsi'].plot(kind='line', figsize=(20,5), marker='o', color='darkorange')
plt.title('Lineplot lagu populer genre Electronic', fontsize=16)
plt.xlabel('Tahun', fontsize=14)
plt.ylabel('Proporsi', fontsize=14)
plt.axhline(y=thresholdLineplot, color='red', linestyle='--')
plt.show()

# Line Plot Genre Rock
# seluruh lagu Rock
allRock = pd.DataFrame(dataRock.groupby('year')['uri'].count())
allRock['proporsi'] = allRock['uri']/dataTotal['uri']
allRock['proporsi'].plot(kind='line', figsize=(20,5), marker='o', color='black')
plt.title('Lineplot seluruh lagu genre Rock', fontsize=16)
plt.xlabel('Tahun', fontsize=14)
plt.ylabel('Proporsi', fontsize=14)
plt.axhline(y=thresholdLineplot, color='red', linestyle='--')
plt.show()

# hanya lagu populer Rock
RockPopularity = pd.DataFrame(dataRock.groupby('year')['popularity'].mean())
filterDataRock = dataRock[dataRock['popularity'] > rata2]
dataPopularRock = pd.DataFrame(filterDataRock.groupby('year')['popularity'].count())
dataPopularRock['proporsi'] = dataPopularRock['popularity'] / dataTotal['uri']
dataPopularRock['proporsi'].plot(kind='line', figsize=(20,5), marker='o', color='black')
plt.title('Lineplot lagu populer genre Rock', fontsize=16)
plt.xlabel('Tahun', fontsize=14)
plt.ylabel('Proporsi', fontsize=14)
plt.axhline(y=thresholdLineplot, color='red', linestyle='--')
plt.show()

# Line Plot Genre Pop
# seluruh lagu Pop
allPop = pd.DataFrame(dataPop.groupby('year')['uri'].count())
allPop['proporsi'] = allPop['uri']/dataTotal['uri']
allPop['proporsi'].plot(kind='line', figsize=(20,5), marker='o', color='deeppink')
plt.title('Lineplot seluruh lagu genre Pop', fontsize=16)
plt.xlabel('Tahun', fontsize=14)
plt.ylabel('Proporsi', fontsize=14)
plt.axhline(y=thresholdLineplot, color='red', linestyle='--')
plt.show()

# hanya lagu populer Pop
PopPopularity = pd.DataFrame(dataPop.groupby('year')['popularity'].mean())
filterDataPop = dataPop[dataPop['popularity'] > rata2]
dataPopularPop = pd.DataFrame(filterDataPop.groupby('year')['popularity'].count())
dataPopularPop['proporsi'] = dataPopularPop['popularity'] / dataTotal['uri']
dataPopularPop['proporsi'].plot(kind='line', figsize=(20,5), marker='o', color='deeppink')
plt.title('Lineplot lagu populer genre Pop', fontsize=16)
plt.xlabel('Tahun', fontsize=14)
plt.ylabel('Proporsi', fontsize=14)
plt.axhline(y=thresholdLineplot, color='red', linestyle='--')
plt.show()

# Line Plot Genre Hip Hop
# seluruh lagu genre Hip Hop
allHipHop = pd.DataFrame(dataHipHop.groupby('year')['uri'].count())
allHipHop['proporsi'] = allHipHop['uri']/dataTotal['uri']
allHipHop['proporsi'].plot(kind='line', figsize=(20,5), marker='o', color='teal')
plt.title('Lineplot seluruh lagu genre Hip Hop', fontsize=16)
plt.xlabel('Tahun', fontsize=14)
plt.ylabel('Proporsi', fontsize=14)
plt.axhline(y=thresholdLineplot, color='red', linestyle='--')
plt.show()

# Hanya lagu populer genre Hip Hop
hiphopPopularity = pd.DataFrame(dataHipHop.groupby('year')['popularity'].mean())
filterDataHipHop = dataHipHop[dataHipHop['popularity'] > rata2]
dataPopularHipHop = pd.DataFrame(filterDataHipHop.groupby('year')['popularity'].count())
dataPopularHipHop['proporsi'] = dataPopularHipHop['popularity'] / dataTotal['uri']
dataPopularHipHop['proporsi'].plot(kind='line', figsize=(20,5), marker='o', color='teal')
plt.title('Lineplot lagu populer genre Hip hop', fontsize=16)
plt.xlabel('Tahun', fontsize=14)
plt.ylabel('Proporsi', fontsize=14)
plt.axhline(y=thresholdLineplot, color='red', linestyle='--')
plt.show()

# Line Plot Genre Blues
# seluruh lagu genre Blues
allBlues = pd.DataFrame(dataBlues.groupby('year')['uri'].count())
allBlues['proporsi'] = allBlues['uri']/dataTotal['uri']
allBlues['proporsi'].plot(kind='line', figsize=(20,5), marker = 'o', color='blue')
plt.title('Lineplot seluruh lagu genre Blues', fontsize=16)
plt.xlabel('Tahun', fontsize=14)
plt.ylabel('Proporsi', fontsize=14)
plt.axhline(y=thresholdLineplot, color='red', linestyle='--')
plt.show()

# Hanya lagu populer genre Blues
bluesPopularity = pd.DataFrame(dataBlues.groupby('year')['popularity'].mean())
filterDataBlues = dataBlues[dataBlues['popularity'] > rata2]
dataPopularBlues = pd.DataFrame(filterDataBlues.groupby('year')['popularity'].count())
dataPopularBlues['proporsi'] = dataPopularBlues['popularity'] / dataTotal['uri']
dataPopularBlues['proporsi'].plot(kind='line', figsize=(20,5), marker='o', color='blue')
plt.title('Lineplot lagu populer genre Electronic', fontsize=16)
plt.xlabel('Tahun', fontsize=14)
plt.ylabel('Proporsi', fontsize=14)
plt.axhline(y=thresholdLineplot, color='red', linestyle='--')
plt.show()

# Line Plot Genre Alternative
# seluruh lagu genre Alternative
allAlternative = pd.DataFrame(dataAlternative.groupby('year')['uri'].count())
allAlternative['proporsi'] = allAlternative['uri']/dataTotal['uri']
allAlternative['proporsi'].plot(kind='line', figsize=(20,5), marker='o', color='olive')
plt.title('Lineplot seluruh lagu genre Alternative', fontsize=16)
plt.xlabel('Tahun', fontsize=14)
plt.ylabel('Proporsi', fontsize=14)
plt.axhline(y=thresholdLineplot, color='red', linestyle='--')
plt.show()

# Hanya lagu populer genre Alternative
alternativePopularity = pd.DataFrame(dataAlternative.groupby('year')['popularity'].mean())
filterDataAlternative = dataAlternative[dataAlternative['popularity'] > rata2]
dataPopularAlternative = pd.DataFrame(filterDataAlternative.groupby('year')['popularity'].count())
dataPopularAlternative['proporsi'] = dataPopularAlternative['popularity'] / dataTotal['uri']
dataPopularAlternative['proporsi'].plot(kind='line', figsize=(20,5), marker='o', color='olive')
plt.title('Lineplot lagu populer genre Alternative', fontsize=16)
plt.xlabel('Tahun', fontsize=14)
plt.ylabel('Proporsi', fontsize=14)
plt.axhline(y=thresholdLineplot, color='red', linestyle='--')
plt.show()

# Line Plot Genre Country
# seluruh lagu genre Country
allCountry = pd.DataFrame(dataCountry.groupby('year')['uri'].count())
allCountry['proporsi'] = allCountry['uri']/dataTotal['uri']
allCountry['proporsi'].plot(kind='line', figsize=(20,5), marker='o', color='purple')
plt.title('Lineplot seluruh lagu genre Country')
plt.xlabel('Tahun')
plt.ylabel('Proporsi')
plt.axhline(y=thresholdLineplot, color='red', linestyle='--')
plt.show()

# Hanya lagu populer genre Country
countryPopularity = pd.DataFrame(dataCountry.groupby('year')['popularity'].mean())
filterDataCountry = dataCountry[dataCountry['popularity'] > rata2]
dataPopularCountry = pd.DataFrame(filterDataCountry.groupby('year')['popularity'].count())
dataPopularCountry['proporsi'] = dataPopularCountry['popularity'] / dataTotal['uri']
dataPopularCountry['proporsi'].plot(kind='line', figsize=(20,5), marker='o', color='purple')
plt.title('Lineplot hanya lagu populer genre Country')
plt.xlabel('Tahun')
plt.ylabel('Proporsi')
plt.axhline(y=thresholdLineplot, color='red', linestyle='--')
plt.show()

# Line Plot Genre Classic
# seluruh lagu Genre Classic
allClassic = pd.DataFrame(dataClassic.groupby('year')['uri'].count())
allClassic['proporsi'] = allClassic['uri']/dataTotal['uri']
allClassic['proporsi'].plot(kind='line', figsize=(20,5), marker='o', color='dimgray')
plt.title('Lineplot seluruh lagu genre Classic', fontsize=16)
plt.xlabel('Tahun', fontsize=14)
plt.ylabel('Proporsi', fontsize=14)
plt.axhline(y=thresholdLineplot, color='red', linestyle='--')
plt.show()

# Hanya Lagu Populer Genre Classic
classicPopularity = pd.DataFrame(dataClassic.groupby('year')['popularity'].mean())
filterDataClassic = dataClassic[dataClassic['popularity'] > rata2]
dataPopularClassic = pd.DataFrame(filterDataClassic.groupby('year')['popularity'].count())
dataPopularClassic['proporsi'] = dataPopularClassic['popularity'] / dataTotal['uri']
dataPopularClassic['proporsi'].plot(kind='line', figsize=(20,5), marker='o', color='dimgray')
plt.title('Lineplot lagu populer genre Classic', fontsize=16)
plt.xlabel('Tahun', fontsize=14)
plt.ylabel('Proporsi', fontsize=14)
plt.axhline(y=thresholdLineplot, color='red', linestyle='--')
plt.show()

# Line Plot Genre Metal
# Semua lagu Genre Metal
allMetal = pd.DataFrame(dataMetal.groupby('year')['uri'].count())
allMetal['proporsi'] = allMetal['uri']/dataTotal['uri']
allMetal['proporsi'].plot(kind='line', figsize=(20,5), marker='o', color='brown')
plt.title('Lineplot semua lagu genre Metal', fontsize=16)
plt.xlabel('Tahun', fontsize=14)
plt.ylabel('Proporsi', fontsize=14)
plt.axhline(y=thresholdLineplot, color='red', linestyle='--')
plt.show()

# Hanya Lagu Populer Genre Metal
metalPopularity = pd.DataFrame(dataMetal.groupby('year')['popularity'].mean())
filterDataMetal = dataMetal[dataMetal['popularity'] > rata2]
dataPopularMetal = pd.DataFrame(filterDataMetal.groupby('year')['popularity'].count())
dataPopularMetal['proporsi'] = dataPopularMetal['popularity'] / dataTotal['uri']
dataPopularMetal['proporsi'].plot(kind='line', figsize=(20,5), marker='o', color='brown')
plt.title('Lineplot hanya lagu populer genre Metal', fontsize=16)
plt.xlabel('Tahun', fontsize=14)
plt.ylabel('Proporsi', fontsize=14)
plt.axhline(y=thresholdLineplot, color='red', linestyle='--')
plt.show()


#boxplot
fig, ax = plt.subplots(figsize=(8, 4))
ax.boxplot([dataJazz['popularity'], dataElectronic['popularity'], dataRock['popularity'], dataPop['popularity'], dataHipHop['popularity'],
                       dataBlues['popularity'], dataAlternative['popularity'], dataCountry['popularity'], dataClassic['popularity']])
ax.set_title('Boxplot Semua Genre')
ax.set_xticklabels(['Jazz', 'Electronic', 'Rock', 'Pop', 'HipHop', 'Blues', 'Alternative', 'Country', 'Classic'])
ax.set_ylabel('Value')
plt.show()

# Pertanyaan No. 2
rock = dataRock[(dataRock['year'] > 1960) & (dataRock['year'] < 2004)]
rock['popularity'] = rock['popularity']/rock['popularity'].max()
rockPopuler = filterDataRock[(filterDataRock['year'] >= 1963) & (filterDataRock['year'] <= 1997)] 


filterDataRock = dataRock[dataRock['popularity'] > rata2]
filterDataRockUnPop = dataRock[dataRock['popularity'] < rata2]
data = data.reset_index(drop=True)

fig, ax = plt.subplots(figsize=(8, 4))
ax.boxplot([filterDataRock['danceability'], filterDataRockUnPop['danceability']])
ax.set_title('Sebaran Danceability Seluruh Lagu Rock', fontsize=16)
ax.set_xticklabels(['Rock Populer', 'Rock Tidak Populer'], fontsize=14)
ax.set_ylabel('Danceability', fontsize=14)
plt.show()

fig, ax = plt.subplots(figsize=(8, 4))
ax.boxplot([filterDataRock['explicit'], filterDataRockUnPop['explicit']])
ax.set_title('Sebaran Explicit Seluruh Lagu Rock', fontsize=16)
ax.set_xticklabels(['Rock Populer', 'Rock Tidak Populer'], fontsize=14)
ax.set_ylabel('Explicit', fontsize=14)
plt.show()

fig, ax = plt.subplots(figsize=(8, 4))
ax.boxplot([filterDataRock['energy'], filterDataRockUnPop['energy']])
ax.set_title('Sebaran Energy Seluruh Lagu Rock', fontsize=16)
ax.set_xticklabels(['Rock Populer', 'Rock Tidak Populer'], fontsize=14)
ax.set_ylabel('Energy', fontsize=14)
plt.show()

fig, ax = plt.subplots(figsize=(8, 4))
ax.boxplot([filterDataRock['loudness'], filterDataRockUnPop['loudness']])
ax.set_title('Sebaran Loudness Seluruh Lagu Rock', fontsize=16)
ax.set_xticklabels(['Rock Populer', 'Rock Tidak Populer'], fontsize=14)
ax.set_ylabel('Loudness', fontsize=14)
plt.show()

fig, ax = plt.subplots(figsize=(8, 4))
ax.boxplot([filterDataRock['key'], filterDataRockUnPop['key']])
ax.set_title('Sebaran Key Seluruh Lagu Rock', fontsize=16)
ax.set_xticklabels(['Rock Populer', 'Rock Tidak Populer'], fontsize=14)
ax.set_ylabel('Key', fontsize=14)
plt.show()

fig, ax = plt.subplots(figsize=(8, 4))
ax.boxplot([filterDataRock['mode'], filterDataRockUnPop['mode']])
ax.set_title('Sebaran Mode Seluruh Lagu Rock', fontsize=16)
ax.set_xticklabels(['Rock Populer', 'Rock Tidak Populer'], fontsize=14)
ax.set_ylabel('Mode', fontsize=14)
plt.show()

fig, ax = plt.subplots(figsize=(8, 4))
ax.boxplot([filterDataRock['instrumentalness'], filterDataRockUnPop['instrumentalness']])
ax.set_title('Sebaran Instrumentalness Seluruh Lagu Rock', fontsize=16)
ax.set_xticklabels(['Rock Populer', 'Rock Tidak Populer'], fontsize=14)
ax.set_ylabel('Instrumentalness', fontsize=14)
plt.show()

fig, ax = plt.subplots(figsize=(8, 4))
ax.boxplot([filterDataRock['liveness'], filterDataRockUnPop['liveness']])
ax.set_title('Sebaran Liveness Seluruh Lagu Rock', fontsize=16)
ax.set_xticklabels(['Rock Populer', 'Rock Tidak Populer'], fontsize=14)
ax.set_ylabel('Liveness', fontsize=14)
plt.show()

fig, ax = plt.subplots(figsize=(8, 4))
ax.boxplot([filterDataRock['valence'], filterDataRockUnPop['valence']])
ax.set_title('Sebaran Valence Seluruh Lagu Rock', fontsize=16)
ax.set_xticklabels(['Rock Populer', 'Rock Tidak Populer'], fontsize=14)
ax.set_ylabel('Valence', fontsize=14)
plt.show()

fig, ax = plt.subplots(figsize=(8, 4))
ax.boxplot([filterDataRock['tempo'], filterDataRockUnPop['tempo']])
ax.set_title('Sebaran Tempo Seluruh Lagu Rock', fontsize=16)
ax.set_xticklabels(['Rock Populer', 'Rock Tidak Populer'], fontsize=14)
ax.set_ylabel('Tempo', fontsize=14)
plt.show()

fig, ax = plt.subplots(figsize=(8, 4))
ax.boxplot([filterDataRock['time_signature'], filterDataRockUnPop['time_signature']])
ax.set_title('Sebaran Time Signature Seluruh Lagu Rock', fontsize=16)
ax.set_xticklabels(['Rock Populer', 'Rock Tidak Populer'], fontsize=14)
ax.set_ylabel('Time Signature', fontsize=14)
plt.show()

fig, ax = plt.subplots(figsize=(8, 4))
ax.boxplot([filterDataRock['year'], filterDataRockUnPop['year']])
ax.set_title('Sebaran Year Seluruh Lagu Rock', fontsize=16)
ax.set_xticklabels(['Rock Populer', 'Rock Tidak Populer'], fontsize=14)
ax.set_ylabel('Year', fontsize=14)
plt.show()

fig, ax = plt.subplots(figsize=(8, 4))
ax.boxplot([filterDataRock['duration_ms'], filterDataRockUnPop['duration_ms']])
ax.set_title('Sebaran Duration_ms Seluruh Lagu Rock', fontsize=16)
ax.set_xticklabels(['Rock Populer', 'Rock Tidak Populer'], fontsize=14)
ax.set_ylabel('Duration_ms', fontsize=14)
plt.show()

#korelasi popularity genre rock
rockCorr = rock.corr()
rockPopCorr = rockPopuler.corr()['popularity']

sns.regplot(x="valence", y="danceability", data=rock, scatter_kws={"s": 1}, line_kws=dict(color= "red"), ci=None)
plt.xlabel('valence')
plt.ylabel('dancebility')
plt.title('Scatter plot valence x dancebility genre rock')
plt.show()

sns.regplot(x="energy", y="loudness", data=rock, scatter_kws={"s": 1}, line_kws=dict(color= "red"), ci=None)
plt.xlabel('energy')
plt.ylabel('loudness')
plt.title('Scatter plot energy x loudness genre rock')
plt.show()

#lagu populer
sns.regplot(x="popularity", y="danceability", data=rockPopuler, scatter_kws={"s": 1}, line_kws=dict(color= "red"), ci=None)
plt.xlabel('popularity')
plt.ylabel('dancebility')
plt.title('Scatter plot lagu populer valence x dancebility genre rock')
plt.show()

sns.regplot(x="popularity", y="liveness", data=rockPopuler, scatter_kws={"s": 1}, line_kws=dict(color= "red"), ci=None)
plt.xlabel('popularity')
plt.ylabel('liveness')
plt.title('Scatter plot lagu populer energy x loudness genre rock')
plt.show()

# Pertanyaan No.3 
# heatmap correlation antar atribut
correlation = data.corr()
f,ax = plt.subplots(figsize=(10,10))
sns.heatmap(correlation, annot = True, linewidths = 0.4, ax=ax, vmin = -1, vmax =1)

# Contoh korelasi
data1975 = data[data['year'] == 1975]
data2006 = data[data['year'] == 2006]
correlation1975 = data1975.corr()
correlation2006 = data1975.corr()

# Scatterplot Danceability x Valence 
for i in range(1960,2005):
    sns.regplot(x="danceability", y="valence", data=data[data['year']==i], scatter_kws={"s": 1}, line_kws=dict(color= "red"), ci=None)
    plt.title("Scatterplot Danceability x Valance" + str(i))
    plt.show()

for i in range(2006,2023):
    sns.regplot(x="danceability", y="valence", data=data[data['year']==i], scatter_kws={"s": 1}, line_kws=dict(color= "red"), ci=None)
    plt.title("Scatterplot Danceability x Valance" + str(i))
    plt.show()
    
# Scatterplot Danceability x Loudness 
for i in range(1960,2005):
    sns.regplot(x="danceability", y="loudness", data=data[data['year']==i], scatter_kws={"s": 1}, line_kws=dict(color= "red"), ci=None)
    plt.title("Scatterplot Danceability x Loudness" + str(i))
    plt.show()

for i in range(2006,2023):
    sns.regplot(x="danceability", y="loudness", data=data[data['year']==i], scatter_kws={"s": 1}, line_kws=dict(color= "red"), ci=None)
    plt.title("Scatterplot Danceability x Loudness" + str(i))
    plt.show()

# Scatterplot Danceability x Energy 
for i in range(1960,2005):
    sns.regplot(x="danceability", y="energy", data=data[data['year']==i], scatter_kws={"s": 1}, line_kws=dict(color= "red"), ci=None)
    plt.title("Scatterplot Danceability x Energy" + str(i))
    plt.show()

for i in range(2006,2023):
    sns.regplot(x="danceability", y="energy", data=data[data['year']==i], scatter_kws={"s": 1}, line_kws=dict(color= "red"), ci=None)
    plt.title("Scatterplot Danceability x Energy" + str(i))
    plt.show()

# Box Plot Danceability x Time Signature
df.boxplot(column=["danceability"], by="time_signature")

#info tambahan
sns.regplot(x="loudness", y="energy", data=data, scatter_kws={"s": 1}, line_kws=dict(color= "red"), ci=None)
plt.title("Scatterplot Loudness x Energy")
plt.show()

sns.regplot(x="speechiness", y="instrumentalness", data=data, scatter_kws={"s": 1}, line_kws=dict(color= "red"), ci=None)
plt.title("Scatterplot Speechiness x Instrumentalness")
plt.show()

#Pertanyaan Machine Learning
dataHipHopJaya = data[(data['year'] >= 1998) & (data['year'] <= 2006)]
corrLoudness = data.corr()['danceability']
dataHipHopJaya['speechiness'].mean()
dataHipHopJaya['speechiness'].std()

dataHipHopJaya['loudness'].mean()
dataHipHopJaya['loudness'].std()

dataHipHopJaya['danceability'].mean()
dataHipHopJaya['danceability'].std()

dataHipHopJaya['popularity'].mean()
dataHipHopJaya['popularity'].std()

dataHipHopJaya['energy'].mean()
dataHipHopJaya['energy'].std()

np.std(dataHipHopJaya['duration_ms'])
np.std(dataHipHopJaya['energy'])

x = dataHipHopJaya[['energy', 'valence', 'loudness']].values
y = dataHipHopJaya[['danceability']].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, 
random_state=3)

model_regres = LinearRegression()
model_regres.fit(x_train, y_train) 

print(model_regres.intercept_)  
print(model_regres.coef_) 

y_pred = model_regres.predict(x_test) 

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred)) 
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred)) 
print('Root Mean Squared:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

#Hitung dan tampilkan R2 
r_2 = r2_score(y_test, y_pred) 
print('R^2:', r_2) 

# calculate IQR
Q1 = data['loudness'].quantile(0.25)
Q3 = data['loudness'].quantile(0.75)
IQR = Q3 - Q1

# define outlier threshold
threshold = Q3 + 1.5*IQR

# identify outliers
outliers = data[data['loudness'] > threshold]

# remove outliers from dataframe
dataClean = data[data['loudness'] <= threshold]


rock = re.compile(r'.*rock.*|.*punk.*|.*grunge.*|.*goth.*')
sublis = []
dataRock = pd.DataFrame()
for key in genreDict.keys():
    if rock.match(key):
        sublis.append(key)
        dataRock = dataRock.append(data.iloc[genreDict[key]])
        dataRock = dataRock.reset_index(drop=True)

subRockDict = {}
for sub in sublis:
    for key in genreDict.keys():
        if sub == key:
            if not key in subRockDict.keys():
                subRockDict[key]=genreDict[key]
            else:
                subRockDict[key].append(genreDict[key])

subRockDF = pd.DataFrame(columns=['key', 'value'])
for key, value in subRockDict.items():
    # subRockDF = subRockDF.append(data.iloc[subRockDict[key]])
    # keys = key
    # subRockDF['genre'] = keys
    new_row = {'key': key, 'value': value}
    subRockDF = subRockDF.append(new_row, ignore_index=True)

subRockDF = subRockDF.reset_index(drop=True)








    