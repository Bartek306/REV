import json
import requests
import zlib
import hashlib


def test():
    message = 'test_message'
    data = {'message': message}
    test_md5 = hashlib.md5(message.encode('utf-8')).hexdigest()
    test_crc32 = zlib.crc32(str.encode(message))
    test_sha1 = hashlib.sha1(str.encode(message)).hexdigest()
    test_sha256 = hashlib.sha256(str.encode(message)).hexdigest()
    data = json.dumps(data)

    request = requests.post("http://localhost:8000/check_sum", data=data)
    assert request.status_code == 200
    dict = request.text
    dict = json.loads(dict)
    assert dict['md5'] == test_md5
    assert dict['crc32'] == test_crc32
    assert dict['sha1'] == test_sha1
    assert dict['sha256'] == test_sha256


test()
