import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from kmodes.kprototypes import KPrototypes
import numpy as np
from Dissimilarity import matching_dissim, euclidean_dissim

class Classifier():
    def __init__(self):
        self.clustering_model = pickle.load(open('./Models/clustering_model.pickle', 'rb'))
        self.os_encoder = pickle.load(open('./Models/os_encoder.pickle','rb'))
        self.brand_encoder = pickle.load(open('./Models/brand_encoder.pickle', 'rb'))
        self.battery_type_encoder = pickle.load(open('./Models/battery_type_encoder.pickle', 'rb'))
        self.battery_removable_encoder = pickle.load(open('./Models/battery_removable_encoder.pickle', 'rb'))
        self.df = pd.read_csv('./Data/final_dataset.csv', encoding='utf8')
    
    def create_vector(self, results):
        # RAM
        # approx_price_EUR	
        # battery_mah	
        # CPU_cores	
        # CPU_speed	
        # internal_memory_gb	
        # brand	
        # OS	
        # battery_removable	
        # battery_type	
        # primary_camera_mp	
        # secondary_camera_mp
        brand, os, battery_type, battery_removable, cores, internal_memory, ram_memory, primary_camera, secondary_camera, cpu_speed, mah_battery, price = results
        if battery_type =='Polímero de litio (Li-Po)':
            battery_type = 'Li-Po'
        else:
            battery_type = 'Li-Ion'
        
        if battery_removable == 'No':
            battery_removable = False
        else:
            battery_removable = True

        brand = self.brand_encoder.transform([brand])[0]
        os = self.os_encoder.transform([os])[0]
        battery_type = self.battery_type_encoder.transform([battery_type])[0]
        battery_removable = self.battery_removable_encoder.transform([battery_removable])[0]
        vector = [ram_memory, price, mah_battery, cores, cpu_speed, internal_memory, brand, os, battery_removable, battery_type, primary_camera, secondary_camera]
        vector = np.array(vector).reshape(1,12)
        return vector
    
    def get_cluster(self, vector):
        cluster = self.clustering_model.predict(vector, categorical=[6,7,8,9])
        return cluster[0]
    
    def get_dissimilarity(self, element, vector):
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
    
    def get_best_option(self, cluster, vector):
        cluster_df = self.df[(self.df.cluster == cluster)]
        cluster_df = cluster_df.reset_index(drop=True)
        min_disssimilarity = 10000
        aux_index = 0
        vector = vector.astype(np.float)
        for index, row in cluster_df.iterrows():
            element = [row['RAM'],row['approx_price_EUR'],row['battery_mah'],row['CPU_cores'], 
                       row['CPU_speed'],row['internal_memory_gb'],row['brand'],row['OS'],
                       row['battery_removable'],row['battery_type'],row['primary_camera_mp'], row['secondary_camera_mp']]
            element = np.array(element).reshape(1,12).astype(np.float)
            dis = self.get_dissimilarity(element,vector)
            if dis < min_disssimilarity:
                min_disssimilarity = dis
                aux_index = index

        best_option = cluster_df.iloc[aux_index]
        best_option = best_option.values[:13]
        best_option[9] = self.brand_encoder.inverse_transform([best_option[9]])[0]
        best_option[10] = self.os_encoder.inverse_transform([best_option[10]])[0]
        best_option[11] = self.battery_removable_encoder.inverse_transform([best_option[11]])[0]
        if best_option[11] == False:
            best_option[11] = 'No'
        else:
            best_option[11] = 'Si'

        best_option[12] = self.battery_type_encoder.inverse_transform([best_option[12]])[0]
        return best_option, min_disssimilarity

