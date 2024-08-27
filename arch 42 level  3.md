
**About arc42**

arc42, the template for documentation of software and system architecture.

Teenter code heremplate Version 8.2 EN. (based upon AsciiDoc version), January 2023

Created, maintained and © by Dr. Peter Hruschka, Dr. Gernot Starke and contributors. See  [https://arc42.org](https://arc42.org/).

This version of the template contains some help and explanations. It is used for familiarization with arc42 and the understanding of the concepts. For documentation of your own system you use better the  _plain_  version.

# Introduction and Goals

O objetivo deste projeto é desenvolver e implementar um aplicativo móvel que simplifique a organização de caronas entre estudantes universitários. A proposta visa promover a mobilidade sustentável e segura dentro das comunidades acadêmicas, incentivando o compartilhamento de veículos entre os alunos. Com funcionalidades intuitivas e de fácil acesso, o aplicativo permitirá que os usuários encontrem e ofereçam caronas de maneira eficiente, contribuindo para a redução do número de veículos em circulação, diminuindo a pegada de carbono e fortalecendo os laços sociais entre os membros da comunidade universitária.

**Link para System Design**
[Sytem Design](https://lucid.app/lucidchart/45490cdb-a854-421d-882d-b4308453c515/edit?viewport_loc=-2625%2C-675%2C4870%2C2126%2C0_0&invitationId=inv_085c1335-7e13-452c-94fc-d7ad48468d4e)



| Prioridade | Objetivos                                           |
|------------|-----------------------------------------------------|
| 1          | O sistema deve ser projetado para ser escalável    |
| 2          | O sistema deve implementar um chat em tempo real  |
| 3          | O sistema deve implementar uma carteira virtual    |
| 4          | O sistema deve implementar geolocalização através de uma API |
| 5          | O sistema deve ser capaz de autenticar alunos      |




## Requirements Overview


| Requisito | Descrição |
|-----------|-----------|
| F1        | Cadastro de usuário: O aplicativo deve permitir que estudantes se cadastrem fornecendo informações pessoais, como nome, foto e matrícula. |
| F1.1      | Cadastro de usuário: O aplicativo deve permitir aos usuários inserir dados adicionais relacionados ao veículo, quando aplicável. |
| F3        | Sistema de avaliação: O aplicativo deve implementar um sistema de avaliação bidirecional entre passageiros e motoristas. |
| F4        | Sistema de geolocalização: O aplicativo deve implementar um sistema de geolocalização para atualizar as posições dos usuários e otimizar rotas de carona. |
| F5        | Sistema de notificações: O aplicativo deve enviar notificações em tempo real para informar os usuários sobre solicitações de carona, confirmações, cancelamentos e atualizações de rota. |


## Quality Goals

| Categoria de Qualidade | Qualidade               | Descrição                                                                 | Cenário |
|------------------------|-------------------------|---------------------------------------------------------------------------|---------|
| Usabilidade            | Facilidade de Uso       | O aplicativo deve ser fácil de navegar tanto para motoristas quanto para passageiros, especialmente em situações de alto tráfego. | SC1     |
|                        | Facilidade de Aprendizado | A interface deve ser intuitiva para novos usuários, exigindo orientação mínima para entender as funcionalidades principais. |         |
| Desempenho             | Precisão                | O rastreamento de localização e as estimativas de viagem devem ser precisas, dentro de uma pequena margem de erro. | SC2     |
|                        | Velocidade & Responsividade | O aplicativo deve carregar e processar solicitações rapidamente, com latência mínima durante os horários de pico. |         |
| Segurança              | Segurança nas Transações | Os processos de pagamento devem ser seguros, garantindo transações seguras para motoristas e passageiros. | SC3     |
| Legal                  | Conformidade Regulamentar | O aplicativo deve aderir às leis locais de transporte e privacidade de dados em todas as regiões de operação. | SC4     |



### Stakeholders

| Nome              | Contato                    | Expectativas |
|-------------------|----------------------------|--------------|
| Gerente de Produto | gerente.produto@gmail.com  | Espera que o aplicativo atenda às necessidades do mercado, seja fácil de usar e proporcione uma boa experiência ao usuário. |
| Equipe de Desenvolvimento | dev.team@gmail.com | Espera que os requisitos sejam claros e bem documentados, e que haja tempo suficiente para implementar funcionalidades. |
| Usuários Finais    | usuarios@gmail.com         | Esperam que o aplicativo seja confiável, rápido, fácil de navegar e atenda às suas necessidades de transporte diário. |
| Motoristas         | motoristas@gmail.com       | Esperam que o aplicativo ofereça um sistema de pagamento justo, suporte eficiente e oportunidades de ganho estáveis. |
| Investidores       | investidores@gmail.com     | Esperam um retorno financeiro positivo. |


# Architecture Constraints

| Categoria               | Restrição                        | Descrição                                                                                                  | Cenário |
|-------------------------|----------------------------------|------------------------------------------------------------------------------------------------------------|---------|
| Plataforma de Nuvem     | Dependência do Azure             | O sistema depende da infraestrutura do Azure, com suas limitações e políticas de serviço.                  | C1      |
| Gerenciamento de Contêineres | Docker & Kubernetes          | A orquestração de contêineres impõe a necessidade de compatibilidade e monitoramento eficiente.            | C2      |
| Armazenamento de Dados  | Banco de Dados MongoDB e SQL     | A arquitetura híbrida deve garantir a consistência entre dados não relacionais e relacionais.               | C3      |
| Monitoramento           | Uso do New Relic                 | Métricas de desempenho e logs serão gerenciados e monitorados pelo New Relic.                               | C4      |
| Escalabilidade          | Replicação e Distribuição        | Os serviços devem ser facilmente escaláveis usando Kubernetes, garantindo alta disponibilidade.             | C5      |
| Alta Disponibilidade    | Chat e Notificações em Tempo Real | O sistema deve garantir alta disponibilidade para suportar comunicação em tempo real e notificações instantâneas.| C6  |
| Segurança               | Autenticação de Estudantes       | O sistema de autenticação deve proteger dados pessoais e estar em conformidade com os padrões de segurança. | C7      |
| Segurança               | Carteira Virtual                 | A segurança financeira e a integridade das transações devem ser garantidas.                                 | C8      |
| Geolocalização          | API de Geolocalização            | Limitações impostas pela API de geolocalização devem ser consideradas para precisão e tratamento de solicitações. | C9   |


# System Scope and Context



## Business Context

| Parceiro de Comunicação | Entradas                                   | Saídas                                |
|-------------------------|-------------------------------------------|---------------------------------------|
| Estudantes (usuários)   | Solicitações de carona, dados de cadastro | Confirmações de carona, notificações  |
| Motoristas (usuários)   | Ofertas de carona, dados de avaliação     | Solicitações de carona, notificações  |
| API de Geolocalização   | Coordenadas de localização                | Rotas otimizadas                      |
| Sistema de Pagamento    | Dados de pagamento                        | Confirmação de transações             |




## Technical Context

**Contents**

| Canal                   | Meio de Transmissão         | Dados de Entrada/Saída                            |
|-------------------------|----------------------------|---------------------------------------------------|
| Aplicativo Móvel        | Conexão de Internet (Wi-Fi/4G/5G) | Solicitações de carona, notificações, pagamentos   |
| Servidor Backend        | HTTP/HTTPS                  | Processamento de requisições, respostas de API    |
| Sistema de Notificações | WebSockets                  | Envio de notificações em tempo real               |
| Banco de Dados          | Conexão de rede (TCP/IP)    | Armazenamento e recuperação de dados do usuário   |

**Diagrama C4 Nivel 1**

[![](https://mermaid.ink/img/pako:eNqtU81q20AQfpVhTw6oRrYlS9YtuKH0UAg1uRRBGaSxsqDdVfcn2DF-mD5LX6wjS7brpIceqot2fr5vvpndOYjK1CQKsU7WRnva-VIDf176lmB0wUeJjUUFW2NhjdZohPuuK_WQ-0jWGT0JjmwEpXhy4ddPK00p_rSgNoBdKyv08sXAj0DQcWVgEAQFynhjpfMIJkCHzmFD0pppKe6GIpu986Qm7vTriVkAMH6Q44Zi99cCHVrmsg1q-YoWqiENSHtLEEZRbuC_aQNrJfWJrD-wJIu1sSP_xQUGnOylIBA0ZElXkp0Oas6-oR2Ef3_Y-QmPkqzGdnNpYjNycCOP2KBieWbs5RwaQGNDnTUV8XAsm-d0mDgCTb3_1NTd26H9pfbsTfEH_dJfER8Uyvb_CfhK7fgurhf35PAmPg78mvBpHOdN1jn8foaf-Y3y64TKqH9AzN5DRCQUWW685j049ASl8M-kqBQFH2vaYmh9KUp95FQM3mz2uhKFt4EiYU1onkWxxdaxFboaPY37cvF2qL8Zo84QNkVxEDtRzJNpGi_TVTafxatllswjsRfFhyyZLrIkixd5nsZJkufHSLyeCOLpapHEaZovk5whyWIZCaolL8-XYY9P63z8DapVTJ4?type=png)](https://mermaid.live/edit#pako:eNqtU81q20AQfpVhTw6oRrYlS9YtuKH0UAg1uRRBGaSxsqDdVfcn2DF-mD5LX6wjS7brpIceqot2fr5vvpndOYjK1CQKsU7WRnva-VIDf176lmB0wUeJjUUFW2NhjdZohPuuK_WQ-0jWGT0JjmwEpXhy4ddPK00p_rSgNoBdKyv08sXAj0DQcWVgEAQFynhjpfMIJkCHzmFD0pppKe6GIpu986Qm7vTriVkAMH6Q44Zi99cCHVrmsg1q-YoWqiENSHtLEEZRbuC_aQNrJfWJrD-wJIu1sSP_xQUGnOylIBA0ZElXkp0Oas6-oR2Ef3_Y-QmPkqzGdnNpYjNycCOP2KBieWbs5RwaQGNDnTUV8XAsm-d0mDgCTb3_1NTd26H9pfbsTfEH_dJfER8Uyvb_CfhK7fgurhf35PAmPg78mvBpHOdN1jn8foaf-Y3y64TKqH9AzN5DRCQUWW685j049ASl8M-kqBQFH2vaYmh9KUp95FQM3mz2uhKFt4EiYU1onkWxxdaxFboaPY37cvF2qL8Zo84QNkVxEDtRzJNpGi_TVTafxatllswjsRfFhyyZLrIkixd5nsZJkufHSLyeCOLpapHEaZovk5whyWIZCaolL8-XYY9P63z8DapVTJ4)

**Diagrama C4 Nivel 2**
[![](https://mermaid.ink/img/pako:eNqVVc1O20AQfpXVnqiUoiaEOOTGnygSSCkOlypSNdiDWdXedXfXgYDyMFUPSFxRnyAv1tn1D04wh_q0P9_MfDPzjfeJRypGPuHHw2MlLQiJei4ZfVbYFNmJgERDBixG5gDrF4dAw3LQwBQ7zFMRgRUL5RGglYS5LD1MURsldwqDusfm_NoU699aqDlv71isGLw5-VUgy4kRIyNWZCxTVmlhLMUqKKYxkKDQanfOP9VhwqWxmP04UoWMQS93jN-7GF3kDFmyp9LSfU3WO_d4c5jnm3Yl16m6R013pty23PoqCGlRw_p5_cdnU9SZLQQwCQtMIFa6ZPw-6g1EP1HGzm-IeiEI6sgelcdV_KW9U7Jcn1H1ZUSegaXr14SIOLjEZP0aCWUYslulJUbIDqfndZtMq8TmIyYxWLgBgy7KEcjIF-2EuBsWfrsoozeLQ53BI0oK7gEaU6DwEoRhkcoU1YRoZK4of0ks5KiuiumxqGxEj7hmKF1HpYdEd2A3yXWwG3TQu1QyUSc3JbONzRZNCeo91fKKnJ2hSlUEqXgsm_nGZbUlaYgzIb1_tyB5atfiKmRzRONhhNMiUKZJ3TcXy0XskPDpg90htEjDRsJh5YDoncqF8EmfOkilRa-Z9bM_xxqAbUDN4IFEKivFOiToCuf1o6y4JYFs5d3ilcOSmmU7mU0hAXepOkjlWkVIY-vv_cE2uItgbaVb8HbBrjCt_itvU3ttoPT4dTabhk0ODlqDWsN2rLJCuumhSpRmV6fhzA3NhmVj0Z6Oi_ULdRRNpHGBpXGjSN_bDReVWFqx3yTyEeF3YQf_F7fD05awnJqgVkBTg_ByNu0m8q7_5_TXo6fBzdB2FrzHM6TJEzE9LP5fO-f2DjPiPKFljLdQpHbO53JFUCisCpcy4hOrC-xxrYrkjk9uIaVq8yKnEmD1DDWnOcjvSmW1CW355Ik_8MnnvS-7o2AUHPQPgtFoODzo8SWdDgaD3fF4OAj2Bvv9YD8Yrnr80Tvo7_ZH4_4o6I-H43HQ3x8MexxjQa_OZfkw-vdx9Q_ku2io?type=png)](https://mermaid.live/edit#pako:eNqVVc1O20AQfpXVnqiUoiaEOOTGnygSSCkOlypSNdiDWdXedXfXgYDyMFUPSFxRnyAv1tn1D04wh_q0P9_MfDPzjfeJRypGPuHHw2MlLQiJei4ZfVbYFNmJgERDBixG5gDrF4dAw3LQwBQ7zFMRgRUL5RGglYS5LD1MURsldwqDusfm_NoU699aqDlv71isGLw5-VUgy4kRIyNWZCxTVmlhLMUqKKYxkKDQanfOP9VhwqWxmP04UoWMQS93jN-7GF3kDFmyp9LSfU3WO_d4c5jnm3Yl16m6R013pty23PoqCGlRw_p5_cdnU9SZLQQwCQtMIFa6ZPw-6g1EP1HGzm-IeiEI6sgelcdV_KW9U7Jcn1H1ZUSegaXr14SIOLjEZP0aCWUYslulJUbIDqfndZtMq8TmIyYxWLgBgy7KEcjIF-2EuBsWfrsoozeLQ53BI0oK7gEaU6DwEoRhkcoU1YRoZK4of0ks5KiuiumxqGxEj7hmKF1HpYdEd2A3yXWwG3TQu1QyUSc3JbONzRZNCeo91fKKnJ2hSlUEqXgsm_nGZbUlaYgzIb1_tyB5atfiKmRzRONhhNMiUKZJ3TcXy0XskPDpg90htEjDRsJh5YDoncqF8EmfOkilRa-Z9bM_xxqAbUDN4IFEKivFOiToCuf1o6y4JYFs5d3ilcOSmmU7mU0hAXepOkjlWkVIY-vv_cE2uItgbaVb8HbBrjCt_itvU3ttoPT4dTabhk0ODlqDWsN2rLJCuumhSpRmV6fhzA3NhmVj0Z6Oi_ULdRRNpHGBpXGjSN_bDReVWFqx3yTyEeF3YQf_F7fD05awnJqgVkBTg_ByNu0m8q7_5_TXo6fBzdB2FrzHM6TJEzE9LP5fO-f2DjPiPKFljLdQpHbO53JFUCisCpcy4hOrC-xxrYrkjk9uIaVq8yKnEmD1DDWnOcjvSmW1CW355Ik_8MnnvS-7o2AUHPQPgtFoODzo8SWdDgaD3fF4OAj2Bvv9YD8Yrnr80Tvo7_ZH4_4o6I-H43HQ3x8MexxjQa_OZfkw-vdx9Q_ku2io)


# Solution Strategy

- Decisões Tecnológicas:
    - Uso de Kubernetes para escalabilidade.
    - Implementação de microserviços para modularidade.
    - Adoção de MongoDB para armazenamento de dados não relacionais e SQL para relacionais.

- Padrões Arquiteturais:
    - Arquitetura baseada em microserviços para facilitar a escalabilidade e manutenção.
    - Uso de contêineres Docker para garantir a consistência dos ambientes de desenvolvimento e produção.

- Estratégias para Metas de Qualidade:
    - Implementação de um sistema de cache para melhorar a responsividade.
    - Uso de APIs de geolocalização otimizadas para garantir a precisão.
    - Adoção de práticas de segurança como OAuth2 para autenticação de usuários e proteção de dados.


# Building Block View

**Content**

The building block view shows the static decomposition of the system into building blocks (modules, components, subsystems, classes, interfaces, packages, libraries, frameworks, layers, partitions, tiers, functions, macros, operations, data structures, …) as well as their dependencies (relationships, associations, …)

This view is mandatory for every architecture documentation. In analogy to a house this is the  _floor plan_.

**Motivation**

Maintain an overview of your source code by making its structure understandable through abstraction.

This allows you to communicate with your stakeholder on an abstract level without disclosing implementation details.

**Form**

The building block view is a hierarchical collection of black boxes and white boxes (see figure below) and their descriptions.


**Level 1**  is the white box description of the overall system together with black box descriptions of all contained building blocks.

**Level 2**  zooms into some building blocks of level 1. Thus it contains the white box description of selected building blocks of level 1, together with black box descriptions of their internal building blocks.

**Level 3**  zooms into selected building blocks of level 2, and so on.

See  [Building Block View](https://docs.arc42.org/section-5/)  in the arc42 documentation.

## Whitebox Overall System

Here you describe the decomposition of the overall system using the following white box template. It contains

-   an overview diagram
    
-   a motivation for the decomposition
    
-   black box descriptions of the contained building blocks. For these we offer you alternatives:
    
    -   use  _one_  table for a short and pragmatic overview of all contained building blocks and their interfaces
        
    -   use a list of black box descriptions of the building blocks according to the black box template (see below). Depending on your choice of tool this list could be sub-chapters (in text files), sub-pages (in a Wiki) or nested elements (in a modeling tool).
        
-   (optional:) important interfaces, that are not explained in the black box templates of a building block, but are very important for understanding the white box. Since there are so many ways to specify interfaces why do not provide a specific template for them. In the worst case you have to specify and describe syntax, semantics, protocols, error handling, restrictions, versions, qualities, necessary compatibilities and many things more. In the best case you will get away with examples or simple signatures.
    

_**<Overview Diagram>**_

Motivation  
_<text explanation>_

Contained Building Blocks  
_<Description of contained building block (black boxes)>_

Important Interfaces  
_<Description of important interfaces>_

Insert your explanations of black boxes from level 1:

If you use tabular form you will only describe your black boxes with name and responsibility according to the following schema:

**Name**

**Responsibility**

_<black box 1>_

_<Text>_

_<black box 2>_

_<Text>_

If you use a list of black box descriptions then you fill in a separate black box template for every important building block . Its headline is the name of the black box.

### <Name black box 1>

Here you describe <black box 1> according the the following black box template:

-   Purpose/Responsibility
    
-   Interface(s), when they are not extracted as separate paragraphs. This interfaces may include qualities and performance characteristics.
    
-   (Optional) Quality-/Performance characteristics of the black box, e.g.availability, run time behavior, ….
    
-   (Optional) directory/file location
    
-   (Optional) Fulfilled requirements (if you need traceability to requirements).
    
-   (Optional) Open issues/problems/risks
    

_<Purpose/Responsibility>_

_<Interface(s)>_

_<(Optional) Quality/Performance Characteristics>_

_<(Optional) Directory/File Location>_

_<(Optional) Fulfilled Requirements>_

_<(optional) Open Issues/Problems/Risks>_

### <Name black box 2>

_<black box template>_

### <Name black box n>

_<black box template>_

### <Name interface 1>

…

### <Name interface m>

## Level 2

Here you can specify the inner structure of (some) building blocks from level 1 as white boxes.

You have to decide which building blocks of your system are important enough to justify such a detailed description. Please prefer relevance over completeness. Specify important, surprising, risky, complex or volatile building blocks. Leave out normal, simple, boring or standardized parts of your system

### White Box  _<building block 1>_

…describes the internal structure of  _building block 1_.

_<white box template>_

### White Box  _<building block 2>_

_<white box template>_

…

### White Box  _<building block m>_

_<white box template>_

## Level 3

Here you can specify the inner structure of (some) building blocks from level 2 as white boxes.

When you need more detailed levels of your architecture please copy this part of arc42 for additional levels.

### White Box <_building block x.1_>

Specifies the internal structure of  _building block x.1_.

_<white box template>_

### White Box <_building block x.2_>

_<white box template>_

### White Box <_building block y.1_>

_<white box template>_

# Runtime View

**Contents**

The runtime view describes concrete behavior and interactions of the system’s building blocks in form of scenarios from the following areas:

-   important use cases or features: how do building blocks execute them?
    
-   interactions at critical external interfaces: how do building blocks cooperate with users and neighboring systems?
    
-   operation and administration: launch, start-up, stop
    
-   error and exception scenarios
    

Remark: The main criterion for the choice of possible scenarios (sequences, workflows) is their  **architectural relevance**. It is  **not**  important to describe a large number of scenarios. You should rather document a representative selection.

**Motivation**

You should understand how (instances of) building blocks of your system perform their job and communicate at runtime. You will mainly capture scenarios in your documentation to communicate your architecture to stakeholders that are less willing or able to read and understand the static models (building block view, deployment view).

**Form**

There are many notations for describing scenarios, e.g.

-   numbered list of steps (in natural language)
    
-   activity diagrams or flow charts
    
-   sequence diagrams
    
-   BPMN or EPCs (event process chains)
    
-   state machines
    
-   …
    

See  [Runtime View](https://docs.arc42.org/section-6/)  in the arc42 documentation.

## <Runtime Scenario 1>

-   _<insert runtime diagram or textual description of the scenario>_
    
-   _<insert description of the notable aspects of the interactions between the building block instances depicted in this diagram.>_
    

## <Runtime Scenario 2>

## …

## <Runtime Scenario n>

# Deployment View

**Content**

The deployment view describes:

1.  technical infrastructure used to execute your system, with infrastructure elements like geographical locations, environments, computers, processors, channels and net topologies as well as other infrastructure elements and
    
2.  mapping of (software) building blocks to that infrastructure elements.
    

Often systems are executed in different environments, e.g. development environment, test environment, production environment. In such cases you should document all relevant environments.

Especially document a deployment view if your software is executed as distributed system with more than one computer, processor, server or container or when you design and construct your own hardware processors and chips.

From a software perspective it is sufficient to capture only those elements of an infrastructure that are needed to show a deployment of your building blocks. Hardware architects can go beyond that and describe an infrastructure to any level of detail they need to capture.

**Motivation**

Software does not run without hardware. This underlying infrastructure can and will influence a system and/or some cross-cutting concepts. Therefore, there is a need to know the infrastructure.

Maybe a highest level deployment diagram is already contained in section 3.2. as technical context with your own infrastructure as ONE black box. In this section one can zoom into this black box using additional deployment diagrams:

-   UML offers deployment diagrams to express that view. Use it, probably with nested diagrams, when your infrastructure is more complex.
    
-   When your (hardware) stakeholders prefer other kinds of diagrams rather than a deployment diagram, let them use any kind that is able to show nodes and channels of the infrastructure.
    

See  [Deployment View](https://docs.arc42.org/section-7/)  in the arc42 documentation.

## Infrastructure Level 1

Describe (usually in a combination of diagrams, tables, and text):

-   distribution of a system to multiple locations, environments, computers, processors, .., as well as physical connections between them
    
-   important justifications or motivations for this deployment structure
    
-   quality and/or performance features of this infrastructure
    
-   mapping of software artifacts to elements of this infrastructure
    

For multiple environments or alternative deployments please copy and adapt this section of arc42 for all relevant environments.

_**<Overview Diagram>**_

Motivation  
_<explanation in text form>_

Quality and/or Performance Features  
_<explanation in text form>_

Mapping of Building Blocks to Infrastructure  
_<description of the mapping>_

## Infrastructure Level 2

Here you can include the internal structure of (some) infrastructure elements from level 1.

Please copy the structure from level 1 for each selected element.

### _<Infrastructure Element 1>_

_<diagram + explanation>_

### _<Infrastructure Element 2>_

_<diagram + explanation>_

…

### _<Infrastructure Element n>_

_<diagram + explanation>_

# Cross-cutting Concepts

**Content**

This section describes overall, principal regulations and solution ideas that are relevant in multiple parts (= cross-cutting) of your system. Such concepts are often related to multiple building blocks. They can include many different topics, such as

-   models, especially domain models
    
-   architecture or design patterns
    
-   rules for using specific technology
    
-   principal, often technical decisions of an overarching (= cross-cutting) nature
    
-   implementation rules
    

**Motivation**

Concepts form the basis for  _conceptual integrity_  (consistency, homogeneity) of the architecture. Thus, they are an important contribution to achieve inner qualities of your system.

Some of these concepts cannot be assigned to individual building blocks, e.g. security or safety.

**Form**

The form can be varied:

-   concept papers with any kind of structure
    
-   cross-cutting model excerpts or scenarios using notations of the architecture views
    
-   sample implementations, especially for technical concepts
    
-   reference to typical usage of standard frameworks (e.g. using Hibernate for object/relational mapping)
    

**Structure**

A potential (but not mandatory) structure for this section could be:

-   Domain concepts
    
-   User Experience concepts (UX)
    
-   Safety and security concepts
    
-   Architecture and design patterns
    
-   "Under-the-hood"
    
-   development concepts
    
-   operational concepts
    

Note: it might be difficult to assign individual concepts to one specific topic on this list.

[![Possible topics for crosscutting concepts](https://github.com/Cyrilzak02/PJBL-PUCARONA/raw/main/images/08-Crosscutting-Concepts-Structure-EN.png)](https://github.com/Cyrilzak02/PJBL-PUCARONA/blob/main/images/08-Crosscutting-Concepts-Structure-EN.png)

See  [Concepts](https://docs.arc42.org/section-8/)  in the arc42 documentation.

## _<Concept 1>_

_<explanation>_

## _<Concept 2>_

_<explanation>_

…

## _<Concept n>_

_<explanation>_

# Architecture Decisions

**Contents**

Important, expensive, large scale or risky architecture decisions including rationales. With "decisions" we mean selecting one alternative based on given criteria.

Please use your judgement to decide whether an architectural decision should be documented here in this central section or whether you better document it locally (e.g. within the white box template of one building block).

Avoid redundancy. Refer to section 4, where you already captured the most important decisions of your architecture.

**Motivation**

Stakeholders of your system should be able to comprehend and retrace your decisions.

**Form**

Various options:

-   ADR ([Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)) for every important decision
    
-   List or table, ordered by importance and consequences or:
    
-   more detailed in form of separate sections per decision
    

See  [Architecture Decisions](https://docs.arc42.org/section-9/)  in the arc42 documentation. There you will find links and examples about ADR.

# Quality Requirements

**Content**

This section contains all quality requirements as quality tree with scenarios. The most important ones have already been described in section 1.2. (quality goals)

Here you can also capture quality requirements with lesser priority, which will not create high risks when they are not fully achieved.

**Motivation**

Since quality requirements will have a lot of influence on architectural decisions you should know for every stakeholder what is really important to them, concrete and measurable.

See  [Quality Requirements](https://docs.arc42.org/section-10/)  in the arc42 documentation.

## Quality Tree

**Content**

The quality tree (as defined in ATAM – Architecture Tradeoff Analysis Method) with quality/evaluation scenarios as leafs.

**Motivation**

The tree structure with priorities provides an overview for a sometimes large number of quality requirements.

**Form**

The quality tree is a high-level overview of the quality goals and requirements:

-   tree-like refinement of the term "quality". Use "quality" or "usefulness" as a root
    
-   a mind map with quality categories as main branches
    

In any case the tree should include links to the scenarios of the following section.

## Quality Scenarios

**Contents**

Concretization of (sometimes vague or implicit) quality requirements using (quality) scenarios.

These scenarios describe what should happen when a stimulus arrives at the system.

For architects, two kinds of scenarios are important:

-   Usage scenarios (also called application scenarios or use case scenarios) describe the system’s runtime reaction to a certain stimulus. This also includes scenarios that describe the system’s efficiency or performance. Example: The system reacts to a user’s request within one second.
    
-   Change scenarios describe a modification of the system or of its immediate environment. Example: Additional functionality is implemented or requirements for a quality attribute change.
    

**Motivation**

Scenarios make quality requirements concrete and allow to more easily measure or decide whether they are fulfilled.

Especially when you want to assess your architecture using methods like ATAM you need to describe your quality goals (from section 1.2) more precisely down to a level of scenarios that can be discussed and evaluated.

**Form**

Tabular or free form text.

# Risks and Technical Debts

**Contents**

A list of identified technical risks or technical debts, ordered by priority

**Motivation**

“Risk management is project management for grown-ups” (Tim Lister, Atlantic Systems Guild.)

This should be your motto for systematic detection and evaluation of risks and technical debts in the architecture, which will be needed by management stakeholders (e.g. project managers, product owners) as part of the overall risk analysis and measurement planning.

**Form**

List of risks and/or technical debts, probably including suggested measures to minimize, mitigate or avoid risks or reduce technical debts.

See  [Risks and Technical Debt](https://docs.arc42.org/section-11/)  in the arc42 documentation.

# Glossary

**Contents**

The most important domain and technical terms that your stakeholders use when discussing the system.

You can also see the glossary as source for translations if you work in multi-language teams.

**Motivation**

You should clearly define your terms, so that all stakeholders

-   have an identical understanding of these terms
    
-   do not use synonyms and homonyms
    

A table with columns <Term> and <Definition>.

Potentially more columns in case you need translations.

See  [Glossary](https://docs.arc42.org/section-12/)  in the arc42 documentation.

Term

Definition

_<Term-1>_

_<definition-1>_

_<Term-2>_

_<definition-2>_
