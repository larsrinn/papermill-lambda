import requests
import papermill as pm

import os


def lambda_handler(request, context):
    url = "http://example.com"
    print(url)
    pm.execute_notebook(
        "get_url.ipynb",
        "output.ipynb",
        parameters=dict(
            url=url,
        )
    )
    return os.path.exists("output.ipynb")


if __name__ == '__main__':
    lambda_handler('', '')
