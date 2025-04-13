import os
import yaml
import argparse
from dotenv import load_dotenv
from settings import Settings

PATH_API_SECRET = "secrets.yaml"


def export_envs(environment: str = "dev") -> None:
    env_file = f".env.{environment}"
    if not os.path.exists(env_file):
        raise FileNotFoundError(f"The environment file '{env_file}' does not exist.")

    load_dotenv(env_file)

    if not os.path.exists(PATH_API_SECRET):
        raise FileNotFoundError(
            f"The API secret file '{PATH_API_SECRET}' does not exist."
        )

    with open(PATH_API_SECRET, "r") as file:
        yaml_secrets = yaml.safe_load(file)

    for key, value in yaml_secrets.items():
        os.environ[key] = value


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API_KEY: ", settings.API_KEY)
