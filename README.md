# Neighborhood Grub System

The Neighborhood Grub System is a social kitchen platform for connecting people
who love to cook and people who love to eat in a community.

# Requirements

These instructions assume that you 

# Installation Instructions

Clone the repository
```
git clone git@gitlab.com:rolandmaio38/ngs.git
```
Change directory to the local git repository
```
cd ngs
```
Set up a virtual environment
```
virtualenv env
```
Activate the virtual environment
```
source env/bin/activate
```
Install the Python dependencies
```
pip install -r requirements.txt
```
Change directory to the Django project directory
```
cd django-project
```
Populate the database with mock data
```
python scripts/manage_dummy_data.py load
```
Add the `config.py` file with the API key.

Run the dev server
```
python manage.py runserver 127.0.0.1:8000
```
The NGS web application will be running and accessible at 127.0.0.1:8000
