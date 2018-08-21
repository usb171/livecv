







    pip3 install django==2.0.7
    pip3 install gunicorn
    


    $ sudo apt-get update
    $ sudo apt-get install software-properties-common
    $ sudo add-apt-repository ppa:certbot/certbot
    $ sudo apt-get update
    $ sudo apt-get install python-certbot-nginx 







    server {
        listen 80;
        server_name srcv.ddns.net;

        access_log /var/log/nginx/nginx-access.log;
        error_log /var/log/nginx/nginx-error.log;

        location = /favicon.ico {
            access_log off;
            log_not_found off;
        }

        location /static {
            alias /home/srcv/livecv/static;
        }

        location / {
            proxy_pass http://localhost:8000;
        }
    }

    server {

        listen               443    ssl;
        server_name          zabbixcv.ddns.net zabbixcv.ddns.net;
        ssl_certificate /etc/letsencrypt/live/zabbixcv.ddns.net/fullchain.pem; # managed by Certbot
        ssl_certificate_key /etc/letsencrypt/live/zabbixcv.ddns.net/privkey.pem; # managed by Certbot

        ssl_session_cache    shared:SSL:1m;
        ssl_session_timeout  5m;

        ssl_ciphers  HIGH:!aNULL:!MD5;
        ssl_prefer_server_ciphers  on;

        access_log /var/log/nginx/nginx-access.log;
        error_log /var/log/nginx/nginx-error.log;

        location = /favicon.ico {
            access_log off;
            log_not_found off;
        }


        location /static {
            alias /home/srcv/livecv/static;
        }
