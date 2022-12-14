# Updates in this fork

This fork simply enables the use of custom user models as opposed to being fixed to Django's default 'auth.User' model, thanks to a solution proposed by an [issue raised](https://gitlab.developers.cam.ac.uk/uis/devops/django/ucamwebauth). The 'raven_for_life' attribute is thus available at 'user.userprofile.raven_for_life' for any generic user.


# Introduction

django-ucamwebauth is a library which provides use of Cambridge University's 
[Raven authentication](http://raven.cam.ac.uk/) for [Django](https://www.djangoproject.com/). It provides a Django 
authentication backend which can be added to `AUTHENTICATION_BACKENDS` in the Django `settings` module.

## Use

Install django-ucamwebauth using pip:

```bash
pip install django-ucamwebauth
```

Then you can enable it within your Django project's settings.py:

```python
AUTHENTICATION_BACKENDS = (
    'ucamwebauth.backends.RavenAuthBackend',
    'django.contrib.auth.backends.ModelBackend'
)
```

This allows both normal Django login and Raven login.

You should then enable the URLs for ucamwebauth:

````python
#Django 1.11
urlpatterns = [
    ...
    url(r'', include('ucamwebauth.urls')),
    ...
]

#Django >=2.0
urlpatterns = [
    ...
    path(r'', include('ucamwebauth.urls')),
    ...
]
````

## Minimum Config Settings

You then need to configure the app's settings. Raven has a live and test environments, the URL and certificate details 
are given below.

There are four minimum config settings:

```
UCAMWEBAUTH_LOGIN_URL: a string representing the URL for the Raven login redirect.
UCAMWEBAUTH_LOGOUT_URL: a string representing the logout URL for Raven.
UCAMWEBAUTH_RETURN_URL: the URL of your app which the Raven service should return the user to after authentication.
    (Default is generated automatically from the urlconf)
UCAMWEBAUTH_LOGOUT_REDIRECT: a string representing the URL to where the user is redirected when she logs out of the app
    (Default to '/').
UCAMWEBAUTH_NOT_CURRENT: a boolean value representing if raven users that are currently not members of the university
    should be allowed to log in (Default to False). More info: http://www.ucs.cam.ac.uk/accounts/ravenleaving
UCAMWEBAUTH_CERTS: a dictionary including key names and their associated certificates which can be downloaded from the
    Raven project pages.
UCAMWEBAUTH_TIMEOUT: An integer with the time (in seconds) that has to pass to consider an authentication timed out
    (Default to 30).
UCAMWEBAUTH_REDIRECT_AFTER_LOGIN: The url where you want to redirect the user after login (Default to '/').
UCAMWEBAUTH_CREATE_USER: This defaults to True, allowing the autocreation of users who have been successfully 
authenticated by Raven, but do not exist in the local database. The user is created with set_unusable_password().
```

An example, referencing the Raven test environment is given below:

```python
UCAMWEBAUTH_LOGIN_URL = 'https://test.legacy.raven.cam.ac.uk/auth/authenticate.html'
UCAMWEBAUTH_LOGOUT_URL = 'https://test.legacy.raven.cam.ac.uk/auth/logout.html'
UCAMWEBAUTH_LOGOUT_REDIRECT = 'http://www.cam.ac.uk/'
UCAMWEBAUTH_CERTS = {901: """-----BEGIN CERTIFICATE-----
MIIDrTCCAxagAwIBAgIBADANBgkqhkiG9w0BAQQFADCBnDELMAkGA1UEBhMCR0Ix
EDAOBgNVBAgTB0VuZ2xhbmQxEjAQBgNVBAcTCUNhbWJyaWRnZTEgMB4GA1UEChMX
VW5pdmVyc2l0eSBvZiBDYW1icmlkZ2UxKDAmBgNVBAsTH0NvbXB1dGluZyBTZXJ2
aWNlIFJhdmVuIFNlcnZpY2UxGzAZBgNVBAMTElJhdmVuIHB1YmxpYyBrZXkgMjAe
Fw0wNDA4MTAxMzM1MjNaFw0wNDA5MDkxMzM1MjNaMIGcMQswCQYDVQQGEwJHQjEQ
MA4GA1UECBMHRW5nbGFuZDESMBAGA1UEBxMJQ2FtYnJpZGdlMSAwHgYDVQQKExdV
bml2ZXJzaXR5IG9mIENhbWJyaWRnZTEoMCYGA1UECxMfQ29tcHV0aW5nIFNlcnZp
Y2UgUmF2ZW4gU2VydmljZTEbMBkGA1UEAxMSUmF2ZW4gcHVibGljIGtleSAyMIGf
MA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC/9qcAW1XCSk0RfAfiulvTouMZKD4j
m99rXtMIcO2bn+3ExQpObbwWugiO8DNEffS7bzSxZqGp7U6bPdi4xfX76wgWGQ6q
Wi55OXJV0oSiqrd3aOEspKmJKuupKXONo2efAt6JkdHVH0O6O8k5LVap6w4y1W/T
/ry4QH7khRxWtQIDAQABo4H8MIH5MB0GA1UdDgQWBBRfhSRqVtJoL0IfzrSh8dv/
CNl16TCByQYDVR0jBIHBMIG+gBRfhSRqVtJoL0IfzrSh8dv/CNl16aGBoqSBnzCB
nDELMAkGA1UEBhMCR0IxEDAOBgNVBAgTB0VuZ2xhbmQxEjAQBgNVBAcTCUNhbWJy
aWRnZTEgMB4GA1UEChMXVW5pdmVyc2l0eSBvZiBDYW1icmlkZ2UxKDAmBgNVBAsT
H0NvbXB1dGluZyBTZXJ2aWNlIFJhdmVuIFNlcnZpY2UxGzAZBgNVBAMTElJhdmVu
IHB1YmxpYyBrZXkgMoIBADAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBBAUAA4GB
AFciErbr6zl5i7ClrpXKA2O2lDzvHTFM8A3rumiOeauckbngNqIBiCRemYapZzGc
W7fgOEEsI4FoLOjQbJgIrgdYR2NIJh6pKKEf+9Ts2q/fuWv2xOLw7w29PIICeFIF
hAM+a6/30F5fdkWpE1smPyrfASyXRfWE4Ccn1RVgYX9u
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
"""}
```

## Errors

There are five possible exceptions that can be raised using this module: MalformedResponseError, InvalidResponseError,
PublicKeyNotFoundError, and OtherStatusCode that return HTTP 500, or UserNotAuthorised that returns 403. You can catch 
these exceptions using process_exception middleware 
(https://docs.djangoproject.com/en/2.2/topics/http/middleware/#process_exception) to customize what the user will 
receive as a response. The module has a default behaviour for these exceptions with HTTP error codes and using their 
corresponding templates. To use the default behaviour just add:
 
```python
MIDDLEWARE = [
    ...
    'ucamwebauth.middleware.DefaultErrorBehaviour',
    ...
]

INSTALLED_APPS = [
    ...
    'ucamwebauth',
    ...
]
```

You can also rewrite the ucamwebauth_\<httpcode\>.html templates. You only need to add the following lines to your own if 
you want to show the user the error message:

```python
{% for message in messages %}
    {{ message }}<br/>
{% endfor %}
```


## Authentication request parameters

This parameters are sent with the authentication request and allows the developer to tune the request to fit their app:

```
UCAMWEBAUTH_DESC: A text description of the resource requesting authentication which may be displayed to the end-user
    to further identify the resource to which his/her identity is being disclosed. Can be omitted.
UCAMWEBAUTH_IACT: The value 'yes' requires that a re-authentication exchange takes place with the user. This could be
    used prior to a sensitive transaction in an attempt to ensure that a previously authenticated user is still present
    at the browser. The value 'no' requires that the authentication request will only succeed if the user's identity
    can be returned without interacting with the user. This could be used as an optimisation to take advantage of any
    existing authentication but without actively soliciting one. If omitted or empty, then a previously established
    identity may be returned if the WLS supports doing so, and if not then the user will be prompted as necessary.
UCAMWEBAUTH_MSG: Text describing why authentication is being requested on this occasion which may be displayed to the
    end-user. Can be omitted.
UCAMWEBAUTH_PARAMS: Data that will be returned unaltered to the WAA in any 'authentication response message' issued as
    a result of this request. This could be used to carry the identity of the resource originally requested or other
    WAA state, or to associate authentication requests with their eventual replies. When returned, this data will be
    protected by the digital signature applied to the authentication response message but nothing else is done to
    ensure the integrity or confidentiality of this data - the WAA MUST take responsibility for this if necessary.
UCAMWEBAUTH_FAIL: If this parameter is 'yes' and the outcome of the request is anything other than success (i.e. the
    status code would be anything other than 200) then the WLS MUST return an informative error to the user and MUST
    not redirect back to the WAA. Setting this makes it easier to implement WAAs at the expense of a loss of
    flexibility in error handling.
```

The details of these can be found in the Raven WLS protocol documentation,
[here](http://raven.cam.ac.uk/project/waa2wls-protocol.txt).
