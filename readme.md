
# MongoDB CRUD Operations with Streamlit

This Streamlit application provides a user-friendly web interface to perform CRUD (Create, Read, Update, Delete) operations on a MongoDB database. The application allows users to interact with the database and manage data for students, courses, and transactions.

## Table of Contents

- [MongoDB CRUD Operations with Streamlit](#mongodb-crud-operations-with-streamlit)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [File Structure](#file-structure)
  - [Contributing](#contributing)
  - [License](#license)

## Features

- Insert data into student, course, and transaction collections.
- Read data from student, course, and transaction collections.
- Update data in student, course, and transaction collections.
- Delete data from student, course, and transaction collections.

## Requirements

- Python 3.11
- MongoDB instance
- Streamlit
- `validator_collection` for data validation
- `pymongo` for MongoDB interaction

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Tirumala2824/CRUD-Operations.git
    cd mongodb-crud-streamlit
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Create necessary Python files**:
    Ensure you have the following Python files in your project directory:
    - `insert.py`
    - `read.py`
    - `update.py`
    - `delete.py`

    These files should contain the logic for interacting with your MongoDB database.

## Usage

1. **Run the Streamlit application**:
    ```bash
    streamlit run app.py
    ```

2. **Interact with the application**:
    - Open your web browser and go to `http://localhost:8501`.
    - Use the sidebar to navigate between the different CRUD operations.
    - Fill in the required fields and execute the desired operations.

## File Structure

```
mongodb-crud-streamlit/
├── streamlit.py              # Main Streamlit application
├── modules/insert.py           # Insert data logic
├── modules/read.py             # Read data logic
├── modules/update.py           # Update data logic
├── modules/delete.py           # Delete data logic
├── requirements.txt    # List of required packages
└── README.md           # This README file
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

1. **Fork the repository**.
2. **Create a new branch**:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. **Commit your changes**:
    ```bash
    git commit -m 'Add some feature'
    ```
4. **Push to the branch**:
    ```bash
    git push origin feature/your-feature-name
    ```
5. **Open a pull request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

