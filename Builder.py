import docx

from Settings import Settings

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.table import WD_TABLE_ALIGNMENT
class Builder():

    def __init__(self, insertData, settings: Settings) -> None:
        self.insertData = insertData
        self.settings = settings
        self.PathToDeploy = settings.ini['PATHS']["Deploy"]
        self.PathToSh = settings.ini["PATHS"]["sh"]
        self.out = Document(self.PathToSh)
        self.tags = {}

    def getTags(self):
        fullText = []
        for para in self.out.paragraphs:
            fullText.append(para.text)
        self.tags = {}
        for text in fullText:
            if "{" in text and "}" in text:
                self.tags.update({text.split('{')[1].split('}')[0]: None})

    def checkInputData(self):

        for tag in self.tags.keys():
            if not (tag in self.insertData.keys()):
                raise Exception(f"{tag} not finded")
        for tag in self.insertData.keys():
            if not (tag in self.tags.keys()):
                print( Warning(f"{tag} not used in document"))

    def build(self):
        self.getTags()
        self.checkInputData()
        self.replaceTags()
        self.createTable1_1(self.insertData["table1_1"])
        self.out.save(self.PathToDeploy + "/Deploy.docx")
    def replaceTags(self):
        for para in self.out.paragraphs:
            text = para.text
            if "{" in text and "}" in text:
                for key in self.insertData.keys():
                    if key in text:
                        para.text = para.text.replace(f"{'{'}{key}{'}'}", self.insertData[key])

    def createRowForTable1_1(self,table,t):
        lenRows = len(table.rows)
        for n in range(t):
            table.add_row()
        for n in range(3):
            for i in range(t):
                table.cell(row_idx=lenRows + i, col_idx=n).merge(table.cell(row_idx=lenRows + n, col_idx=n))
        return table
    def createTable1_1(self,table1_1):
            table=self.out.tables[0]
            ind=1
            for RPD in table1_1:
                lenRows = len(table.rows)
                table=self.createRowForTable1_1(table,len(RPD["indexes"]))
                table.cell(row_idx=lenRows+2,col_idx=0).text=str(ind)
                table.cell(row_idx=lenRows + 2, col_idx=1).text = str(RPD['codeRPDs'])
                table.cell(row_idx=lenRows + 2, col_idx=2).text = str(RPD['soder_komp'])
                i=0
                for index in RPD["indexes"]:
                    table.cell(row_idx=lenRows + i, col_idx=3).text = str(index["index"])
                    table.cell(row_idx=lenRows + i, col_idx=4).text = str(index["rez"])
                    table.cell(row_idx=lenRows + i, col_idx=5).text = str(index["name"])
                    i+=1
                ind+=1

            table.style = 'Table Grid'
