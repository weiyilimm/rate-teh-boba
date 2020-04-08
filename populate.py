import os



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ratetehboba.settings')

import django

django.setup()
from ratings.models import Cafe, Feedback
from users.models import Profile
from django.utils.dateparse import parse_date

from django.contrib.auth.models import User


def populate():
    # Creating the data
    # template
    # {"title": ,
    #  "address": ,
    #  "city": ,
    #  "email": ,
    #  "content": ,
    #  "date_posted": ,
    #  "author": ,
    #  "image": ,},

    cafes = [{"title": "The alley",
              "address": "49-GF, Jalan Austin Heights 8/1, Taman Austin Heights, 81100 Johor Bahru, Johor",
              "city": "Johor Bahru",
              "phone": "",
              "email": "thealley@hotmail.com",
              "content": "2",
              "date_posted": "2020-04-07",
              "author": "2474554l",
              "image": "images/bubbletea.jpg", },
             {"title": "Xing Fu Tang",
              "address": "29 Frith St, Soho, London W1D 5LG, United Kingdom",
              "city": "London",
              "phone": "",
              "email": "",
              "content": "",
              "date_posted": "",
              "author": "",
              "image": "", },
             {"title": "",
              "address": "",
              "city": "",
              "phone": "",
              "email": "",
              "content": "",
              "date_posted": "",
              "author": "",
              "image": "", },
             ]
    # creating users. Template:
    # {"username":"",
    #  "image":"profile_pics/wex.jpeg",
    #  "first_name":"first",
    #  "last_name":"last",
    #  "bio":"lorem ipsum dolor sit amet" },
    users = [{"username":"",
              "image":"profile_pics/wex.jpeg",
              "first_name":"first",
              "last_name":"last",
              "bio":"lorem ipsum dolor sit amet" },]
    # creating feedbacks
    feedback = [{"comment":"somerandomcomment"}]

    userlist = [add_user(u['username'],
                         u['image'],
                         u['first_name'],
                         u['last_name'],
                         u['bio'], ) for u in users]

    cafelist = [add_book(c['title'],
                         c['address'],
                         c['city'],
                         c['phone'],
                         c['email'],
                         c['content'],
                         c['date_posted'],
                         c['author'],
                         c['image'],) for c in cafes]



    feedbacklist = [add_feedback(f['comment']) for f in feedback]

    for l in listings:
        add_listing(l['user'],
                    l['book'],
                    l['description'],
                    )


def add_cafe(title, address, city, phone, email, content, author, image):
    cafe = Cafe.objects.get_or_create(title=title,
                                      address=address,
                                      city=city,
                                      phone=phone,
                                      email=email,
                                      content=content,
                                      # date_posted=date_posted,
                                      author=author,
                                      image=image,)[0]
    cafe.save()
    return cafe


def add_feedback(comment):
    cafe = random.choice(cafelist)
    author = random.choice(userlist)
    feedback = Feedback, objects.get_or_create(cafe=cafe,
                                               comment=comment,
                                               # date_posted=date_posted,
                                               author=author,)[0]
    feedback.save()
    return feedback


def add_user(username, image, first_name, last_name, bio):
    user = User.objects.get_or_create(username=username)[0]
    user.set_password("password")
    user.save()

    profile = Profile.objects.get_or_create(user=user,
                                            image=image,
                                            first_name=first_name,
                                            last_name=last_name,
                                            bio=bio,)[0]
    profile.save()
    return profile


# Start execution here!
if __name__ == '__main__':
    print('Starting ratetehboba population script...')
    populate()
