# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, Iterable, Optional, Type, TypeVar, Union

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_request(
    resource_group_name: str,
    managed_instance_name: str,
    database_name: str,
    query_id: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-11-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/databases/{databaseName}/queries/{queryId}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "managedInstanceName": _SERIALIZER.url("managed_instance_name", managed_instance_name, "str"),
        "databaseName": _SERIALIZER.url("database_name", database_name, "str"),
        "queryId": _SERIALIZER.url("query_id", query_id, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_by_query_request(
    resource_group_name: str,
    managed_instance_name: str,
    database_name: str,
    query_id: str,
    subscription_id: str,
    *,
    start_time: Optional[str] = None,
    end_time: Optional[str] = None,
    interval: Optional[Union[str, _models.QueryTimeGrainType]] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-11-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/databases/{databaseName}/queries/{queryId}/statistics",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "managedInstanceName": _SERIALIZER.url("managed_instance_name", managed_instance_name, "str"),
        "databaseName": _SERIALIZER.url("database_name", database_name, "str"),
        "queryId": _SERIALIZER.url("query_id", query_id, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    if start_time is not None:
        _params["startTime"] = _SERIALIZER.query("start_time", start_time, "str")
    if end_time is not None:
        _params["endTime"] = _SERIALIZER.query("end_time", end_time, "str")
    if interval is not None:
        _params["interval"] = _SERIALIZER.query("interval", interval, "str")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class ManagedDatabaseQueriesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.sql.SqlManagementClient`'s
        :attr:`managed_database_queries` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get(
        self, resource_group_name: str, managed_instance_name: str, database_name: str, query_id: str, **kwargs: Any
    ) -> _models.ManagedInstanceQuery:
        """Get query by query id.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param managed_instance_name: The name of the managed instance. Required.
        :type managed_instance_name: str
        :param database_name: The name of the database. Required.
        :type database_name: str
        :param query_id: Required.
        :type query_id: str
        :return: ManagedInstanceQuery or the result of cls(response)
        :rtype: ~azure.mgmt.sql.models.ManagedInstanceQuery
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-11-01-preview"))
        cls: ClsType[_models.ManagedInstanceQuery] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            managed_instance_name=managed_instance_name,
            database_name=database_name,
            query_id=query_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ManagedInstanceQuery", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def list_by_query(
        self,
        resource_group_name: str,
        managed_instance_name: str,
        database_name: str,
        query_id: str,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        interval: Optional[Union[str, _models.QueryTimeGrainType]] = None,
        **kwargs: Any
    ) -> Iterable["_models.QueryStatistics"]:
        """Get query execution statistics by query id.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param managed_instance_name: The name of the managed instance. Required.
        :type managed_instance_name: str
        :param database_name: The name of the database. Required.
        :type database_name: str
        :param query_id: Required.
        :type query_id: str
        :param start_time: Start time for observed period. Default value is None.
        :type start_time: str
        :param end_time: End time for observed period. Default value is None.
        :type end_time: str
        :param interval: The time step to be used to summarize the metric values. Known values are:
         "PT1H" and "P1D". Default value is None.
        :type interval: str or ~azure.mgmt.sql.models.QueryTimeGrainType
        :return: An iterator like instance of either QueryStatistics or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.sql.models.QueryStatistics]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-11-01-preview"))
        cls: ClsType[_models.ManagedInstanceQueryStatistics] = kwargs.pop("cls", None)

        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_by_query_request(
                    resource_group_name=resource_group_name,
                    managed_instance_name=managed_instance_name,
                    database_name=database_name,
                    query_id=query_id,
                    subscription_id=self._config.subscription_id,
                    start_time=start_time,
                    end_time=end_time,
                    interval=interval,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
                _request.url = self._client.format_url(_request.url)

            else:
                _request = HttpRequest("GET", next_link)
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("ManagedInstanceQueryStatistics", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)
