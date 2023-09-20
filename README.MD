
"Donation" is a Django-based application designed to facilitate the donation of items to charitable causes, with the added functionalities of user registration and login, as well as email confirmation. Here's a brief description of the app:

User Registration and Login: Users can create accounts, log in using their credentials, or utilize email confirmation for added security and protection against unauthorized access.

Adding Items for Donation: Users can easily add items they wish to donate to charitable causes. They can provide item descriptions, upload photos, and specify item availability.

Browsing Charitable Organizations: The app allows users to explore a list of available charitable organizations that accept donations. Users can choose where they want to donate their items.

Contacting Charities: Users can directly contact charitable organizations through an integrated messaging system to discuss donation details.

Email Confirmation: To ensure the validity and accuracy of user accounts, the app requires email confirmation during the registration process, enhancing user security and authenticity.

Notifications: Users receive notifications about new messages, the status of donated items, and other important updates to stay informed.

Donation History: Each user has access to their donation history, making it easy to track what and when they've contributed.

The "Donation" app connects individuals eager to help with charitable organizations in need of support, providing a transparent and secure platform for donating items to charitable causes. With email confirmation and other security measures in place, users can engage with the app with confidence, knowing their acts of kindness are directed where they're needed most.

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



