# coding=utf-8
from __future__ import unicode_literals

from pod_base import APIException, PodException
from examples.config import *
from pod_social import PodSocial, PostType

try:
    pod_social = PodSocial(api_token=API_TOKEN, server_type=SERVER_MODE)
    params = {
        # "type": PostType.PRODUCT | PostType.CUSTOM_POST,
        # "guildCodes": ["API_GUILD", "INFORMATION_TECHNOLOGY_GUILD"],
        "tags": ["Tag 1", "Tag 2"],
        # "tagTrees": [""],
        # "tagTreesCodes": [""],
        # "dateFrom": "1399/01/25",
        # "dateTo": "1399/01/31",
        # "lat": 35.123456,
        # "lng": 36.123456,
        # "distance": 1,  # distance by KM
    }

    query = "محصول"

    print(pod_social.full_text_search(query=query, page=1, size=20, **params))

    # OUTPUT
    # [
    #   {
    #     "type": 1,
    #     "item": "{\"id\":83080,\"version\":0,\"timelineId\":43640,\"entityId\":40888,\"forwardedId\":0,\"numOf...}"
    #   },
    #   {
    #     "type": 1,
    #     "item": "{\"id\":81756,\"version\":4,\"timelineId\":42316,\"entityId\":39989,\"forwardedId\":0,\"numOf...}"
    #   }
    # ]

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
