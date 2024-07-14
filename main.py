
from modules.insert import InsertData
from modules.read import readData
from modules.update import updateData
from modules.delete import deleteData
from validator_collection import validators, checkers, errors

while True:
    print('*'*50)
    print('\t\t Enter an choice Given Below ')
    print('*'*50)
    print('\t\t\t 1. INSERT DATA')
    print('\t\t\t 2. READ DATA')
    print('\t\t\t 3. UPDATE DATA')
    print('\t\t\t 4. DELETE DATA')
    print('*'*50)
    ch=int(input('Enter Your Choice  : '))
    match ch:
        case 1:
            print('*'*50)
            print('\t\t Enter an choice Given Below ')
            print('*'*50)
            print('\t\t\t 1. Insert DATA in Student ')
            print('\t\t\t 2. Insert DATA in Course ')
            print('\t\t\t 3. Insert DATA in Transaction')
            print('*'*50)
            ch_insert=int(input('Enter Your Choice  : '))
            ins=InsertData()
            match ch_insert:
                case 1:
                    print('='*100)
                    print('\t \t \t Enter an Data of Student ')
                    print('='*100)
                    try:
                        inp_std={
                            '_id':validators.variable_name(input('Enter a ID of Student :  ')),
                            'name':validators.variable_name(input('Enter an Name of student : ')),
                            'email':validators.email(input('Enter an Email : ')),
                            'mobileNumber':validators.numeric(int(input('Enter a Mobile Number :'))),
                            'branch':validators.variable_name(input('Enter an branch of student : '))
                        }
                        print(ins.studentData(inp_std))
                    except errors.InvalidVariableNameError as err:
                        print(f'error : {err}')
                    except errors.InvalidEmailError as emm:
                        print(f'error : {emm}')
                    except errors.NotAnIntegerError as inn:
                        print(f'error : {inn}')
                    except Exception as exx:
                        print(f'error : {exx}')
                case 2:
                    print('='*100)
                    print('\t \t \t Enter an Data of Course ')
                    print('='*100)
                    try:
                        inp_std={
                            '_id':validators.variable_name(input('Enter a ID of Course :  ')),
                            'st_id':validators.variable_name(input('Enter a ID of student :  ')),
                            'courseName':validators.variable_name(input('Enter an Name of Course : ')),
                            'branch':validators.variable_name(input('Enter an branch of student : '))
                        }
                        print(ins.courseData(inp_std))
                    except errors.InvalidVariableNameError as err:
                        print(f'error : {err}')
                    except Exception as exx:
                        print(f'error : {exx}')
                case 3:
                    print('='*100)
                    print('\t \t \t Enter an Data of Transaction ')
                    print('='*100)
                    try:
                        inp_std={
                            'st_id':validators.variable_name(input('Enter a ID of student :  ')),
                            '_id':validators.variable_name(input('Enter a ID of Transaction :  ')),
                            'cur_id':validators.variable_name(input('Enter a ID of course :  ')),
                            'amount':validators.numeric(int(input('Enter an amount of student : '))),
                            'email':validators.email(input('Enter an Email : ')),
                            'mobileNumber':validators.numeric(int(input('Enter a Mobile Number'))),
                            'branch':validators.variable_name(input('Enter an branch of student : '))
                        }
                        print(ins.transactionData(inp_std))
                    except errors.InvalidVariableNameError as err:
                        print(f'error : {err}')
                    except errors.InvalidEmailError as emm:
                        print(f'error : {emm}')
                    except errors.NotAnIntegerError as inn:
                        print(f'error : {inn}')
                    except Exception as exx:
                        print(f'error : {exx}')
                case '_':
                    print('please Enter above option only')
        case 2:
            print('*'*50)
            print('\t\t Enter an choice Given Below ')
            print('*'*50)
            print('\t\t\t 1. READ DATA in Student ')
            print('\t\t\t 2. READ DATA in Course ')
            print('\t\t\t 3. READ DATA in Transaction')
            print('*'*50)
            ch_cur=int(input('Enter an READ CHOICE : '))
            rd=readData()

            match ch_cur:
                case 1:
                    readD=rd.readSt('student')
                    for st_coll in readD:
                        # print(type(st_coll))
                        for st_key,col in st_coll.items():
                            print(f'\t \t {st_key} : {col}')
                case 2:
                    readC=rd.readSt('course')
                    for st_coll in readC:
                        # print(type(st_coll))
                        for st_key,col in st_coll.items():
                            print(f'\t \t {st_key} : {col}')
                case 3:
                    readT=rd.readSt('trans')
                    for st_coll in readT:
                        # print(type(st_coll))
                        for st_key,col in st_coll.items():
                            print(f'\t \t {st_key} : {col}')
                case '_':
                    print('Enter above option only')

        case 3:
            print('*'*50)
            print('\t\t Enter an choice Given Below ')
            print('*'*50)
            print('\t\t\t 1. UPDATE DATA in Student ')
            print('\t\t\t 2. UPDATE DATA in Course ')
            print('\t\t\t 3. UPDATE DATA in Transaction')
            print('*'*50)
            ch_up=int(input('Select Above Solution : '))
            upD=updateData()
            match ch_up:
                case 1:
                    st_id=input('Enter an student ID : ')
                    print('#'*50)
                    print('\t\t Update fields are given below ')
                    print('#'*50)
                    print('\t\t \t name, email, mobileNumber, branch \n Fields Should be like these only ')
                    print('\t \t \t Total Fields to Update : 4') 
                    need_fields_to_update=int(input('Enter an No of fields to Update :  '))
                    updateField={}
                    for i in range(need_fields_to_update):
                        field_nam=input('Fields name : ')
                        updateField[field_nam]=input('Enter Field Value : ')
                    print(upD.dUpdate('student',st_id,updateField))
                case 2:
                    st_id=input('Enter an course ID : ')
                    print('#'*50)
                    print('\t\t Update fields are given below ')
                    print('#'*50)
                    print('\t\t \t st_id, courseName, branch \n Fields Should be like these only ')
                    print('\t \t \t Total Fields to Update : 3') 
                    need_fields_to_update=int(input('Enter an No of fields to Update :  '))
                    updateField={}
                    for i in range(need_fields_to_update):
                        field_nam=input('Fields name : ')
                        updateField[field_nam]=input('Enter Field Value : ')
                    print(upD.dUpdate('course',st_id,updateField))
                case 3:
                    st_id=input('Enter an Transaction ID : ')
                    print('#'*50)
                    print('\t\t Update fields are given below ')
                    print('#'*50)
                    print('\t\t \t st_id,cur_id,amount, email, mobileNumber, branch \n Fields Should be like these only ')
                    print('\t \t \t Total Fields to Update : 6') 
                    need_fields_to_update=int(input('Enter an No of fields to Update :  '))
                    updateField={}
                    for i in range(need_fields_to_update):
                        field_nam=input('Fields name : ')
                        updateField[field_nam]=input('Enter Field Value : ')
                    print(upD.dUpdate('trans',st_id,updateField))
                case '_':
                    print('Please Enter above option Only')
        case 4:
            print('*'*50)
            print('\t\t Enter an choice Given Below ')
            print('*'*50)
            print('\t\t\t 1. DELETE DATA in Student ')
            print('\t\t\t 2. DELETE DATA in Course ')
            print('\t\t\t 3. DELETE DATA in Transaction')
            print('*'*50)
            ch_up=int(input('Select Above Solution : '))
            upD=deleteData()
            match ch_up:
                case 1:
                    st_id=input('Enter an student ID : ')
                    print(upD.dUpdate('student',st_id))
                case 2:
                    st_id=input('Enter an course ID : ')
                    print(upD.dUpdate('course',st_id))
                case 3:
                    st_id=input('Enter an Transaction ID : ')
                    print(upD.dUpdate('trans',st_id))
                case '_':
                    print('Please Enter above option Only')
        case 0:
            break
        case '_':
            print('Enter only above option only')