from simple_image_download.simple_image_download import simple_image_download

response = simple_image_download
keyword = ["turkey free range"]

for kw in keyword:
    response().download(kw, 30)