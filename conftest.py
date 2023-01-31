import pytest

from donations.models import Category, Institution, Donation


@pytest.fixture
def user(db, django_user_model):
    yield django_user_model.objects.create_user(email="test@admin.pl", first_name="Jan", last_name="Test",
                                                password='Test12345')

@pytest.fixture
def category(db):
    yield Category.objects.create(name="test_category")

@pytest.fixture
def institution(db, category):
    institution = Institution.objects.create(name="test_institution", type=3, description='Opis test')
    institution.categories.add(category)
    yield institution


@pytest.fixture
def donation(db, category, institution, user):
    donation = Donation.objects.create(quantity=8, institution=institution, address='Test', phone_number="7777777",
                                       city="test", zip_code="11-111", pick_up_date="2022-12-12", pick_up_time="12:30",
                                       user=user)
    donation.categories.add(category)
    yield donation


