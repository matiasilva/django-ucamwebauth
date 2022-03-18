import logging
from django.core.management import execute_from_command_line
from django.conf import settings

settings.configure(
    DEBUG=False,
    DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'test.db', }},
    TIME_ZONE='Europe/London',
    USE_TZ=True,
    SITE_ID=1,
    ROOT_URLCONF='ucamwebauth.urls',
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'ucamwebauth',
    ),
    AUTHENTICATION_BACKENDS=('ucamwebauth.backends.RavenAuthBackend', ),
    MIDDLEWARE=[
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware'
    ],
    UCAMWEBAUTH_LOGIN_URL='https://test.legacy.raven.cam.ac.uk/auth/authenticate.html',
    UCAMWEBAUTH_LOGOUT_URL='https://test.legacy.raven.cam.ac.uk/auth/logout.html',
    UCAMWEBAUTH_CERTS={
        901: """-----BEGIN CERTIFICATE-----
MIIDzTCCAzagAwIBAgIBADANBgkqhkiG9w0BAQQFADCBpjELMAkGA1UEBhMCR0Ix
EDAOBgNVBAgTB0VuZ2xhbmQxEjAQBgNVBAcTCUNhbWJyaWRnZTEgMB4GA1UEChMX
VW5pdmVyc2l0eSBvZiBDYW1icmlkZ2UxLTArBgNVBAsTJENvbXB1dGluZyBTZXJ2
aWNlIERFTU8gUmF2ZW4gU2VydmljZTEgMB4GA1UEAxMXUmF2ZW4gREVNTyBwdWJs
aWMga2V5IDEwHhcNMDUwNzI2MTMyMTIwWhcNMDUwODI1MTMyMTIwWjCBpjELMAkG
A1UEBhMCR0IxEDAOBgNVBAgTB0VuZ2xhbmQxEjAQBgNVBAcTCUNhbWJyaWRnZTEg
MB4GA1UEChMXVW5pdmVyc2l0eSBvZiBDYW1icmlkZ2UxLTArBgNVBAsTJENvbXB1
dGluZyBTZXJ2aWNlIERFTU8gUmF2ZW4gU2VydmljZTEgMB4GA1UEAxMXUmF2ZW4g
REVNTyBwdWJsaWMga2V5IDEwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBALhF
i9tIZvjYQQRfOzP3cy5ujR91ZntQnQehldByHlchHRmXwA1ot/e1WlHPgIjYkFRW
lSNcSDM5r7BkFu69zM66IHcF80NIopBp+3FYqi5uglEDlpzFrd+vYllzw7lBzUnp
CrwTxyO5JBaWnFMZrQkSdspXv89VQUO4V4QjXV7/AgMBAAGjggEHMIIBAzAdBgNV
HQ4EFgQUgjC6WtA4jFf54kxlidhFi8w+0HkwgdMGA1UdIwSByzCByIAUgjC6WtA4
jFf54kxlidhFi8w+0HmhgaykgakwgaYxCzAJBgNVBAYTAkdCMRAwDgYDVQQIEwdF
bmdsYW5kMRIwEAYDVQQHEwlDYW1icmlkZ2UxIDAeBgNVBAoTF1VuaXZlcnNpdHkg
b2YgQ2FtYnJpZGdlMS0wKwYDVQQLEyRDb21wdXRpbmcgU2VydmljZSBERU1PIFJh
dmVuIFNlcnZpY2UxIDAeBgNVBAMTF1JhdmVuIERFTU8gcHVibGljIGtleSAxggEA
MAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEEBQADgYEAsdyB+9szctHHIHE+S2Kg
LSxbGuFG9yfPFIqaSntlYMxKKB5ba/tIAMzyAOHxdEM5hi1DXRsOok3ElWjOw9oN
6Psvk/hLUN+YfC1saaUs3oh+OTfD7I4gRTbXPgsd6JgJQ0TQtuGygJdaht9cRBHW
wOq24EIbX5LquL9w+uvnfXw=
-----END CERTIFICATE-----
""",
        900: """-----BEGIN CERTIFICATE-----
MIID1jCCAr4CCQCeVWORbpJWcTANBgkqhkiG9w0BAQsFADCBrDELMAkGA1UEBhMC
VUsxFzAVBgNVBAgMDkNhbWJyaWRnZXNoaXJlMRIwEAYDVQQHDAlDYW1icmlkZ2Ux
IDAeBgNVBAoMF1VuaXZlcnNpdHkgb2YgQ2FtYnJpZGdlMSgwJgYDVQQLDB9Vbml2
ZXJzaXR5IEluZm9ybWF0aW9uIFNlcnZpY2VzMSQwIgYDVQQDDBt0ZXN0LmxlZ2Fj
eS5yYXZlbi5jYW0uYWMudWswHhcNMjEwNzEzMDc0NzQzWhcNMjEwODEyMDc0NzQz
WjCBrDELMAkGA1UEBhMCVUsxFzAVBgNVBAgMDkNhbWJyaWRnZXNoaXJlMRIwEAYD
VQQHDAlDYW1icmlkZ2UxIDAeBgNVBAoMF1VuaXZlcnNpdHkgb2YgQ2FtYnJpZGdl
MSgwJgYDVQQLDB9Vbml2ZXJzaXR5IEluZm9ybWF0aW9uIFNlcnZpY2VzMSQwIgYD
VQQDDBt0ZXN0LmxlZ2FjeS5yYXZlbi5jYW0uYWMudWswggEiMA0GCSqGSIb3DQEB
AQUAA4IBDwAwggEKAoIBAQCpHtVwwK0VAcMAKTdKIyG7OgQjha9U1+a+3gpQMolP
dhjssTh1fs3+EfixZY7wb92+f+vqOV5Hu6n55Y7LXArKoqLshVfyR1uOjB5/UlFi
FFS0LG7L1O0wMKbzDLJ94G3UNwBXOD+KFL5zcfCAzZNFqCentiHO08LfX/tr7+q6
DaMuIh8RQpOfowDsIhaiB2YtK1A+B6dJxnHAq+a6sX7ZBwtZoWyBtUalrNMyGGN4
eaEuRUIL9ilCksI7Nb4X91dyryO/L/QI4XQtbaz7j8K8hSJJ4MGb6Boc1Ov69ZEk
GY322DIS84WfeSem6Ujy4TyZSkmUPOiiT9bFN2MUomKJAgMBAAEwDQYJKoZIhvcN
AQELBQADggEBAGg+4IDXLtypkoxteb8KQWvt11d4xMljNmJ6k20gBpPEd5nzocQ7
MeSv9l66NrlsHCJ+BwJjJDgIS4dwkofu+hmkLNE6/d3uHugKazv3ySw+g5oIcLNB
vjgIhbD4krVSh4LvZxQR+sffQnrkzSSAB6/6QMTtAcor61A+0Xo4OhvPHMWOcS9I
rT57/9Slr9eEtSUcpKs+cyY9G6t9GxdC627diApsw+mG2X1raFIROXuXMzQQysEI
6SzxRFof2AutEgcyYRERLbHIqH5K1EgjLWs3s4PujOhTvhUoJZ7OlTjNmzNrFXKj
9nU4Uo6qClXDVKK7JecERsAfIedKgFGbQqY=
-----END CERTIFICATE-----
"""},
    UCAMWEBAUTH_TIMEOUT=60,
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                # insert your TEMPLATE_DIRS here
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                    # list if you haven't customized them:
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.debug',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
)

logging.basicConfig()
execute_from_command_line(['', 'test'])
