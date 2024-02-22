1: Use pipenv install in the folder where the pipfile is, run pipenv shell then run python manage.py runserver


Superuser Django-Admin:
username: admin
password: admin
passwords for all testusers: password0388

MySQL username/password:
username: sqluser
password: password

Working Tokens:

admin
18a9bd083ea30cdde0d673e2a18892d1dba5e659
testuser
0bc57e8029b42b73652396c46ff9ce6cdc099812
testuser_2
bdf6283c59834468eb233c90392f94c16f8e7f4a

**********************************************************

Routers/API's to check via Insomnia:

/routers/booking/
/routers/menu-items/

Authorization tokens via AOI:

/api/api-token-auth/
/api/message/

/auth/auth/token/login/ ---- djoser.views.TokenCreateView    login
/auth/auth/token/logout/ ----      djoser.views.TokenDestroyView   logout
