import flickrapi
import urllib
import requests

import csv

def save_list_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow([row])
            
# Set Flickr API key
api_key = 'Your Key'
api_secret = 'Your Secret'

flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')

keyword = "food"  # Replace with the keyword you want to search for

for page in range(1,50):
    photos = flickr.photos.search(text=keyword, per_page=500, page = page, sort='relevance')
    urls = []
    count = 0
    for photo in photos['photos']['photo']:
        photo_id = photo['id']
        photo_secret = photo['secret']
        
        photo_sizes = flickr.photos.getSizes(photo_id=photo_id)['sizes']['size']
        for size in photo_sizes:
            if size['label'] == 'Original':
                original_url = size['source']
                count = count + 1
                print("{}:{}".format(count, original_url))
                urls.append(original_url)
    print('output_{}.csv'.format(page))
    save_list_to_csv(urls, 'output_{}.csv'.format(page))
