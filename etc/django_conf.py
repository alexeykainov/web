server {

  listen 80 default;

  location ^~ /uploads/ {
    root /home/box/web;
  }

  location ~* ^.+\.\w+$ {
    root /home/box/web/public;
  }

  location /hello/ {
    proxy_pass http://127.0.0.1:8080;
    }
  location / {
    proxy_pass http://127.0.0.1:8000;
    }
}
