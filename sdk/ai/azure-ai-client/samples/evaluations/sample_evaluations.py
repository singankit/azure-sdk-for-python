from azure.ai.client import AzureAIClient
from azure.identity import DefaultAzureCredential

from azure.ai.client.models import Evaluation, Dataset, EvaluatorConfiguration


# Create an Azure AI client

client = AzureAIClient(
    # subscription_id="2d385bf4-0756-4a76-aa95-28bf9ed3b625",
    # resource_group_name="rg-anksingai",
    # workspace_name="anksing-canary",
    # subscription_id="b17253fa-f327-42d6-9686-f3e553e24763",
    # resource_group_name="rg-anksingai",
    # workspace_name="anksing-int",
    endpoint="https://int.api.azureml-test.ms",
    credential=DefaultAzureCredential(),
)

# Create an evaluation
evaluation = Evaluation(
    display_name="Remote Evaluation",
    description="Evaluation of dataset",
    data=Dataset(
        id="azureml://locations/eastus2euap/workspaces/a51c1ea7-5c29-4c32-a98e-7fa752f36e7c/data/test-remote-eval-data/versions/1"
    ),
    evaluators={
        "f1_score": EvaluatorConfiguration(id="azureml://registries/RAI-Simulator/models/F1ScoreEvaluator/versions/1"),
    },
    properties={"Environment": "azureml://registries/jamahaja-evals-registry/environments/eval-remote-env/versions/2"},
    # environment="azureml://registries/RAI-Simulator/environments/eval-remote-env/versions/4",
)

evaluation_json = {
    "Data": {
        "Uri": "azureml://locations/centraluseuap/workspaces/3f4a76ca-9402-4089-8526-ca4632151e74/data/test-remote-eval-data/versions/1"
    },
    "DisplayName": "Remote Evaluation",
    "Description": "Testing",
    # "Environment": "azureml://registries/jamahaja-evals-registry/environments/eval-remote-env/versions/2",
    "Evaluators": {
        "f1_score": {"Id": "azureml://registries/jamahaja-evals-registry/models/F1ScoreEvaluator/versions/1"},
        # "relevance": {
        #     "Id": "azureml://registries/jamahaja-evals-registry/models/Relevance-Evaluator-AI-Evaluation/versions/1",
        #     "initParams":{
        #         "model_config": {
        #             "api_key": "/subscriptions/2d385bf4-0756-4a76-aa95-28bf9ed3b625/resourceGroups/rg-anksingai/providers/Microsoft.MachineLearningServices/workspaces/anksing_ai_canary/connections/ai-anksingaicanary931822963616_aoai/credentials/key",
        #             "azure_deployment": "gpt-4",
        #             "api_version": "2023-07-01-preview",
        #             "azure_endpoint": "https://ai-anksingaicanary931822963616.openai.azure.com/"
        #         }
        #     }
        # },
        # "hate_unfairness": {
        #     "Id": "azureml://registries/RAI-Simulator/models/HateUnfairnessEvaluator/versions/3",
        #     "initParams":{
        #         "azure_ai_project": {
        #            "subscription_id": "2d385bf4-0756-4a76-aa95-28bf9ed3b625",
        #             "resource_group_name": "rg-anksingai",
        #             "workspace_name": "anksing-remote-evals",
        #         }
        #     }
        # }
    },
    "properties": {"Environment": "azureml://registries/jamahaja-evals-registry/environments/eval-remote-env/versions/2"},
}

client.evaluations.create(
    evaluation=evaluation_json,
    # endpoint="https://int.api.azureml-test.ms",
    subscription_id="b17253fa-f327-42d6-9686-f3e553e24763",
    resource_group_name="rg-anksingai",
    workspace_name="anksing-int",
    headers={
        "x-azureml-token": DefaultAzureCredential().get_token("https://ml.azure.com/.default").token,
    }
)

