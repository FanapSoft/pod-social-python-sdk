# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_social import PodSocial

try:
    pod_social = PodSocial(api_token=API_TOKEN, server_type=SERVER_MODE)

    other_params = {
        "page": 1,  # or lastId or firstId
        "size": 50
    }

    print(pod_social.get_confirm_comments(post_id=101201, token=ACCESS_TOKEN, **other_params))
    # OUTPUT
    # [
    #   {
    #     "id": 9685,
    #     "text": "Python Unittest",
    #     "timestamp": 1587186236448,
    #     "user": {
    #       "id": 16849,
    #       "name": "رضا زارع",
    #       "ssoId": "11923337",
    #       "ssoIssuerCode": 1,
    #       "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #     },
    #     "confirmed": false,
    #     "numOfLikes": 0,
    #     "numOfComments": 0,
    #     "liked": false
    #   }
    # ]

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
