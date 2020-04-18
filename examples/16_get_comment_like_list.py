# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_social import PodSocial

try:
    pod_social = PodSocial(api_token=API_TOKEN, server_type=SERVER_MODE)

    token = ACCESS_TOKEN  # USER ACCESS TOKEN
    print(pod_social.get_comment_like_list(comment_id=9677, token=token))
    # OUTPUT
    # [
    #   {
    #     "id": 3967,
    #     "timestamp": 1586868101200,
    #     "user": {
    #       "id": 18305,
    #       "name": "TestNeda",
    #       "ssoId": "13099474",
    #       "ssoIssuerCode": 1,
    #       "profileImage": "http://sandbox.pod.ir:8080/nzh/image/2"
    #     }
    #   }
    # ]

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
