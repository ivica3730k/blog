[Previous (Home)](../../README.md)
# Terraform With Github Actions
Automate the deployment of infrastructure using Terraform and Github Actions.

### Table of Contents
| Section  |
| ---  |
| [Abstract and Introduction](#abstract-and-introduction) | 
| [Table of Contents](#table-of-contents) |
| [Main](#main) |
| [Tags](#tags) | 

<!-- Short description of the project and what it is. -->
## Abstract and Introduction
This little project is a test to see if I can use Github Actions to deploy infrastructure using Terraform. I have been using Terraform for a while now, but I have not used Github Actions to deploy infrastructure. I have used Github Actions to deploy code, but not infrastructure. I am hoping that this project will help me learn how to use Github Actions to deploy infrastructure.

Note: main section was generated using ChatGPT

<!-- Tags are used to categorize posts. For example, if this project is a 2M Ham Radio Amplifier, then the tags could be "Ham Radio", "Radio Engineering" -->
#### Tags
Terraform, Github Actions, Infrastructure, Automation
## Main
<!-- The main section is where the main content of the project goes. -->
The project repo is available at https://github.com/ivica3730k/github-actions-terraform-azure

It consists of 2 main parts, github jobs for pull requests and github jobs for pushes to the branch.

### Pull Requests

This job is triggered by a pull request and checks out the code, performs an envsubst on the provider_secrets_template file with environment variables, sets up the Terraform provider, initializes Terraform with a new backend configuration file, validates the Terraform code, and runs Terraform plan.

If the validation and plan succeed, the script outputs the results to a comment on the pull request. If either the validation or plan fails, the script outputs the error message to a comment and fails the build. The action has permission to read the contents and write issues and pull requests.

The script uses a standardized template for Terraform plan on pull request to branch made by @ivica3730k, and users can customize it by changing the branch names, environment name, and secret names.

The snippet is written in YAML and uses GitHub Actions, which is a feature of GitHub that automates tasks in a GitHub repository. The script runs on the ubuntu-latest environment and uses the hashicorp/setup-terraform@v2 action to set up the Terraform provider. The script also uses the peter-evans/create-or-update-comment@v2 action to output the results to a comment on the pull request.

### Pushes to the branch

The action is triggered by a push event to the main branch, and it runs on an Ubuntu environment.

The action sets environment variables for the Terraform command to run, which are sourced from the repository secrets. It checks out the code, performs a substitution on the provider_secrets_template file with the environment variables, sets up the Terraform provider, initializes Terraform with the newly created backend configuration file, and validates the Terraform code. If validation or apply fails, it creates a GitHub issue with the error message and fails the build.

The YAML file includes several steps to accomplish these tasks, including checking out the code, extracting the branch name, performing envsubst, setting up Terraform provider, initializing Terraform with backend config, validating Terraform code, running Terraform apply, creating or updating an issue with a validate or apply error message, and failing the build if Terraform validate or apply fails.
