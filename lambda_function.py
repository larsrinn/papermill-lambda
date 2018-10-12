import requests
import papermill as pm

import os

import sys
sys.path.append("/var/task/bin")


def lambda_handler(request, context):
    url = "http://example.com"
    pm.execute_notebook(
        "get_url.ipynb",
        "/tmp/output.ipynb",
        parameters=dict(
            url=url,
        )
    )
    return os.path.exists("/tmp/output.ipynb")


if __name__ == '__main__':
    lambda_handler('', '')
