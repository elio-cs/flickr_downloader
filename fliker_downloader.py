import flickrapi
import urllib
import requests

import csv

def save_list_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow([row])
            
# 设置 Flickr API 密钥
api_key = '333e75d82fbaec0f8896b9f1596d843d'
api_secret = '6a0dd45f41af5628'

# 创建 Flickr API 实例
flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')

# 设置搜索参数
keyword = "food"  # 替换为你想要搜索的关键词


# 调用 Flickr API 进行搜索
for page in range(51,100):
    photos = flickr.photos.search(text=keyword, per_page=500, page = page, sort='relevance')
    # 遍历搜索结果
    urls = []
    count = 0
    for photo in photos['photos']['photo']:
        # 获取图片信息
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
