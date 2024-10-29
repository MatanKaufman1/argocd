import requests


def url_test(url):
    try:
        response = requests.head(url)
        print(response)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError as error:
        return error

if __name__ == '__main__':
    url = "https://10.1.0.8:9090"
    print(url_test(url))
