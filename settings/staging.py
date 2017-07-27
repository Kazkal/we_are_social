from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_ZXY4MBdKiY7v0c8o1DBwKmRl')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_V4miNGDi3sOjWuNukaRsifIr')

# Paypal environment variables
SITE_URL = 'code-institute-social-staging2.herokuapp.com/'
PAYPAL_NOTIFY_URL =  'code-institute-social-staging2.herokuapp.com/'
PAYPAL_RECEIVER_EMAIL = 'AuctionHouse@gmail.com'
