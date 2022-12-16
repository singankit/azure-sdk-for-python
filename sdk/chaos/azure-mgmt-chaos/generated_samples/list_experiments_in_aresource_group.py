# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.chaos import ChaosManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-chaos
# USAGE
    python list_experiments_in_aresource_group.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ChaosManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="6b052e15-03d3-4f17-b2e1-be7f07588291",
    )

    response = client.experiments.list(
        resource_group_name="exampleRG",
    )
    for item in response:
        print(item)


# x-ms-original-file: specification/chaos/resource-manager/Microsoft.Chaos/preview/2022-10-01-preview/examples/ListExperimentsInAResourceGroup.json
if __name__ == "__main__":
    main()
