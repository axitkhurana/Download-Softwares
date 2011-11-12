CATEGORY_CHOICES = ( 
    ('Internet',(
        ('browser ','Browsers'),
        ('plugins','Plugins'),
        ('chat','Chat'),
    )),
    ('Security Software',(
        ('antivirus','Antivirus'),
        ('anti_spyware','Anti Spyware'),
        ('firewall','Firewall'),
    )),
    ('Multimedia',(
        ('media_players','Media Players'),
        ('converters','Converters'),
        ('plugins','Plugins'),
    )),
    ('Drivers',(
        ('audio_drivers','Audio Drivers'),
        ('laptop_drivers','Laptop Drivers'),
        ('network_drivers','Network Drivers'),
    )),
    ('Office',(
        ('office_suites','Office Suites'),
        ('dbms','DBMS'),
        ('business_apps','Business Apps'),
    )),
    ('Developer Tools',(
        ('compilers','Compilers'),
        ('web_development','Web Development'),
        ('ide_software','IDE Softwares'),
    )),
)

#('educational','Educational'),('file_transfer','File Transfer'),('system_tuning','System Tuning'))

OS_CHOICES = (('w','Windows'),('l','Linux'),('m','Mac'))

CATEGORY_LIST=[]
for k in CATEGORY_CHOICES:
    CATEGORY_LIST.append(('_'.join(k[0].split(' ')).lower(),k[0]))

CATEGORY_TUPLE=tuple(CATEGORY_LIST)

CATEGORY_DICT={}
for k in CATEGORY_CHOICES:
    CATEGORY_DICT[k[0]]=k[1]

DEFAULT_OS = 'w'
