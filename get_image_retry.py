import requests
import sys
import time

headers = {
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
    # "Accept-Encoding": "gzip, deflate", 
    # "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
    # "Dnt": "1", 
    # "Host": "httpbin.org", 
    # "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "XY", #"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36", 
}

def get_image_retry(img_url, retries_left):
    while retries_left > 0:
       
        try:
            response = requests.get(img_url, headers={"User-Agent": "XY"+str(retries_left)}, timeout=5, stream=True)
            return response
        except Exception as e:
            print(f"error getting image: {e}" + " - trying again" if retries_left > 0 else "" )
            if retries_left == 0:
                print(f"failed to get image with retries")
                return None
            else:
                time.sleep(7)
                retries_left -= 1

if __name__ == '__main__':
    print(f"args are {sys.argv}")
    if len(sys.argv) < 3:
        print("Error: No arguments supplied. Please give the url as arguments\nRun the script as:\npython3 get_image_retry.py <some_url> <retry count>")
        exit(1)
    retries = 3
    if  len(sys.argv) > 1:
        try:
            retries = int(sys.argv[2])
        except ValueError as ve:
            print(f"conversion to int error: {ve}")
            exit(2)
        resp = get_image_retry(sys.argv[1], retries)
        print(f"got response {resp}")