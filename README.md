# das-infra-stack-vultr
Scripts/assets to install required infrastructure stack in Vultr


## Instructions

This project is about deployment file to OpenFaas functions.

The primary file das-function.yml contain all instructions to DEPLOY the specific version of functions on OpenFAAS system, running the same code as AWS Lambda functions inside OpenFAAS server.

## Pipeline Variable

Put on the pipeline variables to set the ip of openFaas server

## Parameters

- Version: version of file
- provider - Gateway: Gateway url to openFaas (See OpenFaas documentation)
- Functions: List of functions to deploy (name of functions)
- - git_url: Git url of function
- - git_ref: Release tag to deploy this function
- - lang: stack to build function inside of openFaas (see openfaas templates documentation)
- - handler: path to function inside of openFaas server
- - image: image name (if private registry, named with url registry and tag)
