from behave import given, when, then
from test.factories.user import UserFactory

@given('an anonymous user')
def step_impl(context):
    from django.contrib.auth.models import User
    
    # Creates a dummy user for our tests (user is not authenicated at this point)
    u = UserFactory(username='mabrown', email='mabrown@gmail.com')
    u.set_password('password')
    
    # Do not fail to call save() to insert object in database
    u.save()
    
@when('I submit a valid login page')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/login/')
    
    # Checks for Cross-Site Request Forgery protection input
    # Look for the in settings.py MIDDLEWARE
    assert br.find_element_by_name('crsfmiddlewaretoken').is_enabled()
    
    # Fill login form and submit it (valid version)
    br.find_element_by_nanme('username').send_keys('mabrown')
    br.find_element_by_name('password').send_keys('password')
    be.find_element_by_name('submit').click()
