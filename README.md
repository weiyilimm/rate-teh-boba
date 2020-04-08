
#Rate Teh Boba

Rate Teh Boba is a review website which was founded in 2020 by Glasgow Students. The website has food and culinary guides and pictures, along with user-generated reviews of bubble tea cafe.

Website: http://2474554l.pythonanywhere.com/

## Prerequisites

The website is built on:

[Python 3.7](https://www.python.org/downloads/release/python-370/)

[Django 2.2.3 (LTS)](https://docs.djangoproject.com/en/3.0/releases/2.2.3/)

[Bootstrap 4](https://getbootstrap.com/)


## Installation

The repository of our webpage could be found here: [https://github.com/weiyilimm/ratetehboba/](https://github.com/weiyilimm/ratetehboba/)

1. Create a virtual environment:
```bash
conda create -n teh python=3.7.2
conda activate teh
```

2. Clone our repository:
```bash
git clone https://github.com/weiyilimm/ratetehboba/
```


3. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages:
```bash
pip install -r requirements.txt
```

4. Migrate database models:
```bash
cd ratetehboba
py manage.py makemigrations
py manage.py migrate
```

5. Run the population script to populate the database for testing.
```bash
python populate.py
```

6. Run the server
```bash
py manage.py runserver
```

## Unit Testing

To run a unit test
```bash
python manage.py test <test-file-name>
```

## Usage

Four accounts are added by the population script, namely:
- 2474554l
- weikang
- weiyilim
- jonathan

with "password" being the password for all four.
### Register as a user
To register as a user, simply press the register button on the home page to create an account. After creating an account, you could now log in to register cafe or write a review.

### Register Cafe

To register a cafe, simply press the register cafe button on the home page to create an account. After creating a cafe, you could now see your cafe listed on the home page.

### Remove a Cafe

If your cafe have been closed down, you can press your cafe and navigate to cafe details page and press the delete button below, and the website will be disappeared.

### Update a Cafe

If your cafe name, phone number or email have been changed, you can press your cafe and navigate to cafe details and press the update button below, and you can update the details.


### Write a review

If you want to make a review on a specific cafe, kindly press the cafe and navigate to cafe details page, you could now write a review for the cafe but not the cafe you created. :))


## Authors and Contact
Code *by* Lab Group 11 Team E
  * [Alan Koo](https://github.com/alankoo12)
  * [Weiyi Lim](https://github.com/weiyilimm)
  * [Karen Tada](https://github.com/trtk298/)

## External Sources
[Make a README](https://www.makeareadme.com/)

[Font Awesome](https://fontawesome.com/)

[Tango With Django](https://github.com/maxwelld90/tango_with_django_2_code)

[StackOverflow](https://stackoverflow.com/)

[Crispy_Form](https://django-crispy-forms.readthedocs.io/en/latest/)

