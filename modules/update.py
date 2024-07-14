from database.database import client

class updateData:
    def __init__(self):
        self.client=client
        self.database=self.client['studentData']

    def dUpdate(self,name,id,keys):
        if 'student'==name.lower():
            readColl=self.database['studentData']
            readColl.update_one(
                {'_id':id},
                {'$set':keys}
                )
            return f'Updated Successfully in student data using Student ID'
        elif 'course'== name.lower():
            readColl=self.database['courseData']
            readColl.update_one(
                {'_id':id},
                {'$set':keys}
                )
            return f'Updated Successfully in student data using Course ID'
        elif 'trans'==name.lower():
            readColl=self.database['transactionData'] 
            readColl.update_one(
                {'_id':id},
                {'$set':keys}
                )
            return f'Updated Successfully in student data using Transaction ID'
