from Builder import Builder
from Settings import Settings

settings=Settings()
insertData={'fig':'dsds','input.inst': "ИГУ", 'upload.department': "ФБКИ", 'input.discipline': "Прикладная информатика", 'input.dirPod': "разработка ПО", 'input.naprav': "ПИ", 'input.developers': "Сергеев Д.В", 'upload.OS_RPD': "Список"}
insertTable1_1=[]
indexes = []
for i in range(3,6):
    indexes = []
    for t in range(i):
        indexes.append({"index":f'{i-2}_{t}',"rez":" test test test test test test test test test test ","name":"test test test test test test test test test test "})
    insertTable1_1.append({"codeRPDs":i+2324234234,"soder_komp":f"soder_{i-2}","indexes":indexes})
insertData.update({'table1_1':insertTable1_1})
build=Builder(insertData=insertData,settings=settings)
print(insertTable1_1)
build.build(
)
