An app to donate things to charity
![image](https://user-images.githubusercontent.com/114153071/216968039-c42a74a3-b5c3-46ae-ad32-a5955ee83ff1.png)


# TESTS COVERAGE:

![Zrzut ekranu z 2023-02-07 09-33-20](https://user-images.githubusercontent.com/114153071/217201065-04cb1093-b382-446b-a1ed-8bb65fc2fce0.png)




# Technologies Used

- python 3.10
- Django 4.1.5


# Donations
Users can support charity institutions.

# Main assumptions of the project:
* User receives account confirmation email.
* User can reset password if it was forgotten.
* User can supply donations to chosen institutions with supported categories.
* User can edit his information, change have to be confirmed with password.
* User can see all of his donations and he confirm if it was taken.
* Anyone can send a message using the contact form.
* Admin can add/modify other users and database models.
# Installation:
- Clone the repository
- `git clone git@github.com:JakubPiecha/donation.git`
- Create virtual environment to install dependencies and activate it:
- `python -m venv venv`
- `source venv/bin/activate`
# Install the dependencies:
- `pip install -r requirements.txt`
- Remember to fill up environmental variables pointed out in env/.env-default.txt.
- File path has to be env/.env ( same dir as .env-default.txt ).

Make migrations and apply them:
```
python manage.py migrate
python manage.py runserver
```

Fill up database through admin panel.



