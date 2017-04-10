import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd




def loadJson(file):
#cargar archivo de json con datos
#crear un array con coordenadas y pm25 llamado dataset
    with open(file) as json_data:
        j = json.load(json_data)
        #print type(j['features'])
        #print len(j['features'])
        dataset=[]
        for medicion in j['features']:
        	#print medicion
        	coord=[]
        	coord.append([medicion['geometry']['coordinates'][0],medicion['geometry']['coordinates'][1], medicion['properties']['pm25']])
        	dataset.append(coord[0])
        dataset=np.array(dataset)
    return dataset

def loadCsv(file):
#cargar un csv con todos los datos
#retorna un dataset con coordenadas y pm25
    dataset=[]
    # with open(file) as rawdata:
    #     for rawline in rawdata:
    #         
    #         linelist=[x for x in rawline.split(',')]
    csv_online = pd.read_csv('https://raw.githubusercontent.com/daquina-io/visualizacionCalidadAire/master/data/points.csv')

    for linelist in np.array(csv_online):
        coord=[]
        linelist=list(linelist)
        #print linelist
        #course es lineslist[5] y speed es linelist[6]
        if "INVALID" not in linelist and 'lat' not in linelist:
            coord.append([float(linelist[0]),float(linelist[1]),float(linelist[9])])
            dataset.append(coord[0])
    dataset=np.array(dataset)
    return dataset

dataset=loadCsv('csv_brolin.txt') #usar esta linea para cargar todos los csv
#dataset=loadJson('aire_brol2.json')#usar esta linea para cargar el json

#redondear las coordenadas de dataset 
#ajustar los decimales en "dec"
dec=5 #numero de decimales de precision de las coordenadas
dataset[:,0]=np.around(dataset[:,0],dec) #redondear los datos x
dataset[:,1]=np.around(dataset[:,1],dec) #redondear los datos y

#buscar posiciones repetidas y guardarlas en "zet"
pos=[(x[0],x[1]) for x in dataset]
zet=set(tuple(i) for i in pos)

#sacar la media de las coordenadas repetidas
#guardar x,y,pm25 en diferentes listas

x_map=[]
y_map=[]
p_map=[]

for position in zet:
	heatid=[]
	for x in dataset:
		if x[:2][0]==position[0]:
			heatid.append(x[2])
	
	x_map.append(position[1])
	y_map.append(position[0])
	p_map.append(np.mean(heatid))

#hacer un plot
plt.scatter(x_map, y_map, marker="s", edgecolors="face", s=5, c=p_map, alpha=0.5)
# plt.xlim(min(x_map),max(x_map))
# plt.ylim(min(y_map),max(y_map))
plt.axis('scaled')

plt.show()