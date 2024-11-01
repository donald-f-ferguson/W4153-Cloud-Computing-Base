# W4153 - Cloud Computing

## Contents

This document is the course overview.

Related documents:
- [Project 1 instructions](P1/README.md)

## Overview

The core/base repository for Columbia University's Department of Computer Science
course [COMS W4153 -- Cloud Computing.](https://wwwapp.cc.columbia.edu/cu/bulletin/uwb/subj/COMS/W4153-20243-001/)
The description from the _Directory of Classes_ is "Software engineering skills necessary for
developing cloud computing and software-as-a-service applications, covering topics such as
service-oriented architectures, message-driven applications, and platform integration. Includes
theoretical study, practical application, and collaborative project work."

There are many definitions for and perspectives on "Cloud computing." The area is also rapidly expanding and
evolving. The course's content continuously evolves to represent new technology and concepts. The course does,
however, have a stable, common core of topics. These include:
- Infrastructure-as-a-Service
- Container-as-a-Service
- Platform-as-a-Service
- Function-as-a-Service
- API-as-a-Service, OpenAPI
- Software-as-a-Service
- Cloud databases and cloud storage
- Multi-tenant applications
- Microservices
- REST, GraphQL
- OpenID, OAuth2, cloud identity and access management
- Cloud and application management, monitoring and operations
- Continuous integration/continuous delivery
- Service, application and infrastructure integration and orchestration
- Architecture, software and cloud design patterns and best practices.

The course content is:
- A set of lectures with references to details.
- Small applications and configuration examples.
- Recommended reading.

Students form small project teams of approximately 5-6 students. The teams:
- Define a project/solution scenario.
- Incrementally implement the application/solution in agile development 2 week sprints.
- Demonstrate understanding of course content by using in their projects and explaining the usage.

The course focuses on the concepts, but provides concrete examples using:
- Amazon Web Services
- Google Cloud
- Microsoft Azure

## Course Work and Grading

The primary contribution to the final grade is the team project. The course defines a set of technologies
that the projects must correctly use in their implementations. Teams also write interim status and architecture
reports.

## Course Calendar

<iframe src="https://calendar.google.com/calendar/embed?src=c_20e9e0f50614367e628dd2152506a45acbdaf8d9ff22207ef9c1c3807f11ace5%40group.calendar.google.com&ctz=America%2FNew_York" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>

## Syllabus

__Note:__
1. This is tentative and the course adapts based on rate of progress and specific interests.
2. Prior experience indicates that lectures can present material much more quickly than students can implement.
So, we will adapt based on progress.

| Lecture Number | Date       | Topics                                                                                                         |
|:---------------|------------|----------------------------------------------------------------------------------------------------------------|
| 1              | 2024-09-06 | - Introduction<br> - Course overview<br> - Core concepts<br> - Microservices<br> - Full stack web apps         |
| 2              | 2024-09-13 | - Virtualization<br> - IaaS<br> - REST<br> - OpenAPI<br> - API GW and management                               |
| 3              | 2024-09-20 | - Containers<br> - Container-as-a-Service<br> -GraphQL <br> - Service composition<br> - Cloud data and storage |
| 4              | 2024-09-27 | - Cloud security, identity and access management<br> - OpenID/OAuth2                                           |
| 5              | 2024-10-04 | - Platform-as-a-Service<br> - Function-as-a-Service<br> - SaaS<br> - Multitenant apps                          |
| 6              | 2024-10-11 | - Review, discussion, Q&A, project discussions, ... ...                                                        |
| 7              | 2024-10-18 | - CI/CD<br> - Monitoring, management, operations<br>                                                           |
| 8              | 2024-10-25 | - Event driven processing<br> - Message driven processing<br> - Service orchestration                          |
| 9              | 2024-11-01 | - Big data.<br> - Data engineering and processing                                                              |
| 10             | 2024-11-08 | - Continue<br> - Big data.<br> - Data engineering and processing                                               |
| 11             | 2024-11-15 | - Micro-frontends<br> - Misc. UI topics                                                                        |
| 12             | 2024-11-22 | - Overflow and discussion                                                                                      |
| NA             | 2024-11-29 | - Thanksgiving                                                                                                 |
| 12             | 2024-12-06 | - Overflow<br> - Advanced topics                                                                               |


## Lectures

- [Lecture 1 - Introduction and Concepts](https://github.com/donald-f-ferguson/W4153-Cloud-Computing-Base/blob/dad4dc930692d6dfdc60ae34fa8dd8e2c942d7a9/Lectures/W4153-2024F-1-Introduction-Concepts/W4153-2024F-1-Introduction-Concepts-V5.pdf)
- [Lecture 2 - REST-Microservices-IaaS](https://github.com/donald-f-ferguson/W4153-Cloud-Computing-Base/blob/68f2bd11e4b1eaa26b3d5b46cb7359e0ba3b1ea7/Lectures/W4153-2024F-2-REST-Microservices-IaaS/W4153-2024F-2-REST-Microservices-IaaS-V2.pdf)
- [Lecture 3 - REST2-Microservices2-CaaS](https://github.com/donald-f-ferguson/W4153-Cloud-Computing-Base/blob/main/Lectures/W4153-2024F-3-REST2-Microservices2-CaaS_WebContent-DB/W4153-2024F-3-REST2-Microservices2-CaaS-web_content-DB.pdf)
- [Lecture 4 - Web-Content-Microservices-DB-OAuth](https://github.com/donald-f-ferguson/W4153-Cloud-Computing-Base/blob/main/Lectures/W4153-2024F-REST(3)-Microservices-WebContent/W4153-2024F-4-Web-Content-Microservices-DB-OAuth2.pdf)
- [Lecture 5 - REST(4)-OAuth2-Middleware-Composition](https://github.com/donald-f-ferguson/W4153-Cloud-Computing-Base/blob/main/Lectures/W4153-2024F-5-REST(4)-OAuth2-Middleware)
- [Lecture 6 - REST(4)-OAuth2-Middleware-Composition](https://github.com/donald-f-ferguson/W4153-Cloud-Computing-Base/blob/main/Lectures/W4153-2024F-6-REST(4)-OAuth2-Middleware-Composition/W4153-2024F-6-REST(4)-OAuth2-Middleware-Composition.pdf)
- [Lecture 7 -W4153-2024F-7-Sprint-2-REST-OAuth2-Middleware-Composition](https://github.com/donald-f-ferguson/W4153-Cloud-Computing-Base/blob/main/Lectures/W4153-2024F-7-Sprint-2-REST-OAuth2-Middleware-Composition.pdf)
- [Lecture 8 - W4153-F24-8-REST-PaaS-FaaS-Logic-Placement-Composition-EDA-MDP-V2](https://github.com/donald-f-ferguson/W4153-Cloud-Computing-Base/blob/main/Lectures/W4153-2024F-8-REST-PaaS-FaaS-Logic-Placement-Composition-EDA-MDP)
- [Lecture 9 -W4153-F24-9-FaaS-Advanced-Composition-GraphQL.pdf](https://github.com/donald-f-ferguson/W4153-Cloud-Computing-Base/blob/main/Lectures/W4153-2024F-9-FaaS-Advanced-Composition-GraphQL.pdf)
