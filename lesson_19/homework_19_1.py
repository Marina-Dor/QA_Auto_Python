import json
import utils
import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'

params = {
    'sol': 1000,
    'camera': 'fhaz',
    'api_key': 'DEMO_KEY'
}

# Request to the API
print("Sending request to api.nasa.gov ...")
utils.print_separator(length=50, symbol="-")
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Get the response data as JSON
    print("Api response:")
    formatted_response = json.dumps(response.json(), indent=4)
    print(formatted_response)

    # Get the list of photos from the response
    data = response.json()
    photos = data['photos']

    for idx, photo in enumerate(photos, start=1):
        # Get the image URL
        img_url = photo['img_src']

        # Download the image
        img_response = requests.get(img_url)

        # Save the image as a local file
        file_name = f"mars_photo{idx}.jpg"
        with open(file_name, 'wb') as f:
            f.write(img_response.content)

        utils.print_separator(length=50, symbol="-")
        print(f"Photo {file_name} was successfully downloaded")
        utils.print_separator(length=50, symbol="-")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    utils.print_separator(length=50, symbol="-")
