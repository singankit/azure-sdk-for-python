from pprint import pprint

from azure.ai.client import AzureAIClient
from azure.identity import DefaultAzureCredential

from azure.ai.client.models import Evaluation, Dataset, EvaluatorConfiguration


# Create an Azure AI client

# Project Configuration INT
# Subscription = "2d385bf4-0756-4a76-aa95-28bf9ed3b625"
# ResourceGroup = "jamahaja-rg"
# Workspace = "jamahaja-int-project"
# DataUri = "azureml://locations/centraluseuap/workspaces/d85a5cc8-fbb1-473a-874f-227c6a7201f9/data/test-remote-eval-data/versions/1"
# Endpoint = "https://int.api.azureml-test.ms"

# DataUri = "azureml://locations/centraluseuap/workspaces/3f4a76ca-9402-4089-8526-ca4632151e74/data/test-remote-eval-data/versions/1"

# Project Configuration Canary
Subscription = "2d385bf4-0756-4a76-aa95-28bf9ed3b625"
ResourceGroup = "rg-anksingai"
Workspace = "anksing-canary"
DataUri = "azureml://locations/eastus2euap/workspaces/a51c1ea7-5c29-4c32-a98e-7fa752f36e7c/data/test-remote-eval-data/versions/1"
Endpoint = "https://eastus2euap.api.azureml.ms"

client = AzureAIClient(
    endpoint=Endpoint,
    credential=DefaultAzureCredential(),
)

# Create an evaluation
evaluation = Evaluation(
    display_name="Remote Evaluation",
    description="Evaluation of dataset",
    data=Dataset(
        uri=DataUri
    ),
    evaluators={
        "f1_score": EvaluatorConfiguration(id="azureml://registries/jamahaja-evals-registry/models/F1ScoreEvaluator/versions/1"),
        "relevance": EvaluatorConfiguration(
            id="azureml://registries/jamahaja-evals-registry/models/Relevance-Evaluator-AI-Evaluation/versions/2",
            init_params={
                "model_config": {
                    "api_key": "/subscriptions/2d385bf4-0756-4a76-aa95-28bf9ed3b625/resourceGroups/rg-anksingai/providers/Microsoft.MachineLearningServices/workspaces/anksing-canary/connections/ai-anksingai0771286510468288/credentials/key",
                    "azure_deployment": "gpt-4",
                    "api_version": "2023-07-01-preview",
                    "azure_endpoint": "https://ai-anksingai0771286510468288.openai.azure.com/"
                }
            }
        ),
    },
    properties={"Environment": "azureml://registries/jamahaja-evals-registry/environments/eval-remote-env/versions/6"},
    # environment="azureml://registries/RAI-Simulator/environments/eval-remote-env/versions/4",
)


evaluation = client.evaluations.create(
    evaluation=evaluation,
    # endpoint="https://int.api.azureml-test.ms",
    subscription_id=Subscription,
    resource_group_name=ResourceGroup,
    workspace_name=Workspace,
    headers={
        "x-azureml-token": DefaultAzureCredential().get_token("https://ml.azure.com/.default").token,
    }
)

pprint(evaluation.as_dict())
















evaluation_json = {
    "Data": {"Uri": DataUri},
    "DisplayName": "Remote Evaluation",
    "Description": "Testing",
    # "Environment": "azureml://registries/jamahaja-evals-registry/environments/eval-remote-env/versions/2",
    "Evaluators": {
        "f1_score": {"Id": "azureml://registries/jamahaja-evals-registry/models/F1ScoreEvaluator/versions/1"},
        "relevance": {
            "Id": "azureml://registries/jamahaja-evals-registry/models/Relevance-Evaluator-AI-Evaluation/versions/1",
            "initParams":{
                "model_config": {
                    "api_key": "/subscriptions/2d385bf4-0756-4a76-aa95-28bf9ed3b625/resourceGroups/rg-anksingai/providers/Microsoft.MachineLearningServices/workspaces/anksing-canary/connections/ai-anksingaicanary931822963616_aoai/credentials/key",
                    "azure_deployment": "gpt-4",
                    "api_version": "2023-07-01-preview",
                    "azure_endpoint": "https://ai-anksingaicanary931822963616.openai.azure.com/"
                }
            }
        },
        "hate_unfairness": {
            "Id": "azureml://registries/jamahaja-evals-registry/models/HateUnfairnessEvaluator/versions/2",
            "initParams":{
                "azure_ai_project": {
                   "subscription_id": "2d385bf4-0756-4a76-aa95-28bf9ed3b625",
                    "resource_group_name": "rg-anksingai",
                    "workspace_name": "anksing-canary",
                }
            }
        }
    },
    "properties": {
        "Environment": "azureml://registries/jamahaja-evals-registry/environments/eval-remote-env/versions/6",
        # "_azureml.evaluation_run": "promptflow.BatchRun"
    },
}