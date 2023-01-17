# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ApiError
from ._models_py3 import ApiErrorBase
from ._models_py3 import CloudService
from ._models_py3 import CloudServiceExtensionProfile
from ._models_py3 import CloudServiceExtensionProperties
from ._models_py3 import CloudServiceInstanceView
from ._models_py3 import CloudServiceListResult
from ._models_py3 import CloudServiceNetworkProfile
from ._models_py3 import CloudServiceOsProfile
from ._models_py3 import CloudServiceProperties
from ._models_py3 import CloudServiceRole
from ._models_py3 import CloudServiceRoleListResult
from ._models_py3 import CloudServiceRoleProfile
from ._models_py3 import CloudServiceRoleProfileProperties
from ._models_py3 import CloudServiceRoleProperties
from ._models_py3 import CloudServiceRoleSku
from ._models_py3 import CloudServiceUpdate
from ._models_py3 import CloudServiceVaultAndSecretReference
from ._models_py3 import CloudServiceVaultCertificate
from ._models_py3 import CloudServiceVaultSecretGroup
from ._models_py3 import ExtendedLocation
from ._models_py3 import Extension
from ._models_py3 import InnerError
from ._models_py3 import InstanceSku
from ._models_py3 import InstanceViewStatusesSummary
from ._models_py3 import LoadBalancerConfiguration
from ._models_py3 import LoadBalancerConfigurationProperties
from ._models_py3 import LoadBalancerFrontendIPConfiguration
from ._models_py3 import LoadBalancerFrontendIPConfigurationProperties
from ._models_py3 import OSFamily
from ._models_py3 import OSFamilyListResult
from ._models_py3 import OSFamilyProperties
from ._models_py3 import OSVersion
from ._models_py3 import OSVersionListResult
from ._models_py3 import OSVersionProperties
from ._models_py3 import OSVersionPropertiesBase
from ._models_py3 import Resource
from ._models_py3 import ResourceInstanceViewStatus
from ._models_py3 import ResourceWithOptionalLocation
from ._models_py3 import RoleInstance
from ._models_py3 import RoleInstanceListResult
from ._models_py3 import RoleInstanceNetworkProfile
from ._models_py3 import RoleInstanceProperties
from ._models_py3 import RoleInstanceView
from ._models_py3 import RoleInstances
from ._models_py3 import StatusCodeCount
from ._models_py3 import SubResource
from ._models_py3 import SubResourceReadOnly
from ._models_py3 import SystemData
from ._models_py3 import UpdateDomain
from ._models_py3 import UpdateDomainListResult
from ._models_py3 import UserAssignedIdentitiesValue

from ._compute_management_client_enums import CloudServiceSlotType
from ._compute_management_client_enums import CloudServiceUpgradeMode
from ._compute_management_client_enums import ExtendedLocationTypes
from ._compute_management_client_enums import InstanceViewTypes
from ._compute_management_client_enums import StatusLevelTypes
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ApiError",
    "ApiErrorBase",
    "CloudService",
    "CloudServiceExtensionProfile",
    "CloudServiceExtensionProperties",
    "CloudServiceInstanceView",
    "CloudServiceListResult",
    "CloudServiceNetworkProfile",
    "CloudServiceOsProfile",
    "CloudServiceProperties",
    "CloudServiceRole",
    "CloudServiceRoleListResult",
    "CloudServiceRoleProfile",
    "CloudServiceRoleProfileProperties",
    "CloudServiceRoleProperties",
    "CloudServiceRoleSku",
    "CloudServiceUpdate",
    "CloudServiceVaultAndSecretReference",
    "CloudServiceVaultCertificate",
    "CloudServiceVaultSecretGroup",
    "ExtendedLocation",
    "Extension",
    "InnerError",
    "InstanceSku",
    "InstanceViewStatusesSummary",
    "LoadBalancerConfiguration",
    "LoadBalancerConfigurationProperties",
    "LoadBalancerFrontendIPConfiguration",
    "LoadBalancerFrontendIPConfigurationProperties",
    "OSFamily",
    "OSFamilyListResult",
    "OSFamilyProperties",
    "OSVersion",
    "OSVersionListResult",
    "OSVersionProperties",
    "OSVersionPropertiesBase",
    "Resource",
    "ResourceInstanceViewStatus",
    "ResourceWithOptionalLocation",
    "RoleInstance",
    "RoleInstanceListResult",
    "RoleInstanceNetworkProfile",
    "RoleInstanceProperties",
    "RoleInstanceView",
    "RoleInstances",
    "StatusCodeCount",
    "SubResource",
    "SubResourceReadOnly",
    "SystemData",
    "UpdateDomain",
    "UpdateDomainListResult",
    "UserAssignedIdentitiesValue",
    "CloudServiceSlotType",
    "CloudServiceUpgradeMode",
    "ExtendedLocationTypes",
    "InstanceViewTypes",
    "StatusLevelTypes",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
