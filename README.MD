An app to donate things to charity

## Technologies Used

- python 3.10

# Donations
Users can supports charity institutions.

# Main assumptions of the project:
* User receives account confirmation email.
* User can reset password if it was forgotten.
* User can supply donations to chosen institutions with supported categories.
* User can edit his information, change have to be confirmed with password.
* User can see all of his donations and he confirm if it was taken.
* Admin can add/modify other users and database models.
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
'''
$ python manage.py makemigrations home
$ python manage.py migrate
$ python manage.py createsuperuser
'''
![image](https://user-images.githubusercontent.com/114153071/216967391-b20a0378-f246-4582-aa44-bcb650226544.png)


Fill up database through admin panel.
