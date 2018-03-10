import os
import sys
import time
import traceback 
import flickrapi
from retry import retry 
from urllib.request import urlretrieve 

keyword = sys.argv[1]
flickr_api_key = sys.argv[2]
secret_key = sys.argv[3]

@retry()
def get_photos(url, filepath):
    urlretrieve(url, filepath)
    time.sleep(1)

flicker = flickrapi.FlickrAPI(flickr_api_key, secret_key, format='parsed-json')
response = flicker.photos.search(text=keyword,
                                 per_page=500,
                                 media='photos',
                                 safe_search=1,
                                 extras='url_q,license')
photos = response['photos']

try:
    for photo in photos['photo']:
        url_q = photo['url_q']
        filepath = sys.argv[4] + '/' + photo['id'] + '.jpg'
        get_photos(url_q, filepath)
except Exception as e:
    traceback.print_exc()

