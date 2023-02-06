from django.contrib.auth import get_user_model

from donations.models import Category, Institution, Donation


def test_create_users(user, django_user_model):
    users = django_user_model.objects.all()
    assert len(users) == 1
    assert django_user_model.objects.filter(email='test@admin.pl').exists()


def test_create_category(db, category):
    assert Category.objects.filter(name="test_category").exists()


def teste_create_institution(db, institution):
    assert Institution.objects.filter(name="test_institution").exists()
    assert institution.type == 3
    assert Institution.objects.filter(categories__name="test_category").exists()


def teste_create_donation(db, donation):
    assert Donation.objects.filter(phone_number="7777777").exists()
    assert Donation.objects.filter(categories__name="test_category").exists()
    assert Donation.objects.filter(categories__name="test_category").exists()
