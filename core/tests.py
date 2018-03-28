import pytest

from django.core.management import call_command


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'core/fixtures/emoji.json')


@pytest.mark.django_db
def test_random_emoji():
    from core.views import TaskSubmitView
    TaskSubmitView.get_random_emoji()
