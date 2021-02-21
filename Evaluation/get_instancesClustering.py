from random import uniform, randint
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from kmodes.kprototypes import KPrototypes
import numpy as np
#from Dissimilarity import matching_dissim, euclidean_dissim

BRANDS = ['Acer','alcatel','Allview','Amazon','Apple','Archos','Asus','BenQ','BlackBerry','BLU',
                       'BQ','Casio','Cat','Celkon','Coolpad','Dell','Gigabyte','Gionee','Google','HP',
                       'HTC','Huawei','Intex','Karbonn','Kyocera','Lava','LeEco','Lenovo','LG','Meizu',
                       'Micromax','Microsoft','Motorola','NEC','Nokia','Nvidia','OnePlus','Oppo','Panasonic','Pantech',
                       'Prestigio','QMobile','Samsung','Sharp','Sonim','Sony','Sony Ericsson','Spice','T-Mobile','Vertu',
                       'verykool','vivo','Vodafone','Wiko','Xiaomi','XOLO','Yezz','Yota','YU','ZTE']
OS = ["Android", "Windows", "iOS", "BlackBerry"]
BATTERY_TYPES = ["Li-Ion", "Li-Po"]
BATTERY_REMOVABLE = ['Si', 'No']
CORES = [1,2,3,4,6,8,10]

# Modelos y encoders #
clustering_model = pickle.load(open('./Models/clustering_model.pickle', 'rb'))
kmeans_model = pickle.load(open('./Models/kmeans_model.pickle', 'rb'))
os_encoder = pickle.load(open('./Models/os_encoder.pickle','rb'))
brand_encoder = pickle.load(open('./Models/brand_encoder.pickle', 'rb'))
battery_type_encoder = pickle.load(open('./Models/battery_type_encoder.pickle', 'rb'))
battery_removable_encoder = pickle.load(open('./Models/battery_removable_encoder.pickle', 'rb'))
df = pd.read_csv('./Data/final_dataset.csv', encoding='utf8')

INPUTS_PATH = './Evaluation/Inputs/'
OUTPUTS_PATH = './Evaluation/Recommendations/'

def matching_dissim(a, b):
    """Simple matching dissimilarity function"""
    return np.sum(a != b, axis=1)[0]

def euclidean_dissim(a, b):
    """Euclidean distance dissimilarity function"""
    if np.isnan(a).any() or np.isnan(b).any():
        raise ValueError("Missing values detected in numerical columns.")
    return np.sum((a - b) ** 2, axis=1)[0]

def get_dissimilarity(element, vector):
    element = element[0]
    vector = vector[0]
    categorical_vector = np.array(vector[6:10]).reshape(1,4)
    categorical_element = np.array(element[6:10]).reshape(1,4)
    cat_dissimilarity = matching_dissim(categorical_element,categorical_vector)
        
    numerical_element = np.array([element[0], element[1], element[2], element[3], element[4],  element[5],  element[10],  element[11]]).reshape(1,8)
    numerical_vector = np.array([vector[0], vector[1], vector[2], vector[3], vector[4],  vector[5],  vector[10],  vector[11]]).reshape(1,8)
    num_disimilarity = euclidean_dissim(numerical_element, numerical_vector)

    dissimilarity = cat_dissimilarity + num_disimilarity
    return dissimilarity

def get_best_option(cluster, vector):
    cluster = cluster[0]
    cluster_df = df[(df.cluster == cluster)]
    cluster_df = cluster_df.reset_index(drop=True)
    min_disssimilarity = 10000
    aux_index = 0
    vector = vector.astype(np.float)
    for index, row in cluster_df.iterrows():
        element = [row['RAM'],row['approx_price_EUR'],row['battery_mah'],row['CPU_cores'], 
                   row['CPU_speed'],row['internal_memory_gb'],row['brand'],row['OS'],
                   row['battery_removable'],row['battery_type'],row['primary_camera_mp'], row['secondary_camera_mp']]
        element = np.array(element).reshape(1,12).astype(np.float)
        dis = get_dissimilarity(element,vector)
        if dis < min_disssimilarity:
            min_disssimilarity = dis
            aux_index = index

        best_option = cluster_df.iloc[aux_index]
        best_option = best_option.values[:13]
        best_option[9] = brand_encoder.inverse_transform([best_option[9]])[0]
        best_option[10] = os_encoder.inverse_transform([best_option[10]])[0]
        best_option[11] = battery_removable_encoder.inverse_transform([best_option[11]])[0]
        best_option[12] = battery_type_encoder.inverse_transform([best_option[12]])[0]
        if best_option[11] == False:
            best_option[11] = 'No'
        else:
            best_option[11] = 'Si'

        
        return best_option, min_disssimilarity



def get_best_option_kmeans(cluster, vector):
    cluster = cluster[0]
    cluster_df = df[(df.cluster == cluster)]
    cluster_df = cluster_df.reset_index(drop=True)
    min_disssimilarity = 10000
    aux_index = 0
    vector = vector.astype(np.float)
    for index, row in cluster_df.iterrows():
        element = [row['RAM'],row['approx_price_EUR'],row['battery_mah'],row['CPU_cores'], 
                   row['CPU_speed'],row['internal_memory_gb'],row['brand'],row['OS'],
                   row['battery_removable'],row['battery_type'],row['primary_camera_mp'], row['secondary_camera_mp']]
        element = np.array(element).reshape(1,12).astype(np.float)
        dis = euclidean_dissim(element,vector)
        if dis < min_disssimilarity:
            min_disssimilarity = dis
            aux_index = index

        best_option = cluster_df.iloc[aux_index]
        best_option = best_option.values[:13]
        best_option[9] = brand_encoder.inverse_transform([best_option[9]])[0]
        best_option[10] = os_encoder.inverse_transform([best_option[10]])[0]
        best_option[11] = battery_removable_encoder.inverse_transform([best_option[11]])[0]
        best_option[12] = battery_type_encoder.inverse_transform([best_option[12]])[0]
        if best_option[11] == False:
            best_option[11] = 'No'
        else:
            best_option[11] = 'Si'

        
        return best_option, min_disssimilarity

for instance in range(100):
    input_file = open(INPUTS_PATH+'input_{}.txt'.format(instance),'w')
    output_file = open(OUTPUTS_PATH+'recommendation_{}.txt'.format(instance),'w')
    input_kmeans_file = open(INPUTS_PATH+'input_kmeans_{}.txt'.format(instance),'w')
    output_kmeans_file = open(OUTPUTS_PATH+'recommendation_kmeans_{}.txt'.format(instance),'w')
    brand_index = randint(0, len(BRANDS)-1)
    os_index = randint(0, len(OS)-1)
    battery_types_index = randint(0, len(BATTERY_TYPES)-1)
    battery_removable_index = randint(0,len(BATTERY_REMOVABLE)-1)
    core_index = randint(0,len(CORES)-1)
    
    brand = BRANDS[brand_index]
    os = OS[os_index]
    battery_type = BATTERY_TYPES[battery_types_index]
    battery_removable = BATTERY_REMOVABLE[battery_removable_index]
    cores = CORES[core_index]
    
    internal_memory = round(uniform(1.0,512.0),3)
    ram_memory = round(uniform(0.128,6.000),3)
    primary_camera = round(uniform(0.60,24.0),3)
    secondary_camera = round(uniform(0.0,20.0),3)
    cpu_speed = round(uniform(0.0,2.7),3)
    mah_battery = round(uniform(10.0,11560.0),3)
    price = round(uniform(30.0,27000.0),3)

    #Escritura de archivo#
    input_file.write('Marca: {}\n'.format(brand))
    input_file.write('Sistema operativo: {}\n'.format(os))
    input_file.write('Tipo de bateria: {}\n'.format(battery_type))
    input_file.write('Bateria removible: {}\n'.format(battery_removable))
    input_file.write('Memoria interna: {} GB\n'.format(internal_memory))
    input_file.write('Memoria RAM: {} GB\n'.format(ram_memory))
    input_file.write('Camera trasera: {} MP\n'.format(primary_camera))
    input_file.write('Camara frontal: {} MP\n'.format(secondary_camera))
    input_file.write('Velocidad del CPU: {} GHz\n'.format(cpu_speed))
    input_file.write('Capacidad de la bateria: {} mAh\n'.format(mah_battery))
    input_file.write('Precio: {} €\n'.format(price))

    #Escritura de archivo#
    input_kmeans_file.write('Marca: {}\n'.format(brand))
    input_kmeans_file.write('Sistema operativo: {}\n'.format(os))
    input_kmeans_file.write('Tipo de bateria: {}\n'.format(battery_type))
    input_kmeans_file.write('Bateria removible: {}\n'.format(battery_removable))
    input_kmeans_file.write('Memoria interna: {} GB\n'.format(internal_memory))
    input_kmeans_file.write('Memoria RAM: {} GB\n'.format(ram_memory))
    input_kmeans_file.write('Camera trasera: {} MP\n'.format(primary_camera))
    input_kmeans_file.write('Camara frontal: {} MP\n'.format(secondary_camera))
    input_kmeans_file.write('Velocidad del CPU: {} GHz\n'.format(cpu_speed))
    input_kmeans_file.write('Capacidad de la bateria: {} mAh\n'.format(mah_battery))
    input_kmeans_file.write('Precio: {} €\n'.format(price))

    if battery_removable == 'No':
        battery_removable = False
    else:
        battery_removable = True

    #Codificación y obtención de vector#
    brand = brand_encoder.transform([brand])[0]
    os = os_encoder.transform([os])[0]
    battery_type = battery_type_encoder.transform([battery_type])[0]
    battery_removable = battery_removable_encoder.transform([battery_removable])[0]
    
    vector = [ram_memory, price, mah_battery, cores, cpu_speed, internal_memory, brand, os, battery_removable, battery_type, primary_camera, secondary_camera]
    vector = np.array(vector).reshape(1,12)

    # Obtener cluster #
    cluster = clustering_model.predict(vector, categorical=[6,7,8,9])
    best_option, min_disssimilarity = get_best_option(cluster,vector)
    
    model = best_option[0]
    ram = best_option[1]
    price = best_option[2]
    mah = best_option[3]
    cores = best_option[4]
    speed = best_option[5]
    prim_camera = best_option[6]
    sec_camera = best_option[7]
    internal_memory = best_option[8]
    brand = best_option[9]
    os = best_option[10]
    removable = best_option[11]
    batt_type = best_option[12]

    # Escritura de archivo de recomendación #
    output_file.write('Marca: {}\n'.format(brand))
    output_file.write('Modelo: {}\n'.format(model))
    output_file.write('Sistema operativo: {}\n'.format(os))
    output_file.write('Tipo de bateria: {}\n'.format(batt_type))
    output_file.write('Bateria removible: {}\n'.format(removable))
    output_file.write('Memoria interna: {} GB\n'.format(internal_memory))
    output_file.write('Memoria RAM: {} GB\n'.format(ram_memory))
    output_file.write('Camera trasera: {} MP\n'.format(primary_camera))
    output_file.write('Camara frontal: {} MP\n'.format(secondary_camera))
    output_file.write('Velocidad del CPU: {} GHz\n'.format(cpu_speed))
    output_file.write('Capacidad de la bateria: {} mAh\n'.format(mah_battery))
    output_file.write('Precio: {} €\n'.format(price))
    output_file.write('\nDisimilaridad: {}\n'.format(min_disssimilarity))

    kmeans_cluster = kmeans_model.predict(vector)
    best_option, min_disssimilarity = get_best_option_kmeans(kmeans_cluster,vector)

    model = best_option[0]
    ram = best_option[1]
    price = best_option[2]
    mah = best_option[3]
    cores = best_option[4]
    speed = best_option[5]
    prim_camera = best_option[6]
    sec_camera = best_option[7]
    internal_memory = best_option[8]
    brand = best_option[9]
    os = best_option[10]
    removable = best_option[11]
    batt_type = best_option[12]

    # Escritura de archivo de recomendación #
    output_kmeans_file.write('Marca: {}\n'.format(brand))
    output_kmeans_file.write('Modelo: {}\n'.format(model))
    output_kmeans_file.write('Sistema operativo: {}\n'.format(os))
    output_kmeans_file.write('Tipo de bateria: {}\n'.format(batt_type))
    output_kmeans_file.write('Bateria removible: {}\n'.format(removable))
    output_kmeans_file.write('Memoria interna: {} GB\n'.format(internal_memory))
    output_kmeans_file.write('Memoria RAM: {} GB\n'.format(ram_memory))
    output_kmeans_file.write('Camera trasera: {} MP\n'.format(primary_camera))
    output_kmeans_file.write('Camara frontal: {} MP\n'.format(secondary_camera))
    output_kmeans_file.write('Velocidad del CPU: {} GHz\n'.format(cpu_speed))
    output_kmeans_file.write('Capacidad de la bateria: {} mAh\n'.format(mah_battery))
    output_kmeans_file.write('Precio: {} €\n'.format(price))
    output_kmeans_file.write('\nDisimilaridad: {}\n'.format(min_disssimilarity))






