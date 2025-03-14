# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.app_manifest_app_repo import AppManifestAppRepo  # noqa: F401,E501
from swagger_server.models.app_manifest_component_spec import AppManifestComponentSpec  # noqa: F401,E501
from swagger_server.models.operating_system import OperatingSystem  # noqa: F401,E501
from swagger_server.models.required_resources import RequiredResources  # noqa: F401,E501
import re  # noqa: F401,E501
from swagger_server import util


class AppManifest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, version: int=None, package_type: str=None, operating_system: OperatingSystem=None, app_repo: AppManifestAppRepo=None, required_resources: RequiredResources=None, component_spec: List[AppManifestComponentSpec]=None):  # noqa: E501
        """AppManifest - a model defined in Swagger

        :param name: The name of this AppManifest.  # noqa: E501
        :type name: str
        :param version: The version of this AppManifest.  # noqa: E501
        :type version: int
        :param package_type: The package_type of this AppManifest.  # noqa: E501
        :type package_type: str
        :param operating_system: The operating_system of this AppManifest.  # noqa: E501
        :type operating_system: OperatingSystem
        :param app_repo: The app_repo of this AppManifest.  # noqa: E501
        :type app_repo: AppManifestAppRepo
        :param required_resources: The required_resources of this AppManifest.  # noqa: E501
        :type required_resources: RequiredResources
        :param component_spec: The component_spec of this AppManifest.  # noqa: E501
        :type component_spec: List[AppManifestComponentSpec]
        """
        self.swagger_types = {
            'name': str,
            'version': int,
            'package_type': str,
            'operating_system': OperatingSystem,
            'app_repo': AppManifestAppRepo,
            'required_resources': RequiredResources,
            'component_spec': List[AppManifestComponentSpec]
        }

        self.attribute_map = {
            'name': 'name',
            'version': 'version',
            'package_type': 'packageType',
            'operating_system': 'operatingSystem',
            'app_repo': 'appRepo',
            'required_resources': 'requiredResources',
            'component_spec': 'componentSpec'
        }
        self._name = name
        self._version = version
        self._package_type = package_type
        self._operating_system = operating_system
        self._app_repo = app_repo
        self._required_resources = required_resources
        self._component_spec = component_spec

    @classmethod
    def from_dict(cls, dikt) -> 'AppManifest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AppManifest of this AppManifest.  # noqa: E501
        :rtype: AppManifest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this AppManifest.

        Name of the application.  # noqa: E501

        :return: The name of this AppManifest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this AppManifest.

        Name of the application.  # noqa: E501

        :param name: The name of this AppManifest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def version(self) -> int:
        """Gets the version of this AppManifest.

        Application version information  # noqa: E501

        :return: The version of this AppManifest.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int):
        """Sets the version of this AppManifest.

        Application version information  # noqa: E501

        :param version: The version of this AppManifest.
        :type version: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def package_type(self) -> str:
        """Gets the package_type of this AppManifest.

        Format of the application image package  # noqa: E501

        :return: The package_type of this AppManifest.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type: str):
        """Sets the package_type of this AppManifest.

        Format of the application image package  # noqa: E501

        :param package_type: The package_type of this AppManifest.
        :type package_type: str
        """
        allowed_values = ["QCOW2", "OVA", "CONTAINER", "HELM"]  # noqa: E501
        if package_type not in allowed_values:
            raise ValueError(
                "Invalid value for `package_type` ({0}), must be one of {1}"
                .format(package_type, allowed_values)
            )

        self._package_type = package_type

    @property
    def operating_system(self) -> OperatingSystem:
        """Gets the operating_system of this AppManifest.


        :return: The operating_system of this AppManifest.
        :rtype: OperatingSystem
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system: OperatingSystem):
        """Sets the operating_system of this AppManifest.


        :param operating_system: The operating_system of this AppManifest.
        :type operating_system: OperatingSystem
        """

        self._operating_system = operating_system

    @property
    def app_repo(self) -> AppManifestAppRepo:
        """Gets the app_repo of this AppManifest.


        :return: The app_repo of this AppManifest.
        :rtype: AppManifestAppRepo
        """
        return self._app_repo

    @app_repo.setter
    def app_repo(self, app_repo: AppManifestAppRepo):
        """Sets the app_repo of this AppManifest.


        :param app_repo: The app_repo of this AppManifest.
        :type app_repo: AppManifestAppRepo
        """
        if app_repo is None:
            raise ValueError("Invalid value for `app_repo`, must not be `None`")  # noqa: E501

        self._app_repo = app_repo

    @property
    def required_resources(self) -> RequiredResources:
        """Gets the required_resources of this AppManifest.


        :return: The required_resources of this AppManifest.
        :rtype: RequiredResources
        """
        return self._required_resources

    @required_resources.setter
    def required_resources(self, required_resources: RequiredResources):
        """Sets the required_resources of this AppManifest.


        :param required_resources: The required_resources of this AppManifest.
        :type required_resources: RequiredResources
        """
        if required_resources is None:
            raise ValueError("Invalid value for `required_resources`, must not be `None`")  # noqa: E501

        self._required_resources = required_resources

    @property
    def component_spec(self) -> List[AppManifestComponentSpec]:
        """Gets the component_spec of this AppManifest.

        Information defined in \"appRepo\" point to the application descriptor e.g. Helm chart, docker-compose yaml file etc. The descriptor may contain one or more containers and their associated meta-data. A component refers to additional details about these containers to expose the instances of the containers to external client applications. App provider can define one or more components (via the associated network port) in componentSpec corresponding to the containers in helm charts or docker-compose yaml file as part of app descriptors.   # noqa: E501

        :return: The component_spec of this AppManifest.
        :rtype: List[AppManifestComponentSpec]
        """
        return self._component_spec

    @component_spec.setter
    def component_spec(self, component_spec: List[AppManifestComponentSpec]):
        """Sets the component_spec of this AppManifest.

        Information defined in \"appRepo\" point to the application descriptor e.g. Helm chart, docker-compose yaml file etc. The descriptor may contain one or more containers and their associated meta-data. A component refers to additional details about these containers to expose the instances of the containers to external client applications. App provider can define one or more components (via the associated network port) in componentSpec corresponding to the containers in helm charts or docker-compose yaml file as part of app descriptors.   # noqa: E501

        :param component_spec: The component_spec of this AppManifest.
        :type component_spec: List[AppManifestComponentSpec]
        """
        if component_spec is None:
            raise ValueError("Invalid value for `component_spec`, must not be `None`")  # noqa: E501

        self._component_spec = component_spec
