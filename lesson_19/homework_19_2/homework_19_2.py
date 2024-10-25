import requests

base_url = "http://127.0.0.1:8080"

image_path = "test_image.jpg"

# 1. Uploading file with POST-request
upload_url = f"{base_url}/upload"
with open(image_path, 'rb') as img:
    files = {'image': img}
    response = requests.post(upload_url, files=files)

# Check, if the request was successful
if response.status_code == 201:
    print(f"Image {image_path} uploaded successfully.")
    image_data = response.json()
    print(f"Image URL: {image_data['image_url']}")
else:
    print(f"Failed to upload image. Status code: {response.status_code}")
    exit()

# 2. GET image
image_url = image_data['image_url']
filename = image_url.split('/')[-1]  # Get image file name
get_image_url = f"{base_url}/image/{filename}"

# GET image URL
response = requests.get(get_image_url, headers={"Content-Type": "text"})
if response.status_code == 200:
    image_info = response.json()
    print(f"Retrieved image URL: {image_info['image_url']}")
else:
    print(f"Failed to retrieve image. Status code: {response.status_code}")

# 3. Deleting image from server with DELETE-request
delete_image_url = f"{base_url}/delete/{filename}"
response = requests.delete(delete_image_url)

if response.status_code == 200:
    print(f"Image {filename} successfully deleted.")
else:
    print(f"Failed to delete image. Status code: {response.status_code}")
