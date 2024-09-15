```mermaid
C4Context
  title Diagrama C4 model level 3 para o Aplicativo de Carona Pucarona
  Enterprise_Boundary(appBoundary, "AppBoundary") {
    Person(user, "Usuário", "Usuário do aplicativo que pode ser um motorista ou passageiro.")
    Person(admin, "Administrador", "Administra o sistema e gerencia os dados.")
    
    System(webApp, "Aplicativo", "React", "Interface e lógica do aplicativo.")
    
    Enterprise_Boundary(backendBoundary, "BackendBoundary") {
      
      System(apiGateway, "API Gateway", "Flask", "Ponto de entrada para requisições.")
      
      System_Boundary(servicesBoundary, "Serviços") {
        System(authService, "Serviço de Autenticação", "Flask", "Autentica e autoriza usuários.")
        System(rideService, "Serviço de Caronas", "Flask", "Gerencia caronas.")
        System(paymentService, "Serviço de Pagamentos", "Flask", "Processa pagamentos.")
        System(notificationService, "Serviço de Notificações", "Flask", "Envia notificações.")
        System(chatService, "Serviço de Chat", "Flask", "Gerencia chat.")
      }

      System_Ext(emailSystem, "Sistema de Envio de Emails", "Serviço externo", "Serviço que envia emails de notificação.")
      System_Ext(paymentSystem, "Sistema de Pagamentos", "Serviço externo", "Processa pagamentos externos.")
    }

    Enterprise_Boundary(databaseBoundary, "DatabaseBoundary") {
      SystemDb(userTable, "Tabela de Usuários", "SQL", "Armazena informações de usuários.")
      SystemDb(rideTable, "Tabela de Caronas", "SQL", "Armazena informações das caronas.")
      SystemDb(paymentTable, "Tabela de Pagamentos", "SQL", "Armazena dados de transações de pagamento.")
      SystemDb(chatTable, "Tabela de Mensagens", "SQL", "Armazena mensagens trocadas.")
    }
  }

  BiRel(user, webApp, "Usa a interface do aplicativo", "HTTPS")
  BiRel(webApp, apiGateway, "Envia requisições", "REST API")
  Rel(apiGateway, authService, "Autentica usuário", "REST API")
  Rel(apiGateway, rideService, "Gerencia caronas", "REST API")
  Rel(apiGateway, paymentService, "Processa pagamentos", "REST API")
  Rel(apiGateway, notificationService, "Envia notificações", "REST API")
  Rel(notificationService, emailSystem, "Envia notificações", "SMTP")
  Rel(paymentService, paymentSystem, "Processa pagamentos", "HTTPS")

  Rel(user, rideService, "Interage com caronas")
  Rel(admin, apiGateway, "Administra o sistema", "HTTPS")

  Rel(authService, userTable, "Consulta e armazena dados de usuários", "SQL")
  Rel(rideService, rideTable, "Consulta e armazena dados de caronas", "SQL")
  Rel(paymentService, paymentTable, "Consulta e armazena dados de pagamentos", "SQL")
  Rel(chatService, chatTable, "Consulta e armazena mensagens", "SQL")

  UpdateElementStyle(user, $fontColor="red", $bgColor="grey", $borderColor="red")
  UpdateRelStyle(user, webApp, $textColor="blue", $lineColor="blue", $offsetX="5")
  UpdateRelStyle(webApp, apiGateway, $textColor="blue", $lineColor="blue", $offsetY="-10")
  UpdateRelStyle(notificationService, emailSystem, $textColor="blue", $lineColor="blue", $offsetY="-40", $offsetX="-50")
  UpdateRelStyle(paymentService, paymentSystem, $textColor="red", $lineColor="red", $offsetX="-50", $offsetY="20")

  UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="1")

