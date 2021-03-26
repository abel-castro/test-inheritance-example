# DDST (Django + Docker Starter Template)
Development and production starter template for projects with django and docker.

## Features
* django + postgres
* serve static files in production with nginx

## Getting started
1. Download a copy of this repository.
2. (Optional) Change the placeholder name `ddst` from the project. 
```
sh rename_project.sh YOUR_PROJECT_NAME
``` 

### Development
- Create a .env file from the template env_template_dev with the desired values.

- Build the development image: ```docker-compose build ```

- Run ```docker-compose up``` and go to http://0.0.0.0:8000
to see your runserver.

### Production
- Create a .env file from the template env_template_prd with the desired values.

- Build the production image:
```
docker-compose -f docker-compose.prod.yml build
``` 

- Start your production server with: 
```
docker-compose -f docker-compose.prod.yml up
```

- Run migrations:
```
docker-compose -f docker-compose.prod.yml run --rm django /app/manage.py migrate
```

### TO-DOs:
- HTTPS for production 
