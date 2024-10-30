Movie Management
Create, Update, Delete, and Fetch Genres: Allows users to manage genre data, such as genre name and associations with movies.
Movie-Genre Relationship:
Each movie can belong to multiple genres.
Each genre can be associated with multiple movies.
GraphQL Queries and Mutations:
getMoviesByGenre: Retrieves a list of movies associated with a specific genre.
getGenreByMovie: Retrieves genres associated with a specific movie.
createGenre, updateGenre, deleteGenre: Add, modify, or delete genre data with validation for input data.
Project Structure
The project is divided into three main files:

app.py: Initializes the Flask server and sets up the GraphQL endpoint.
models.py: Defines SQLAlchemy models for the movie and genre tables, including the many-to-many relationship.
schema.py: Contains the GraphQL schema with queries and mutations for interacting with movie and genre data.
Setup Instructions
Prerequisites
Python 3.8+
MySQL or a compatible SQL database
Pip (Python package manager)
Installation Steps
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/movie-genre-management-api.git
cd movie-genre-management-api
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Set Up MySQL Database:

Create a database named movie_db (or any name you prefer).
Update the database URI in app.py:
python
Copy code
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/movie_db'
Initialize the Database:

Open a Python shell:
bash
Copy code
python
Run the following commands to create tables:
python
Copy code
from app import db
db.create_all()
Run the Flask Application:

bash
Copy code
python app.py
Access GraphiQL Interface:

Open a browser and go to http://localhost:5000/graphql to interact with the API using GraphiQL.
Sample GraphQL Queries and Mutations
Add a New Genre:

graphql
Copy code
mutation {
  createGenre(name: "Action") {
    id
    name
  }
}
Retrieve Movies by Genre:

graphql
Copy code
query {
  getMoviesByGenre(genreId: 1) {
    id
    title
    release_year
  }
}
Update a Genre:

graphql
Copy code
mutation {
  updateGenre(id: 1, name: "Adventure") {
    id
    name
  }
}
Delete a Genre:

graphql
Copy code
mutation {
  deleteGenre(id: 1) {
    id
    name
  }
}
