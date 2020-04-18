# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_social import PodSocial

try:
    pod_social = PodSocial(api_token=API_TOKEN, server_type=SERVER_MODE)

    posts = [
        {
            "name": "پست گروهی یک",
            "content": "این محتوای پست است",
            "canComment": True,
            "canLike": True,
            "enable": True,
            "canRate": True,
            "metadata": {"post": "group", "id": 1},
            "lat": 35.123456,
            "lng": 36.123456,
            "tags": ["Tag 1", "Tag 2"],
            # "tagTrees": [],
            # "tagTreeCategoryName": []
        },
        {
            "name": "پست گروهی دو",
            "content": "این محتوای پست است",
            "canComment": True,
            "canLike": True,
            "enable": True,
            "canRate": True,
            "metadata": {"post": "group", "id": 2},
            "lat": 35.123456,
            "lng": 36.123456,
            "tags": ["Tag 2", "Tag 3", "Tag 4", "Tag 5"],
            # "tagTrees": [],
            # "tagTreeCategoryName": []
        }
    ]

    print(pod_social.add_custom_post_list(posts=posts))
    # OUTPUT
    # [
    #   {
    #     "id": 101472,
    #     "version": 0,
    #     "timelineId": 61961,
    #     "entityId": 21327,
    #     "forwardedId": 0,
    #     "numOfLikes": 0,
    #     "numOfDisLikes": 0,
    #     "numOfShare": 0,
    #     "numOfFavorites": 0,
    #     "numOfComments": 0,
    #     "timestamp": 1586957740904,
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
    #     "metadata": "{\"post\": \"group\", \"id\": 1}",
    #     "latitude": 35.123456,
    #     "longitude": 36.123456,
    #     "canComment": true,
    #     "canLike": true,
    #     "canRate": true,
    #     "tags": [
    #       "Tag 1",
    #       "Tag 2"
    #     ],
    #     "tagTrees": [],
    #     "name": "پست گروهی یک",
    #     "data": "این محتوای پست است",
    #     "categoryList": []
    #   },
    #   {
    #     "id": 101473,
    #     "version": 0,
    #     "timelineId": 61962,
    #     "entityId": 21328,
    #     "forwardedId": 0,
    #     "numOfLikes": 0,
    #     "numOfDisLikes": 0,
    #     "numOfShare": 0,
    #     "numOfFavorites": 0,
    #     "numOfComments": 0,
    #     "timestamp": 1586957740978,
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
    #     "metadata": "{\"post\": \"group\", \"id\": 2}",
    #     "latitude": 35.123456,
    #     "longitude": 36.123456,
    #     "canComment": true,
    #     "canLike": true,
    #     "canRate": true,
    #     "tags": [
    #       "Tag 2",
    #       "Tag 3",
    #       "Tag 4",
    #       "Tag 5"
    #     ],
    #     "tagTrees": [],
    #     "name": "پست گروهی دو",
    #     "data": "این محتوای پست است",
    #     "categoryList": []
    #   }
    # ]

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
