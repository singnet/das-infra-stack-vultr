# Openfaas-functions

This repository contains configurations and scripts for managing OpenFaaS functions. The functions are deployed in an OpenFaaS environment based on the settings defined in the `functions.yaml` file.

## Repository Structure

- `functions-up.sh`: This script is used to deploy OpenFaaS functions based on the configurations defined in the `functions.yaml` file. It uses the `faas-cli` tool to do this.

- `functions.yaml`: This file contains the configurations for OpenFaaS functions, including details such as name, programming language, Docker image, environment variables, and other related parameters.

- `pull-handlers.sh`: This script is used to update the handlers of the functions from the Git repository. It pulls the latest changes from relevant branches (e.g., "main" and "meetup") to keep the functions up-to-date.

- `push.sh`: This script facilitates sending the configurations and scripts needed to the OpenFaaS server. It copies the `functions.yaml` and `pull-handlers.sh` files to the server and runs `pull-handlers.sh` remotely to update the handlers.

- `ssh.sh`: This script allows you to access the OpenFaaS server via SSH using the specified authentication key.

## Function Configuration

The configurations for OpenFaaS functions are defined in the `functions.yaml` file. Each function is configured with the following details:

- Function name.
- Programming language.
- Handler (path to the function's code).
- Docker image.
- Environment variables related to the function.

## Using the Scripts

To use the provided scripts in this repository, follow these steps:

1. **Function Deployment**:

   - Use the `functions-up.sh` script to deploy functions in the OpenFaaS environment. You can specify an optional filter to deploy only specific functions if needed.

2. **Handler Updates**:

   - Use the `pull-handlers.sh` script to keep the handlers of the functions updated. It will pull the latest changes from relevant branches in the Git repositories of the functions.

3. **Sending Configurations and Scripts**:

   - The `push.sh` script makes it easy to send the configurations and scripts to the OpenFaaS server. It will copy the `functions.yaml` and `pull-handlers.sh` files to the server and run `pull-handlers.sh` remotely to update the handlers.

4. **Accessing the OpenFaaS Server**:
   - Use the `ssh.sh` script to access the OpenFaaS server via SSH using the specified authentication key.

Make sure to properly configure the environment variables and other necessary parameters in the function configurations in `functions.yaml` before deploying the functions.

Note: Ensure that you have the appropriate permissions and correctly configure SSH keys and other authentication details for the OpenFaaS server before using these scripts.
