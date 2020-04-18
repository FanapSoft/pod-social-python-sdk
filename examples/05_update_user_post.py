# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_social import PodSocial

try:
    pod_social = PodSocial(api_token=API_TOKEN, server_type=SERVER_MODE)

    other_params = {
        # "repliedPostId": 123,
        # "metadata": {},
        # "lat": 35.123456,
        # "lng": 36.123456,
        # "tags": ["Tag 1", "Tag 2"]
    }

    content = "Why do we use it? It is a long established fact that a reader will be distracted by the readable " \
              "content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a " \
              "more-or-less normal distribution of letters, as opposed to using 'Content here, content here', " \
              "making it look like readable English. Many desktop publishing packages and web page editors now use " \
              "Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites " \
              "still in their infancy. Various versions have evolved over the years, sometimes by accident, " \
              "sometimes on purpose (injected humour and the like). "

    print(pod_social.update_user_post(entity_id=21274, name="Edited Post", content=content, can_comment=True,
                                      token=ACCESS_TOKEN, can_like=True, enable=True, **other_params))
    # OUTPUT
    # {
    #   "id": 101201,
    #   "version": 1,
    #   "timelineId": 61717,
    #   "entityId": 21274,
    #   "forwardedId": 0,
    #   "numOfLikes": 0,
    #   "numOfDisLikes": 0,
    #   "numOfShare": 0,
    #   "numOfFavorites": 0,
    #   "numOfComments": 0,
    #   "timestamp": 1586781718347,
    #   "enable": true,
    #   "hide": false,
    #   "business": {
    #     "id": 12240,
    #     "name": "پشتیبانی پاد",
    #     "numOfProducts": 2,
    #     "rate": {
    #       "rate": 0,
    #       "rateCount": 0
    #     },
    #     "sheba": "98070*****************01"
    #   },
    #   "rate": {
    #     "rate": 0,
    #     "rateCount": 0
    #   },
    #   "latitude": 0,
    #   "longitude": 0,
    #   "canComment": false,
    #   "canLike": false,
    #   "canRate": false,
    #   "tags": [],
    #   "tagTrees": [],
    #   "name": "Edited Post",
    #   "data": "Why do we use it? It is a long established fact that a reader will be distracted by .....",
    #   "categoryList": []
    # }

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
