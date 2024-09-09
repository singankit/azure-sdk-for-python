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
class TestSqlManagementManagedInstanceAdministratorsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(SqlManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_instance(self, resource_group):
        response = self.client.managed_instance_administrators.list_by_instance(
            resource_group_name=resource_group.name,
            managed_instance_name="str",
            api_version="2020-11-01-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.managed_instance_administrators.get(
            resource_group_name=resource_group.name,
            managed_instance_name="str",
            administrator_name="str",
            api_version="2020-11-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.managed_instance_administrators.begin_create_or_update(
            resource_group_name=resource_group.name,
            managed_instance_name="str",
            administrator_name="str",
            parameters={
                "administratorType": "str",
                "id": "str",
                "login": "str",
                "name": "str",
                "sid": "str",
                "tenantId": "str",
                "type": "str",
            },
            api_version="2020-11-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.managed_instance_administrators.begin_delete(
            resource_group_name=resource_group.name,
            managed_instance_name="str",
            administrator_name="str",
            api_version="2020-11-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
