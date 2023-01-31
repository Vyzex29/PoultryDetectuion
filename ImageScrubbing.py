from simple_image_download.simple_image_download import simple_image_download

response = simple_image_download
keyword = ["chicken on field"]

for kw in keyword:
    response().download(kw, 50)