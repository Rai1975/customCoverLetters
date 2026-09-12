import os
import boto3
from strands import Agent
from strands.models import BedrockModel
from tools import get_profile_summary

# def get_boto_session() -> boto3.Session:
#     """
#     Reads AWS_PROFILE from the environment.
#     Set it per-project in your .env or shell before running:
#         export AWS_PROFILE=my-dev-profile
#     Falls back to the default profile if not set.
#     """
#     profile = os.environ.get("AWS_PROFILE", None)
#     region  = os.environ.get("AWS_REGION", "us-east-1")
#     return boto3.Session(profile_name=profile, region_name=region)


# def build_agent() -> Agent:
#     """
#     Constructs the Strands agent responsible for finding and recording
#     relationships between an existing pattern and other patterns already
#     in the graph.
#     """
#     session = get_boto_session()

#     model = BedrockModel(
#         model_id="moonshot.kimi-k2-thinking",
#         boto_session=session,
#     )

#     agent = Agent(
#         model=model,
#         system_prompt=PATTERN_RELATION_SYSTEM_PROMPT,
#         tools=[],
#     )

#     return agent

if __name__ == "__main__":
    string = ""
    with open(os.path.join(os.getcwd(), "cover_letter_agent_prompt.txt"), "r+") as f:
        string = (f.read())

    print(string)