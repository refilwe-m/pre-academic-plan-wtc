from sys import argv,exit
import requests

api_key="placholder_key_can't_commit_to_git"
try:
    [_,n] = argv
    value = float(n)
    resp = requests.get(f"https://rest.coincap.io/v3/assets/bitcoint?apiKey={api_key}")
    bitcoin = resp.json()["data"]
    print(f'${(float(bitcoin["priceUsd"])*value):,.4f}')
except requests.RequestException:
    exit()
except ValueError:
    exit("Command-line argument is not a number")
except:
    exit("Missing command-line argument")