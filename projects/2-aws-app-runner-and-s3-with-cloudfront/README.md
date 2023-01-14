<!-- Each page should have a link to the previous page and (if applicable)the next page. -->
[Previous (page_name)](../README.md)

<!-- Specify the project name, use Pascal Case with spaces. For example, "2M Ham Radio Amplifier". -->
# AWS App Runner and S3 + CloudFront Terraform Template
A template for deploying an AWS App Runner backend service with frontend hosted on S3 + CloudFront.

<!-- Short description of the project and what it is. -->
## Abstract and Introduction
Throughout my work I have been tasked numerous times to setup hosting for an Application which requires
some sort of a backend service with accompanying frontend. Sometimes that would just be setting up a simple VM machine on EC2 and use docker, but with serverless services like AWS App Runner and AWS Amplify, it is possible to setup a full stack application with minimal costs compared to traditional hosting. Only downside is that it is not as easy to setup as a simple EC2 machine. This is where Terraform comes in. Terraform is a tool which allows you to setup infrastructure as code. This means that you can setup your infrastructure with a single command and it will be reproducible. Idea is to create a template for setting up a backend service on App Runner with frontend hosted on S3 + CloudFront. 

<!-- Did the project live section start-->
## Did the project live?
If you are reading this, then the answer is no. I have not started working on this project yet. I will update this section once I start working on it.

<!-- List the projects that could be related to this project. For example, if this project is a 2M Ham Radio Amplifier, then the related projects could be a 70cm Ham Radio Amplifier and a 6M Ham Radio Amplifier. -->
### Related Projects

<!-- List the goals of the project. For example, if this project is a 2M Ham Radio Amplifier, then the goals could be to build a 2M Ham Radio Amplifier that is capable of 100W output. -->
### Project Goals
- Create a Terraform template for setting up a backend service on App Runner with frontend hosted on S3 + CloudFront
- Maybe create a custom Terraform module?

<!-- List the requirements of the project. For example, if this project is a 2M Ham Radio Amplifier, then the requirements could be W6PXL pallet, some coax, etc -->
### Project Requirements
- AWS Account with access to a region that supports App Runner
- Terraform installed

<!-- Tags are used to categorize projects. For example, if this project is a 2M Ham Radio Amplifier, then the tags could be "Ham Radio", "Radio Engineering" -->
#### Tags
AWS, Terraform, App Runner, S3, CloudFront, Docker, Serverless
## Main

### Table of Contents
| Section  |
| ---  |
| [Abstract and Introduction](#abstract-and-introduction) | 
| [Related Projects](#related-projects) | 
| [Project Goals](#project-goals) | 
| [Project Requirements](#project-requirements) | 
| [Tags](#tags) | 

## A bit about technologies used
**Disclaimer: Some sections of this might be written by GitHub Copilot and ChatGPT.
**


### What is Terraform?
Terraform is an open-source infrastructure as code software tool created by HashiCorp. Users define and provide data center infrastructure using a declarative configuration language known as HashiCorp Configuration Language, or optionally JSON. Terraform generates an execution plan describing what it will do to reach the desired state, and then executes it to build the described infrastructure. As of May 2021, Terraform supports more than 90 infrastructure and service providers. Terraform is free and open-source software under the Mozilla Public License 2.0. 

## What is AWS App Runner?
AWS App Runner is a fully managed container application service that makes it easy for developers to quickly deploy containerized applications from a source repository. You can use AWS App Runner to deploy and run containerized web applications that are accessible through a custom URL. You don't need to provision, scale, and manage servers to run your applications, because AWS App Runner automatically handles the infrastructure management.

### What is S3?
Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. This means customers of all sizes and industries can use it to store and protect any amount of data for a range of use cases, such as websites, mobile applications, backup and restore, archive, enterprise applications, IoT devices, and big data analytics. Amazon S3 provides easy-to-use management features so you can organize your data and configure finely-tuned access controls to meet your specific business, organizational, and compliance requirements. Amazon S3 is designed for 99.999999999% (11 9’s) of durability, and stores data for millions of applications for companies all around the world.

### What is CloudFront?
Amazon CloudFront is a content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency, high transfer speeds, all within a developer friendly environment.

## What is the plan?
The plan is to create a Terraform template for setting up a backend service on App Runner with frontend hosted on S3 + CloudFront. Once created, the link to the template will be added here.