# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_social import PodSocial, PostType

try:
    pod_social = PodSocial(api_token=API_TOKEN, server_type=SERVER_MODE)
    params = {
        "page": 1,  # or lastId or firstId
        "size": 2,
        # "userId": 123,
        # "postIds": [123],
        # "orderBy": ["post:asc"],     # field_name:asc
        "type": PostType.PRODUCT | PostType.CUSTOM_POST,
    }

    meta_query = {
        "field": "scPriceCalculationType",
        "is": "FIXED"
    }

    print(pod_social.search_time_line_by_metadata(meta_query=meta_query, **params))
    # OUTPUT
    # [
    #   {
    #     "type": 4096,
    #     "item": {
    #       "id": 101201,
    #       "version": 4,
    #       "timelineId": 61717,
    #       "entityId": 21274,
    #       "forwardedId": 0,
    #       "numOfLikes": 1,
    #       "numOfDisLikes": 0,
    #       "numOfShare": 0,
    #       "numOfFavorites": 0,
    #       "numOfComments": 3,
    #       "timestamp": 1586781718347,
    #       "enable": true,
    #       "hide": false,
    #       "business": {
    #         "id": 12240,
    #         "name": "پشتیبانی پاد",
    #         "numOfProducts": 2,
    #         "rate": {
    #           "rate": 0,
    #           "rateCount": 0
    #         },
    #         "sheba": "98********************01"
    #       },
    #       "rate": {
    #         "rate": 0,
    #         "rateCount": 0
    #       },
    #       "userPostInfo": {
    #         "postId": 101201,
    #         "liked": false,
    #         "favorite": false
    #       },
    #       "latitude": 0,
    #       "longitude": 0,
    #       "canComment": true,
    #       "canLike": true,
    #       "canRate": true,
    #       "tags": [],
    #       "tagTrees": [],
    #       "name": "Edited Post",
    #       "data": "Why do we use it? It is a long established fact that a reader will be ....",
    #       "categoryList": []
    #     }
    #   },
    #   {
    #     "type": 4096,
    #     "item": {
    #       "id": 101197,
    #       "version": 0,
    #       "timelineId": 61716,
    #       "entityId": 21273,
    #       "forwardedId": 0,
    #       "numOfLikes": 0,
    #       "numOfDisLikes": 0,
    #       "numOfShare": 0,
    #       "numOfFavorites": 0,
    #       "numOfComments": 0,
    #       "timestamp": 1586781562141,
    #       "enable": false,
    #       "hide": false,
    #       "business": {
    #         "id": 12240,
    #         "name": "پشتیبانی پاد",
    #         "numOfProducts": 2,
    #         "rate": {
    #           "rate": 0,
    #           "rateCount": 0
    #         },
    #         "sheba": "98********************01"
    #       },
    #       "rate": {
    #         "rate": 0,
    #         "rateCount": 0
    #       },
    #       "userPostInfo": {
    #         "postId": 101197,
    #         "liked": false,
    #         "favorite": false
    #       },
    #       "metadata": "{}",
    #       "latitude": 35.123456,
    #       "longitude": 36.123456,
    #       "uniqueId": "123",
    #       "canComment": false,
    #       "canLike": false,
    #       "canRate": false,
    #       "tags": [
    #         "Tag 1",
    #         "Tag 2"
    #       ],
    #       "tagTrees": [],
    #       "name": "First Post",
    #       "data": "این یک پست تستی است",
    #       "categoryList": []
    #     }
    #   }
    # ]

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
