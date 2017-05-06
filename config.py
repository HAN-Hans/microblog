import os
besedir = os.path.abspath(os.path.dirname(__file__))


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(besedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(besedir, 'db_repository')


WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]


# 839: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds 
# significant overhead and will be disabled by default in the future.
#   Set it to True or False to suppress this warning.
#   'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
SQLALCHEMY_TRACK_MODIFICATIONS = True
    