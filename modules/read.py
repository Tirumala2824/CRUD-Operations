from database.database import client

class readData:
    def __init__(self):
        self.client=client
        self.database=self.client['studentData']
    def readSt(self,name):
        if 'student'==name.lower():
            readColl=self.database['studentData']
            return readColl.find()
        elif 'course'== name.lower():
            readColl=self.database['courseData']
            return readColl.find()
        elif 'trans'==name.lower():
            readColl=self.database['transactionData'] 
            return readColl.find()  
        # for st_coll in readColl.find():
        #     # print(type(st_coll))
        #     for st_key,col in st_coll.items():
        #         print(f'\t \t {st_key} : {col}')
