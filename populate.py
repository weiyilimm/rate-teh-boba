import os



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ratetehboba.settings')

import django

django.setup()
from rating.models import Cafe, Feedback
from users.models import Profile
from django.utils.dateparse import parse_date

from django.contrib.auth.models import User


def populate():

    cafes = [{"title": "The alley",
              "address": "49-GF, Jalan Austin Heights 8/1, Taman Austin Heights, 81100 Johor Bahru, Johor",
              "city": "Johor Bahru",
              "phone": "+6073648276",
              "email": "thealley@hotmail.com",
              "content": "1",
              "date_posted": "2020-04-07",
              "author": "2474554l",
              "image": "images/bubbletea.jpg", },
             {"title": "Xing Fu Tang",
              "address": "29 Frith St, Soho, London W1D 5LG, United Kingdom",
              "city": "London",
              "phone": "+447928265421",
              "email": "xingfutang@hotmail.com",
              "content": "2",
              "date_posted": "2020-04-07",
              "author": "2474554l",
              "image": "images/xingfutang.jpg", },
             {"title": "Yi Fang",
              "address": "104 Shaftesbury Ave, West End, London W1D 5EQ, United Kingdom",
              "city": "London",
              "phone": "+443330147136",
              "email": "yifang@hotmail.com",
              "content": "3",
              "date_posted": "2020-04-07",
              "author": "weikang",
              "image": "images/yifang.jpg", },
             {"title": "Machi Machi",
              "address": "59 Shaftesbury Ave, Soho, London W1D 6LF, United Kingdom",
              "city": "London",
              "phone": "+442089610362",
              "email": "machimachi@hotmail.com",
              "content": "4",
              "date_posted": "2020-04-07",
              "author": "weikang",
              "image": "images/machimachi.jpg", },
             {"title": "Koi",
              "address": "133 New Bridge Rd, #01-39 ChinaTown Point, Singapore 059413",
              "city": "Singapore",
              "phone": "+6562212140",
              "email": "koi@hotmail.com",
              "content": "5",
              "date_posted": "2020-04-07",
              "author": "weikang",
              "image": "images/koi.jpg", },
             ]

    users = [{"username":"weikang",
              "image":"profile_pics/wex.jpeg",
              "first_name":"weikang",
              "last_name":"aw",
              "bio":"I want to try bubble tea" },
              {"username":"weiyilim",
              "image":"profile_pics/default.jpg",
              "first_name":"weiyi",
              "last_name":"lim",
              "bio":"I love bubble tea" },
              {"username":"Jonathan",
              "image":"profile_pics/default.jpg",
              "first_name":"weikang",
              "last_name":"aw",
              "bio":"I own bubble tea shop" },
              {"username":"2474554l",
              "image":"profile_pics/default.jpg",
              "first_name":"wei",
              "last_name":"ah",
              "bio":"I own bubble tea shops" },
              ]

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
