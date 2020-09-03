import os, sys
import time
from stat import *
from tkinter import filedialog
from PIL import Image
from PIL.ExifTags import TAGS
import exifread


class MainMethods:

    @staticmethod
    def browse_file():
        file_types = [
            ("all files", "*.*")
        ]

        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=file_types)
        # ("all files", "*.*")
        # label_file_explorer.configure(text="File Opened: " + filename)
        return filename

    @staticmethod
    def check_file_ext(filename):
        if filename.endswith('.doc') | filename.endswith('.docx') | filename.endswith('.xls') \
                | filename.endswith('.xlsx') | filename.endswith('.pdf') | filename.endswith('.png') \
                | filename.endswith('.ppt') | filename.endswith('.pptx') | filename.endswith('.docm') \
                | filename.endswith('.xlsm') | filename.endswith('.gif') | filename.endswith('.JPG') \
                | filename.endswith('.jpg') | filename.endswith('.jpeg') | filename.endswith('.txt'):
            return True
        else:
            return False

    @staticmethod
    def get_file_properties(filename):
        file_prop = {}
        info = []
        try:
            info = os.stat(filename)
            file_prop["File Name"] = os.path.splitext(filename)[0]
            file_prop["Extension"] = os.path.splitext(filename)[1]
            file_prop["Size"] = info[ST_SIZE]
            file_prop["Time Created"] = time.asctime(time.localtime(info[ST_CTIME]))
            file_prop["Time Last Access"] = time.asctime(time.localtime(info[ST_ATIME]))
            file_prop["Time Modified"] = time.asctime(time.localtime(info[ST_MTIME]))
        except Exception as e:
            print("Failed to get information ", str(filename), "Exception: ", str(e))
        # else:
        # print(info)
        # print(file_prop)
        # for key, value in file_prop.items():
        #    print(key, ':', value)
        return file_prop

    @staticmethod
    def get_image_metadata(filename):
        file_prop = {}
        result = {}
        if filename.endswith('.png') | filename.endswith('.gif') | filename.endswith('.JPG') \
                | filename.endswith('.jpg') | filename.endswith('.jpeg'):
            try:
                # exif_data = Image.open(filename)._getexif()
                # for key, value in exif_data.items():
                #    file_prop.update({TAGS.get(key): value})
                #    #print('%s = %s ' % (TAGS.get(key), value))

                f = open(filename, 'rb')
                res = exifread.process_file(f)
                file_prop.update({'Metadata Type': 'EXIF'})
                for tag in res.keys():
                    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                        file_prop.update({tag: res[tag]})
                        # print("%s = %s" % (tag, res[tag]))

                for key, value in file_prop.items():
                    if value not in result.values():
                        result[key] = value

            except Exception as e:
                print("Failed to get information ", str(filename), "Exception: ", str(e))
        return result

    @staticmethod
    def clean_image_metadata(simplefilename, extension):
        filename = str(simplefilename) + str(extension)
        if filename.endswith('.png') | filename.endswith('.gif') | filename.endswith('.JPG') \
                | filename.endswith('.jpg') | filename.endswith('.jpeg'):
            try:
                image = Image.open(filename)
                data = list(image.getdata())
                image_without_exif = Image.new(image.mode, image.size)
                image_without_exif.putdata(data)
                image_without_exif.save(str(simplefilename) + '_clean_' + str(extension))
                return True
            except Exception as e:
                print("Failed to get information ", str(filename), "Exception: ", str(e))
        return False
