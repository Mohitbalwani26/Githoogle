## Githoogle
A simple platform for finding out the top repositories of given organisation and their top Committees. 

Live website can be found [here](https://sleepy-dusk-32194.herokuapp.com) 

Demo can be found [here](https://www.youtube.com/watch?v=klg-UPV2J3Y) 

**Assumptions:**  
 1. Top repositories should be searched of organisation only i.e. First
    input field should be organisation handle not personal github
    profile or any URL.
 2. Number of top contributors should always be less than 500 as github api does not store more data than this.
 3. Data may not match exactly to the point because syncing with actual github takes time. In general github api lacks data by some hours/days.
 4. The limit for calling the github api is very low so website may show API limit exceeded in that case, try after few hours.
 5. If you searched for top 10 contributors in a repository and there were only 7 so all 7 will be displayed in that case same goes with repositories.

Currently the website is not mobile responsive so please, try it on desktop devices.

**How to run locally?**

choose the directory where you want to clone the project and setup a virtual environment for the same. For better understanding, lets say you are choosing Desktop as directory.

Note : If running with pip or python shows error then try with pip3 or python3 respectively.


 1. `cd Desktop`
 2. `mkdir almabase`
 3. `cd almabase`
 4. `git clone https://github.com/Mohitbalwani26/Githoogle.git`
 5. `virtualenv env` (if virtualenv is not installed then first run `pip install virtualenv`)
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

 
