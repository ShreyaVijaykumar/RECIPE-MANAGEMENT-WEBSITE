from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Configure MySQL connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",  # Your MySQL server host
        user="root",       # Your MySQL username
        password="Student@123",  # Your MySQL password
        database="recipe_manager"  # The database you're using
    )

# Initialize the database and create tables if they don't exist
def init_db():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Create Users Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) UNIQUE NOT NULL,
                email VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
            )
        ''')
        # Create Recipes Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS recipes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                type VARCHAR(255) NOT NULL,
                allergens TEXT,
                ingredients TEXT NOT NULL,
                description TEXT NOT NULL,
                image TEXT
            )
        ''')
        conn.commit()
        cursor.close()
        conn.close()
    except Error as e:
        print("Error while initializing the database:", e)

# Route to display all recipes
@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM recipes')
        recipes = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('index.html', recipes=recipes)
    except Error as e:
        print(f"Error: {e}")
        return "Database connection error."

# Route to add a new recipe
@app.route('/add_recipe.html', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        # Fetch form data
        name = request.form.get('name')
        type_ = request.form.get('type')
        allergens = request.form.get('allergens')
        ingredients = request.form.get('ingredients')
        description = request.form.get('description')
        image = request.form.get('image')  # Assuming this is a URL to an image

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Insert recipe data into the database
            cursor.execute(''' 
                INSERT INTO recipes (name, type, allergens, ingredients, description, image)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (name, type_, allergens, ingredients, description, image))
            conn.commit()

            cursor.close()
            conn.close()
            return redirect(url_for('index'))  # Redirect back to the homepage to view all recipes
        except Error as e:
            print(f"Error: {e}")
            return "Error adding recipe."

    return render_template('add_recipe.html')  # Render the form to add a new recipe

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
            user = cursor.fetchone()
            cursor.close()
            conn.close()

            if user:
                return redirect(url_for('index'))
            else:
                return "Invalid login details."
        except Error as e:
            print(f"Error: {e}")
            return "Database connection error."

    return render_template('login.html')

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (username, email, password)
                VALUES (%s, %s, %s)
            ''', (username, email, password))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('login'))
        except Error as e:
            print(f"Error: {e}")
            return "Error registering user."

    return render_template('register.html')

# Route for user profile (without sessions)
@app.route('/profile')
def profile():
    return redirect(url_for('login'))

if __name__ == '__main__':
    init_db()  # Initialize the database when the app starts
    app.run(debug=True)
