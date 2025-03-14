# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.app_instance_info import AppInstanceInfo  # noqa: F401,E501
from swagger_server import util


class InlineResponse202(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, app_instaces: List[AppInstanceInfo]=None):  # noqa: E501
        """InlineResponse202 - a model defined in Swagger

        :param app_instaces: The app_instaces of this InlineResponse202.  # noqa: E501
        :type app_instaces: List[AppInstanceInfo]
        """
        self.swagger_types = {
            'app_instaces': List[AppInstanceInfo]
        }

        self.attribute_map = {
            'app_instaces': 'appInstaces'
        }
        self._app_instaces = app_instaces

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse202':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_202 of this InlineResponse202.  # noqa: E501
        :rtype: InlineResponse202
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_instaces(self) -> List[AppInstanceInfo]:
        """Gets the app_instaces of this InlineResponse202.


        :return: The app_instaces of this InlineResponse202.
        :rtype: List[AppInstanceInfo]
        """
        return self._app_instaces

    @app_instaces.setter
    def app_instaces(self, app_instaces: List[AppInstanceInfo]):
        """Sets the app_instaces of this InlineResponse202.


        :param app_instaces: The app_instaces of this InlineResponse202.
        :type app_instaces: List[AppInstanceInfo]
        """

        self._app_instaces = app_instaces
