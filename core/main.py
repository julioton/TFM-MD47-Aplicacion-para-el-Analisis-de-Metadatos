from tkinter import filedialog


class MainMethods:

    @staticmethod
    def browse_file():
        file_types = [
            ("all files", "*.*")
        ]

        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=file_types)
                                                        #("all files", "*.*")
        #label_file_explorer.configure(text="File Opened: " + filename)
        return filename
