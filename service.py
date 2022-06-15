import requests
import yaml
import traceback

with open("config.yml") as file:
    parameters = yaml.load(file, Loader=yaml.FullLoader)
    inference_url = parameters["inference_url"]


def inference(data):
    try:
        resp = requests.post(inference_url, json=data)
        return resp.json()
    except:
        print(traceback.format_exc())
