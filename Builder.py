import docx

from Settings import Settings
from PyPDF2 import PdfReader
from docx import Document
class Builder():

    def __init__(self,insertData,settings:Settings) -> None:
     self.insertData=insertData
     self.settings=settings
     self.PathToDeploy=settings.ini['PATHS']["Deploy"]
     self.PathToSh=settings.ini["PATHS"]["sh"]
     self.out =Document(self.PathToSh)
     self.tags={}
    def getTags(self):
     fullText = []
     for para in self.out.paragraphs:
      fullText.append(para.text)
     self.tags={}
     for text in fullText:
      if "{" in text and "}" in text:
       self.tags.update({text.split('{')[1].split('}')[0]:None})
    def checkInputData(self):

     for tag in self.tags.keys():
      if not(tag in self.insertData.keys()):
       raise Exception(f"{tag} not finded")
     for tag in self.insertData.keys():
      if not (tag in self.tags.keys()):
       raise Warning(f"{tag} not used in document")

    def build(self):
     self.getTags()
     self.checkInputData()
     for para in self.out.paragraphs:
       text=para.text
       if "{" in text and "}" in text:
        for key in self.insertData.keys():
         if key in text:
          para.text=para.text.replace(f"{'{'}{key}{'}'}",self.insertData[key])
     self.out.save(self.PathToDeploy+"/Deploy.docx")





