from database.database import client

class InsertData:
    def __init__(self):
        self.client=client
        self.database=self.client['studentData']
    def studentData(self,student):
        collStudent=self.database['studentData']
        collStudent.insert_one(student)
        '''
        {
            '_id':id,
            'name': name,
            'email':email,
            'mobileNumber':mobileNumber
        }
        '''
        return f'SuccessFully inserted an Student data '
    def courseData(self,course):
        collCourse=self.database['courseData']
        collCourse.insert_one(course)
        '''
        {
            'course ID':course_id,
            'Student ID':st_id,
            'Course Name':courseName,
            'Teacher':courseTeacher
        }
        '''
        return f'Successfully Inserted an Course Data'
    def transactionData(self,trans):
        databaseTransaction=self.database['transactionData']
        databaseTransaction.insert_one(trans)
        '''
        {
            'Transaction Id':tran_id,
            'Student ID':st_id,
            'Course ID':cur_id,
            'Transaction Amount':tran_amount,
            'status':status
        }
        '''
        return f'SuccessFully Inserted In Transaction Data'
