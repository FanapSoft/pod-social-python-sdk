# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_social import PodSocial

try:
    pod_social = PodSocial(api_token=API_TOKEN, server_type=SERVER_MODE)

    other_params = {
        # "uniqueId": "123",
        # "metadata": {},
        "lat": 35.123456,
        "lng": 36.123456,
        "tags": ["Tag 1", "Tag 2"],
        # "tagTrees": [],
        # "tagTreeCategoryName": []
    }

    print(pod_social.add_custom_post(name="Second Post", content="این یک پست تستی است", can_comment=False,
                                     can_like=False, can_rate=False, enable=True, **other_params))
    # OUTPUT
    # {
    #   "id": 2805868,
    #   "version": 0,
    #   "timelineId": 2804695,
    #   "entityId": 2751006,
    #   "forwardedId": 0,
    #   "numOfLikes": 0,
    #   "numOfDisLikes": 0,
    #   "numOfShare": 0,
    #   "numOfFavorites": 0,
    #   "numOfComments": 0,
    #   "timestamp": 1586779697918,
    #   "enable": False,
    #   "hide": False,
    #   "business": {
    #     "id": 6066,
    #     "name": "پشتیبانی پاد",
    #     "numOfProducts": 1,
    #     "rate": {
    #       "rate": 0.0,
    #       "rateCount": 0
    #     },
    #     "sheba": "98070*****************01"
    #   },
    #   "rate": {
    #     "rate": 0.0,
    #     "rateCount": 0
    #   },
    #   "latitude": 0.0,
    #   "longitude": 0.0,
    #   "canComment": False,
    #   "canLike": False,
    #   "canRate": False,
    #   "tags": [],
    #   "tagTrees": [],
    #   "name": "First Post",
    #   "data": "این یک پست تستی است",
    #   "categoryList": []
    # }

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
