<VirtualHost *:8889>
    #My site Name
    ServerName srcv.ddns.net.com

    #Demon process for multiple virtual hosts
    WSGIDaemonProcess srcv.ddns.net.com threads=5

    #Pointing wsgi script to config file
    WSGIScriptAlias / /var/www/livecv/livecv/django.wsgi
    WSGIProcessGroup srcv.ddns.net.com

    #Your static files location
    Alias /static/ "/var/www/livecv/core/static/"
    <Location "/media">
        SetHandler None
    </Location>
    <LocationMatch "\.(jpg|gif|png|js|css)$">
        SetHandler None
    </LocationMatch>
    <Directory /var/www/livecv/livecv >
        WSGIProcessGroup srcv.ddns.net.com
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
    </Directory>
</VirtualHost>
