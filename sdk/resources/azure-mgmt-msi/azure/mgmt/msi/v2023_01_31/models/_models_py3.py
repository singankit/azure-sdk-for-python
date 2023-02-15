# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, Dict, List, Optional, TYPE_CHECKING, Union

from ... import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class CloudErrorBody(_serialization.Model):
    """An error response from the ManagedServiceIdentity service.

    :ivar code: An identifier for the error.
    :vartype code: str
    :ivar message: A message describing the error, intended to be suitable for display in a user
     interface.
    :vartype message: str
    :ivar target: The target of the particular error. For example, the name of the property in
     error.
    :vartype target: str
    :ivar details: A list of additional details about the error.
    :vartype details: list[~azure.mgmt.msi.v2023_01_31.models.CloudErrorBody]
    """

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "target": {"key": "target", "type": "str"},
        "details": {"key": "details", "type": "[CloudErrorBody]"},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        target: Optional[str] = None,
        details: Optional[List["_models.CloudErrorBody"]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword code: An identifier for the error.
        :paramtype code: str
        :keyword message: A message describing the error, intended to be suitable for display in a user
         interface.
        :paramtype message: str
        :keyword target: The target of the particular error. For example, the name of the property in
         error.
        :paramtype target: str
        :keyword details: A list of additional details about the error.
        :paramtype details: list[~azure.mgmt.msi.v2023_01_31.models.CloudErrorBody]
        """
        super().__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target
        self.details = details


class Resource(_serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. E.g.
     "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}".
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.msi.v2023_01_31.models.SystemData
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.system_data = None


class ProxyResource(Resource):
    """The resource model definition for a Azure Resource Manager proxy resource. It will not have
    tags and a location.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. E.g.
     "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}".
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.msi.v2023_01_31.models.SystemData
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)


class FederatedIdentityCredential(ProxyResource):
    """Describes a federated identity credential.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. E.g.
     "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}".
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.msi.v2023_01_31.models.SystemData
    :ivar issuer: The URL of the issuer to be trusted.
    :vartype issuer: str
    :ivar subject: The identifier of the external identity.
    :vartype subject: str
    :ivar audiences: The list of audiences that can appear in the issued token.
    :vartype audiences: list[str]
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "issuer": {"key": "properties.issuer", "type": "str"},
        "subject": {"key": "properties.subject", "type": "str"},
        "audiences": {"key": "properties.audiences", "type": "[str]"},
    }

    def __init__(
        self,
        *,
        issuer: Optional[str] = None,
        subject: Optional[str] = None,
        audiences: Optional[List[str]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword issuer: The URL of the issuer to be trusted.
        :paramtype issuer: str
        :keyword subject: The identifier of the external identity.
        :paramtype subject: str
        :keyword audiences: The list of audiences that can appear in the issued token.
        :paramtype audiences: list[str]
        """
        super().__init__(**kwargs)
        self.issuer = issuer
        self.subject = subject
        self.audiences = audiences


class FederatedIdentityCredentialsListResult(_serialization.Model):
    """Values returned by the List operation for federated identity credentials.

    :ivar value: The collection of federated identity credentials returned by the listing
     operation.
    :vartype value: list[~azure.mgmt.msi.v2023_01_31.models.FederatedIdentityCredential]
    :ivar next_link: The url to get the next page of results, if any.
    :vartype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[FederatedIdentityCredential]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self,
        *,
        value: Optional[List["_models.FederatedIdentityCredential"]] = None,
        next_link: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword value: The collection of federated identity credentials returned by the listing
         operation.
        :paramtype value: list[~azure.mgmt.msi.v2023_01_31.models.FederatedIdentityCredential]
        :keyword next_link: The url to get the next page of results, if any.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class TrackedResource(Resource):
    """The resource model definition for an Azure Resource Manager tracked top level resource which
    has 'tags' and a 'location'.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. E.g.
     "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}".
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.msi.v2023_01_31.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
        "location": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "tags": {"key": "tags", "type": "{str}"},
        "location": {"key": "location", "type": "str"},
    }

    def __init__(self, *, location: str, tags: Optional[Dict[str, str]] = None, **kwargs: Any) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword location: The geo-location where the resource lives. Required.
        :paramtype location: str
        """
        super().__init__(**kwargs)
        self.tags = tags
        self.location = location


class Identity(TrackedResource):
    """Describes an identity resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. E.g.
     "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}".
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.msi.v2023_01_31.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    :ivar tenant_id: The id of the tenant which the identity belongs to.
    :vartype tenant_id: str
    :ivar principal_id: The id of the service principal object associated with the created
     identity.
    :vartype principal_id: str
    :ivar client_id: The id of the app associated with the identity. This is a random generated
     UUID by MSI.
    :vartype client_id: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
        "location": {"required": True},
        "tenant_id": {"readonly": True},
        "principal_id": {"readonly": True},
        "client_id": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "tags": {"key": "tags", "type": "{str}"},
        "location": {"key": "location", "type": "str"},
        "tenant_id": {"key": "properties.tenantId", "type": "str"},
        "principal_id": {"key": "properties.principalId", "type": "str"},
        "client_id": {"key": "properties.clientId", "type": "str"},
    }

    def __init__(self, *, location: str, tags: Optional[Dict[str, str]] = None, **kwargs: Any) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword location: The geo-location where the resource lives. Required.
        :paramtype location: str
        """
        super().__init__(tags=tags, location=location, **kwargs)
        self.tenant_id = None
        self.principal_id = None
        self.client_id = None


class IdentityUpdate(Resource):
    """Describes an identity resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. E.g.
     "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}".
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.msi.v2023_01_31.models.SystemData
    :ivar location: The geo-location where the resource lives.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar tenant_id: The id of the tenant which the identity belongs to.
    :vartype tenant_id: str
    :ivar principal_id: The id of the service principal object associated with the created
     identity.
    :vartype principal_id: str
    :ivar client_id: The id of the app associated with the identity. This is a random generated
     UUID by MSI.
    :vartype client_id: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
        "tenant_id": {"readonly": True},
        "principal_id": {"readonly": True},
        "client_id": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "tenant_id": {"key": "properties.tenantId", "type": "str"},
        "principal_id": {"key": "properties.principalId", "type": "str"},
        "client_id": {"key": "properties.clientId", "type": "str"},
    }

    def __init__(self, *, location: Optional[str] = None, tags: Optional[Dict[str, str]] = None, **kwargs: Any) -> None:
        """
        :keyword location: The geo-location where the resource lives.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        """
        super().__init__(**kwargs)
        self.location = location
        self.tags = tags
        self.tenant_id = None
        self.principal_id = None
        self.client_id = None


class Operation(_serialization.Model):
    """Operation supported by the Microsoft.ManagedIdentity REST API.

    :ivar name: The name of the REST Operation. This is of the format
     {provider}/{resource}/{operation}.
    :vartype name: str
    :ivar display: The object that describes the operation.
    :vartype display: ~azure.mgmt.msi.v2023_01_31.models.OperationDisplay
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "display": {"key": "display", "type": "OperationDisplay"},
    }

    def __init__(
        self, *, name: Optional[str] = None, display: Optional["_models.OperationDisplay"] = None, **kwargs: Any
    ) -> None:
        """
        :keyword name: The name of the REST Operation. This is of the format
         {provider}/{resource}/{operation}.
        :paramtype name: str
        :keyword display: The object that describes the operation.
        :paramtype display: ~azure.mgmt.msi.v2023_01_31.models.OperationDisplay
        """
        super().__init__(**kwargs)
        self.name = name
        self.display = display


class OperationDisplay(_serialization.Model):
    """The object that describes the operation.

    :ivar provider: Friendly name of the resource provider.
    :vartype provider: str
    :ivar operation: The type of operation. For example: read, write, delete.
    :vartype operation: str
    :ivar resource: The resource type on which the operation is performed.
    :vartype resource: str
    :ivar description: A description of the operation.
    :vartype description: str
    """

    _attribute_map = {
        "provider": {"key": "provider", "type": "str"},
        "operation": {"key": "operation", "type": "str"},
        "resource": {"key": "resource", "type": "str"},
        "description": {"key": "description", "type": "str"},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        operation: Optional[str] = None,
        resource: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword provider: Friendly name of the resource provider.
        :paramtype provider: str
        :keyword operation: The type of operation. For example: read, write, delete.
        :paramtype operation: str
        :keyword resource: The resource type on which the operation is performed.
        :paramtype resource: str
        :keyword description: A description of the operation.
        :paramtype description: str
        """
        super().__init__(**kwargs)
        self.provider = provider
        self.operation = operation
        self.resource = resource
        self.description = description


class OperationListResult(_serialization.Model):
    """A list of operations supported by Microsoft.ManagedIdentity Resource Provider.

    :ivar value: A list of operations supported by Microsoft.ManagedIdentity Resource Provider.
    :vartype value: list[~azure.mgmt.msi.v2023_01_31.models.Operation]
    :ivar next_link: The url to get the next page of results, if any.
    :vartype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[Operation]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self, *, value: Optional[List["_models.Operation"]] = None, next_link: Optional[str] = None, **kwargs: Any
    ) -> None:
        """
        :keyword value: A list of operations supported by Microsoft.ManagedIdentity Resource Provider.
        :paramtype value: list[~azure.mgmt.msi.v2023_01_31.models.Operation]
        :keyword next_link: The url to get the next page of results, if any.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class SystemAssignedIdentity(ProxyResource):
    """Describes a system assigned identity resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. E.g.
     "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}".
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.msi.v2023_01_31.models.SystemData
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar tenant_id: The id of the tenant which the identity belongs to.
    :vartype tenant_id: str
    :ivar principal_id: The id of the service principal object associated with the created
     identity.
    :vartype principal_id: str
    :ivar client_id: The id of the app associated with the identity. This is a random generated
     UUID by MSI.
    :vartype client_id: str
    :ivar client_secret_url: The ManagedServiceIdentity DataPlane URL that can be queried to obtain
     the identity credentials.
    :vartype client_secret_url: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
        "location": {"required": True},
        "tenant_id": {"readonly": True},
        "principal_id": {"readonly": True},
        "client_id": {"readonly": True},
        "client_secret_url": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "tenant_id": {"key": "properties.tenantId", "type": "str"},
        "principal_id": {"key": "properties.principalId", "type": "str"},
        "client_id": {"key": "properties.clientId", "type": "str"},
        "client_secret_url": {"key": "properties.clientSecretUrl", "type": "str"},
    }

    def __init__(self, *, location: str, tags: Optional[Dict[str, str]] = None, **kwargs: Any) -> None:
        """
        :keyword location: The geo-location where the resource lives. Required.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        """
        super().__init__(**kwargs)
        self.location = location
        self.tags = tags
        self.tenant_id = None
        self.principal_id = None
        self.client_id = None
        self.client_secret_url = None


class SystemData(_serialization.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :ivar created_by: The identity that created the resource.
    :vartype created_by: str
    :ivar created_by_type: The type of identity that created the resource. Known values are:
     "User", "Application", "ManagedIdentity", and "Key".
    :vartype created_by_type: str or ~azure.mgmt.msi.v2023_01_31.models.CreatedByType
    :ivar created_at: The timestamp of resource creation (UTC).
    :vartype created_at: ~datetime.datetime
    :ivar last_modified_by: The identity that last modified the resource.
    :vartype last_modified_by: str
    :ivar last_modified_by_type: The type of identity that last modified the resource. Known values
     are: "User", "Application", "ManagedIdentity", and "Key".
    :vartype last_modified_by_type: str or ~azure.mgmt.msi.v2023_01_31.models.CreatedByType
    :ivar last_modified_at: The timestamp of resource last modification (UTC).
    :vartype last_modified_at: ~datetime.datetime
    """

    _attribute_map = {
        "created_by": {"key": "createdBy", "type": "str"},
        "created_by_type": {"key": "createdByType", "type": "str"},
        "created_at": {"key": "createdAt", "type": "iso-8601"},
        "last_modified_by": {"key": "lastModifiedBy", "type": "str"},
        "last_modified_by_type": {"key": "lastModifiedByType", "type": "str"},
        "last_modified_at": {"key": "lastModifiedAt", "type": "iso-8601"},
    }

    def __init__(
        self,
        *,
        created_by: Optional[str] = None,
        created_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        created_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        last_modified_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        last_modified_at: Optional[datetime.datetime] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword created_by: The identity that created the resource.
        :paramtype created_by: str
        :keyword created_by_type: The type of identity that created the resource. Known values are:
         "User", "Application", "ManagedIdentity", and "Key".
        :paramtype created_by_type: str or ~azure.mgmt.msi.v2023_01_31.models.CreatedByType
        :keyword created_at: The timestamp of resource creation (UTC).
        :paramtype created_at: ~datetime.datetime
        :keyword last_modified_by: The identity that last modified the resource.
        :paramtype last_modified_by: str
        :keyword last_modified_by_type: The type of identity that last modified the resource. Known
         values are: "User", "Application", "ManagedIdentity", and "Key".
        :paramtype last_modified_by_type: str or ~azure.mgmt.msi.v2023_01_31.models.CreatedByType
        :keyword last_modified_at: The timestamp of resource last modification (UTC).
        :paramtype last_modified_at: ~datetime.datetime
        """
        super().__init__(**kwargs)
        self.created_by = created_by
        self.created_by_type = created_by_type
        self.created_at = created_at
        self.last_modified_by = last_modified_by
        self.last_modified_by_type = last_modified_by_type
        self.last_modified_at = last_modified_at


class UserAssignedIdentitiesListResult(_serialization.Model):
    """Values returned by the List operation.

    :ivar value: The collection of userAssignedIdentities returned by the listing operation.
    :vartype value: list[~azure.mgmt.msi.v2023_01_31.models.Identity]
    :ivar next_link: The url to get the next page of results, if any.
    :vartype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[Identity]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self, *, value: Optional[List["_models.Identity"]] = None, next_link: Optional[str] = None, **kwargs: Any
    ) -> None:
        """
        :keyword value: The collection of userAssignedIdentities returned by the listing operation.
        :paramtype value: list[~azure.mgmt.msi.v2023_01_31.models.Identity]
        :keyword next_link: The url to get the next page of results, if any.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link