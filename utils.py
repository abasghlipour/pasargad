import requests

def send_sms(phone_number,otp_code):
    api_key='ZQRQG0sNkZzSwnlgpAy8cExVr4-EtCdTjBWHt32DC6M='
    requests.get(
        f'http://ippanel.com:8080/?apikey={api_key}&pid=7uvx79ioelosoty&fnum=3000505&tnum={phone_number}&p1=verification-code&v1={otp_code}'
    )