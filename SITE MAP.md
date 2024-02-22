/admin/ django.contrib.admin.sites.index        admin:index
/admin/<app_label>/     django.contrib.admin.sites.app_index    admin:app_list
/admin/<url>    django.contrib.admin.sites.catch_all_view
/admin/auth/group/      django.contrib.admin.options.changelist_view    admin:auth_group_changelist
/admin/auth/group/<path:object_id>/     django.views.generic.base.RedirectView
/admin/auth/group/<path:object_id>/change/      django.contrib.admin.options.change_view        admin:auth_group_change
/admin/auth/group/<path:object_id>/delete/      django.contrib.admin.options.delete_view        admin:auth_group_delete
/admin/auth/group/<path:object_id>/history/     django.contrib.admin.options.history_view       admin:auth_group_history
/admin/auth/group/add/  django.contrib.admin.options.add_view   admin:auth_group_add
/admin/auth/user/       django.contrib.admin.options.changelist_view    admin:auth_user_changelist
/admin/auth/user/<id>/password/ django.contrib.auth.admin.user_change_password  admin:auth_user_password_change
/admin/auth/user/<path:object_id>/      django.views.generic.base.RedirectView
/admin/auth/user/<path:object_id>/change/       django.contrib.admin.options.change_view        admin:auth_user_change
/admin/auth/user/<path:object_id>/delete/       django.contrib.admin.options.delete_view        admin:auth_user_delete
/admin/auth/user/<path:object_id>/history/      django.contrib.admin.options.history_view       admin:auth_user_history
/admin/auth/user/add/   django.contrib.auth.admin.add_view      admin:auth_user_add
/admin/authtoken/tokenproxy/    django.contrib.admin.options.changelist_view    admin:authtoken_tokenproxy_changelist
/admin/authtoken/tokenproxy/<path:object_id>/   django.views.generic.base.RedirectView
/admin/authtoken/tokenproxy/<path:object_id>/change/    django.contrib.admin.options.change_view        admin:authtoken_tokenproxy_change
/admin/authtoken/tokenproxy/<path:object_id>/delete/    django.contrib.admin.options.delete_view        admin:authtoken_tokenproxy_delete
/admin/authtoken/tokenproxy/<path:object_id>/history/   django.contrib.admin.options.history_view       admin:authtoken_tokenproxy_history
/admin/authtoken/tokenproxy/add/        django.contrib.admin.options.add_view   admin:authtoken_tokenproxy_add
/admin/autocomplete/    django.contrib.admin.sites.autocomplete_view    admin:autocomplete
/admin/jsi18n/  django.contrib.admin.sites.i18n_javascript      admin:jsi18n
/admin/login/   django.contrib.admin.sites.login        admin:login
/admin/logout/  django.contrib.admin.sites.logout       admin:logout
/admin/password_change/ django.contrib.admin.sites.password_change      admin:password_change
/admin/password_change/done/    django.contrib.admin.sites.password_change_done admin:password_change_done
/admin/r/<int:content_type_id>/<path:object_id>/        django.contrib.contenttypes.views.shortcut      admin:view_on_site
/admin/restaurant/booking/      django.contrib.admin.options.changelist_view    admin:restaurant_booking_changelist
/admin/restaurant/booking/<path:object_id>/     django.views.generic.base.RedirectView
/admin/restaurant/booking/<path:object_id>/change/      django.contrib.admin.options.change_view        admin:restaurant_booking_change
/admin/restaurant/booking/<path:object_id>/delete/      django.contrib.admin.options.delete_view        admin:restaurant_booking_delete
/admin/restaurant/booking/<path:object_id>/history/     django.contrib.admin.options.history_view       admin:restaurant_booking_history
/admin/restaurant/booking/add/  django.contrib.admin.options.add_view   admin:restaurant_booking_add
/admin/restaurant/employees/    django.contrib.admin.options.changelist_view    admin:restaurant_employees_changelist
/admin/restaurant/employees/<path:object_id>/   django.views.generic.base.RedirectView
/admin/restaurant/employees/<path:object_id>/change/    django.contrib.admin.options.change_view        admin:restaurant_employees_change
/admin/restaurant/employees/<path:object_id>/delete/    django.contrib.admin.options.delete_view        admin:restaurant_employees_delete
/admin/restaurant/employees/<path:object_id>/history/   django.contrib.admin.options.history_view       admin:restaurant_employees_history
/admin/restaurant/employees/add/        django.contrib.admin.options.add_view   admin:restaurant_employees_add
/admin/restaurant/menu/ django.contrib.admin.options.changelist_view    admin:restaurant_menu_changelist
/admin/restaurant/menu/<path:object_id>/        django.views.generic.base.RedirectView
/admin/restaurant/menu/<path:object_id>/change/ django.contrib.admin.options.change_view        admin:restaurant_menu_change
/admin/restaurant/menu/<path:object_id>/delete/ django.contrib.admin.options.delete_view        admin:restaurant_menu_delete
/admin/restaurant/menu/<path:object_id>/history/        django.contrib.admin.options.history_view       admin:restaurant_menu_history
/admin/restaurant/menu/add/     django.contrib.admin.options.add_view   admin:restaurant_menu_add
/api/api-token-auth/    rest_framework.authtoken.views.ObtainAuthToken
/api/message/   restaurant.views.msg
/auth/auth/     rest_framework.routers.APIRootView      api-root
/auth/auth/\.<format>/  rest_framework.routers.APIRootView      api-root
/auth/auth/token/login/ djoser.views.TokenCreateView    login
/auth/auth/token/logout/        djoser.views.TokenDestroyView   logout
/auth/auth/users/       djoser.views.UserViewSet        user-list
/auth/auth/users/<username>/    djoser.views.UserViewSet        user-detail
/auth/auth/users/<username>\.<format>/  djoser.views.UserViewSet        user-detail
/auth/auth/users/activation/    djoser.views.UserViewSet        user-activation
/auth/auth/users/activation\.<format>/  djoser.views.UserViewSet        user-activation
/auth/auth/users/me/    djoser.views.UserViewSet        user-me
/auth/auth/users/me\.<format>/  djoser.views.UserViewSet        user-me
/auth/auth/users/resend_activation/     djoser.views.UserViewSet        user-resend-activation
/auth/auth/users/resend_activation\.<format>/   djoser.views.UserViewSet        user-resend-activation
/auth/auth/users/reset_password/        djoser.views.UserViewSet        user-reset-password
/auth/auth/users/reset_password\.<format>/      djoser.views.UserViewSet        user-reset-password
/auth/auth/users/reset_password_confirm/        djoser.views.UserViewSet        user-reset-password-confirm
/auth/auth/users/reset_password_confirm\.<format>/      djoser.views.UserViewSet        user-reset-password-confirm
/auth/auth/users/reset_username/        djoser.views.UserViewSet        user-reset-username
/auth/auth/users/reset_username\.<format>/      djoser.views.UserViewSet        user-reset-username
/auth/auth/users/reset_username_confirm/        djoser.views.UserViewSet        user-reset-username-confirm
/auth/auth/users/reset_username_confirm\.<format>/      djoser.views.UserViewSet        user-reset-username-confirm
/auth/auth/users/set_password/  djoser.views.UserViewSet        user-set-password
/auth/auth/users/set_password\.<format>/        djoser.views.UserViewSet        user-set-password
/auth/auth/users/set_username/  djoser.views.UserViewSet        user-set-username
/auth/auth/users/set_username\.<format>/        djoser.views.UserViewSet        user-set-username
/auth/auth/users\.<format>/     djoser.views.UserViewSet        user-list
/restaurant/    restaurant.views.index  index
/restaurant/menu-items/<int:pk> restaurant.views.SingleMenuItemView
/restaurant/menu/<int:pk>       restaurant.views.SingleMenuItemView
/routers/       rest_framework.routers.APIRootView      api-root
/routers/\.<format>/    rest_framework.routers.APIRootView      api-root
/routers/booking/       restaurant.views.BookingViewSet booking-list
/routers/booking/<pk>/  restaurant.views.BookingViewSet booking-detail
/routers/booking/<pk>\.<format>/        restaurant.views.BookingViewSet booking-detail
/routers/booking\.<format>/     restaurant.views.BookingViewSet booking-list
/routers/menu-items/    restaurant.views.MenuItemsView  Menu_Items-list
/routers/menu-items/<pk>/       restaurant.views.MenuItemsView  Menu_Items-detail
/routers/menu-items/<pk>\.<format>/     restaurant.views.MenuItemsView  Menu_Items-detail
/routers/menu-items\.<format>/  restaurant.views.MenuItemsView  Menu_Items-list


***********************************************************************************************
***********************************************************************************************
***********************************************************************************************
***********************************************************************************************


admin.LogEntry
    Fields:
        id -
        action_time -
        user -
        content_type -
        object_id -
        object_repr -
        action_flag -
        change_message -
    Methods (non-private/internal):
        adelete()
        arefresh_from_db()
        asave()
        get_action_flag_display()
        get_admin_url()
        get_change_message()
        get_constraints()
        get_edited_object()
        get_next_by_action_time()
        get_previous_by_action_time()
        is_addition()
        is_change()
        is_deletion()
        validate_constraints()

auth.Group
    Fields:
        user -
        id -
        name -
        permissions -
    Methods (non-private/internal):
        adelete()
        arefresh_from_db()
        asave()
        get_constraints()
        natural_key()
        validate_constraints()

auth.Permission
    Fields:
        group -
        user -
        id -
        name -
        content_type -
        codename -
    Methods (non-private/internal):
        adelete()
        arefresh_from_db()
        asave()
        get_constraints()
        natural_key()
        validate_constraints()

auth.User
    Fields:
        logentry -
        auth_token -
        id -
        password -
        last_login -
        is_superuser -
        username -
        first_name -
        last_name -
        email -
        is_staff -
        is_active -
        date_joined -
        groups -
        user_permissions -
    Methods (non-private/internal):
        adelete()
        arefresh_from_db()
        asave()
        check_password()
        email_user()
        get_all_permissions()
        get_constraints()
        get_email_field_name()
        get_full_name()
        get_group_permissions()
        get_next_by_date_joined()
        get_previous_by_date_joined()
        get_session_auth_fallback_hash()
        get_session_auth_hash()
        get_short_name()
        get_user_permissions()
        get_username()
        has_module_perms()
        has_perm()
        has_perms()
        has_usable_password()
        natural_key()
        normalize_username()
        set_password()
        set_unusable_password()
        username_validator()
        validate_constraints()

authtoken.Token
    Fields:
        key -
        user -
        created -
    Methods (non-private/internal):
        adelete()
        arefresh_from_db()
        asave()
        generate_key()
        get_constraints()
        get_next_by_created()
        get_previous_by_created()
        validate_constraints()

authtoken.TokenProxy
    Fields:
        key -
        user -
        created -
    Methods (non-private/internal):
        adelete()
        arefresh_from_db()
        asave()
        generate_key()
        get_constraints()
        get_next_by_created()
        get_previous_by_created()
        validate_constraints()

contenttypes.ContentType
    Fields:
        logentry -
        permission -
        id -
        app_label -
        model -
    Methods (non-private/internal):
        adelete()
        arefresh_from_db()
        asave()
        get_all_objects_for_this_type()
        get_constraints()
        get_object_for_this_type()
        model_class()
        natural_key()
        validate_constraints()

restaurant.Booking
    Fields:
        id -
        name -
        no_of_guests -
        BookingDate -
        email -
        phone_number -
    Methods (non-private/internal):
        adelete()
        arefresh_from_db()
        asave()
        get_constraints()
        get_next_by_BookingDate()
        get_previous_by_BookingDate()
        validate_constraints()

restaurant.Employees
    Fields:
        id -
        name -
        department -
    Methods (non-private/internal):
        adelete()
        arefresh_from_db()
        asave()
        get_constraints()
        validate_constraints()

restaurant.Menu
    Fields:
        id -
        title -
        price -
        inventory -
        description -
        image -
    Methods (non-private/internal):
        adelete()
        arefresh_from_db()
        asave()
        get_constraints()
        validate_constraints()

restaurant.MenuItem
    Fields:
        id -
        title -
        price -
        inventory -
    Methods (non-private/internal):
        adelete()
        arefresh_from_db()
        asave()
        get_constraints()
        validate_constraints()

sessions.Session
    Fields:
        session_key -
        session_data -
        expire_date -
    Methods (non-private/internal):
        adelete()
        arefresh_from_db()
        asave()
        get_constraints()
        get_decoded()
        get_next_by_expire_date()
        get_previous_by_expire_date()
        get_session_store_class()
        validate_constraints()

Total Models Listed: 12


***********************************************************************************************
***********************************************************************************************
***********************************************************************************************
***********************************************************************************************



PS C:\Users\njasm\Desktop\Course\MetaBackEnd-main\Back-End Developer Capstone\Back-End_capstone\LittleLemon\BE_LittleLemon\littlelemon> python manage.py print_settings
ABSOLUTE_URL_OVERRIDES                   = {}
ADMINS                                   = []
ALLOWED_HOSTS                            = ['*']
APPEND_SLASH                             = False
AUTHENTICATION_BACKENDS                  = ['django.contrib.auth.backends.ModelBackend']
AUTH_PASSWORD_VALIDATORS                 = [{'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'}, {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'}, {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'}, {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}]
AUTH_USER_MODEL                          = 'auth.User'
BASE_DIR                                 = WindowsPath('C:/Users/njasm/Desktop/Course/MetaBackEnd-main/Back-End Developer Capstone/Back-End_capstone/LittleLemon/BE_LittleLemon/littlelemon')
CACHES                                   = {'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}}
CACHE_MIDDLEWARE_ALIAS                   = 'default'
CACHE_MIDDLEWARE_KEY_PREFIX              = ''
CACHE_MIDDLEWARE_SECONDS                 = 600
CORS_ALLOW_ALL_ORIGINS                   = True
CSRF_COOKIE_AGE                          = 31449600
CSRF_COOKIE_DOMAIN                       = None
CSRF_COOKIE_HTTPONLY                     = False
CSRF_COOKIE_MASKED                       = False
CSRF_COOKIE_NAME                         = 'csrftoken'
CSRF_COOKIE_PATH                         = '/'
CSRF_COOKIE_SAMESITE                     = 'Lax'
CSRF_COOKIE_SECURE                       = False
CSRF_FAILURE_VIEW                        = 'django.views.csrf.csrf_failure'
CSRF_HEADER_NAME                         = 'HTTP_X_CSRFTOKEN'
CSRF_TRUSTED_ORIGINS                     = []
CSRF_USE_SESSIONS                        = False
DATABASES                                = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': WindowsPath('C:/Users/njasm/Desktop/Course/MetaBackEnd-main/Back-End Developer Capstone/Back-End_capstone/LittleLemon/BE_LittleLemon/littlelemon/db.sqlite3'), 'ATOMIC_REQUESTS': False, 'AUTOCOMMIT': True, 'CONN_MAX_AGE': 0, 'CONN_HEALTH_CHECKS': False, 'OPTIONS': {}, 'TIME_ZONE': None, 'USER': '', 'PASSWORD': '', 'HOST': '', 'PORT': '', 'TEST': {'CHARSET': None, 'COLLATION': None, 'MIGRATE': True, 'MIRROR': None, 'NAME': None}}, 'little_lemon': {'ENGINE': 'django.db.backends.mysql', 'NAME': 'restaurant', 'USER': 'sqluser', 'PASSWORD': 'password', 'HOST': '127.0.0.1', 'PORT': '3306', 'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"}, 'ATOMIC_REQUESTS': False, 'AUTOCOMMIT': True, 'CONN_MAX_AGE': 0, 'CONN_HEALTH_CHECKS': False, 'TIME_ZONE': None, 'TEST': {'CHARSET': None, 'COLLATION': None, 'MIGRATE': True, 'MIRROR': None, 'NAME': None}}}
DATABASE_ROUTERS                         = []
DATA_UPLOAD_MAX_MEMORY_SIZE              = 2621440
DATA_UPLOAD_MAX_NUMBER_FIELDS            = 1000
DATA_UPLOAD_MAX_NUMBER_FILES             = 100
DATETIME_FORMAT                          = 'N j, Y, P'
DATETIME_INPUT_FORMATS                   = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M:%S.%f', '%Y-%m-%d %H:%M', '%m/%d/%Y %H:%M:%S', '%m/%d/%Y %H:%M:%S.%f', '%m/%d/%Y %H:%M', '%m/%d/%y %H:%M:%S', '%m/%d/%y %H:%M:%S.%f', '%m/%d/%y %H:%M']
DATE_FORMAT                              = 'N j, Y'
DATE_INPUT_FORMATS                       = ['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', '%b %d %Y', '%b %d, %Y', '%d %b %Y', '%d %b, %Y', '%B %d %Y', '%B %d, %Y', '%d %B %Y', '%d %B, %Y']
DEBUG                                    = True
DEBUG_PROPAGATE_EXCEPTIONS               = False
DECIMAL_SEPARATOR                        = '.'
DEFAULT_AUTO_FIELD                       = 'django.db.models.BigAutoField'
DEFAULT_CHARSET                          = 'utf-8'
DEFAULT_EXCEPTION_REPORTER               = 'django.views.debug.ExceptionReporter'
DEFAULT_EXCEPTION_REPORTER_FILTER        = 'django.views.debug.SafeExceptionReporterFilter'
DEFAULT_FILE_STORAGE                     = 'django.core.files.storage.FileSystemStorage'
DEFAULT_FROM_EMAIL                       = 'webmaster@localhost'
DEFAULT_INDEX_TABLESPACE                 = ''
DEFAULT_TABLESPACE                       = ''
DISALLOWED_USER_AGENTS                   = []
DJOSER                                   = {'USER_ID_FIELD': 'username'}
EMAIL_BACKEND                            = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST                               = 'localhost'
EMAIL_HOST_PASSWORD                      = ''
EMAIL_HOST_USER                          = ''
EMAIL_PORT                               = 25
EMAIL_SSL_CERTFILE                       = None
EMAIL_SSL_KEYFILE                        = None
EMAIL_SUBJECT_PREFIX                     = '[Django] '
EMAIL_TIMEOUT                            = None
EMAIL_USE_LOCALTIME                      = False
EMAIL_USE_SSL                            = False
EMAIL_USE_TLS                            = False
FILE_UPLOAD_DIRECTORY_PERMISSIONS        = None
FILE_UPLOAD_HANDLERS                     = ['django.core.files.uploadhandler.MemoryFileUploadHandler', 'django.core.files.uploadhandler.TemporaryFileUploadHandler']
FILE_UPLOAD_MAX_MEMORY_SIZE              = 2621440
FILE_UPLOAD_PERMISSIONS                  = 420
FILE_UPLOAD_TEMP_DIR                     = None
FIRST_DAY_OF_WEEK                        = 0
FIXTURE_DIRS                             = []
FORCE_SCRIPT_NAME                        = None
FORMAT_MODULE_PATH                       = None
FORM_RENDERER                            = 'django.forms.renderers.DjangoTemplates'
IGNORABLE_404_URLS                       = []
INSTALLED_APPS                           = ['django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles', 'django_extensions', 'restaurant', 'rest_framework', 'rest_framework.authtoken', 'djoser', 'corsheaders', 'tests']  
INTERNAL_IPS                             = []
LANGUAGES                                = [('af', 'Afrikaans'), ('ar', 'Arabic'), ('ar-dz', 'Algerian Arabic'), ('ast', 'Asturian'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('br', 'Breton'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('ckb', 'Central Kurdish (Sorani)'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('dsb', 'Lower Sorbian'), ('el', 'Greek'), ('en', 'English'), ('en-au', 'Australian English'), ('en-gb', 'British English'), ('eo', 'Esperanto'), ('es', 'Spanish'), ('es-ar', 'Argentinian Spanish'), ('es-co', 'Colombian Spanish'), ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'), ('es-ve', 'Venezuelan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('ga', 'Irish'), ('gd', 'Scottish Gaelic'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hsb', 'Upper Sorbian'), ('hu', 'Hungarian'), ('hy', 'Armenian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('ig', 'Igbo'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('kab', 'Kabyle'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('ky', 'Kyrgyz'), ('lb', 'Luxembourgish'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'Marathi'), ('ms', 'Malay'), ('my', 'Burmese'), ('nb', 'Norwegian Bokmål'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('nn', 'Norwegian Nynorsk'), ('os', 'Ossetic'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('tg', 'Tajik'), ('th', 'Thai'), ('tk', 'Turkmen'), ('tr', 'Turkish'), ('tt', 'Tatar'), ('udm', 'Udmurt'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('vi', 'Vietnamese'), ('zh-hans', 'Simplified Chinese'), ('zh-hant', 'Traditional Chinese')]
LANGUAGES_BIDI                           = ['he', 'ar', 'ar-dz', 'ckb', 'fa', 'ur']
LANGUAGE_CODE                            = 'en-us'
LANGUAGE_COOKIE_AGE                      = None
LANGUAGE_COOKIE_DOMAIN                   = None
LANGUAGE_COOKIE_HTTPONLY                 = False
LANGUAGE_COOKIE_NAME                     = 'django_language'
LANGUAGE_COOKIE_PATH                     = '/'
LANGUAGE_COOKIE_SAMESITE                 = None
LANGUAGE_COOKIE_SECURE                   = False
LOCALE_PATHS                             = []
LOGGING                                  = {}
LOGGING_CONFIG                           = 'logging.config.dictConfig'
LOGIN_REDIRECT_URL                       = '/accounts/profile/'
LOGIN_URL                                = '/accounts/login/'
LOGOUT_REDIRECT_URL                      = None
MANAGERS                                 = []
MEDIA_ROOT                               = ''
MEDIA_URL                                = '/'
MESSAGE_STORAGE                          = 'django.contrib.messages.storage.fallback.FallbackStorage'
MIDDLEWARE                               = ['django.middleware.security.SecurityMiddleware', 'django.contrib.sessions.middleware.SessionMiddleware', 'corsheaders.middleware.CorsMiddleware', 'django.middleware.common.CommonMiddleware', 'django.middleware.csrf.CsrfViewMiddleware', 'django.contrib.auth.middleware.AuthenticationMiddleware', 'django.contrib.messages.middleware.MessageMiddleware', 'django.middleware.clickjacking.XFrameOptionsMiddleware']
MIGRATION_MODULES                        = {}
MONTH_DAY_FORMAT                         = 'F j'
NUMBER_GROUPING                          = 0
PASSWORD_HASHERS                         = ['django.contrib.auth.hashers.PBKDF2PasswordHasher', 'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher', 'django.contrib.auth.hashers.Argon2PasswordHasher', 'django.contrib.auth.hashers.BCryptSHA256PasswordHasher', 'django.contrib.auth.hashers.ScryptPasswordHasher']
PASSWORD_RESET_TIMEOUT                   = 259200
PREPEND_WWW                              = False
REST_FRAMEWORK                           = {'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.BasicAuthentication', 'rest_framework.authentication.TokenAuthentication', 'rest_framework.authentication.SessionAuthentication'], 'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAdminUser']}        
ROOT_URLCONF                             = 'littlelemon.urls'
SECRET_KEY                               = 'django-insecure-960=yvbte$lx@4^)$2jm+m+^g^&x+pjhe@rv$lq=0a@ud%nevh'
SECRET_KEY_FALLBACKS                     = []
SECURE_CONTENT_TYPE_NOSNIFF              = True
SECURE_CROSS_ORIGIN_OPENER_POLICY        = 'same-origin'
SECURE_HSTS_INCLUDE_SUBDOMAINS           = False
SECURE_HSTS_PRELOAD                      = False
SECURE_HSTS_SECONDS                      = 0
SECURE_PROXY_SSL_HEADER                  = None
SECURE_REDIRECT_EXEMPT                   = []
SECURE_REFERRER_POLICY                   = 'same-origin'
SECURE_SSL_HOST                          = None
SECURE_SSL_REDIRECT                      = False
SERVER_EMAIL                             = 'root@localhost'
SESSION_CACHE_ALIAS                      = 'default'
SESSION_COOKIE_AGE                       = 1209600
SESSION_COOKIE_DOMAIN                    = None
SESSION_COOKIE_HTTPONLY                  = True
SESSION_COOKIE_NAME                      = 'sessionid'
SESSION_COOKIE_PATH                      = '/'
SESSION_COOKIE_SAMESITE                  = 'Lax'
SESSION_COOKIE_SECURE                    = False
SESSION_ENGINE                           = 'django.contrib.sessions.backends.db'
SESSION_EXPIRE_AT_BROWSER_CLOSE          = False
SESSION_FILE_PATH                        = None
SESSION_SAVE_EVERY_REQUEST               = False
SESSION_SERIALIZER                       = 'django.contrib.sessions.serializers.JSONSerializer'
SETTINGS_MODULE                          = 'littlelemon.settings'
SHORT_DATETIME_FORMAT                    = 'm/d/Y P'
SHORT_DATE_FORMAT                        = 'm/d/Y'
SIGNING_BACKEND                          = 'django.core.signing.TimestampSigner'
SILENCED_SYSTEM_CHECKS                   = []
STATICFILES_DIRS                         = []
STATICFILES_FINDERS                      = ['django.contrib.staticfiles.finders.FileSystemFinder', 'django.contrib.staticfiles.finders.AppDirectoriesFinder']    
STATICFILES_STORAGE                      = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATIC_ROOT                              = None
STATIC_URL                               = '/static/restaurant/'
STORAGES                                 = {'default': {'BACKEND': 'django.core.files.storage.FileSystemStorage'}, 'staticfiles': {'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage'}}
TEMPLATES                                = [{'BACKEND': 'django.template.backends.django.DjangoTemplates', 'DIRS': ['templates'], 'APP_DIRS': True, 'OPTIONS': {'context_processors': ['django.template.context_processors.debug', 'django.template.context_processors.request', 'django.contrib.auth.context_processors.auth', 'django.contrib.messages.context_processors.messages']}}]
TEST_DISCOVER_PATTERN                    = ['test_models', 'test_views']
TEST_NON_SERIALIZED_APPS                 = []
TEST_RUNNER                              = 'django.test.runner.DiscoverRunner'
THOUSAND_SEPARATOR                       = ','
TIME_FORMAT                              = 'P'
TIME_INPUT_FORMATS                       = ['%H:%M:%S', '%H:%M:%S.%f', '%H:%M']
TIME_ZONE                                = 'UTC'
USE_DEPRECATED_PYTZ                      = False
USE_I18N                                 = True
USE_L10N                                 = True
USE_THOUSAND_SEPARATOR                   = False
USE_TZ                                   = True
USE_X_FORWARDED_HOST                     = False
USE_X_FORWARDED_PORT                     = False
WSGI_APPLICATION                         = 'littlelemon.wsgi.application'
X_FRAME_OPTIONS                          = 'DENY'
YEAR_MONTH_FORMAT                        = 'F Y'