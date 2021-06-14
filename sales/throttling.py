from rest_framework.throttling import UserRateThrottle,AnonRateThrottle

class ProductRateThrottle(UserRateThrottle):
    scope = 'product'
