from database.database import client

class deleteData:
    def __init__(self):
        self.client=client
        self.database=self.client['studentData']

    def dUpdate(self,name,id):
        if 'student'==name.lower():
            readColl=self.database['studentData']
            readColl.delete_one({'_id':id})
            return f'Deleted Successfully in student data using Student ID'
        elif 'course'== name.lower():
            readColl=self.database['courseData']
            readColl.delete_one({'_id':id})
            return f'Deleted Successfully in student data using Course ID'
        elif 'trans'==name.lower():
            readColl=self.database['transactionData'] 
            readColl.delete_one({'_id':id})
            return f'Deleted Successfully in student data using Transaction ID'


