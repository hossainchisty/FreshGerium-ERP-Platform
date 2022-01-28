'''
In Bangladesh, we have offices in all eight administrative divisions. These divisions are divided into 64 districts.
'''
DISTRICTS = (
    ('dhaka', 'Dhaka'),
    ('faridpur', 'Faridpur'),
    ('gazipur', 'Gazipur'),
    ('gopalganj', 'Gopalganj'),
    ('jamalpur', 'Jamalpur'),
    ('kishoreganj', 'Kishoreganj'),
    ('madaripur', 'Madaripur'),
    ('manikganj', 'Manikganj'),
    ('munshiganj', 'Munshiganj'),
    ('narayanganj', 'Narayanganj'),
    ('narsingdi', 'Narsingdi'),
    ('netrokona', 'Netrokona'),
    ('rajbari', 'Rajbari'),
    ('shariatpur', 'Shariatpur'),
    ('sherpur', 'Sherpur'),
    ('tangail', 'Tangail'),
    ('bogra', 'Bogra'),
    ('joypurhat', 'Joypurhat'),
    ('naogaon', 'Naogaon'),
    ('natore', 'Natore'),
    ('nawabganj', 'Nawabganj'),
    ('pabna', 'Pabna'),
    ('rajshahi', 'Rajshahi'),
    ('sirajganj', 'Sirajganj'),
    ('dinajpur', 'Dinajpur'),
    ('gaibandha', 'Gaibandha'),
    ('kurigram', 'Kurigram'),
    ('lalmonirhat', 'Lalmonirhat'),
    ('nilphamari', 'Nilphamari'),
    ('panchagarh', 'Panchagarh'),
    ('rangpur', 'Rangpur'),
    ('thakurgaon', 'Thakurgaon'),
    ('barguna', 'Barguna'),
    ('barisal', 'Barisal'),
    ('bhola', 'Bhola'),
    ('jhalokati', 'Jhalokati'),
    ('patuakhali', 'Patuakhali'),
    ('pirojpur', 'Pirojpur'),
    ('bandarban', 'Bandarban'),
    ('brahmanbaria', 'Brahmanbaria'),
    ('chandpur', 'Chandpur'),
    ('chittagong', 'Chittagong'),
    ('comilla', 'Comilla'),
    ('cox\'s bazar', 'Cox\'s bazar'),
    ('feni', 'Feni'),
    ('khagrachhari', 'Khagrachhari'),
    ('lakshmipur', 'Lakshmipur'),
    ('noakhali', 'Noakhali'),
    ('rangamati', 'Rangamati'),
    ('habiganj', 'Habiganj'),
    ('moulvibazar', 'Moulvibazar'),
    ('sunamganj', 'Sunamganj'),
    ('sylhet', 'Sylhet'),
    ('bagerhat', 'Bagerhat'),
    ('chuadanga', 'Chuadanga'),
    ('jessore', 'Jessore'),
    ('jhenaidah', 'Jhenaidah'),
    ('khulna', 'Khulna'),
    ('kushtia', 'Kushtia'),
    ('magura', 'Magura'),
    ('meherpur', 'Meherpur'),
    ('narail', 'Narail'),
    ('satkhira', 'Satkhira'),
)


'''
The administrative structure of Bangladesh currently comprises eight divisions.

Barishal, Chattogram, Dhaka, Khulna, Rajshahi, Rangpur, Mymensingh and Sylhet.
'''
DIVISIONS = (
    ('dhaka', 'Dhaka'),
    ('sylhet', 'Sylhet'),
    ('barishal', 'Barishal'),
    ('chattogram', 'Chattogram'),
    ('khulna', 'Khulna'),
    ('rajshahi', 'Rajshahi'),
    ('rangpur', 'Rangpur'),
    ('mymensingh', 'Mymensingh'),
)


ACCOUNT_STATUS_CHOICE = (("open", "Open"), ("close", "Close"))

ACCOUNT_TYPE = (
    ('savings account', 'Savings Account'),
    ('current account', 'Current Account'),
    ('fixed Deposit account', 'Fixed Deposit Account'),
    ('recurring Deposit account', 'Recurring Deposit Account'),
)

INDUSTRYCHOICES = (
    ("ADVERTISING", "ADVERTISING"),
    ("AGRICULTURE", "AGRICULTURE"),
    ("APPAREL & ACCESSORIES", "APPAREL & ACCESSORIES"),
    ("AUTOMOTIVE", "AUTOMOTIVE"),
    ("BANKING", "BANKING"),
    ("BIOTECHNOLOGY", "BIOTECHNOLOGY"),
    ("BUILDING MATERIALS & EQUIPMENT", "BUILDING MATERIALS & EQUIPMENT"),
    ("CHEMICAL", "CHEMICAL"),
    ("COMPUTER", "COMPUTER"),
    ("EDUCATION", "EDUCATION"),
    ("ELECTRONICS", "ELECTRONICS"),
    ("ENERGY", "ENERGY"),
    ("ENTERTAINMENT & LEISURE", "ENTERTAINMENT & LEISURE"),
    ("FINANCE", "FINANCE"),
    ("FOOD & BEVERAGE", "FOOD & BEVERAGE"),
    ("GROCERY", "GROCERY"),
    ("HEALTHCARE", "HEALTHCARE"),
    ("INSURANCE", "INSURANCE"),
    ("LEGAL", "LEGAL"),
    ("MANUFACTURING", "MANUFACTURING"),
    ("PUBLISHING", "PUBLISHING"),
    ("REAL ESTATE", "REAL ESTATE"),
    ("SERVICE", "SERVICE"),
    ("SOFTWARE", "SOFTWARE"),
    ("SPORTS", "SPORTS"),
    ("TECHNOLOGY", "TECHNOLOGY"),
    ("TELECOMMUNICATIONS", "TELECOMMUNICATIONS"),
    ("TELEVISION", "TELEVISION"),
    ("TRANSPORTATION", "TRANSPORTATION"),
    ("VENTURE CAPITAL", "VENTURE CAPITAL"),
)


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
