# Flask Blogly

Flask Blogly is a simple blogging platform built using Flask, a lightweight web framework for Python. It allows users to create accounts, write posts, and tag them with relevant topics.

## Installation

1. **Clone the Repository:** Navigate to the desired directory and clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. **Navigate to the Project Directory:** Change your current directory to the project directory:

    ```bash
    cd flask-blogly
    ```

3. **Install Dependencies:** Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Environment Variables:** Create a `.env` file in the project root directory and set the following environment variables:

    ```plaintext
    FLASK_APP=app.py
    FLASK_ENV=development
    DATABASE_URL=<your_database_url>
    ```

5. **Initialize the Database:** Run the following command to initialize the database:

    ```bash
    flask init-db
    ```

6. **Run the Application:** Start the Flask application by running:

    ```bash
    flask run
    ```

7. **Access the Application:** Open your web browser and navigate to [http://localhost:5000](http://localhost:5000) to access the application.

## Usage

- **Sign Up:** Register for a new account by providing your details.
- **Log In:** Log in with your username and password to access the platform.
- **Create Post:** Click on the "New Post" button to create a new blog post. Provide a title, content, and select relevant tags.
- **Edit Post:** Users can edit their own posts by clicking on the "Edit" button next to the post.
- **View User Profiles:** Click on a user's name to view their profile page, displaying their information and authored posts.

## Technologies Used

- **Flask:** Web framework for building the application.
- **SQLAlchemy:** ORM for interacting with the database.
- **SQLite:** Lightweight relational database used for storing data.
- **HTML/CSS:** Frontend for the web interface.
- **Bootstrap:** CSS framework for styling the application.

## Contributors

- Ricardo Albornoz

