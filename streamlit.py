import streamlit as st
from modules.insert import InsertData
from modules.read import readData
from modules.update import updateData
from modules.delete import deleteData
from validator_collection import validators, errors

# Streamlit application title and description
st.title("MongoDB CRUD Operations")
st.sidebar.title("Navigation")

# Sidebar navigation options
options = ["Insert Data", "Read Data", "Update Data", "Delete Data"]
choice = st.sidebar.selectbox("Choose an option", options)

if choice == "Insert Data":
    st.header("Insert Data")
    insert_options = ["Student", "Course", "Transaction"]
    insert_choice = st.selectbox("Choose a category to insert data into", insert_options)
    ins = InsertData()

    if insert_choice == "Student":
        st.subheader("Insert Data in Student")
        inp_std = {}
        inp_std['_id'] = st.text_input("Enter a ID of Student:")
        inp_std['name'] = st.text_input("Enter a Name of Student:")
        inp_std['email'] = st.text_input("Enter an Email:")
        inp_std['mobileNumber'] = st.text_input("Enter a Mobile Number:")
        inp_std['branch'] = st.text_input("Enter a Branch of Student:")

        if st.button("Insert"):
            try:
                inp_std['_id'] = validators.variable_name(inp_std['_id'])
                inp_std['name'] = validators.variable_name(inp_std['name'])
                inp_std['email'] = validators.email(inp_std['email'])
                inp_std['mobileNumber'] = validators.numeric(int(inp_std['mobileNumber']))
                inp_std['branch'] = validators.variable_name(inp_std['branch'])
                result = ins.studentData(inp_std)
                st.success(result)
            except errors.InvalidVariableNameError as err:
                st.error(f'Invalid Variable Name: {err}')
            except errors.InvalidEmailError as emm:
                st.error(f'Invalid Email: {emm}')
            except errors.NotAnIntegerError as inn:
                st.error(f'Not an Integer: {inn}')
            except Exception as exx:
                st.error(f'Error: {exx}')

    elif insert_choice == "Course":
        st.subheader("Insert Data in Course")
        inp_std = {}
        inp_std['_id'] = st.text_input("Enter a ID of Course:")
        inp_std['st_id'] = st.text_input("Enter a ID of Student:")
        inp_std['courseName'] = st.text_input("Enter a Name of Course:")
        inp_std['branch'] = st.text_input("Enter a Branch of Student:")

        if st.button("Insert"):
            try:
                inp_std['_id'] = validators.variable_name(inp_std['_id'])
                inp_std['st_id'] = validators.variable_name(inp_std['st_id'])
                inp_std['courseName'] = validators.variable_name(inp_std['courseName'])
                inp_std['branch'] = validators.variable_name(inp_std['branch'])
                result = ins.courseData(inp_std)
                st.success(result)
            except errors.InvalidVariableNameError as err:
                st.error(f'Invalid Variable Name: {err}')
            except Exception as exx:
                st.error(f'Error: {exx}')

    elif insert_choice == "Transaction":
        st.subheader("Insert Data in Transaction")
        inp_std = {}
        inp_std['st_id'] = st.text_input("Enter a ID of Student:")
        inp_std['_id'] = st.text_input("Enter a ID of Transaction:")
        inp_std['cur_id'] = st.text_input("Enter a ID of Course:")
        inp_std['amount'] = st.text_input("Enter an Amount of Student:")
        inp_std['email'] = st.text_input("Enter an Email:")
        inp_std['mobileNumber'] = st.text_input("Enter a Mobile Number:")
        inp_std['branch'] = st.text_input("Enter a Branch of Student:")

        if st.button("Insert"):
            try:
                inp_std['st_id'] = validators.variable_name(inp_std['st_id'])
                inp_std['_id'] = validators.variable_name(inp_std['_id'])
                inp_std['cur_id'] = validators.variable_name(inp_std['cur_id'])
                inp_std['amount'] = validators.numeric(int(inp_std['amount']))
                inp_std['email'] = validators.email(inp_std['email'])
                inp_std['mobileNumber'] = validators.numeric(int(inp_std['mobileNumber']))
                inp_std['branch'] = validators.variable_name(inp_std['branch'])
                result = ins.transactionData(inp_std)
                st.success(result)
            except errors.InvalidVariableNameError as err:
                st.error(f'Invalid Variable Name: {err}')
            except errors.InvalidEmailError as emm:
                st.error(f'Invalid Email: {emm}')
            except errors.NotAnIntegerError as inn:
                st.error(f'Not an Integer: {inn}')
            except Exception as exx:
                st.error(f'Error: {exx}')

elif choice == "Read Data":
    st.header("Read Data")
    read_options = ["Student", "Course", "Transaction"]
    read_choice = st.selectbox("Choose a category to read data from", read_options)
    rd = readData()

    if read_choice == "Student":
        st.subheader("Read Data from Student")
        data = rd.readSt('student')
        for item in data:
            st.json(item)

    elif read_choice == "Course":
        st.subheader("Read Data from Course")
        data = rd.readSt('course')
        for item in data:
            st.json(item)

    elif read_choice == "Transaction":
        st.subheader("Read Data from Transaction")
        data = rd.readSt('trans')
        for item in data:
            st.json(item)

elif choice == "Update Data":
    st.header("Update Data")
    update_options = ["Student", "Course", "Transaction"]
    update_choice = st.selectbox("Choose a category to update data in", update_options)
    upD = updateData()

    if update_choice == "Student":
        st.subheader("Update Data in Student")
        st_id = st.text_input("Enter the Student ID to update:")
        fields = ['name', 'email', 'mobileNumber', 'branch']
        updateField = {}
        for field in fields:
            value = st.text_input(f"Enter new value for {field} (leave blank if no change):")
            if value:
                updateField[field] = value

        if st.button("Update"):
            try:
                result = upD.dUpdate('student', st_id, updateField)
                st.success(result)
            except Exception as exx:
                st.error(f'Error: {exx}')

    elif update_choice == "Course":
        st.subheader("Update Data in Course")
        st_id = st.text_input("Enter the Course ID to update:")
        fields = ['st_id', 'courseName', 'branch']
        updateField = {}
        for field in fields:
            value = st.text_input(f"Enter new value for {field} (leave blank if no change):")
            if value:
                updateField[field] = value

        if st.button("Update"):
            try:
                result = upD.dUpdate('course', st_id, updateField)
                st.success(result)
            except Exception as exx:
                st.error(f'Error: {exx}')

    elif update_choice == "Transaction":
        st.subheader("Update Data in Transaction")
        st_id = st.text_input("Enter the Transaction ID to update:")
        fields = ['st_id', 'cur_id', 'amount', 'email', 'mobileNumber', 'branch']
        updateField = {}
        for field in fields:
            value = st.text_input(f"Enter new value for {field} (leave blank if no change):")
            if value:
                updateField[field] = value

        if st.button("Update"):
            try:
                result = upD.dUpdate('trans', st_id, updateField)
                st.success(result)
            except Exception as exx:
                st.error(f'Error: {exx}')

elif choice == "Delete Data":
    st.header("Delete Data")
    delete_options = ["Student", "Course", "Transaction"]
    delete_choice = st.selectbox("Choose a category to delete data from", delete_options)
    delD = deleteData()

    if delete_choice == "Student":
        st.subheader("Delete Data in Student")
        st_id = st.text_input("Enter the Student ID to delete:")

        if st.button("Delete"):
            try:
                result = delD.dUpdate('student', st_id)
                st.success(result)
            except Exception as exx:
                st.error(f'Error: {exx}')

    elif delete_choice == "Course":
        st.subheader("Delete Data in Course")
        st_id = st.text_input("Enter the Course ID to delete:")

        if st.button("Delete"):
            try:
                result = delD.dUpdate('course', st_id)
                st.success(result)
            except Exception as exx:
                st.error(f'Error: {exx}')

    elif delete_choice == "Transaction":
        st.subheader("Delete Data in Transaction")
        st_id = st.text_input("Enter the Transaction ID to delete:")

        if st.button("Delete"):
            try:
                result = delD.dUpdate('trans', st_id)
                st.success(result)
            except Exception as exx:
                st.error(f'Error: {exx}')
