import os
import time
from stat import *
from tkinter import *
from tkinter import filedialog
from docx import Document

import PyPDF2
import exifread
from PIL import Image
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import NameObject, createStringObject
from oletools import olemeta
import olefile
from lib import pdf_metadata
from core.definitions import tdPressAnalyze


class MainMethods:

    @staticmethod
    def browse_file():
        file_types = [
            ("all files", "*.*")
        ]
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=file_types)
        return filename

    @staticmethod
    def check_file_ext(filename):
        if filename.endswith('.doc') | filename.endswith('.docx') | filename.endswith('.xls') \
                | filename.endswith('.xlsx') | filename.endswith('.docm') | filename.endswith('.dotx') \
                | filename.endswith('.dotm') | filename.endswith('.DOC') | filename.endswith('.DOCX') \
                | filename.endswith('.XLS') | filename.endswith('.XLSX') | filename.endswith('.DOCM') \
                | filename.endswith('.DOTX') | filename.endswith('.DOTM') | filename.endswith('.PDF') \
                | filename.endswith('.PNG') | filename.endswith('.pdf') | filename.endswith('.png') \
                | filename.endswith('.ppt') | filename.endswith('.pptx') | filename.endswith('.pps') \
                | filename.endswith('.xlsm') | filename.endswith('.gif') | filename.endswith('.JPG') \
                | filename.endswith('.jpg') | filename.endswith('.jpeg') | filename.endswith('.txt') \
                | filename.endswith('.PDF'):
            return True
        else:
            return False

    @staticmethod
    def print_results(output_item, input_data):
        for key, value in input_data.items():
            output_item.insert(INSERT, str(key) + ': ' + str(value) + '\n')

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
            print("Failed ", str(filename), "Exception: ", str(e))
        return file_prop

    @staticmethod
    def get_metadata(filename, fileprops):
        if filename.endswith('.png') | filename.endswith('.gif') | filename.endswith('.JPG') \
                | filename.endswith('.jpg') | filename.endswith('.jpeg'):
            return MainMethods.get_image_metadata(filename)
        elif filename.endswith('.pdf') | filename.endswith('.PDF'):
            return MainMethods.get_pdf_metadata(filename, fileprops)
        elif filename.endswith('.xlsx') | filename.endswith('.XLSX') | filename.endswith('.XLS') \
                | filename.endswith('.xls') | filename.endswith('.doc') | filename.endswith('.DOC') \
                | filename.endswith('.docx') | filename.endswith('.DOCX') \
                | filename.endswith('.docm') | filename.endswith('.dotx'):
            return MainMethods.get_office_metadata(filename, fileprops)
        else:
            return False

    @staticmethod
    def get_image_metadata(filename):
        file_prop = {}
        result = {}
        try:
            '''
            exif_data = Image.open(filename)._getexif()
            if exif_data:
                print("Exif data")
                for key, value in exif_data.items():
                    file_prop.update({TAGS.get(key): value})
                    #print('%s = %s ' % (TAGS.get(key), value))
            '''
            f = open(filename, 'rb')
            res = exifread.process_file(f)
            if res:
                print("Exif read data")
                file_prop.update({tdPressAnalyze + 'Metadata Type ': 'EXIF\n'})
                for tag in res.keys():
                    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                        file_prop.update({tag: res[tag]})
                        # print("%s = %s" % (tag, res[tag]))
            if file_prop:
                for key, value in file_prop.items():
                    if value not in result.values():
                        result[key] = value

            if int(len(result.items())) == 0:
                result.update({'\nMetadata Type EXIF': 'No Metadata to show'})

        except Exception as e:
            print("Failed ", str(filename), "Exception: ", str(e))
        return result

    @staticmethod
    def get_pdf_metadata(filename, fileprops):
        result_py_pdf = {}
        result_py_pdf_xmp = {}
        result_pdf_meta = {}
        result = {}
        result.update({tdPressAnalyze + 'Metadata Type ': 'PDF\n'})

        try:
            filepdf1 = PyPDF2.PdfFileReader(open(filename, 'rb'))
            result_py_pdf = filepdf1.getDocumentInfo()
        except Exception as e:
            print("Failed PyPDF2 getDocumentInfo", str(filename), "Exception: ", str(e))

        try:
            filepdf2 = PyPDF2.PdfFileReader(open(filename, 'rb'))
            result_py_pdf_xmp = filepdf2.getXmpMetadata()
        except Exception as e:
            print("Failed PyPDF2 getXmpMetadata", str(filename), "Exception: ", str(e))

        try:
            arg_list = [filename, '', '']
            result_pdf_meta = pdf_metadata.input_main(arg_list)
        except Exception as e:
            print("Failed pdf_meta", str(filename), "Exception: ", str(e))

        if result_py_pdf:
            count = 0
            try:
                for key, value in result_py_pdf.items():
                    ++count
                    if value not in result.values():
                        result[key] = value
            except Exception as e:
                print("Failed for result_py_pdf", str(filename), "Exception: ", str(e))

        if result_py_pdf_xmp:
            print(result_py_pdf_xmp)
            count = 0
            try:
                for key, value in result_py_pdf_xmp.items():
                    ++count
                    if value not in result.values():
                        result[key] = value
            except Exception as e:
                print("Failed for result_py_pdf_xmp", str(filename), "Exception: ", str(e))

        if result_pdf_meta:
            count = 0
            try:
                for key, value in result_pdf_meta.items():
                    ++count
                    if value not in result.values():
                        result[key] = value
            except Exception as e:
                print("Failed for result_pdf_meta", str(filename), "Exception: ", str(e))

        if int(len(result.items())) == 0:
            result.update({'\nMetadata Type PDF': 'No Metadata to show'})

        return result

    @staticmethod
    def get_office_metadata(filename, fileprops):
        file_prop = {}
        result_metadata = {}
        result = {}
        try:
            f = open(filename, 'rb')
            print(filename)
            ole = olefile.OleFileIO(filename)
            result_metadata = ole.get_metadata()

            if result_metadata:
                count = 0
                try:
                    for prop in result_metadata.SUMMARY_ATTRIBS:
                        value = getattr(result_metadata, prop)
                        ++count
                        if value not in result.values():
                            result[prop] = value
                except Exception as e:
                    print("Failed for result_metadata SUMMARY_ATTRIBS", str(filename), "Exception: ", str(e))

                try:
                    for prop in result_metadata.DOCSUM_ATTRIBS:
                        value = getattr(result_metadata, prop)
                        ++count
                        if value not in result.values():
                            result[prop] = value

                except Exception as e:
                    print("Failed for result_metadata DOCSUM_ATTRIBS", str(filename), "Exception: ", str(e))

            if int(len(result.items())) == 0:
                result.update({'\nMetadata Type MS Office': 'No Metadata to show'})

            return result

        except Exception as e:
            print("Failed ", str(filename), "Exception: ", str(e))
            result.update({'\nFailed': str(e)})
        return result

    @staticmethod
    def clean_metadata(simplefilename, extension):
        filename = str(simplefilename) + str(extension)
        if filename.endswith('.png') | filename.endswith('.gif') | filename.endswith('.JPG') \
                | filename.endswith('.jpg') | filename.endswith('.jpeg'):
            return MainMethods.clean_image_metadata(simplefilename, extension)
        elif filename.endswith('.pdf') | filename.endswith('.PDF'):
            return MainMethods.clean_pdf_metadata(simplefilename, extension)
        elif filename.endswith('.xlsx') | filename.endswith('.XLSX') | filename.endswith('.XLS') \
                | filename.endswith('.xls') | filename.endswith('.doc') | filename.endswith('.DOC') \
                | filename.endswith('.docx') | filename.endswith('.DOCX') \
                | filename.endswith('.docm') | filename.endswith('.dotx'):
            return MainMethods.clean_office_metadata(simplefilename, extension)

    @staticmethod
    def clean_image_metadata(simplefilename, extension):
        filename = str(simplefilename) + str(extension)
        try:
            image = Image.open(filename)
            data = list(image.getdata())
            image_without_exif = Image.new(image.mode, image.size)
            image_without_exif.putdata(data)
            image_without_exif.save(str(simplefilename) + '_clean_' + str(extension))
            return str(simplefilename) + '_clean_' + str(extension)
        except Exception as e:
            print("Failed ", str(filename), "Exception: ", str(e))
        return False

    @staticmethod
    def clean_pdf_metadata(simplefilename, extension):
        filename = str(simplefilename) + str(extension)
        try:

            OUTPUT = simplefilename + str('_CLEAN_.pdf')
            INPUTS = [filename, ]
            inputs = {}
            output = PdfFileWriter()

            infoDict = output._info.getObject()
            infoDict.update({
                NameObject('/Title'): createStringObject(u'Title'),
                NameObject('/Producer'): createStringObject(u'MD47'),
                NameObject('/Author'): createStringObject(u'MD47'),
                NameObject('/Subject'): createStringObject(u'subject'),
                NameObject('/Creator'): createStringObject(u'MD47')
            })

            try:
                inputs = [PdfFileReader(open(i, "rb")) for i in INPUTS]
            except Exception as e:
                print("Failed PdfFileReader", str(filename), "Exception: ", str(e))

            if len(inputs) > 0:
                try:
                    for input in inputs:
                        for page in range(input.getNumPages()):
                            output.addPage(input.getPage(page))
                except Exception as e:
                    print("Failed for input", str(filename), "Exception: ", str(e))

                try:
                    outputStream = open(OUTPUT, 'wb')
                    output.write(outputStream)
                    outputStream.close()
                except Exception as e:
                    print("Failed outputStream", str(filename), "Exception: ", str(e))
            else:
                return False

            return OUTPUT

        except Exception as e:
            print("Failed ", str(filename), "Exception: ", str(e))
        return False

    @staticmethod
    def clean_office_metadata(simplefilename, extension):
        filename = str(simplefilename) + str(extension)
        try:

            document = Document(filename)
            core_properties = document.core_properties
            print(core_properties)
            meta_fields = ["author", "category", "comments", "content_status", "created", "identifier", "keywords",
                           "language", "revision", "subject", "title", "version"]
            for meta_field in meta_fields:
                setattr(core_properties, meta_field, "")
            document.save(str(simplefilename) + '_clean_' + str(extension))

            return str(simplefilename) + '_clean_' + str(extension)
        except Exception as e:
            print("Failed 99 ", str(filename), "Exception: ", str(e))
        return False

