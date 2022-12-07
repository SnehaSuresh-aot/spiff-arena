"""Terraform-deployed environment."""
from os import environ

# default.py already ensured that this key existed as was not None
environment_identifier_for_this_config_file_only = environ["SPIFFWORKFLOW_BACKEND_ENV"]

GIT_COMMIT_ON_SAVE = True
GIT_COMMIT_USERNAME = environment_identifier_for_this_config_file_only
GIT_COMMIT_EMAIL = f"{environment_identifier_for_this_config_file_only}@example.com"
SPIFFWORKFLOW_BACKEND_PERMISSIONS_FILE_NAME = environ.get(
    "SPIFFWORKFLOW_BACKEND_PERMISSIONS_FILE_NAME", default="terraform_deployed_environment.yml"
)

RUN_BACKGROUND_SCHEDULER = (
    environ.get("RUN_BACKGROUND_SCHEDULER", default="false") == "true"
)

OPEN_ID_SERVER_URL = f"https://keycloak.{environment_identifier_for_this_config_file_only}.spiffworkflow.org/realms/spiffworkflow"
SPIFFWORKFLOW_FRONTEND_URL = f"https://{environment_identifier_for_this_config_file_only}.spiffworkflow.org"
SPIFFWORKFLOW_BACKEND_URL = f"https://api.{environment_identifier_for_this_config_file_only}.spiffworkflow.org"
CONNECTOR_PROXY_URL = f"https://connector-proxy.{environment_identifier_for_this_config_file_only}.spiffworkflow.org"