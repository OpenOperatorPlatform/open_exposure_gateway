import connexion
import six

from swagger_server.configs.logger_config import logger
from swagger_server.filters.service_functions import find_requested_service_function
from swagger_server.models.app_id import AppId  # noqa: E501
from swagger_server.models.app_instance_id import AppInstanceId  # noqa: E501
from swagger_server.models.app_manifest import AppManifest  # noqa: E501
from swagger_server.models.edge_cloud_region import EdgeCloudRegion  # noqa: E501
from swagger_server.models.edge_cloud_zone import EdgeCloudZone  # noqa: E501
from swagger_server.models.error_info import ErrorInfo  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response202 import InlineResponse202  # noqa: E501
from swagger_server.models.submitted_app import SubmittedApp  # noqa: E501
from swagger_server import util
from swagger_server.schema_mappers.application_instantiation_mapper import (
    map_to_pi_edge_deployed_service_function,
)
from swagger_server.services.pi_edge_services import PiEdgeAPIClientFactory


def create_app_instance(body, app_id, x_correlator=None):  # noqa: E501
    """Instantiation of an Application

    Ask the Edge Cloud Platform to instantiate an application to one or several Edge Cloud Zones with an Application as an input and an Application Instance as the output.  # noqa: E501

    :param body: Array of Edge Cloud Zone
    :type body: list | bytes
    :param app_id: A globally unique identifier associated with the application. Edge Cloud Provider generates this identifier when the application is submitted.
    :type app_id: dict | bytes
    :param x_correlator: Correlation id for the different services
    :type x_correlator: str

    :rtype: InlineResponse202
    """
    try:
        if connexion.request.is_json:
            body = [
                EdgeCloudZone.from_dict(d) for d in connexion.request.get_json()
            ]  # noqa: E501
        # if connexion.request.is_json:
        #     app_id = AppId.from_dict(connexion.request.get_json())  # noqa: E501

        logger.critical(body)
        logger.critical(f"Test: {app_id}")

        pi_edge_factory = PiEdgeAPIClientFactory()
        pi_edge_api_client = pi_edge_factory.create_pi_edge_api_client()

        service_functions_catalogue = (
            pi_edge_api_client.get_service_functions_catalogue()
        )
        requested_application = find_requested_service_function(
            service_functions_catalogue, app_id
        )
        if requested_application is None:
            return {
                "status": 400,
                "code": "INVALID_ARGUMENT",
                "message": "The requested appId could not be retrieved. Please verify application metadata for the provided id do exists.",
            }, 400

        deployed_service_functions = [
            map_to_pi_edge_deployed_service_function(
                edge_cloud, requested_application["name"]
            )
            for edge_cloud in body
        ]

        for service_function in deployed_service_functions:
            result = pi_edge_api_client.deploy_service_function(data=service_function)
            if result != None:  # an error occurred
                if "error" in result.keys():
                    raise Exception(result["error"])
                else:
                    raise Exception("Unexpected error in app instantiation")
        return {}, 202  # application instantiation accepted
    except:
        logger.exception("Error instantiating application")
        return {
            "status": 500,
            "code": "INTERNAL",
            "message": "Internal server error.",
        }, 500


def delete_app(app_id, x_correlator=None):  # noqa: E501
    """Delete an Application from an Edge Cloud Provider

    Delete all the information and content related to an Application # noqa: E501

    :param app_id: Identificator of the application to be deleted provided by the Edge Cloud Provider once the submission was successful
    :type app_id: dict | bytes
    :param x_correlator: Correlation id for the different services
    :type x_correlator: str

    :rtype: None
    """
    if connexion.request.is_json:
        app_id = AppId.from_dict(connexion.request.get_json())  # noqa: E501
    return "do some magic!"


def delete_app_instance(app_id, app_instance_id, x_correlator=None):  # noqa: E501
    """Terminate an Application Instance

    Terminate a running instance of an application within an Edge Cloud Zone  # noqa: E501

    :param app_id: A globally unique identifier associated with the application. Edge Cloud Provider generates this identifier when the application is submitted.
    :type app_id: dict | bytes
    :param app_instance_id: Identificator of the specific application instance that will be terminated
    :type app_instance_id: dict | bytes
    :param x_correlator: Correlation id for the different services
    :type x_correlator: str

    :rtype: None
    """
    if connexion.request.is_json:
        app_id = AppId.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        app_instance_id = AppInstanceId.from_dict(
            connexion.request.get_json()
        )  # noqa: E501
    return "do some magic!"


def get_app(app_id, x_correlator=None):  # noqa: E501
    """Retrieve the information of an Application

    Ask the Edge Cloud Provider the information for a given application  # noqa: E501

    :param app_id: A globally unique identifier associated with the application. Edge Cloud Provider generates this identifier when the application is submitted.
    :type app_id: dict | bytes
    :param x_correlator: Correlation id for the different services
    :type x_correlator: str

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        app_id = AppId.from_dict(connexion.request.get_json())  # noqa: E501
    return "do some magic!"


def get_app_instance(
    app_id, x_correlator=None, app_instance_id=None, region=None
):  # noqa: E501
    """Retrieve the information of Application Instances for a given App

    Ask the Edge Cloud Provider the information of the instances for a given application  # noqa: E501

    :param app_id: A globally unique identifier associated with the application. Edge Cloud Provider generates this identifier when the application is submitted.
    :type app_id: dict | bytes
    :param x_correlator: Correlation id for the different services
    :type x_correlator: str
    :param app_instance_id: A globally unique identifier associated with a running instance of an application within an specific Edge Cloud Zone. Edge Cloud Provider generates this identifier.
    :type app_instance_id: dict | bytes
    :param region: Human readable name of the geographical Edge Cloud Region of the Edge Cloud. Defined by the Edge Cloud Provider.
    :type region: dict | bytes

    :rtype: InlineResponse2001
    """
    if connexion.request.is_json:
        app_id = AppId.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        app_instance_id = AppInstanceId.from_dict(
            connexion.request.get_json()
        )  # noqa: E501
    if connexion.request.is_json:
        region = EdgeCloudRegion.from_dict(connexion.request.get_json())  # noqa: E501
    return "do some magic!"


def submit_app(body, x_correlator=None):  # noqa: E501
    """Submit application metadata to the Edge Cloud Provider.

        Contains the information about the application to be instantiated in the Edge Cloud  # noqa: E501

        :param body: The Application Provider request contains mandatory
    criteria (e.g. required CPU, memory, storage, bandwidth) and
    optional parameters.

        :type body: dict | bytes
        :param x_correlator: Correlation id for the different services
        :type x_correlator: str

        :rtype: SubmittedApp
    """
    if connexion.request.is_json:
        body = AppManifest.from_dict(connexion.request.get_json())  # noqa: E501
    return "do some magic!"
