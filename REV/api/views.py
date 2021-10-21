import hashlib
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
import zlib


def home(request):
    return HttpResponse("")


@csrf_exempt
def check_sum(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    data = body['message']
    md5_sum = hashlib.md5(data.encode('utf-8')).hexdigest()
    crc32_sum = zlib.crc32(str.encode(data))
    sha1_sum = hashlib.sha1(str.encode(data)).hexdigest()
    sha256_sum = hashlib.sha256(str.encode(data)).hexdigest()

    response = {'md5': md5_sum, 'crc32': crc32_sum, 'sha1': sha1_sum, 'sha256': sha256_sum}
    return HttpResponse(json.dumps(response), content_type='application/json')
