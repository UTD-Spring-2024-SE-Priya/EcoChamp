import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from ecochamp.forms import SignUpForm, CustomAuthenticationForm

@pytest.mark.django_db
def test_start_view(client):
    url = reverse('start')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_home_view(client, authenticated_user):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
    assert 'random_statistic' in response.context
    assert 'corresponding_challenge' in response.context

@pytest.mark.django_db
def test_signup_view(client):
    url = reverse('signup')
    response = client.get(url)
    assert response.status_code == 200

    form_data = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password1': 'testpassword',
        'password2': 'testpassword',
    }
    response = client.post(url, form_data)
    assert response.status_code == 302  # Redirect after successful signup
    assert User.objects.filter(username='testuser').exists()

@pytest.mark.django_db
def test_profile_view(client, authenticated_user):
    url = reverse('profile')
    client.force_login(authenticated_user)
    response = client.get(url)
    assert response.status_code == 200
    assert authenticated_user.username in str(response.content)

@pytest.mark.django_db
def test_avatar_view(client):
    url = reverse('avatar')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_help_view(client):
    url = reverse('help')
    response = client.get(url)
    assert response.status_code == 200


@pytest.fixture
def authenticated_user(client):
    user = User.objects.create_user(username='testuser', password='testpass')
    client.force_login(user)
    return user