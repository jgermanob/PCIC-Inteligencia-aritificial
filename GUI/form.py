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
        self.brand_label.place(x=50, y=50)
        self.brand_combo = ttk.Combobox(main_window)
        self.brand_combo.place(x=180, y=50)
        self.brand_combo["values"] = ["Samsung", "Apple", "Xiaomi", "LG"]
        
        # Sistema operativo #
        self.os_label = ttk.Label(main_window, text="Sistema operativo")
        self.os_label.place(x=50, y=80)
        self.os_combo = ttk.Combobox(main_window)
        self.os_combo.place(x=180, y=80)
        self.os_combo["values"] = ["Android", "iOS", "Windows"]

        # Tipo de bateria #
        self.batteryType_label = ttk.Label(main_window, text="Tipo de bateria")
        self.batteryType_label.place(x=50, y=110)
        self.batteryType_combo = ttk.Combobox(main_window)
        self.batteryType_combo.place(x=180, y=110)
        self.batteryType_combo["values"] = ["Tipo 1", "Tipo 2", "Tipo 3"]

        # Bateria removible #
        self.batteryRemovable_label = ttk.Label(main_window, text="Bateria removible")
        self.batteryRemovable_label.place(x=50, y=140)
        self.batteryRemovable_combo = ttk.Combobox(main_window)
        self.batteryRemovable_combo.place(x=180, y=140)
        self.batteryRemovable_combo["values"] = ["Si", "No"]
        
        # Cores del CPU #
        self.cpuCores_label = ttk.Label(main_window, text="Nucleos del CPU")
        self.cpuCores_label.place(x=50, y=170)
        self.cpuCores_combo = ttk.Combobox(main_window)
        self.cpuCores_combo.place(x=180, y=170)
        self.cpuCores_combo["values"] = ["1", "2", "3", "4", "6", "8", "10"]

        main_window.configure(width=500, height=500)
        self.place(width=300, height=200)

main_window = tk.Tk()
app = Application(main_window)
app.mainloop()