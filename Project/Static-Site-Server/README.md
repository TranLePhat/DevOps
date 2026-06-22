# Static Site Server

## Objective

Deploy a simple static website using Nginx and automate deployment with rsync.

## Features

* Install and configure Nginx
* Serve a static website
* Deploy website files using rsync
* Access website through a web browser

## Project Structure

```text
Static-Site-Server/
├── website/
│   ├── index.html
│   └── style.css
├── deploy.sh
├── screenshots/
└── README.md
```

## Deploy Website

```bash
chmod +x deploy.sh

./deploy.sh
```

## Verify Nginx

```bash
systemctl status nginx
```

## Screenshots

### Nginx Service

![Nginx Status](screenshots/nginx%20service%20status.png)

### Website

![Website](screenshots/output.png)

