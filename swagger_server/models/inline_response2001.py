# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.app_instance_info import AppInstanceInfo  # noqa: F401,E501
from swagger_server import util


class InlineResponse2001(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, app_instace_info: List[AppInstanceInfo]=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger

        :param app_instace_info: The app_instace_info of this InlineResponse2001.  # noqa: E501
        :type app_instace_info: List[AppInstanceInfo]
        """
        self.swagger_types = {
            'app_instace_info': List[AppInstanceInfo]
        }

        self.attribute_map = {
            'app_instace_info': 'appInstaceInfo'
        }
        self._app_instace_info = app_instace_info

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2001':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_1 of this InlineResponse2001.  # noqa: E501
        :rtype: InlineResponse2001
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_instace_info(self) -> List[AppInstanceInfo]:
        """Gets the app_instace_info of this InlineResponse2001.


        :return: The app_instace_info of this InlineResponse2001.
        :rtype: List[AppInstanceInfo]
        """
        return self._app_instace_info

    @app_instace_info.setter
    def app_instace_info(self, app_instace_info: List[AppInstanceInfo]):
        """Sets the app_instace_info of this InlineResponse2001.


        :param app_instace_info: The app_instace_info of this InlineResponse2001.
        :type app_instace_info: List[AppInstanceInfo]
        """

        self._app_instace_info = app_instace_info
