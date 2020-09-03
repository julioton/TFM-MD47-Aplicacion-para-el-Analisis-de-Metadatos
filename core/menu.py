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