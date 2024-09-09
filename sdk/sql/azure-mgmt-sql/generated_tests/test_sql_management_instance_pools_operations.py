# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.sql import SqlManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSqlManagementInstancePoolsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(SqlManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list(self, resource_group):
        response = self.client.instance_pools.list(
            api_version="2023-05-01-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_resource_group(self, resource_group):
        response = self.client.instance_pools.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2023-05-01-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.instance_pools.get(
            resource_group_name=resource_group.name,
            instance_pool_name="str",
            api_version="2023-05-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.instance_pools.begin_create_or_update(
            resource_group_name=resource_group.name,
            instance_pool_name="str",
            parameters={
                "location": "str",
                "dnsZone": "str",
                "id": "str",
                "licenseType": "str",
                "maintenanceConfigurationId": "str",
                "name": "str",
                "sku": {"name": "str", "capacity": 0, "family": "str", "size": "str", "tier": "str"},
                "subnetId": "str",
                "tags": {"str": "str"},
                "type": "str",
                "vCores": 0,
            },
            api_version="2023-05-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.instance_pools.begin_delete(
            resource_group_name=resource_group.name,
            instance_pool_name="str",
            api_version="2023-05-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_update(self, resource_group):
        response = self.client.instance_pools.begin_update(
            resource_group_name=resource_group.name,
            instance_pool_name="str",
            parameters={
                "dnsZone": "str",
                "licenseType": "str",
                "maintenanceConfigurationId": "str",
                "sku": {"name": "str", "capacity": 0, "family": "str", "size": "str", "tier": "str"},
                "subnetId": "str",
                "tags": {"str": "str"},
                "vCores": 0,
            },
            api_version="2023-05-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
