# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_social import PodSocial

try:
    pod_social = PodSocial(api_token=API_TOKEN, server_type=SERVER_MODE)

    other_params = {
        # "id": [123],
        # "uniqueId": ["123"],
        # "page": 1,  # or firstId or lastId
        "fromDate": "1399/01/25",
        "toDate": "1399/01/31",
        # "tags": ["Tag 1", "Tag 2"],
        # "tagTrees": [],
        # "tagTreeCategoryName": [],
        # "activityInfo": False
    }

    token = None  # اکسس توکن کاربر - در صورت عدم ارسال توکن کسب و کار ارسال می شود
    print(pod_social.get_custom_post_list(business_id=12240, page=1, size=50, token=token, **other_params))
    # OUTPUT
    # [
    #   {
    #     "id": 101201,
    #     "version": 0,
    #     "timelineId": 61717,
    #     "entityId": 21274,
    #     "forwardedId": 0,
    #     "numOfLikes": 0,
    #     "numOfDisLikes": 0,
    #     "numOfShare": 0,
    #     "numOfFavorites": 0,
    #     "numOfComments": 0,
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
    #       "sheba": "98070*****************01"
    #     },
    #     "rate": {
    #       "rate": 0,
    #       "rateCount": 0
    #     },
    #     "latitude": 35.123456,
    #     "longitude": 36.123456,
    #     "canComment": false,
    #     "canLike": false,
    #     "canRate": false,
    #     "tags": [
    #       "Tag 1",
    #       "Tag 2"
    #     ],
    #     "tagTrees": [],
    #     "name": "Second Post",
    #     "data": "Why do we use it? It is a long established fact that a reader will ......",
    #     "categoryList": []
    #   }
    # ]

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
