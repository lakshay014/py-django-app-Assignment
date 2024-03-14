A django based web app where you can add event and like them created with use of Python Django and mysql
This is project for assigment for internship.

**Required**: Docker, Python

1. Begin by installing the required Python libraries with the command `pip install -r requirements.txt`.
2. Launch the Docker container using `docker compose up -d`. This action initiates your MySQL server.
3. Proceed to execute migrations by running `python manage.py migrate`. This step will create tables and perform necessary updates in your database.
4. Finally, start your Django application with `python manage.py runserver`. You can then access the page by following the link provided in the console output of the above command.
## Stopping server

1. Stop the python django server.
2. Do `docker compose down`


# Output of the Project

### 1. Simple Start Page
![Screenshot of simple start page](https://github.com/kuldeepdev407/py-django-app/assets/46247376/ee43f30f-4c19-4d80-8974-2adef29c41be)
### 2. Add Event Form
![Screenshot of form](https://github.com/kuldeepdev407/py-django-app/assets/46247376/755bc63d-7873-487d-98a1-a9936952cc05)
### 3. Filled Event Form
![Screenshot of filledform](https://github.com/kuldeepdev407/py-django-app/assets/46247376/f1b4a5fb-7c04-457f-9a04-3dcdc44b9097)
### 4. Event after Added
![Screenshot of Event Added](https://github.com/kuldeepdev407/py-django-app/assets/46247376/c0c6a2f2-f8e0-4406-a5c2-5dbf3b6d4b76)
### 5. Event after Liked
![Screenshot of Event Liked](https://github.com/kuldeepdev407/py-django-app/assets/46247376/4ec8ee5d-e096-4c16-bd02-22390d576361)
### 6. Event After added more Event
![Screenshot of Event after added more event](https://github.com/kuldeepdev407/py-django-app/assets/46247376/13b4c739-9a98-444c-9265-bd7b15819980)
### 7 Database structure
![Screeshot of Datebase Description](https://github.com/kuldeepdev407/py-django-app/assets/46247376/3cf53fff-80ec-4493-aee6-bd4f3252a9e5)

