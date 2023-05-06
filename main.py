from Builder import Builder
from Settings import Settings

settings=Settings()
print(settings.ini)
insertData={'input.inst': "ИГУ", 'upload.department': "ФБКИ", 'input.discipline': "Прикладная информатика", 'input.dirPod': "разработка ПО", 'input.naprav': "ПИ", 'input.developers': "Сергеев Д.В", 'upload.OS_RPD': "Список"}
build=Builder(insertData=insertData,settings=settings)
build.build()
