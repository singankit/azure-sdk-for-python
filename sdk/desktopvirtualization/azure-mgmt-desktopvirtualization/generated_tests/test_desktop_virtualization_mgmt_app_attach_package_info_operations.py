# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.desktopvirtualization import DesktopVirtualizationMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDesktopVirtualizationMgmtAppAttachPackageInfoOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(DesktopVirtualizationMgmtClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_import_method(self, resource_group):
        response = self.client.app_attach_package_info.import_method(
            resource_group_name=resource_group.name,
            host_pool_name="str",
            import_package_info_request={"packageArchitecture": "str", "path": "str"},
            api_version="2024-04-03",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
