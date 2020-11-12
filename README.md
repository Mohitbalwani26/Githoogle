Githoogle -
**How to run locally?**
choose the directory where you want to clone the project and setup a virtual environment for the same. For better understanding, lets say you are choosing Desktop as directory.

 1. `cd Desktop`
 2. `mkdir almabase`
 3. `cd almabase`
 4. `git clone https://github.com/Mohitbalwani26/Githoogle.git`
 5. `virtualenv env`
 6. `source env/bin/activate`
 7. `cd Githoogle`
 8. `pip install -r requirements.txt`
 9. `touch githoogle/secret_settings.py`
 10. open secret_settings.py in text editor and write `SECRET_KEY = "key"`where key can be generated from https://miniwebtool.com/django-secret-key-generator/ .
 11. `python manage.py migrate`
 12. `python manage.py createsuperuser`
 13. `python manage.py makemigrations gitoogle`
 14. `python manage.py migrate`
 15. `python manage.py runserver`

 
