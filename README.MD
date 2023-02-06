An app to donate things to charity


# Donations
Users can supports charity institutions.

# Main assumptions of the project:
* User receives account confirmation email.
* User can reset password if it was forgotten.
User can supply donations to chosen institutions with supported categories.
User can edit his information, change have to be confirmed with password.
User can see all of his donations and he confirm if it was taken.
Admin can add/modify other users and database models.
# Installation:
Clone the repository
$ git clone 
Create virtual environment to install dependencies and activate it:
$ python -m venv venv
$ source venv/bin/activate
# Install the dependencies:
(venv)$ pip install -r requirements.txt
Remember to fill up environmental variables pointed out in env/.env-default.txt. File path has to be env/.env ( same dir as .env-default.txt ).

Make migrations and apply them:
(venv)$ python manage.py makemigrations home
(venv)$ python manage.py migrate
(venv)$ python manage.py createsuperuser
Fill up database through admin panel.
