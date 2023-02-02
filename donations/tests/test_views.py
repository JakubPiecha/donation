from django.contrib.auth import login, authenticate
from django.core import mail
from django.urls import reverse

from donations.models import Donation


def test_home_view(db, client, donation):
    url = reverse('donations:home')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Zacznij pomagać' in response.content.decode('UTF-8')
    assert '<em>8</em>' in response.content.decode('UTF-8')
    assert '<em>1</em>' in response.content.decode('UTF-8')
    assert '<div class="title">test_institution</div>' in response.content.decode('UTF-8')
    assert 'index.html' in (t.name for t in response.templates)


def test_add_donation_view_get_no_login(db, client, user):
    url = reverse('donations:add_donation')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('donations:login'))


def test_add_donation_view_get_login(db, client, user):
    client.force_login(user)
    url = reverse('donations:add_donation')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Zaznacz co chcesz oddać:' in response.content.decode('UTF-8')
    assert 'form.html' in (t.name for t in response.templates)


def test_add_donation_view_post(db, client, user, institution, category):
    client.force_login(user)
    url = reverse('donations:add_donation')
    data = {"quantity": 6, 'institution': institution.id, 'categories': category.id, 'address': 'Test',
            'phone_number': "8888888", 'city': "test", 'zip_code': "11-111", 'pick_up_date': "2023-12-12",
            'pick_up_time': "12:45", 'user': user.id}
    response = client.post(url, data)
    assert response.status_code == 302
    assert Donation.objects.filter(phone_number="8888888").exists()
    assert response.url.startswith(reverse('donations:confirmation'))


def test_register_view_get(db, client):
    url = reverse('donations:register')
    response = client.get(url)
    assert response.status_code == 200
    assert '<h2>Załóż konto</h2>' in response.content.decode('UTF-8')
    assert 'register.html' in (t.name for t in response.templates)


def test_register_view_post(db, client, django_user_model):
    url = reverse('donations:register')
    data = {'first_name': 'Jan', 'last_name': 'Kowalski', 'email': 'z@z.pl', 'password1': 'Test12345',
            'password2': 'Test12345'}
    response = client.post(url, data)
    user = django_user_model.objects.get(last_name='Kowalski')
    assert len(mail.outbox) == 1
    assert response.status_code == 302
    assert response.url.startswith(reverse('donations:login'))
    assert django_user_model.objects.get(last_name='Kowalski')
    assert user.is_active == False
    url = mail.outbox[0].body.split()[-1]
    response = client.get(url)
    user.refresh_from_db()
    assert user.is_active == True
    assert response.status_code == 302
    assert response.url.startswith(reverse('donations:login'))


def test_register_view_post_no_data(db, client, django_user_model):
    url = reverse('donations:register')
    data = {'first_name': 'Jan', 'last_name': 'Kowalski', 'email': '', 'password1': '',
            'password2': ''}
    response = client.post(url, data)
    assert response.status_code == 200
    assert 'To pole jest wymagane.' in response.content.decode('UTF-8')
    assert django_user_model.objects.filter(last_name='Kowalski').exists() == False


def test_login_view_get(db, client):
    url = reverse('donations:login')
    response = client.get(url)
    assert response.status_code == 200
    assert '<h2>Zaloguj się</h2>' in response.content.decode('UTF-8')
    assert 'login.html' in (t.name for t in response.templates)


def test_login_view_post(db, client, user):
    url = reverse('donations:login')
    data = {'username': 'test@admin.pl', 'password': 'Test12345'}
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url.startswith(reverse('donations:home'))


def test_login_view_post_wrong_password(db, client, user):
    url = reverse('donations:login')
    data = {'username': 'test@admin.pl', 'password': 'aaa'}
    response = client.post(url, data)
    assert response.status_code == 200
    assert 'Wprowadź poprawne wartości pól email oraz hasło. Uwaga: wielkość liter ma znaczenie.' in response.content.decode(
        'UTF-8')


def test_login_view_post_no_password(db, client, user):
    url = reverse('donations:login')
    data = {'username': 'test@admin.pl', 'password': ''}
    response = client.post(url, data)
    assert response.status_code == 200
    assert 'To pole jest wymagane.' in response.content.decode('UTF-8')


def test_login_view_post_no_user(db, client):
    url = reverse('donations:login')
    data = {'username': 't@a.pl', 'password': 'wasd'}
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url.startswith(reverse('donations:register'))


def test_confirmation_view_get(db, client, user):
    client.force_login(user)
    url = reverse('donations:confirmation')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Dziękujemy za przesłanie formularza' in response.content.decode('UTF-8')
    assert 'form-confirmation.html' in (t.name for t in response.templates)


def test_confirmation_view_get_no_login(db, client, user):
    url = reverse('donations:confirmation')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('donations:login'))


def test_profile_view_get(db, client, user, donation):
    client.force_login(user)
    url = reverse('donations:profile')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Podsumowanie Twoich darowizn:' in response.content.decode('UTF-8')
    assert '<h1> Liczba worków: 8 </h1>' in response.content.decode('UTF-8')
    assert '<h1> Dla: test_institution </h1>' in response.content.decode('UTF-8')
    assert 'profile.html' in (t.name for t in response.templates)


def test_profile_view_get_no_login(db, client, user, donation):
    url = reverse('donations:profile')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('donations:login'))


def test_confirm_taken_view_get(db, client, user, donation):
    client.force_login(user)
    url = reverse('donations:confirm-taken-donation', kwargs={'pk': donation.id})
    response = client.get(url)
    assert response.status_code == 200
    assert 'Potwierdzasz przekazanie darowizny:' in response.content.decode('UTF-8')
    assert '<h1> Liczba worków: 8 </h1>' in response.content.decode('UTF-8')
    assert '<h1> Dla: test_institution </h1>' in response.content.decode('UTF-8')
    assert 'confirm--taken-donation.html' in (t.name for t in response.templates)


def test_confirm_taken_view_post(db, client, user, donation):
    client.force_login(user)
    url = reverse('donations:confirm-taken-donation', kwargs={'pk': donation.id})
    response = client.post(url)
    assert response.status_code == 302
    assert Donation.objects.get(is_taken=True)
    assert response.url.startswith(reverse('donations:profile'))


def test_edit_profile_view_get(db, client, user):
    client.force_login(user)
    url = reverse('donations:edite-profile', kwargs={'pk': user.id})
    response = client.get(url)
    assert response.status_code == 200
    assert 'Edycja danych' in response.content.decode('UTF-8')
    assert f'{user.first_name}' in response.content.decode('UTF-8')
    assert 'edite-profile.html' in (t.name for t in response.templates)


def test_edit_profile_view_post(db, client, user, django_user_model):
    client.force_login(user)
    data = {'first_name': 'Adaś', 'email': 'a@a.pl', 'validation_pass': 'Test12345'}
    url = reverse('donations:edite-profile', kwargs={'pk': user.id})
    response = client.post(url, data)
    assert response.status_code == 302
    assert django_user_model.objects.get(first_name='Adaś')
    assert response.url.startswith(reverse('donations:profile'))


def test_edit_profile_view_post_no_password(db, client, user, django_user_model):
    client.force_login(user)
    data = {'first_name': 'Adaś', 'email': 'a@a.pl', 'validation_pass': ''}
    url = reverse('donations:edite-profile', kwargs={'pk': user.id})
    response = client.post(url, data)
    assert response.status_code == 200
    assert 'To pole jest wymagane' in response.content.decode('UTF-8')
    assert django_user_model.objects.get(first_name='Jan')


def test_edit_profile_view_post_wrong_password(db, client, user, django_user_model):
    client.force_login(user)
    data = {'first_name': 'Adaś', 'email': 'a@a.pl', 'validation_pass': 'aasd'}
    url = reverse('donations:edite-profile', kwargs={'pk': user.id})
    response = client.post(url, data)
    assert response.status_code == 200
    assert 'Błędne hasło' in response.content.decode('UTF-8')
    assert django_user_model.objects.get(first_name='Jan')


def test_change_password_view_get(db, client, user):
    client.force_login(user)
    url = reverse('donations:change-password')
    response = client.get(url)
    assert response.status_code == 200
    assert '<h2>Zmień hasło</h2>' in response.content.decode('UTF-8')
    assert 'change-password.html' in (t.name for t in response.templates)


def test_change_password_view_post(db, client, user):
    client.force_login(user)
    data = {'old_password': 'Test12345', 'new_password1': 'Test123456', 'new_password2': 'Test123456'}
    url = reverse('donations:change-password')
    response = client.post(url, data)
    assert response.status_code == 302
    assert authenticate(email='test@admin.pl', password='Test123456')
    assert response.url.startswith(reverse('donations:profile'))


def test_change_password_view_post_wrong_pass2(db, client, user):
    client.force_login(user)
    data = {'old_password': 'Test12345', 'new_password1': 'Test123456', 'new_password2': 'Test12'}
    url = reverse('donations:change-password')
    response = client.post(url, data)
    assert response.status_code == 200
    assert 'Hasła w obu polach nie są zgodne' in response.content.decode('UTF-8')
    # assert authenticate(email='test@admin.pl', password='Test12345')


def test_change_password_view_post_wrong_old_password(db, client, user):
    client.force_login(user)
    data = {'old_password': 'Test123456', 'new_password1': 'Test123456', 'new_password2': 'Test123456'}
    url = reverse('donations:change-password')
    response = client.post(url, data)
    assert response.status_code == 200
    assert 'Podane stare hasło jest niepoprawne. Proszę podać je jeszcze raz.' in response.content.decode('UTF-8')
    assert authenticate(email='test@admin.pl', password='Test12345')


def test_change_password_view_post_no_data(db, client, user):
    client.force_login(user)
    data = {'old_password': '', 'new_password1': '', 'new_password2': ''}
    url = reverse('donations:change-password')
    response = client.post(url, data)
    assert response.status_code == 200
    assert 'To pole jest wymagane.' in response.content.decode('UTF-8')
    assert authenticate(email='test@admin.pl', password='Test12345')
