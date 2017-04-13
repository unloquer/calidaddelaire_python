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

def loadCsv():
#cargar un csv con todos los datos desde una direccion web
#retorna un dataset con coordenadas y pm25
    dataset=[]
    datatoheal=[]
    # with open(file) as rawdata:
    #     for rawline in rawdata:
    #         
    #         linelist=[x for x in rawline.split(',')]
    csv_online = pd.read_csv('https://raw.githubusercontent.com/daquina-io/visualizacionCalidadAire/master/data/points.csv')
    #estos son los headers del dataset
    #lat,lng,date,hour,altitude,course,speed,humidity,temperature,pm25

    for linelist in np.array(csv_online):
        coord=[]
        linelist=list(linelist)
        datatoheal.append(linelist)
        #print linelist

        
        if "INVALID" not in linelist and 'lat' not in linelist:
            coord.append([float(linelist[0]),float(linelist[1]),float(linelist[9])]) #escoger lat long y pm25
            dataset.append(coord[0])
    dataset=np.array(dataset)


    #revisar si el primer dato es invalido y
    # si es asi sanarlo partiendo 
    #desde el primero que no sea valido
    healedlist=list(datatoheal)
    if datatoheal[0][0] =="INVALID": #si el primer dato es INVALID debemos sanar esa primera referencia
        n=0
        while True: #hacer este loop para encontrar la primera que no es invalid en lat long course y speed
            #chekthis=[datatoheal[n][0],datatoheal[n][1],datatoheal[n][6],datatoheal[n][6]]
            if "INVALID" not in datatoheal[n]:
                PLNM=n #guardar aqui el indice de la primera linea con los datos completos
                #print "linea no mala", n
                break
            else:
                n=n+1

        #hacer un loop desde la linea n hasta el primer dato para ir pasando los datos de lat y long "sanados"
        for n in reversed(range(PLNM+1)):
            #print n
            #usando la aproxmacion de Brolin y tomando lat y long como residuos
            #posicion: long = longanterior+v*t | posicion: lat = latanterior+v*t
            #v es speed que debe ser en metros por segundo(???)
            #en el ecuador por cada cambio de 0.0001 grados hay un cambio de 11.13 m
            v=float(datatoheal[n][6]) #extraer la velocidad de la linea buena
            deg=float(datatoheal[n][5]) #extraer el angulo de la linea buena
            
            if healedlist[n-1][0] =="INVALID":
                delta_lat=(v*np.cos(np.radians(deg))) #esta equacion debee estar en metros. cambio en direccion Y
                healedlist[n-1][0]=((float(delta_lat)/11.13)*0.0001)+ float(healedlist[n][0])#anotar la latitud calculada en la lista con los datos corregidos
                
            if healedlist[n-1][1] =="INVALID":
                delta_long=(v*np.sin(np.deg2rad(deg))) #esta equacion debe estar en metros. cambio en direccion X
                healedlist[n-1][1]=((float(delta_long)/11.13)*0.0001)+float(healedlist[n][1]) #anotar la longitud calculada en la ista con los datos corregidos
            
            if datatoheal[n-1][5]== "INVALID":
                healedlist[n-1][5]=deg #Si el angulo es invalid reescribirlo
            
            if datatoheal[n-1][6]== "INVALID":
                healedlist[n-1][6]=v #si el speed es invalido reescribirlo

            #para las siguientes columnas solo copiar el dato anterior porque no se puede aproximar
            if datatoheal[n-1][2]=="INVALID":
                datatoheal[n-1][2]=datatoheal[n][2] #copiar la fecha anterior
            if datatoheal[n-1][3]=="INVALID":
                datatoheal[n-1][3]=datatoheal[n][3] #copiar la hora anterior
            if datatoheal[n-1][4]=="INVALID":
                datatoheal[n-1][4]=datatoheal[n][4] #copiar la altitud anterior
            if datatoheal[n-1][7]=="INVALID":
                datatoheal[n-1][7]=datatoheal[n][7] #copiar la humedad anterior
            if datatoheal[n-1][8]=="INVALID":
                datatoheal[n-1][8]=datatoheal[n][8] #copiar la temperatura anterior

    #ya que los primeros estan correctos vamos a corregir todos los que tengan cualquier valor invalid
    #esta vez lo hacemos en orden cronologico: n va ascendente.
    healedout=[] #aqui guardamos posicion y pm25
    for n in range(len(healedlist)-1):
        
        #usando la aproxmacion de Brolin y tomando lat y long como residuos
        #posicion: long = longanterior+v*t | posicion: lat = latanterior+v*t
        #v es speed que debe ser en metros por segundo(???)
        #en el ecuador por cada cambio de 0.0001 grados hay un cambio de 11.13 m
        v=float(datatoheal[n][6]) #extraer la velocidad de la linea buena
        deg=float(datatoheal[n][5]) #extraer el angulo de la linea buena
        
        if healedlist[n+1][0] =="INVALID":
            delta_lat=(v*np.cos(np.radians(deg))) #esta equacion debee estar en metros. cambio en direccion Y
            healedlist[n+1][0]=((float(delta_lat)/11.13)*0.0001)+ float(healedlist[n][0])#anotar la latitud calculada en la lista con los datos corregidos
            
        if healedlist[n+1][1] =="INVALID":
            delta_long=(v*np.sin(np.deg2rad(deg))) #esta equacion debe estar en metros. cambio en direccion X
            healedlist[n+1][1]=((float(delta_long)/11.13)*0.0001)+float(healedlist[n][1]) #anotar la longitud calculada en la ista con los datos corregidos
        if datatoheal[n+1][5]== "INVALID":
            healedlist[n+1][5]=deg #Si el angulo es invalid reescribirlo
        if datatoheal[n+1][6]== "INVALID":
            healedlist[n+1][6]=v #si el speed es invalido reescribirlo

        #para los siguientes datos solo copiar el dato anterior porque no se puede aproximar
        if datatoheal[n+1][2]=="INVALID":
            datatoheal[n+1][2]=datatoheal[n][2] #copiar la fecha anterior
        if datatoheal[n+1][3]=="INVALID":
            datatoheal[n+1][3]=datatoheal[n][3] #copiar la hora anterior
        if datatoheal[n+1][4]=="INVALID":
            datatoheal[n+1][4]=datatoheal[n][4] #copiar la altitud anterior
        if datatoheal[n+1][7]=="INVALID":
            datatoheal[n+1][7]=datatoheal[n][7] #copiar la humedad anterior
        if datatoheal[n+1][8]=="INVALID":
            datatoheal[n+1][8]=datatoheal[n][8] #copiar la temperatura anterior
        
        #ahora solo copmilamos la posicion y el valor en una lista de floats
        healedout.append([float(healedlist[n][0]),float(healedlist[n][1]),float(healedlist[n][9])])
        
    healedout=np.array(healedout)
    return healedout

dataset=loadCsv() #usar esta linea para cargar todos los csv
#dataset=loadJson('aire_brol2.json')#usar esta linea para cargar el json

#print dataset
#redondear las coordenadas de dataset 
#ajustar los decimales en "dec"
dec=4 #numero de decimales de precision de las coordenadas
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
plt.scatter(x_map, y_map, marker="s", edgecolors="face", s=20, c=p_map, alpha=0.5)
# plt.xlim(min(x_map),max(x_map))
# plt.ylim(min(y_map),max(y_map))
plt.axis('scaled')

plt.show()