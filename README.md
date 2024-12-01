# RECIPE-MANAGEMENT-WEBSITE
A web-based application built with Flask and MySQL to manage and share recipes. Features include user authentication, recipe categorization, and image uploads.
## Features
- User registration and login.
- Add, view, and manage recipes.
- Filter recipes by type (e.g., veg, non-veg).
- Upload and display recipe images.
- User profile management.
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ShreyaVijaykumar/RECIPE-MANAGEMENT-WEBSITE.git
   
2. Navigate to the project directory:
   ```bash
   cd recipe_manager
   
3. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
5. Set up the database:
    . Create a MySQL database.
    . Update the config.py file with your database credentials.
    . Initialize the database by running the setup_db.py script.
   ```bash
    python setup_db.py

6. Start the application:
   ```bash
   flask run

7. Open your browser and go to http://127.0.0.1:5000/
   
8. Contributing
## Contributing
Contributions are welcome! Feel free to fork this repository and create a pull request.

9. License
## License
This project is licensed under the MIT License - see the LICENSE file for details.







   



