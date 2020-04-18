# coding=utf-8
from __future__ import unicode_literals

from pod_base import APIException, PodException
from examples.config import *
from pod_social import PodSocial, PostType

try:
    pod_social = PodSocial(api_token=API_TOKEN, server_type=SERVER_MODE)
    other_params = {
        "metadata": {},
        "repliedPostId": 101201,
        "tags": ["پست_کاربری", "تست_پایتون"],
        # "lat": 35.123456,
        # "lng": 36.123456,
    }

    print(pod_social.add_user_post(name="پست کاربری", content="این یک پست کاربری است", token=ACCESS_TOKEN,
                                   can_comment=True, can_like=True, can_rate=True, **other_params))

    # OUTPUT
    # {
    #   "id": 101454,
    #   "version": 0,
    #   "timelineId": 61943,
    #   "entityId": 2461,
    #   "forwardedId": 0,
    #   "numOfLikes": 0,
    #   "numOfDisLikes": 0,
    #   "numOfShare": 0,
    #   "numOfFavorites": 0,
    #   "numOfComments": 0,
    #   "timestamp": 1586952071627,
    #   "enable": true,
    #   "hide": false,
    #   "userSrv": {
    #     "id": 16849,
    #     "name": "رضا زارع",
    #     "ssoId": "11923337",
    #     "ssoIssuerCode": 1,
    #     "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #   },
    #   "rate": {
    #     "rate": 0,
    #     "rateCount": 0
    #   },
    #   "userPostInfo": {
    #     "postId": 101454,
    #     "liked": false,
    #     "favorite": false
    #   },
    #   "metadata": "{}",
    #   "latitude": 0,
    #   "longitude": 0,
    #   "canComment": true,
    #   "canLike": true,
    #   "canRate": true,
    #   "tags": [
    #     "پست_کاربری",
    #     "تست_پایتون"
    #   ],
    #   "tagTrees": [],
    #   "repliedItemSrv": {
    #     "id": 101201,
    #     "version": 4,
    #     "timelineId": 61717,
    #     "entityId": 21274,
    #     "forwardedId": 0,
    #     "numOfLikes": 1,
    #     "numOfDisLikes": 0,
    #     "numOfShare": 0,
    #     "numOfFavorites": 0,
    #     "numOfComments": 3,
    #     "timestamp": 1586781718347,
    #     "enable": true,
    #     "hide": false,
    #     "business": {
    #       "id": 12240,
    #       "name": "پشتیبانی پاد",
    #       "numOfProducts": 2,
    #       "rate": {
    #         "rate": 0,
    #         "rateCount": 0
    #       },
    #       "sheba": "98********************01"
    #     },
    #     "rate": {
    #       "rate": 0,
    #       "rateCount": 0
    #     },
    #     "userPostInfo": {
    #       "postId": 101201,
    #       "liked": true,
    #       "favorite": false
    #     },
    #     "latitude": 0,
    #     "longitude": 0,
    #     "canComment": true,
    #     "canLike": true,
    #     "canRate": true,
    #     "tags": [],
    #     "tagTrees": [],
    #     "name": "Edited Post",
    #     "data": "Why do we use it? It is a long established fact that a reader will be distrac....",
    #     "categoryList": []
    #   },
    #   "name": "پست کاربری",
    #   "content": "این یک پست کاربری است"
    # }

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
