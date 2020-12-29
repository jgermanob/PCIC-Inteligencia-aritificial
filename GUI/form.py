from tkinter import ttk
import tkinter as tk

class Application(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Sistema de recomendación de celulares")
        main_window.configure(width=500, height=500)
        
        # Configuración de elementos del formulario #
        # Marca #
        self.brand_label = ttk.Label(main_window, text="Marca")
        self.brand_label.place(x=40, y=50)
        self.brand_combo = ttk.Combobox(main_window)
        self.brand_combo.place(x=180, y=50)
        self.brand_combo["values"] = ["Samsung", "Apple", "Xiaomi", "LG"]
        
        # Sistema operativo #
        self.os_label = ttk.Label(main_window, text="Sistema operativo")
        self.os_label.place(x=40, y=80)
        self.os_combo = ttk.Combobox(main_window)
        self.os_combo.place(x=180, y=80)
        self.os_combo["values"] = ["Android", "iOS", "Windows"]

        # Tipo de bateria #
        self.batteryType_label = ttk.Label(main_window, text="Tipo de bateria")
        self.batteryType_label.place(x=40, y=110)
        self.batteryType_combo = ttk.Combobox(main_window)
        self.batteryType_combo.place(x=180, y=110)
        self.batteryType_combo["values"] = ["Tipo 1", "Tipo 2", "Tipo 3"]

        # Bateria removible #
        self.batteryRemovable_label = ttk.Label(main_window, text="Bateria removible")
        self.batteryRemovable_label.place(x=40, y=140)
        self.batteryRemovable_combo = ttk.Combobox(main_window)
        self.batteryRemovable_combo.place(x=180, y=140)
        self.batteryRemovable_combo["values"] = ["Si", "No"]
        
        # Cores del CPU #
        self.cpuCores_label = ttk.Label(main_window, text="Nucleos del CPU")
        self.cpuCores_label.place(x=40, y=170)
        self.cpuCores_combo = ttk.Combobox(main_window)
        self.cpuCores_combo.place(x=180, y=170)
        self.cpuCores_combo["values"] = ["1", "2", "3", "4", "6", "8", "10"]

        # Memoria interna #
        self.internalMemory_label = ttk.Label(main_window, text="Memoria interna")
        self.internalMemory_label.place(x=40, y=200)
        self.internalMemory_entry = ttk.Entry(main_window)
        self.internalMemory_entry.insert(tk.END,'Memoria interna en GB')
        self.internalMemory_entry.place(x=180, y=200)

        # Memoria RAM #
        self.ramMemory_label = ttk.Label(main_window, text="Memoria RAM")
        self.ramMemory_label.place(x=40, y=230)
        self.ramMemory_entry = ttk.Entry(main_window)
        self.ramMemory_entry.insert(tk.END,'Memoria RAM en GB')
        self.ramMemory_entry.place(x=180, y=230)       

        # Camara trasera #
        self.primaryCamera_label = ttk.Label(main_window, text="Camara principal")
        self.primaryCamera_label.place(x=40, y=260)
        self.primaryCamera_entry = ttk.Entry(main_window)
        self.primaryCamera_entry.insert(tk.END,'Camara trasera en MP')
        self.primaryCamera_entry.place(x=180, y=260)

        # Camara frontal #
        self.secondaryCamera_label = ttk.Label(main_window, text="Camara secundaria")
        self.secondaryCamera_label.place(x=40, y=290)
        self.secondaryCamera_entry = ttk.Entry(main_window)
        self.secondaryCamera_entry.insert(tk.END,'Camara frontal en MP')
        self.secondaryCamera_entry.place(x=180, y=290)

        # Velocidad del cpu #
        self.cpuSpeed_label = ttk.Label(main_window, text="Velocidad del cpu")
        self.cpuSpeed_label.place(x=40, y=320)
        self.cpuSpeed_entry = ttk.Entry(main_window)
        self.cpuSpeed_entry.insert(tk.END,'Velocidad en GHz')
        self.cpuSpeed_entry.place(x=180, y=320)

        # Miliamperios de la bateria #
        self.mahBattery_label = ttk.Label(main_window, text="Capacidad de bateria")
        self.mahBattery_label.place(x=40, y=350)
        self.mahBattery_entry = ttk.Entry(main_window)
        self.mahBattery_entry.insert(tk.END,'Capacidad en mAh')
        self.mahBattery_entry.place(x=180, y=350)

        # Precio #
        self.price_label = ttk.Label(main_window, text="Precio")
        self.price_label.place(x=40, y=380)
        self.price_entry = ttk.Entry(main_window)
        self.price_entry.insert(tk.END,'Precio en €')
        self.price_entry.place(x=180, y=380)                

        main_window.configure(width=500, height=500)
        self.place(width=300, height=200)

main_window = tk.Tk()
app = Application(main_window)
app.mainloop()