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
        # "timelineId": 123,
        # "entityId": 123,
        # "uniqueId": [123],
        # "postId": [123],
        # "fromDate": "1399/01/25",
        # "toDate": "1399/01/31",
        "type": PostType.PRODUCT | PostType.CUSTOM_POST,
        # "guildCodes": ["API_GUILD"],
        # "metadata": {},
        # "tags": ["Tag1"],
        # "tagTreeCategoryName": [""],
        # "tagTrees": [""],
    }

    print(pod_social.get_business_time_line(**params))
    # OUTPUT
    # [
    #   {
    #     "type": 1,
    #     "item": {
    #       "id": 83080,
    #       "version": 0,
    #       "timelineId": 43640,
    #       "entityId": 40888,
    #       "forwardedId": 0,
    #       "numOfLikes": 0,
    #       "numOfDisLikes": 0,
    #       "numOfShare": 0,
    #       "numOfFavorites": 0,
    #       "numOfComments": 0,
    #       "timestamp": 1573384257840,
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
    #         "postId": 83080,
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
    #       "name": "تهران مشهد",
    #       "description": "فول فرست کلاس",
    #       "categoryList": [],
    #       "unlimited": false,
    #       "availableCount": 115,
    #       "price": 8000000,
    #       "discount": 0,
    #       "attributeValues": [],
    #       "guild": {
    #         "id": 47,
    #         "name": "فناوری اطلاعات",
    #         "code": "INFORMATION_TECHNOLOGY_GUILD"
    #       },
    #       "allowUserInvoice": false,
    #       "allowUserPrice": false,
    #       "currency": {
    #         "name": "ریال",
    #         "code": "IRR"
    #       },
    #       "preferredTaxRate": 0.09
    #     }
    #   },
    #   {
    #     "type": 1,
    #     "item": {
    #       "id": 81756,
    #       "version": 4,
    #       "timelineId": 42316,
    #       "entityId": 39989,
    #       "forwardedId": 0,
    #       "numOfLikes": 0,
    #       "numOfDisLikes": 0,
    #       "numOfShare": 0,
    #       "numOfFavorites": 0,
    #       "numOfComments": 0,
    #       "timestamp": 1572696763554,
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
    #         "postId": 81756,
    #         "liked": false,
    #         "favorite": false
    #       },
    #       "metadata": "",
    #       "latitude": 0,
    #       "longitude": 0,
    #       "canComment": false,
    #       "canLike": false,
    #       "canRate": true,
    #       "tags": [],
    #       "tagTrees": [],
    #       "name": "test",
    #       "description": "test test",
    #       "categoryList": [],
    #       "unlimited": true,
    #       "availableCount": 0,
    #       "price": 100,
    #       "discount": 0,
    #       "attributeValues": [
    #         {
    #           "code": "provider",
    #           "name": "تامین کننده",
    #           "value": "core"
    #         },
    #         {
    #           "code": "guildcode",
    #           "name": "صنف",
    #           "value": "INFORMATION_TECHNOLOGY_GUILD"
    #         },
    #         {
    #           "code": "methodtype",
    #           "name": "نوع متد",
    #           "value": "rest"
    #         }
    #       ],
    #       "guild": {
    #         "id": 47,
    #         "name": "فناوری اطلاعات",
    #         "code": "INFORMATION_TECHNOLOGY_GUILD"
    #       },
    #       "allowUserInvoice": false,
    #       "allowUserPrice": false,
    #       "templateCode": "service_call",
    #       "currency": {
    #         "name": "ریال",
    #         "code": "IRR"
    #       },
    #       "preferredTaxRate": 0
    #     }
    #   }
    # ]

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
