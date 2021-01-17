from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import re
import pandas as pd
from Utils import Classifier

df = pd.read_csv('./Data/final_dataset.csv')

class Application(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Sistema de recomendación de celulares")
        main_window.configure(width=600, height=600)
        
        # Valores por defecto en los campos de texto #
        self.INTERNAL_MEMORY_DEFAULT_VALUE = "Memoria interna en GB"
        self.RAM_MEMORY_DEFAULT_VALUE = "Memoria RAM en GB"
        self.PRIMARY_CAMERA_DEFAULT_VALUE = "Camara trasera en MP"
        self.SECONDARY_CAMERA_DEFAULT_VALUE = "Camara frontal en MP"
        self.CPU_SPEED_DEFAULT_VALUE = "Velocidad en GHz"
        self.MAH_BATTERY_DEFAULT_VALUE = "Capacidad en mAh"
        self.PRICE_DEFAULT_VALUE = "Precio en €"

        # Opciones para los elementos de tipo Combobox #
        self.BRANDS = ['Acer','alcatel','Allview','Amazon','Apple','Archos','Asus','BenQ','BlackBerry','BLU',
                       'BQ','Casio','Cat','Celkon','Coolpad','Dell','Gigabyte','Gionee','Google','HP',
                       'HTC','Huawei','Intex','Karbonn','Kyocera','Lava','LeEco','Lenovo','LG','Meizu',
                       'Micromax','Microsoft','Motorola','NEC','Nokia','Nvidia','OnePlus','Oppo','Panasonic','Pantech',
                       'Prestigio','QMobile','Samsung','Sharp','Sonim','Sony','Sony Ericsson','Spice','T-Mobile','Vertu',
                       'verykool','vivo','Vodafone','Wiko','Xiaomi','XOLO','Yezz','Yota','YU','ZTE']
        
        self.OS = ["Android", "Windows", "iOS", "BlackBerry"]

        self.BATTERY_TYPES = ["Ion de litio (Li-Ion)", "Polímero de litio (Li-Po)"]

        self.BATTERY_REMOVABLE = ['Si', 'No']

        self.CPU_CORES = ["1", "2", "3", "4", "6", "8", "10"]

        # Expresión regular para verificar valores numéricos #
        self.DECIMAL_RE = re.compile(r"^\d*[.,]?\d*$")

        # Configuración de elementos del formulario #
        # Marca #
        self.brand_label = ttk.Label(main_window, text="Marca")
        self.brand_label.place(x=40, y=50)
        self.brand_combo = ttk.Combobox(main_window)
        self.brand_combo.place(x=180, y=50)
        self.brand_combo["values"] = self.BRANDS
        
        # Sistema operativo #
        self.os_label = ttk.Label(main_window, text="Sistema operativo")
        self.os_label.place(x=40, y=80)
        self.os_combo = ttk.Combobox(main_window)
        self.os_combo.place(x=180, y=80)
        self.os_combo["values"] = self.OS

        # Tipo de bateria #
        self.batteryType_label = ttk.Label(main_window, text="Tipo de bateria")
        self.batteryType_label.place(x=40, y=110)
        self.batteryType_combo = ttk.Combobox(main_window)
        self.batteryType_combo.place(x=180, y=110)
        self.batteryType_combo["values"] = self.BATTERY_TYPES

        # Bateria removible #
        self.batteryRemovable_label = ttk.Label(main_window, text="Bateria removible")
        self.batteryRemovable_label.place(x=40, y=140)
        self.batteryRemovable_combo = ttk.Combobox(main_window)
        self.batteryRemovable_combo.place(x=180, y=140)
        self.batteryRemovable_combo["values"] = self.BATTERY_REMOVABLE
        
        # Cores del CPU #
        self.cpuCores_label = ttk.Label(main_window, text="Nucleos del CPU")
        self.cpuCores_label.place(x=40, y=170)
        self.cpuCores_combo = ttk.Combobox(main_window)
        self.cpuCores_combo.place(x=180, y=170)
        self.cpuCores_combo["values"] = self.CPU_CORES

        # Memoria interna #
        self.internalMemory_label = ttk.Label(main_window, text="Memoria interna")
        self.internalMemory_label.place(x=40, y=200)
        self.internalMemory_entry = ttk.Entry(main_window)
        self.internalMemory_entry.insert(tk.END, self.INTERNAL_MEMORY_DEFAULT_VALUE)
        self.internalMemory_entry.place(x=180, y=200)

        # Memoria RAM #
        self.ramMemory_label = ttk.Label(main_window, text="Memoria RAM")
        self.ramMemory_label.place(x=40, y=230)
        self.ramMemory_entry = ttk.Entry(main_window)
        self.ramMemory_entry.insert(tk.END, self.RAM_MEMORY_DEFAULT_VALUE)
        self.ramMemory_entry.place(x=180, y=230)       

        # Camara trasera #
        self.primaryCamera_label = ttk.Label(main_window, text="Camara principal")
        self.primaryCamera_label.place(x=40, y=260)
        self.primaryCamera_entry = ttk.Entry(main_window)
        self.primaryCamera_entry.insert(tk.END, self.PRIMARY_CAMERA_DEFAULT_VALUE)
        self.primaryCamera_entry.place(x=180, y=260)

        # Camara frontal #
        self.secondaryCamera_label = ttk.Label(main_window, text="Camara secundaria")
        self.secondaryCamera_label.place(x=40, y=290)
        self.secondaryCamera_entry = ttk.Entry(main_window)
        self.secondaryCamera_entry.insert(tk.END, self.SECONDARY_CAMERA_DEFAULT_VALUE)
        self.secondaryCamera_entry.place(x=180, y=290)

        # Velocidad del cpu #
        self.cpuSpeed_label = ttk.Label(main_window, text="Velocidad del cpu")
        self.cpuSpeed_label.place(x=40, y=320)
        self.cpuSpeed_entry = ttk.Entry(main_window)
        self.cpuSpeed_entry.insert(tk.END, self.CPU_SPEED_DEFAULT_VALUE)
        self.cpuSpeed_entry.place(x=180, y=320)

        # Miliamperios de la bateria #
        self.mahBattery_label = ttk.Label(main_window, text="Capacidad de bateria")
        self.mahBattery_label.place(x=40, y=350)
        self.mahBattery_entry = ttk.Entry(main_window)
        self.mahBattery_entry.insert(tk.END, self.MAH_BATTERY_DEFAULT_VALUE)
        self.mahBattery_entry.place(x=180, y=350)

        # Precio #
        self.price_label = ttk.Label(main_window, text="Precio")
        self.price_label.place(x=40, y=380)
        self.price_entry = ttk.Entry(main_window)
        self.price_entry.insert(tk.END, self.PRICE_DEFAULT_VALUE)
        self.price_entry.place(x=180, y=380)

        # Boton para buscar recomendacion #
        self.search_button = ttk.Button(main_window, text="Buscar", command=self.onClick_searchButton)
        self.search_button.place(x=250, y=410)

        main_window.configure(width=600, height=600)
        self.place(width=600, height=600)

    def openResultsWindow(self, best_option, min_dissimilarity):
        results_window = tk.Toplevel(main_window)
        results_window.title("Mejor resultado") 
        results_window.geometry("500x500")
        # Obtención de información #
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

        model_label = ttk.Label(results_window, text='Modelo:')
        model_label.place(x=40, y=40)
        model_result = ttk.Label(results_window, text=model)
        model_result.place(x=180, y=40)
        
        ram_label = ttk.Label(results_window, text='RAM:')
        ram_label.place(x=40, y=70)
        ram_result = ttk.Label(results_window, text=ram)
        ram_result.place(x=180, y=70)

        price_label = ttk.Label(results_window, text='Precio:')
        price_label.place(x=40, y=110)
        price_result = ttk.Label(results_window, text=price)
        price_result.place(x=180, y=110)
        
        mah_label = ttk.Label(results_window, text='Capacidad de la bateria:')
        mah_label.place(x=40, y=140)
        mah_result = ttk.Label(results_window, text=mah)
        mah_result.place(x=220, y=140)        

        cores_label = ttk.Label(results_window, text='Núcleos:')
        cores_label.place(x=40, y=170)
        cores_result = ttk.Label(results_window, text=cores)
        cores_result.place(x=180, y=170)

        speed_label = ttk.Label(results_window, text='Velocidad del CPU:')
        speed_label.place(x=40, y=200)
        speed_result = ttk.Label(results_window, text=speed)
        speed_result.place(x=180, y=200)

        prim_label = ttk.Label(results_window, text='Camara principal:')
        prim_label.place(x=40, y=230)
        prim_result = ttk.Label(results_window, text=prim_camera)
        prim_result.place(x=180, y=230)
    
        sec_label = ttk.Label(results_window, text='Camara secundaria:')
        sec_label.place(x=40, y=260)
        sec_result = ttk.Label(results_window, text=sec_camera)
        sec_result.place(x=180, y=260)

        int_label = ttk.Label(results_window, text='Memoria interna:')
        int_label.place(x=40, y=290)
        int_result = ttk.Label(results_window, text=internal_memory)
        int_result.place(x=180, y=290)

        brand_label = ttk.Label(results_window, text='Marca:')
        brand_label.place(x=40, y=320)
        brand_result = ttk.Label(results_window, text=brand)
        brand_result.place(x=180, y=320)

        os_label = ttk.Label(results_window, text='Sistema operativo:')
        os_label.place(x=40, y=350)
        os_result = ttk.Label(results_window, text=os)
        os_result.place(x=180, y=350)

        rem_label = ttk.Label(results_window, text='Bateria removible:')
        rem_label.place(x=40, y=380)
        rem_result = ttk.Label(results_window, text=removable)
        rem_result.place(x=180, y=380)

        type_label = ttk.Label(results_window, text='Tipo de bateria:')
        type_label.place(x=40, y=410)
        type_result = ttk.Label(results_window, text=batt_type)
        type_result.place(x=180, y=410)

    def onClick_searchButton(self):
        result = self.onCheck_Entries()
        if result == None:
            messagebox.showerror("Error", "Valores invalidos")
        else:
            classifier = Classifier()
            vector = classifier.create_vector(result)
            cluster = classifier.get_cluster(vector)
            best_option, min_diss = classifier.get_best_option(cluster, vector)
            self.openResultsWindow(best_option, min_diss)
            
    def onCheck_Entries(self):
        # Obtención de valores de elementos Entry #
        internal_memory = self.internalMemory_entry.get()
        ram_memory = self.ramMemory_entry.get()
        primary_camera = self.primaryCamera_entry.get()
        secondary_camera = self.secondaryCamera_entry.get()
        cpu_speed = self.cpuSpeed_entry.get()
        mah_battery = self.mahBattery_entry.get()
        price = self.price_entry.get()

        # Obtención de valores de los combobox #
        brand = self.brand_combo.get()
        os = self.os_combo.get()
        battery_type = self.batteryType_combo.get()
        battery_removable = self.batteryRemovable_combo.get()
        cores = self.cpuCores_combo.get()
        
        # Se revisa que los valores de los combobox no estén vacios o sea una opción inválida#
        if brand == '' or brand not in self.BRANDS:
            print("brand error")
            return None
        if os == '' or os not in self.OS:
            print("os error")
            return None
        if battery_type == '' or battery_type not in self.BATTERY_TYPES:
            print('battery type error:',battery_type)
            return None
        if battery_removable == '' or battery_removable not in self.BATTERY_REMOVABLE:
            print('battery removable error')
            return None
        if cores == '' or cores not in self.CPU_CORES:
            print('cores error')
            return None

        # Se revisa que los campos de texto no tengan los valores por defecto o estén vacios #
        if internal_memory == self.INTERNAL_MEMORY_DEFAULT_VALUE or internal_memory == "":
            return None
        if ram_memory == self.RAM_MEMORY_DEFAULT_VALUE or ram_memory == '':
            return None
        if primary_camera == self.PRIMARY_CAMERA_DEFAULT_VALUE or primary_camera == '':
            return None
        if secondary_camera == self.SECONDARY_CAMERA_DEFAULT_VALUE or secondary_camera == '':
            return None
        if cpu_speed == self.CPU_SPEED_DEFAULT_VALUE or cpu_speed == '':
            return None
        if mah_battery == self.MAH_BATTERY_DEFAULT_VALUE or mah_battery == '':
            return None
        if price == self.PRICE_DEFAULT_VALUE or price == '':
            return None
        
        if not self.DECIMAL_RE.match(internal_memory):
            return None
        if not self.DECIMAL_RE.match(ram_memory):
            return None
        if not self.DECIMAL_RE.match(primary_camera):
            return None
        if not self.DECIMAL_RE.match(secondary_camera):
            return None
        if not self.DECIMAL_RE.match(cpu_speed):
            return None
        if not self.DECIMAL_RE.match(mah_battery):
            return None
        if not self.DECIMAL_RE.match(price):
            return None
        
        return (brand, os, battery_type, battery_removable, cores, internal_memory, ram_memory, primary_camera, secondary_camera, cpu_speed, mah_battery, price)

        

main_window = tk.Tk()
app = Application(main_window)
app.mainloop()