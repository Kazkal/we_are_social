from base import *
import dj_database_url

DEBUG = False

# Load the ClearDB connection details from the environment variable
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_ZXY4MBdKiY7v0c8o1DBwKmRl')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_V4miNGDi3sOjWuNukaRsifIr')

# Paypal environment variables
SITE_URL = 'code-institute-social-staging2.herokuapp.com/'
PAYPAL_NOTIFY_URL =  'code-institute-social-staging2.herokuapp.com/'
PAYPAL_RECEIVER_EMAIL = 'AuctionHouse@gmail.com'
