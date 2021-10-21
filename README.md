# REV

## How to run server
git clone
cd /REV/REV
python manage.py runserver

## Request
{'message': 'your_data'}

## Response
{
    'md5': 'your_md5_sum',
    'crc32': 'your_crc32_sum',
    'sha1': 'your_sha1_sum',
    'sha256': 'your_sha256_sum'
}

## Test
run server
run api_tests.py