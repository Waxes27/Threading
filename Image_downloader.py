import requests
import time
import concurrent.futures
import threading
import os
import sys
import json


def get_topics():
    print('Getting topics...')
    try:
        request = requests.get('https://unsplash.com').text
    except requests.exceptions.ConnectionError:
        print("Check your internet connection")
        return -1

    topics = request.split('topicsSubNavSlugs')[1].split('}')[0].split('\\')

    topic = []
    for i in topics:
        if len(i) == 0:
            topics.remove(i)
        try:
            topics.remove('",')
            topics.remove('"]')
            i.strip('"')
        except ValueError:
            pass
        # topics = i.strip('"')
        if i != '':
            topic.append(i.strip('"'))

    # print("Finished")
    return topic



def user_topic(topics):
    for k,v in topics.items():
        print(f" {k}.{v}")

    user_t = input(f"\nSelect a topic number...")
    while not user_t.isdigit() and user_t not in range(v):
        user_t = input(f"\nSelect a topic number...")

    selected_topic = topics[int(user_t)]

    print(f"Your selected topic is '{selected_topic.capitalize()}'")
    return selected_topic


def photos(topic):
    img_url = []
    try:
        request = requests.get(f'https://unsplash.com/t/{topic}').text
    except requests.exceptions.ConnectionError:
        print("No Internet Connection\n")
        
    for i in request.split('srcSet'):
        if 'https://' in i and 'profile' not in i:
            img_url.append(i.split('="')[1].split('?')[0])

    if 'http-equiv' in img_url[0]:
        img_url.remove(img_url[0])
    print(img_url)
    return img_url


def downloader(topic, img_url_list):
    os.system('clear')
    failed = {}

    if not os.path.exists(f"{os.environ['HOME']}/Splash_Pictures/"):
        os.mkdir(f"{os.environ['HOME']}/Splash_Pictures/")

    if not os.path.exists(f"{os.environ['HOME']}/Splash_Pictures/{topic.capitalize()}/"):

        os.mkdir(f"{os.environ['HOME']}/Splash_Pictures/{topic.capitalize()}")

    for img_url in img_url_list:
        img_name = img_url.split('/')[3]
        img_name = f'{img_name}.jpg'
        print(f"Download [{img_name}] started...")

        try:
            img_bytes = requests.get(img_url).content
        except requests.exceptions.ConnectionError:
            print("Download failed (Check internet connection)...")
            return -1
            # failed_downloads(img)
            # failed[topic] = img_name

        topic_folder = f"{os.environ['HOME']}/Splash_Pictures/{topic.capitalize()}/"
        print("Topic folder open")
        with open(f'{topic_folder}/{img_name}', 'wb') as img_file:
            img_file.write(img_bytes)
            print(f"{img_name} has been downloaded...")


def main():
    picture_topics = get_topics()
    if picture_topics == -1:
        print("\nClosing Script\n\n")
        return
    
    topics = {}
    for _ in range(1,len(picture_topics)+1):
        for i in picture_topics:
            topics[_] = picture_topics[_-1]
            break
    
    topic = user_topic(topics)
    img_url_list = photos(topic)

    downloader(topic,img_url_list)
    


main()

















# img_url = [
#     'https://unsplash.com/photos/Ap97C_0GMSk'
#     'https://unsplash.com/photos/dJee93WuSJg'

# ]

# t1 = time.perf_counter()

# for img in img_url:
#     img_bytes = requests.get(img_url).content
#     img_name = img_url.split('/')[3]
#     img_name = f'{img_name}.jpg'

#     with open(img_name, 'wb') as img_file:
#         img_file.write(img_bytes)
#         print(f"{img_name} was downloaded...")

# t2 = time.perf_counter()