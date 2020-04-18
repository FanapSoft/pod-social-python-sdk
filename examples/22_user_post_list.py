# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_social import PodSocial

try:
    pod_social = PodSocial(api_token=API_TOKEN, server_type=SERVER_MODE)

    other_params = {
        "page": 1,  # or firstId or lastId
        "size": 20,
        "parentPostId": 101201,
        # "tags": ["Tag 1", "Tag 2"],
    }

    token = ACCESS_TOKEN  # اکسس توکن کاربر - در صورت عدم ارسال توکن کسب و کار ارسال می شود
    print(pod_social.user_post_list(token=token, **other_params))
    # OUTPUT
    # [
    #   {
    #     "id": 101454,
    #     "version": 0,
    #     "timelineId": 61943,
    #     "entityId": 2461,
    #     "forwardedId": 0,
    #     "numOfLikes": 0,
    #     "numOfDisLikes": 0,
    #     "numOfShare": 0,
    #     "numOfFavorites": 0,
    #     "numOfComments": 0,
    #     "timestamp": 1586952071627,
    #     "enable": true,
    #     "hide": false,
    #     "userSrv": {
    #       "id": 16849,
    #       "name": "رضا زارع",
    #       "ssoId": "11923337",
    #       "ssoIssuerCode": 1,
    #       "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=...."
    #     },
    #     "rate": {
    #       "rate": 0,
    #       "rateCount": 0
    #     },
    #     "userPostInfo": {
    #       "postId": 101454,
    #       "liked": false,
    #       "favorite": false
    #     },
    #     "metadata": "{}",
    #     "latitude": 0,
    #     "longitude": 0,
    #     "canComment": true,
    #     "canLike": true,
    #     "canRate": true,
    #     "tags": [
    #       "پست_کاربری",
    #       "تست_پایتون"
    #     ],
    #     "tagTrees": [],
    #     "name": "پست کاربری",
    #     "content": "این یک پست کاربری است",
    #     "repliedPostId": 101201
    #   }
    # ]

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
