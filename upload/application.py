# coding=utf-8
from flask import Flask, render_template, request, jsonify
import os, sys

from werkzeug.utils import secure_filename

from config import Bucket_name_appid,client
app = Flask(__name__)


@app.route('/muilti-upload', methods=['GET', 'POST'])
def muiltiUpload():
    if request.method == 'POST':
        """Handle the upload of a file."""
        # 这里获取绝对路径
        abpath = os.path.abspath('./upload/')
        for upload in request.files.getlist("file"):
            response = client.put_object(
                Bucket=Bucket_name_appid,  # Bucket由bucketname-appid组成
                Body=upload.read(),
                Key=secure_filename(upload.filename),
                StorageClass='STANDARD',
                CacheControl='no-cache',
                ContentDisposition='tb1d.txt'
            )
        return jsonify(status='ok', msg='OVER')
    else:
        return render_template('muilti-upload.html')



if __name__ == '__main__':
    app.run(host="localhost", debug=True)
