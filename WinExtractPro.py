import os
import rarfile
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import logging
import threading

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )

class ExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Descompresor de Archivos RAR y ZIP")
        self.root.geometry("400x200")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.label = tk.Label(root, text="Selecciona la carpeta con los archivos RAR o ZIP")
        self.label.pack(pady=10)
        
        self.select_button = tk.Button(root, text="Seleccionar Carpeta", command=self.start_extraction)
        self.select_button.pack(pady=10)
        
        self.progress = ttk.Progressbar(root, length=300, mode='determinate')
        self.progress.pack(pady=10)
        
        self.status_label = tk.Label(root, text="")
        self.status_label.pack(pady=10)
        
        self.extracted_count = 0
        self.total_files = 0
        self.is_processing = False

    def on_closing(self):
        if self.is_processing:
            if messagebox.askokcancel("Salir", "¿Estás seguro de que quieres cerrar? El proceso de descompresión está en curso."):
                self.root.destroy()
        else:
            self.root.destroy()

    def select_directory(self):
        folder_path = filedialog.askdirectory(title="Selecciona la carpeta con los archivos RAR o ZIP")
        return folder_path

    def extract_single_file(self, file_path, folder_path):
        try:
            file_name = os.path.splitext(os.path.basename(file_path))[0]
            extract_path = os.path.join(folder_path, file_name)
            os.makedirs(extract_path, exist_ok=True)
            
            if file_path.lower().endswith('.rar'):
                with rarfile.RarFile(file_path) as rf:
                    logging.info(f"Descomprimiendo {file_name}.rar en {extract_path}")
                    rf.extractall(path=extract_path)
            elif file_path.lower().endswith('.zip'):
                with zipfile.ZipFile(file_path, 'r') as zf:
                    logging.info(f"Descomprimiendo {file_name}.zip en {extract_path}")
                    zf.extractall(path=extract_path)
            
            logging.info(f"Archivo {file_name} descomprimido exitosamente.")
            return True
        except Exception as e:
            logging.error(f"Error al descomprimir {file_name}: {str(e)}")
            return False

    def update_progress(self):
        self.extracted_count += 1
        progress_value = (self.extracted_count / self.total_files) * 100
        self.progress['value'] = progress_value
        self.status_label.config(text=f"Progreso: {self.extracted_count}/{self.total_files} archivos")
        self.root.update_idletasks()

    def extract_files(self, folder_path):
        self.is_processing = True
        self.select_button.config(state='disabled')
        
        if not os.path.exists(folder_path):
            logging.error("La carpeta seleccionada no existe.")
            messagebox.showerror("Error", "La carpeta seleccionada no existe.")
            self.finish_processing()
            return

        archive_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.rar', '.zip'))]
        if not archive_files:
            logging.warning("No se encontraron archivos RAR o ZIP en la carpeta seleccionada.")
            messagebox.showwarning("Advertencia", "No se encontraron archivos RAR o ZIP en la carpeta seleccionada.")
            self.finish_processing()
            return

        self.total_files = len(archive_files)
        self.extracted_count = 0
        self.progress['maximum'] = 100
        self.status_label.config(text=f"Progreso: 0/{self.total_files} archivos")

        for archive_file in archive_files:
            file_path = os.path.join(folder_path, archive_file)
            success = self.extract_single_file(file_path, folder_path)
            if success:
                self.update_progress()

        messagebox.showinfo(
            "Completado",
            f"Proceso finalizado. {self.extracted_count} de {self.total_files} archivos descomprimidos."
        )
        self.finish_processing()

    def finish_processing(self):
        self.is_processing = False
        self.select_button.config(state='normal')
        self.root.destroy()

    def start_extraction(self):
        folder_path = self.select_directory()
        if folder_path:
            threading.Thread(target=self.extract_files, args=(folder_path,), daemon=True).start()
        else:
            logging.info("No se seleccionó ninguna carpeta.")
            messagebox.showinfo("Información", "No se seleccionó ninguna carpeta.")

def main():
    setup_logging()
    root = tk.Tk()
    app = ExtractorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
