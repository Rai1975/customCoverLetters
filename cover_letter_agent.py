import os
import boto3
from colorama import init, Fore, Style
from strands import Agent
from strands.models import BedrockModel
from tools import get_profile_summary, generate_cover_letter, job_description_scraper

init(autoreset=True)  # auto-reset color after each print, and enables ANSI on Windows

COVER_LETTER_SYSTEM_PROMPT = ""
with open(os.path.join(os.getcwd(), "cover_letter_agent_prompt.txt"), "r") as f:
    COVER_LETTER_SYSTEM_PROMPT = f.read()


def get_boto_session() -> boto3.Session:
    """
    Reads AWS_PROFILE from the environment.
    Set it per-project in your .env or shell before running:
        export AWS_PROFILE=my-dev-profile
    Falls back to the default profile if not set.
    """
    profile = os.environ.get("AWS_PROFILE", None)
    region = os.environ.get("AWS_REGION", "us-east-1")
    return boto3.Session(profile_name=profile, region_name=region)


def build_agent() -> Agent:
    session = get_boto_session()

    model = BedrockModel(
        model_id="moonshot.kimi-k2-thinking",
        boto_session=session,
    )

    agent = Agent(
        model=model,
        system_prompt=COVER_LETTER_SYSTEM_PROMPT,
        tools=[get_profile_summary, generate_cover_letter, job_description_scraper],
        callback_handler=None
    )

    return agent


def run_chat():
    agent = build_agent()

    print(Fore.CYAN + Style.BRIGHT + "Cover Letter Agent" + Style.RESET_ALL +
          Fore.YELLOW + "  (type 'exit' or 'quit' to stop)\n")

    while True:
        try:
            user_input = input(Fore.GREEN + "You: " + Style.RESET_ALL).strip()
        except (KeyboardInterrupt, EOFError):
            print(Fore.YELLOW + "\nExiting.")
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit"):
            print(Fore.YELLOW + "Exiting.")
            break

        try:
            response = agent(user_input)
        except Exception as e:
            print(Fore.RED + f"\n[Error running agent: {e}]\n")
            continue

        print(Fore.CYAN + Style.BRIGHT + "\nAgent: " + Style.RESET_ALL + f"{response}\n")


if __name__ == "__main__":
    run_chat()