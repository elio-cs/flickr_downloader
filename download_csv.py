import os
import csv
import requests

folder_path = './url_csv'
download_path = '/data/zhangxinyu/dataset/flickr'
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

count = 1

for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)
    
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        
        for row in reader:
            image_url = row[0]
            response = requests.get(image_url)
            
            if response.status_code == 200:
                index = str(count).zfill(6)
                image_name = f'{index}.jpg'
                image_path = os.path.join(download_path, image_name)
                count = count + 1
                with open(image_path, 'wb') as image_file:
                    image_file.write(response.content)
                    
                print(f"Download {index} successful")
            else:
                print(f"can not download {image_url}")


