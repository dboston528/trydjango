# To start the application:

Activate the virtual environment run

`source bin/activate`

Change the directory to the project folder and run

`cd src`

Start server run

`python manage.py runserver`

# Creating a new app:

Run the following code in the src directory:

`python manage.py startapp [app name of your choice]`

# Making chages to models:

Everytime you make a change to a model run the following code:

`python manage.py makemigrations`
then
`python manage.py migrate`

