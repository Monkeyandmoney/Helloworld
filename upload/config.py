# encoding:utf-8
# 配置存储桶的相关信息
from werkzeug.utils import secure_filename
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

# appid已在配置中移除,请在参数Bucket中带上appid。Bucket由bucketname-appid组成
# 1. 设置用户配置, 包括 secretId，secretKey 以及 Region

secret_id = 'xxx'  # 替换为用户的 secretId
secret_key = 'xxx'  # 替换为用户的 secretKey
Bucket_name_appid = 'xx-125456498303'
region = 'ap-shanghai'  # 替换为用户的 Region

token = ''  # 使用临时秘钥需要传入 Token，默认为空，可不填
config = CosConfig(Secret_id=secret_id, Secret_key=secret_key, Region=region, Token=token)
# 2. 获取客户端对象
client = CosS3Client(config)
