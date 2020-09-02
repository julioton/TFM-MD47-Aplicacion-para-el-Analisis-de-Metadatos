from io import open
import pickle


class Files:
    file = ''
    content = ''

    def openFile(self, url='', mode='r+'):
        self.file = open(url, mode)
        return self.file

    def readFile(self, file):
        file.seek(0)
        self.content = file.read()
        print(self.content)
        file.close()

    def writeFile(self, file, content=''):
        file.write(content)
        file.close()

    def saveBinary(self, file, content):
        self.openFile(file, 'wb')
        pickle.dump(content, self.file)
        self.file.close()
        del self.file

    def readBinary(self, file):
        self.openFile(file, 'rb')
        self.content = pickle.load(self.file)
        print(self.file)
        self.file.close()
        del self.file
