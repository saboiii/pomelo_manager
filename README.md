# pomelo_manager
POMELO is a task manager app with a user-friendly interface, authentication and exporting capabilities (in the form of an Excel sheet). Built using Django, PostgreSQL, AJAX and Openpyxl. The project is containerized using Docker, allowing for easy deployment and consistent development environments.

To install this, clone the repo and set up your desired ENV variables for Postgres.
```
cp .env.example .env
```

Start the container, run migrations and load up dummy data.
```
docker-compose up -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py loaddata initial_data.json
```

Feel free to change the ports based on your needs.

<video src='https://github.com/user-attachments/assets/7ba4f0c4-ae60-438b-85e6-18f2bb77006e' width=180/>
