import urllib.request as urllib
input_url = input("Enter the url of the site: ")

def main(url):
    response = urllib.urlopen(url)
    print(f"Connected to {url} successfully")
    print(f"Response: {response.getcode()}")



main(input_url)

