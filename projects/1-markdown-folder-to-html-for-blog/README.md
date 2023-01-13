<!-- Each page should have a link to the previous page and (if applicable)the next page. -->
[Previous (Home)](../../README.md)

<!-- Specify the project name, use Pascal Case with spaces. For example, "2M Ham Radio Amplifier". -->
# Markdown Folder to HTML
A reusable workflow which can create docs-style html folder out of folder.

<!-- Short description of the project and what it is. -->
## Abstract and Introduction
This project, which is available here https://github.com/joakin/markdown-folder-to-html could be used to make a html site for this whole repository. It would be a good way to organize the projects and make them easier to navigate. It would also be a good way to learn how to use the project.

Being a core idea of this potential-projects-repo, it would be a good idea to use this project to create a html site for this repository. It would be a good way to learn how to use the project and also to make the projects easier to navigate.

### Table of Contents
| Section  |
| ---  |
| [Abstract and Introduction](#abstract-and-introduction) | 
| [Related Projects](#related-projects) | 
| [Project Goals](#project-goals) | 
| [Project Requirements](#project-requirements) | 
| [Tags](#tags) | 

<!-- List the projects that could be related to this project. For example, if this project is a 2M Ham Radio Amplifier, then the related projects could be a 70cm Ham Radio Amplifier and a 6M Ham Radio Amplifier. -->
### Related Projects

<!-- List the goals of the project. For example, if this project is a 2M Ham Radio Amplifier, then the goals could be to build a 2M Ham Radio Amplifier that is capable of 100W output. -->
### Project Goals
- Create a html site for this repository using markdown-folder-to-html
- Create a script to automatically update the html site when a new project is added
- Host the html site on GitHub Pages or something cheap like S3

<!-- List the requirements of the project. For example, if this project is a 2M Ham Radio Amplifier, then the requirements could be W6PXL pallet, some coax, etc -->
### Project Requirements

<!-- Tags are used to categorize projects. For example, if this project is a 2M Ham Radio Amplifier, then the tags could be "Ham Radio", "Radio Engineering" -->
#### Tags
CICD, GitHub, Markdown, HTML, JavaScript, Node.js
## Main

Markdown to html docs would be useful(even for this page) to create a static HTML content out of folder full or markdown.
It could be used to make simple blogs where users without huge amount of technical knowledge could just learn a bit of github and start writing.
Advantage of a github way would also be ability to leverage all user permissions stuff and data flows that github offer, which could result in a system where articles would need to be approved, spelling checks on pull requests, etc.

### Potential CICD Pipelines that could be used
- Spellcheck on creating pull request
- Creating appropriate folder structure on opening a new issue
- Automatically making a table of contents on the main landing page