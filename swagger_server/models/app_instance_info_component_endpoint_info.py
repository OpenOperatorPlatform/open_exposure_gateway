# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.access_endpoint import AccessEndpoint  # noqa: F401,E501
import re  # noqa: F401,E501
from swagger_server import util


class AppInstanceInfoComponentEndpointInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, interface_id: str=None, access_points: AccessEndpoint=None):  # noqa: E501
        """AppInstanceInfoComponentEndpointInfo - a model defined in Swagger

        :param interface_id: The interface_id of this AppInstanceInfoComponentEndpointInfo.  # noqa: E501
        :type interface_id: str
        :param access_points: The access_points of this AppInstanceInfoComponentEndpointInfo.  # noqa: E501
        :type access_points: AccessEndpoint
        """
        self.swagger_types = {
            'interface_id': str,
            'access_points': AccessEndpoint
        }

        self.attribute_map = {
            'interface_id': 'interfaceId',
            'access_points': 'accessPoints'
        }
        self._interface_id = interface_id
        self._access_points = access_points

    @classmethod
    def from_dict(cls, dikt) -> 'AppInstanceInfoComponentEndpointInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AppInstanceInfo_componentEndpointInfo of this AppInstanceInfoComponentEndpointInfo.  # noqa: E501
        :rtype: AppInstanceInfoComponentEndpointInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def interface_id(self) -> str:
        """Gets the interface_id of this AppInstanceInfoComponentEndpointInfo.

        This is the interface Identifier that Application Provider defines when application is being submitted.   # noqa: E501

        :return: The interface_id of this AppInstanceInfoComponentEndpointInfo.
        :rtype: str
        """
        return self._interface_id

    @interface_id.setter
    def interface_id(self, interface_id: str):
        """Sets the interface_id of this AppInstanceInfoComponentEndpointInfo.

        This is the interface Identifier that Application Provider defines when application is being submitted.   # noqa: E501

        :param interface_id: The interface_id of this AppInstanceInfoComponentEndpointInfo.
        :type interface_id: str
        """
        if interface_id is None:
            raise ValueError("Invalid value for `interface_id`, must not be `None`")  # noqa: E501

        self._interface_id = interface_id

    @property
    def access_points(self) -> AccessEndpoint:
        """Gets the access_points of this AppInstanceInfoComponentEndpointInfo.


        :return: The access_points of this AppInstanceInfoComponentEndpointInfo.
        :rtype: AccessEndpoint
        """
        return self._access_points

    @access_points.setter
    def access_points(self, access_points: AccessEndpoint):
        """Sets the access_points of this AppInstanceInfoComponentEndpointInfo.


        :param access_points: The access_points of this AppInstanceInfoComponentEndpointInfo.
        :type access_points: AccessEndpoint
        """
        if access_points is None:
            raise ValueError("Invalid value for `access_points`, must not be `None`")  # noqa: E501

        self._access_points = access_points
