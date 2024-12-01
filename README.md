# Recipe Management Application 🍲
A web-based application built with Flask and MySQL to manage and share recipes. This project allows users to authenticate, create, categorize, and upload recipes with images, fostering a collaborative cooking experience.

## Features
- User Authentication: Secure user registration and login system.
- Recipe Management: Add, view, and categorize recipes as "veg" or "non-veg."
- Allergen Tracking: Specify allergens for each recipe.
- Image Uploads: Upload images for recipes using Flask-Uploads.
- Dynamic Dashboard: Interactive and responsive user interface built with HTML, CSS, and Bootstrap.

## Technologies Used
- Backend
Framework: Flask (Python)
Database: MySQL (with mysql-connector for database connectivity)
- Frontend
HTML, CSS, and Bootstrap for a responsive and intuitive UI.
- File Management
Flask-Uploads for managing recipe image uploads.
- Version Control
Git for source control and collaboration.

## Getting Started
Prerequisites
  1. Basic knowledge of Python (if using a framework like Flask or Django).
  2. Familiarity with HTML, CSS, and Jinja templating.
  
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
   flask run     # any one of these can be used
   python app.py

  
7. Open your browser:
   Go to http://127.0.0.1:5000/
   (or) equivalent URL.

## Project Flow
   recipe-management-system/
├── templates/
│   ├── index.html        # Main template with form and layout
│   ├── add_recipe.html   # Form to add new recipes
│   ├── login.html        # Login page for users
│   ├── profile.html      # User profile details
│   ├── register.html     # Registration form
├── static/
│   ├── style.css         # CSS styling
├── app.py                # Flask server setup
├── recipes.db            # SQLite database for storing recipes and user data
├── README.md             # Project documentation

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
4. Make your changes and commit them:
   ```bash
   git commit -m 'Add new feature'
6. Push to the branch:
   ```bash
   git push origin feature-name
8. Submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.







   



