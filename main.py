from Builder import Builder
from Settings import Settings

settings = Settings()
insertData = {'fig': 'dsds',
              'input.inst': "ИГУ",
              'upload.department': "ФБКИ",
              'input.discipline': "Прикладная информатика",
              'input.dirPod': "разработка ПО",
              'input.naprav': "ПИ",
              'input.developers': "Сергеев Д.В",
              'upload.OS_RPD': "Список"}
insertTable1_1 = []
insertTable1_2 = []
insertTable1_3 = []
for i in range(3, 6):
    indexes = []
    for t in range(i):
        indexes.append({"index": f'{i - 2}_{t}',
                        "rez": " test test test test test test test test test test ",
                        "name": "test test test test test test test test test test "})
    insertTable1_1.append({"codeRPDs": i + 2324234234,
                           "soder_komp": f"soder_{i - 2}",
                           "indexes": indexes})
for i in range(8):
    insertTable1_2.append({"theme":f"test_{i+1}",
                           "code":f"{243423434+i}.{i+2}",
                           "rez":f"test test\n\n test test \n\n test test\n\n test test",
                           "mark":"test test test test test test test test test test test test ",
                           "krit":"test test test test test test test test test ",
                           "TK": "1)test 2)test 3)test 4)test ",
                           "PA": "1)test 2)test 3)test 4)test ",
                           })
for i in range(7):
    krit=[]
    for n in range(7-i):
        krit.append({
            "body":f"body_test_{n+1}",
            "mark":n
        })
    insertTable1_3.append({
        "sred":f"sred_{i+1}",
        "krit":krit,
    })

insertData.update({'table3': insertTable1_3})
insertData.update({'table2': insertTable1_2})
insertData.update({'table1': insertTable1_1})
builder = Builder(insertData=insertData, settings=settings)

builder.build()
