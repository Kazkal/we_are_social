from base import *

DEBUG=True
INSTALLED_APPS.append('debug_toolbar')

MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

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
SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL='http://bdccdcba.ngrok.io/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL='AuctionHouse@gmail.com'
