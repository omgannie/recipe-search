# TODOS
[ ] setup basic models
[ ] setup DRF api backend endpoints
[ ] build out service layers (if needed)
[ ] setup additional models (Category, Tag, Comment, Like, Save)

Recipe search by ingredients app

Models
Recipe
* Title, method, ingredients, yield size, categories
Ingredient
* Name, measurement
User
* Email, password, recipes
Category
* Name



Endpoints
GET /recipes?search_terms=,&search_type=‘’
* Search type choices: ingredient, category

Return a list of recipes that match search terms

POST /recipes
* Create a new recipe by user
* Title, ingredients, method

POST /users
* Create a new user
* Email, password

POST /token
* Create a token for a returning user logging in


## Endpoints
* /users
    - POST - new sign up user
    - PUT - update user details
    - DELETE - delete user from system
* /token
    - POST - create new access token for session, authenticate user
    - DELETE - delete token for session, logout user
* /recipes
    - GET - fetch all recipes matching search params (search by ingredients or name)
    - POST - create new recipe
    - PUT - update recipe by id
    - DELETE - delete by id

...eventually add
* /categories
* /tags

# get it runnin'
`$ pip install -r requirements.txt`
`$ python3 manage.py migrate`
`$ python3 manage.py runserver`