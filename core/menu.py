from tkinter import messagebox


class MenuFunctions:

    @staticmethod
    def about():
        messagebox.showinfo("Acerca de...", "El Analizador de Metadatos MD47 es una aplicación que permite "
                            + "ver los metadatos ocultos en muchos de tus archivos de uso "
                            + "diario. Este es el proyecto final de gradación para el "
                            + "Máster Universitario en Ciberseguridad de la Universidad "
                            + "de Alcalá de Henares, España, periodo 2019-2020, "
                            + "estudiante Ing. Julio Chinchilla Moya.")

    @staticmethod
    def exit_app():
        return messagebox.askyesno("¿Cerrar Aplicación?", "¿Realmente desea cerrar la aplicación completamente?")

    @staticmethod
    def error_file_empty():
        messagebox.showerror("¡Ocurrió un Error!", "Debe de seleccionar un archivo válido.")

    @staticmethod
    def info_file_clean():
        messagebox.showinfo("Información", "Se ha finalizado el proceso de limpieza de metadatos.")

    @staticmethod
    def info_file_clean_failed():
        messagebox.showinfo("¡Ocurrió un Error!", "Ha fallado el proceso de limpieza de metadatos, no es posible limpiar el archivo seleccionado.")