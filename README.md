# Forum
### This is a dynamic web application built using Django framework in Python.

## Prerequisites
Before you begin, ensure you have the following tools installed on your system:

- Python (version 3.x)
- pip (Python package installer)
- Git
- PyCharm (optional but recommended)
  
## Installation
To install and run this application, follow these steps:

### 1. Clone the Repository:


    git clone https://github.com/Alewx123/Forum.git

### 2. Navigate to the Project Directory:

    cd 'your-repository'

### 3. Set Up a Virtual Environment (Optional but Recommended):

- If using PyCharm:

Open the project in PyCharm. PyCharm will detect the project's Python interpreter and suggest creating a virtual environment. Accept this suggestion to create a virtual environment for your project.

- If not using PyCharm:

Create a virtual environment using the following command:

    python -m venv venv

Activate the virtual environment:

- On Windows:
---------------------------------------------------------------
    venv\Scripts\activate

- On macOS and Linux:
---------------------------------------------------------------
    source venv/bin/activate

### 4. Install Dependencies:

Install the required dependencies using pip:

    pip install -r requirements.txt
    
### 5 .Configure Environment Variables (if necessary):

If your application requires environment variables, you can configure them in your development environment or directly in PyCharm.

### 6. Run the Application:

- If using PyCharm:

Run the Django server configuration provided by PyCharm. PyCharm will handle starting the development server.

- If not using PyCharm:

Start the development server using the following command:

    python manage.py runserver

### 7. Access the Application:

Once the development server is running, you can access the application at `http://localhost:8000` in your web browser.
