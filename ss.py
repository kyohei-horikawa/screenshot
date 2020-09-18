import json
import requests
import os

path = "{0}/tmp.png".format(os.environ['HOME'])
os.system(f"screencapture -i -x {path}")

WEBHOOK_URL = os.environ['QIITA_WEBHOOK_URL_FOR_SCREENSHOT']

# 画像添付
with open(path, 'rb') as f:
    file_bin = f.read()
files_qiita = {
    "ss": ("tmp.png", file_bin),
}
res = requests.post(WEBHOOK_URL, files=files_qiita)
print(res.status_code)

os.system(f"rm {path}")
