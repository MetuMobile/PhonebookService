from PhonebookBridge import PhonebookBridge

class Phonebook:
    def __init__(self):
        # self.phonebookBridge = MockPhonebookBridge()
        self.phonebookBridge = PhonebookBridge()
        pass

    def get(self):
        rawDbResult = self.phonebookBridge.fetchAllFromDb()
        activePhonebookRecords = []
        for eachRecord in rawDbResult:
            if eachRecord['durum'] == "aktif":
                recordDict = {}
                recordDict['title'] = eachRecord['title']
                recordDict['pinned'] = False
                name = eachRecord['name']
                if name[0] == " " or name[0] == "!":
                    name = name[1:]
                    recordDict['pinned'] = True
                recordDict['name'] = name
                recordDict['surname'] = eachRecord['surname']
                recordDict['position'] = eachRecord['position']
                recordDict['officeTel'] = eachRecord['oftelno']
                recordDict['unit'] = eachRecord['unit']
                recordDict['officeLocation'] = eachRecord['ofno']
                try:
                    recordDict['email'] = str(eachRecord['email']) + "@metu.edu.tr"
                except:
                    recordDict['email'] = None
                activePhonebookRecords.append(recordDict)
        return activePhonebookRecords

class MockPhonebookBridge:
    def fetchAllFromDb(self):
        return [
            {
                'durum':'aktif',
                'oftelno':'oftelno',
                'unit':'unit',
                'ofno':'ofno',
                'position':'position',
                'surname':'surname',
                'name':' name',
                'title':'title',
                'surname':'aktif',
                'email':'email',
            },
            {
                'durum':'pasif',
                'oftelno':'oftelno',
                'unit':'unit',
                'ofno':'ofno',
                'position':'position',
                'surname':'surname',
                'name':'name',
                'title':'title',
                'surname':'aktif',
                'email':'email',
            },
            {
                'durum':'aktif',
                'oftelno':'oftelno',
                'unit':'unit',
                'ofno':'ofno',
                'position':'position',
                'surname':'surname',
                'name':'name',
                'title':'title',
                'surname':'aktif',
                'email':'email',
            },
        ]