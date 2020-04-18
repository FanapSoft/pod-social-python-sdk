# coding=utf-8
from __future__ import unicode_literals

import unittest

from pod_base import InvalidDataException, APIException
from random import randint
from pod_social import PodSocial, PostType
from tests.config import *


class TestPodSettlement(unittest.TestCase):
    __slots__ = "__social"

    def setUp(self):
        self.__social = PodSocial(api_token=API_TOKEN, server_type=SERVER_MODE)

    def test_01_add_custom_post(self):
        name = "پست سفارشی {}".format(randint(100, 999))
        content = "این محتوای {} است".format(name)
        result = self.__social.add_custom_post(name=name, content=content)
        self.assertIsInstance(result, dict, msg="add custom post : check instance")

    def test_01_add_custom_post_all_params(self):
        name = "پست سفارشی {}".format(randint(100, 999))
        content = "این محتوای {} است".format(name)

        other_params = {
            "can_comment": True,
            "can_like": True,
            "can_rate": True,
            "enable": True,
            "uniqueId": "{}".format(10000, 99999),
            "metadata": {"post": True, "custom": True},
            "lat": 35.123456,
            "lng": 36.123456,
            "tags": ["Tag 1", "Tag 2"],
            "tagTrees": ["موبایل"],
            "tagTreeCategoryName": ["محصولات دیجیتال"]
        }

        result = self.__social.add_custom_post(name=name, content=content, **other_params)
        self.assertIsInstance(result, dict, msg="add custom post (all params): check instance")

    def test_01_add_custom_post_required_param(self):
        with self.assertRaises(TypeError, msg="add custom post : required param"):
            self.__social.add_custom_post()

    def test_01_add_custom_post_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="add custom post : validation error"):
            self.__social.add_custom_post(name="", content="", can_comment="True", can_like="True")

    def test_02_get_custom_post_list(self):
        result = self.__social.get_custom_post_list(business_id=BUSINESS_ID)
        self.assertIsInstance(result, list, msg="get custom post list : check instance")

    def test_02_get_custom_post_list_all_params(self):
        params = {
            # "id": [123],
            "uniqueId": ["123"],
            "page": 1,  # or firstId or lastId
            "fromDate": "1399/01/25",
            "toDate": "1402/12/29",
            "tags": ["Tag 1", "Tag 2"],
            "tagTrees": ["موبایل"],
            "tagTreeCategoryName": ["محصولات دیجیتال"],
            "activityInfo": False
        }
        result = self.__social.get_custom_post_list(business_id=BUSINESS_ID, **params)
        self.assertIsInstance(result, list, msg="get custom post list (all params): check instance")

    def test_02_get_custom_post_list_required_param(self):
        with self.assertRaises(TypeError, msg="get custom post list : required param"):
            self.__social.get_custom_post_list()

    def test_02_get_custom_post_list_validation_error(self):
        params = {
            "id": ["123"],
            "uniqueId": 132,
            "fromDate": "1399_01_25",
            "toDate": "1402_12_29",
            "tags": "Tag 1",
            "tagTrees": "موبایل",
            "tagTreeCategoryName": "محصولات دیجیتال",
            "activityInfo": "False"
        }
        with self.assertRaises(InvalidDataException, msg="get custom post list : validation error"):
            self.__social.get_custom_post_list(business_id="123456", **params)

    def test_03_add_custom_post_list(self):
        random = randint(10000, 999999)

        posts = [
            {
                "name": "پست گروهی {}".format(random),
                "content": "این محتوای پست گروهی {} است".format(random),
                "canComment": True,
                "canLike": True,
                "enable": True,
                "canRate": True,
                "metadata": {"post": "group", "id": random},
                "lat": 35.123456,
                "lng": 36.123456,
                "tags": ["Tag 1", "Tag 2"],
                "tagTrees": ["موبایل"],
                "tagTreeCategoryName": ["محصولات دیجیتال"]
            },
            {
                "name": "پست گروهی {}_2".format(random),
                "content": "این محتوای پست گروهی {}_2 است".format(random),
                "canComment": True,
                "canLike": True,
                "enable": True,
                "canRate": True,
                "metadata": {"post": "group", "id": str(random) + "_2"},
                "lat": 35.123456,
                "lng": 36.123456,
                "tags": ["Tag 2", "Tag 3", "Tag 4", "Tag 5"],
                "tagTrees": ["موبایل"],
                "tagTreeCategoryName": ["محصولات دیجیتال"]
            }
        ]

        result = self.__social.add_custom_post_list(posts=posts)
        self.assertIsInstance(result, list, msg="add custom post list : check instance")

    def test_03_add_custom_post_list_required_param(self):
        with self.assertRaises(TypeError, msg="add custom post list : required param"):
            self.__social.add_custom_post_list()

    def test_03_add_custom_post_list_validation_error(self):
        random = randint(10000, 999999)

        posts = [
            {
                "name": "پست گروهی {}".format(random),
                "content": "این محتوای پست گروهی {} است".format(random),
                "canComment": "True",
                "canLike": "True",
                "enable": True,
                "canRate": True,
                "metadata": "asdsd",
                "lat": "35.123456",
                "lng": "36.123456",
                "tags": ["Tag 1", "Tag 2"],
                "tagTrees": ["موبایل"],
                "tagTreeCategoryName": ["محصولات دیجیتال"]
            },
            {
                "name": "پست گروهی {}_2".format(random),
                "content": "این محتوای پست گروهی {}_2 است".format(random),
                "canComment": True,
                "canLike": True,
                "enable": "True",
                "canRate": "True",
                "metadata": {"post": "group", "id": str(random) + "_2"},
                "lat": 35.123456,
                "lng": 36.123456,
                "tags": "Tag2",
                "tagTrees": "موبایل",
                "tagTreeCategoryName": "محصولات دیجیتال"
            }
        ]
        with self.assertRaises(InvalidDataException, msg="add custom post list : validation error"):
            self.__social.add_custom_post_list(posts=posts)

    def __add_custom_post(self):
        name = "پست سفارشی تستی {}".format(randint(10000, 999999))
        content = "این محتوای {} به صورت تستی است".format(name)

        other_params = {
            "can_comment": True,
            "can_like": True,
            "can_rate": True,
            "enable": True,
        }

        return self.__social.add_custom_post(name=name, content=content, **other_params)

    def test_04_update_custom_post(self):
        post = self.__add_custom_post()

        result = self.__social.update_custom_post(entity_id=post["entityId"], name="نام ویرایش شده",
                                                  content="محتوای ویرایش شده")
        self.assertIsInstance(result, dict, msg="update custom post : check instance")

    def test_04_update_custom_post_required_params(self):

        with self.assertRaises(TypeError, msg="update custom post : required params"):
            self.__social.update_custom_post()

    def test_04_update_custom_post_validation_error(self):

        with self.assertRaises(InvalidDataException, msg="update custom post : validation error"):
            self.__social.update_custom_post(entity_id="12346", name="", content="", can_like="True")

    def __add_user_post(self):
        other_params = {
            "metadata": {"user_post": True},
            # "repliedPostId": 101201,
            "tags": ["پست_کاربری", "تست_پایتون"],
            # "lat": 35.123456,
            # "lng": 36.123456,
        }
        return self.__social.add_user_post(name="پست کاربری", content="این یک پست کاربری است", token=ACCESS_TOKEN,
                                           can_comment=True, can_like=True, can_rate=True, **other_params)

    def test_05_update_user_post(self):
        post = self.__add_user_post()
        result = self.__social.update_user_post(entity_id=post["entityId"], name="پست کاربری ویرایش شده",
                                                content="این پست کاربری است که ویرایش شده", token=ACCESS_TOKEN)
        self.assertIsInstance(result, dict, msg="update user post : check instance")

    def test_05_update_user_post_all_params(self):
        post = self.__add_user_post()
        result = self.__social.update_user_post(entity_id=post["entityId"], name="پست کاربری ویرایش شده",
                                                content="این پست کاربری است که ویرایش شده", token=ACCESS_TOKEN,
                                                can_comment=True, can_like=True)
        self.assertIsInstance(result, dict, msg="update user post (all params): check instance")

    def test_05_update_user_post_required_params(self):
        with self.assertRaises(TypeError, msg="update user post : required params"):
            self.__social.update_user_post()

    def test_05_update_user_post_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="update user post : validation errors"):
            self.__social.update_user_post(entity_id="123465", name="", content="", can_like="True", can_comment="True",
                                           token=ACCESS_TOKEN)

    def test_06_add_comment(self):
        result = self.__social.add_comment(post_id=101498, comment="Python Unittest", token=ACCESS_TOKEN)
        self.assertIsInstance(result, int, msg="add comment : check instance")

    def test_06_add_comment_required_params(self):
        with self.assertRaises(TypeError, msg="add comment : required params"):
            self.__social.add_comment()

    def test_06_add_comment_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="add comment : validation errors"):
            self.__social.add_comment(post_id="101498", comment="", token=ACCESS_TOKEN)

    def test_07_get_comment_list(self):
        result = self.__social.get_comment_list(post_id=101498)
        self.assertIsInstance(result, list, msg="get comment list : check instance")

    def test_07_get_comment_list_required_params(self):
        with self.assertRaises(TypeError, msg="get comment list : required params"):
            self.__social.get_comment_list()

    def test_07_get_comment_list_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="get comment list : validation errors"):
            self.__social.get_comment_list(post_id="101498")

    def test_08_confirm_comment_of_custom_post(self):
        comments = self.__social.get_comment_list(post_id=101498)
        if len(comments) == 0:
            self.skipTest("confirm comment of custom post : comments empty")

        result = self.__social.confirm_comment_of_custom_post(comment_id=comments[0]["id"])
        self.assertIsInstance(result, bool, msg="confirm comment of custom post : check instance")

    def test_08_confirm_comment_of_custom_post_required_params(self):
        with self.assertRaises(TypeError, msg="confirm comment of custom post : required params"):
            self.__social.confirm_comment_of_custom_post()

    def test_08_confirm_comment_of_custom_post_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="confirm comment of custom post : validation errors"):
            self.__social.confirm_comment_of_custom_post(comment_id="123465")

    def test_09_un_confirm_comment_of_custom_post(self):
        comments = self.__social.get_comment_list(post_id=101498)
        if len(comments) == 0:
            self.skipTest("unconfirm comment of custom post : comments empty")

        result = self.__social.un_confirm_comment_of_custom_post(comment_id=comments[0]["id"])
        self.assertIsInstance(result, bool, msg="unconfirm comment of custom post : check instance")

    def test_09_un_confirm_comment_of_custom_post_required_params(self):
        with self.assertRaises(TypeError, msg="unconfirm comment of custom post : required params"):
            self.__social.un_confirm_comment_of_custom_post()

    def test_09_un_confirm_comment_of_custom_post_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="unconfirm comment of custom post : validation errors"):
            self.__social.un_confirm_comment_of_custom_post(comment_id="123465")

    def test_10_get_confirm_comments(self):
        result = self.__social.get_confirm_comments(post_id=101498, token=ACCESS_TOKEN)
        self.assertIsInstance(result, list, msg="get confirm comments : check instance")

    def test_10_get_confirm_comments_required_params(self):
        with self.assertRaises(TypeError, msg="get confirm comments : required params"):
            self.__social.get_confirm_comments()

    def test_10_get_confirm_comments_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="get confirm comments : validation errors"):
            self.__social.get_confirm_comments(post_id="101498", token=ACCESS_TOKEN)

    def test_11_like_post(self):
        result = self.__social.like_post(post_id=101498, token=ACCESS_TOKEN)
        self.assertIsInstance(result, bool, msg="like post : check instance")

    def test_11_like_post_required_params(self):
        with self.assertRaises(TypeError, msg="like post : required params"):
            self.__social.like_post()

    def test_11_like_post_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="like post : validation errors"):
            self.__social.like_post(post_id="101498", token=ACCESS_TOKEN)

    def test_12_dislike_post(self):
        result = self.__social.dislike_post(post_id=101498, token=ACCESS_TOKEN)
        self.assertIsInstance(result, bool, msg="dislike post : check instance")

    def test_12_dislike_post_required_params(self):
        with self.assertRaises(TypeError, msg="dislike post : required params"):
            self.__social.dislike_post()

    def test_12_dislike_post_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="dislike post : validation errors"):
            self.__social.dislike_post(post_id="101498", token=ACCESS_TOKEN)

    def test_13_get_like_list(self):
        result = self.__social.get_like_list(post_id=101498, token=ACCESS_TOKEN)
        self.assertIsInstance(result, list, msg="get like list : check instance")

    def test_13_get_like_list_required_params(self):
        with self.assertRaises(TypeError, msg="get like list : required params"):
            self.__social.get_like_list()

    def test_13_get_like_list_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="get like list : validation errors"):
            self.__social.get_like_list(post_id="101498", token=ACCESS_TOKEN)

    def test_14_like_comment(self):
        comments = self.__social.get_comment_list(post_id=101498)
        if len(comments) == 0:
            self.skipTest("like comment : comments empty")
        self.__social.confirm_comment_of_custom_post(comments[0]["id"])

        result = self.__social.like_comment(comment_id=comments[0]["id"], token=ACCESS_TOKEN)
        self.assertIsInstance(result, bool, msg="like comment : check instance")

    def test_14_like_comment_required_params(self):
        with self.assertRaises(TypeError, msg="like comment : required params"):
            self.__social.like_comment()

    def test_14_like_comment_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="like comment : validation errors"):
            self.__social.like_comment(comment_id="101498", token=ACCESS_TOKEN)

    def test_15_dislike_comment(self):
        comments = self.__social.get_comment_list(post_id=101498)
        if len(comments) == 0:
            self.skipTest("dislike comment : comments empty")
        self.__social.confirm_comment_of_custom_post(comments[0]["id"])

        result = self.__social.dislike_comment(comment_id=comments[0]["id"], token=ACCESS_TOKEN)
        self.assertIsInstance(result, bool, msg="dislike comment : check instance")

    def test_15_dislike_comment_required_params(self):
        with self.assertRaises(TypeError, msg="dislike comment : required params"):
            self.__social.dislike_comment()

    def test_15_dislike_comment_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="dislike comment : validation errors"):
            self.__social.dislike_comment(comment_id="101498", token=ACCESS_TOKEN)

    def test_16_get_comment_like_list(self):
        comments = self.__social.get_comment_list(post_id=101498)
        if len(comments) == 0:
            self.skipTest("get comment like list : comments empty")

        result = self.__social.get_comment_like_list(comment_id=comments[0]["id"], token=ACCESS_TOKEN)
        self.assertIsInstance(result, list, msg="get comment like list : check instance")

    def test_16_get_comment_like_list_required_params(self):
        with self.assertRaises(TypeError, msg="get comment like list : required params"):
            self.__social.get_comment_like_list()

    def test_16_get_comment_like_list_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="get comment like list : validation errors"):
            self.__social.get_comment_like_list(comment_id="101498", token=ACCESS_TOKEN)

    def test_17_get_business_time_line(self):
        result = self.__social.get_business_time_line()
        self.assertIsInstance(result, list, msg="get business time line : check instance")

    def test_18_get_time_line(self):
        result = self.__social.get_time_line(token=ACCESS_TOKEN)
        self.assertIsInstance(result, list, msg="get time line : check instance")

    def test_18_get_time_line_required_params(self):
        with self.assertRaises(TypeError, msg="get time line : required params"):
            self.__social.get_time_line()

    def test_19_search_time_line_by_metadata(self):
        meta_query = {
            "field": "post",
            "is": True
        }
        result = self.__social.search_time_line_by_metadata(meta_query=meta_query)
        self.assertIsInstance(result, list, msg="search time line by metadata : check instance")

    def test_19_search_time_line_by_metadata_all_params(self):
        params = {
            "page": 1,  # or lastId or firstId
            "size": 2,
            "userId": 123,
            "postIds": [123],
            "orderBy": ["post:asc"],  # field_name:asc
            "type": PostType.PRODUCT | PostType.CUSTOM_POST,
        }
        meta_query = {
            "field": "post",
            "is": True
        }

        result = self.__social.search_time_line_by_metadata(meta_query=meta_query, **params)
        self.assertIsInstance(result, list, msg="search time line by metadata (all params) : check instance")

    def test_19_search_time_line_by_metadata_required_params(self):
        with self.assertRaises(TypeError, msg="search time line by metadata : required params"):
            self.__social.search_time_line_by_metadata()

    def test_19_search_time_line_by_metadata_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="search time line by metadata : validation errors"):
            self.__social.search_time_line_by_metadata(meta_query="")

    def test_20_full_text_search(self):
        result = self.__social.full_text_search(query="محصول")
        self.assertIsInstance(result, list, msg="full text search : check instance")

    def test_20_full_text_search_all_params(self):
        params = {
            "type": PostType.PRODUCT | PostType.CUSTOM_POST,
            "guildCodes": ["API_GUILD", "INFORMATION_TECHNOLOGY_GUILD"],
            "tags": ["Tag 1", "Tag 2"],
            # "tagTrees": ["موبایل"],
            # "tagTreesCodes": ["محصولات دیجیتال"],
            # "dateFrom": "1399/01/25",
            # "dateTo": "1399/01/31",
            # "lat": 35.123456,
            # "lng": 36.123456,
            # "distance": 1,  # distance by KM
        }

        result = self.__social.full_text_search(query="محصول", **params)
        self.assertIsInstance(result, list, msg="full text search (all params) : check instance")

    def test_20_full_text_search_required_params(self):
        with self.assertRaises(TypeError, msg="full text search : required params"):
            self.__social.full_text_search()

    def test_20_full_text_search_validation_errors(self):
        params = {
            "type": "564",
            "guildCodes": "API_GUILD",
            "tags": "Tag1",
            # "tagTrees": ["موبایل"],
            # "tagTreesCodes": ["محصولات دیجیتال"],
            # "dateFrom": "1399/01/25",
            # "dateTo": "1399/01/31",
            # "lat": 35.123456,
            # "lng": 36.123456,
            # "distance": 1,  # distance by KM
        }
        with self.assertRaises(InvalidDataException, msg="full text search : validation errors"):
            self.__social.full_text_search(query=123, **params)

    def test_21_add_user_post(self):
        result = self.__social.add_user_post(name="پست کاربری", content="این یک پست کاربری است", token=ACCESS_TOKEN,
                                             can_comment=True, can_like=True, can_rate=True)
        self.assertIsInstance(result, dict, msg="add user post : check instance")

    def test_21_add_user_post_all_params(self):
        params = {
            "metadata": {"user_post": True},
            "repliedPostId": 101498,
            "tags": ["پست_کاربری", "تست_پایتون"],
            "lat": 35.123456,
            "lng": 36.123456,
        }

        result = self.__social.add_user_post(name="پست کاربری", content="این یک پست کاربری است", token=ACCESS_TOKEN,
                                             can_comment=True, can_like=True, can_rate=True, **params)
        self.assertIsInstance(result, dict, msg="add user post (all params) : check instance")

    def test_21_add_user_post_required_params(self):
        with self.assertRaises(TypeError, msg="add user post : required params"):
            self.__social.add_user_post()

    def test_21_add_user_post_validation_errors(self):
        params = {
            "metadata": "ASDASD",
            "repliedPostId": "101498",
            "tags": "پست_کاربری",
            "lat": "35.123456",
            "lng": "36.123456",
        }
        with self.assertRaises(InvalidDataException, msg="add user post : validation errors"):
            self.__social.add_user_post(name=13, content=213, token=ACCESS_TOKEN, can_comment="False", **params)

    def test_22_user_post_list(self):
        result = self.__social.user_post_list()
        self.assertIsInstance(result, list, msg="user post list : check instance")

    def test_22_user_post_list_all_params(self):
        params = {
            "page": 1,  # or firstId or lastId
            "size": 20,
            "parentPostId": 101498,
            # "tags": ["Tag 1", "Tag 2"],
        }

        result = self.__social.user_post_list(**params)
        self.assertIsInstance(result, list, msg="user post list (all params) : check instance")

    def test_22_user_post_list_validation_errors(self):
        params = {
            "page": 1,  # or firstId or lastId
            "size": 20,
            "parentPostId": "101498",
            "tags": "Tag 1",
        }
        with self.assertRaises(InvalidDataException, msg="user post list : validation errors"):
            self.__social.user_post_list(**params)

    def test_23_load_user_post(self):
        user_posts = self.__social.user_post_list()
        if len(user_posts) == 0:
            self.skipTest("load user post : empty user post")

        result = self.__social.load_user_post(user_posts[0]["entityId"])
        self.assertIsInstance(result, dict, msg="load user post : check instance")

    def test_23_load_user_post_required_params(self):
        with self.assertRaises(TypeError, msg="load user post : required params"):
            self.__social.load_user_post()

    def test_23_load_user_post_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="load user post : validation errors"):
            self.__social.load_user_post(entity_id="123")

    def test_24_search_on_user_post_by_metadata(self):
        meta_query = {
            "field": "user_post",
            "is": True
        }
        result = self.__social.search_on_user_post_by_metadata(meta_query=meta_query, user_id=USER_ID)
        self.assertIsInstance(result, list, msg="search on user post by metadata : check instance")

    def test_24_search_on_user_post_by_metadata_required_params(self):
        with self.assertRaises(TypeError, msg="search on user post by metadata : required params"):
            self.__social.search_on_user_post_by_metadata()

    def test_24_search_on_user_post_by_metadata_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="search on user post by metadata : validation errors"):
            self.__social.search_on_user_post_by_metadata(meta_query="123", user_id="123")

    def test_25_confirm_comment_of_user_post(self):
        comments = self.__social.get_comment_list(post_id=101498)
        if len(comments) == 0:
            self.skipTest("confirm comment of user post : empty comment list")

        result = self.__social.confirm_comment_of_user_post(comment_id=comments[0]["id"])
        self.assertIsInstance(result, bool, msg="confirm comment of user post : check instance")

    def test_25_confirm_comment_of_user_post_required_params(self):
        with self.assertRaises(TypeError, msg="confirm comment of user post : required params"):
            self.__social.confirm_comment_of_user_post()

    def test_25_confirm_comment_of_user_post_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="confirm comment of user post : validation errors"):
            self.__social.confirm_comment_of_user_post(comment_id="123")

    def test_26_un_confirm_comment_of_user_post(self):
        comments = self.__social.get_comment_list(post_id=101498)
        if len(comments) == 0:
            self.skipTest("unconfirm comment of user post : empty comment list")

        result = self.__social.un_confirm_comment_of_user_post(comment_id=comments[0]["id"])
        self.assertIsInstance(result, bool, msg="unconfirm comment of user post : check instance")

    def test_26_un_confirm_comment_of_user_post_required_params(self):
        with self.assertRaises(TypeError, msg="unconfirm comment of user post : required params"):
            self.__social.un_confirm_comment_of_user_post()

    def test_26_un_confirm_comment_of_user_post_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="unconfirm comment of user post : validation errors"):
            self.__social.un_confirm_comment_of_user_post(comment_id="123")

    def test_27_share_user_post(self):
        result = self.__social.share_user_post(forwarded_post_id=101498, token=ACCESS_TOKEN)
        self.assertIsInstance(result, bool, msg="share user post : check instance")

    def test_27_share_user_post_required_params(self):
        with self.assertRaises(TypeError, msg="share user post : required params"):
            self.__social.share_user_post()

    def test_27_share_user_post_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="share user post : validation errors"):
            self.__social.share_user_post(forwarded_post_id="123", can_comment="True", token=ACCESS_TOKEN)
