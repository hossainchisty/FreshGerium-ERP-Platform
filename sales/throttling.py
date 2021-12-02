from rest_framework.throttling import UserRateThrottle


class SaleRateThrottle(UserRateThrottle):
    scope = 'sale'
