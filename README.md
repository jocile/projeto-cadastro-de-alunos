[16:46, 7/3/2024] +55 88 9922-7597: # Sistema de Gerenciamento de Alunos Do Curso de Progamação do Senac

<img src="https://i0.wp.com/multarte.com.br/wp-content/uploads/2020/09/senac-logomarca.jpg?w=860&ssl=1" alt="Exemplo imagem">

Este script em Python implementa um sistema simples de gerenciamento de alunos que permite aos usuários cadastrar, consultar e excluir registros de alunos. Abaixo está uma visão geral das funcionalidades e estrutura do código:

## Funcionalidades

### Cadastro de Aluno (cadastrar_aluno()):

- Solicitação de Dados:
  - Nome completo do aluno.
  - Data de nascimento do aluno, validada para garantir que o aluno tenha pelo menos 4 anos de idade.
  - E-mail válido do aluno.
  - Endereço completo do aluno, incluindo rua, bairro e número da residência.
  - Número de contato do aluno, formatado para padrão local.
  - Nome completo do responsável pelo aluno.
  - Número de contato do responsável, formatado para padrão local.
  - Número de identidade do aluno, formatado com dígitos e separador.
  - Grau de escolaridade do aluno.

- Geração Automática de Matrícula:
  - Cada aluno cadastrado recebe uma matrícula única, baseada na data e hora do cadastro.

### Consulta de Aluno (consultar_aluno()):

- Consulta por Matrícula:
  - Permite buscar alunos específicos usando sua matrícula única gerada no cadastro.
  - Exibe todos os detalhes cadastrados do aluno encontrado, incluindo nome, data de nascimento, idade, e-mail, endereço, contato, responsável, grau de escolaridade, matrícula e identidade.

- Consulta de Dados dos Responsáveis:
  - Além dos detalhes do aluno, oferece a opção de consultar apenas os dados do responsável pelo aluno encontrado.

- Listagem de Todos os Alunos Matriculados:
  - Apresenta uma lista completa de todos os alunos atualmente registrados no sistema, exibindo seus nomes e matrículas.

### Exclusão de Aluno (excluir_aluno()):

- Remoção Segura de Dados:
  - Permite excluir um aluno do sistema após confirmação do usuário, usando a matrícula como identificador único.
  - Confirmação solicitada para evitar exclusões acidentais.

### Menu Principal (menu()):

- Interface Interativa:
  - Apresenta um menu claro com opções numeradas para facilitar a navegação.
  - Limpa a tela do console entre transições de menu para melhorar a experiência do usuário.
    ## :cyclone: Fluxo Principal De Requisitos:
1. O usuário seleciona a opção "Adicionar Novo Aluno".
2. O sistema solicita as informações do aluno (nome, idade, matrícula, curso).
3. O usuário insere as informações e confirma.
4. O sistema valida as informações e adiciona o novo aluno no banco de dados.
5. O sistema confirma a adição do aluno e exibe os detalhes inseridos.

## :sparkles: Características do Cadastro de Alunos

A proposta é de criar um sistema deinformação, que colete os seguintes dados:

* Nome do Aluno
* Data de Nascimento
* Gênero
* Responsável
* CPF do aluno
* CPF do responsável
* Estado
* Cidade
* CEP
* Endereço e numero
* Num. Celular do ALuno
* Num. Celular do Responsável
* Grau de Escolaridade

> O programa deve receber esses dados, editar esses dados, atualizar esses dados e deletar esses dados.

### :space_invader: Backend
Menu Principal: 

 1. Cadastrar Aluno
 2. Consultar Aluno
 3. Excluir Aluno  
 4. Sair
 Digite sua opção: 
 --> 
`           `

- Funcionalidades essenciais: adicionar aluno, excluir aluno, consultar aluno.
- Classifique os dados segundo os tipos das variáveis (numéricos, literais ou lógicos) que irão armazená-los.

Variáveis literais: nome do aluno, sexo, endereço, cidade, estado, nome do pai, nome da mãe.
Variáveis numéricas: telefone, CEP, RG, data de nascimento, grau de escolaridade.

### :computer: Frontend

- Menu de Ações do APP:
  - Cadastrar ALuno
  - Consultar ALuno
  - Excluir Aluno
  - Listar Alunos
  - Sair

- Janelas para cada ação executada pelo usuário

- Janela de Erro - Atributo vazio

## Colaboradores
### RESPONSAVEIS PELO README E O CONSULTAR ALUNO
- Marcos David e Marcos Graziel![e6b4a85a-0360-4d70-a8cc-9b0c5fe581c0](https://github.com/marcosgbin/cadastro_de_aluno01/assets/168863262/20ecaef5-e60c-4608-ac2e-4667fbc1acd9)


### RESPONSAVEIS POR CADASTRAR E EXCLUIR ALUNO E A CRIAÇÃO DOS DIAGRAMAS DE CASO DE USO E DESCREVENDO PROJETO
- David Andrade e Erik Jasen![7d770ff4-927f-4b1f-8827-370a0a63ef7c](https://github.com/marcosgbin/cadastro_de_aluno01/assets/168863262/4285abd4-81ae-4d21-b3d0-9cf1258b032c)

### RESPONSAVEIS PELO FRONT END E BANCO DE DADOS
- kauã e Madson![1b51ab62-d219-4046-a8da-56b04130e622](https://github.com/marcosgbin/cadastro_de_aluno01/assets/168863262/49f83ab8-e2aa-460b-b2df-79602254ea35)


## Execução do Programa

Para executar o programa, basta rodar o script Python. O menu principal guiará o usuário através das opções disponíveis para interação com o sistema de gerenciamento de alunos.

## Melhorias Futuras

- Implementação de tratamento de erros mais robusto para garantir a integridade dos dados.
- Persistência de dados utilizando um banco de dados para armazenamento durável.
- Melhorias na interface do usuário para uma experiência mais intuitiva.
- Adição de funcionalidades como atualização de registros de alunos.

Este sistema foi desenvolvido como parte de um projeto colaborativo envolvendo os colaboradores listados acima, cada um contribuindo com sua expertise para o seu desenvolvimento e aprimoramento.
[16:51, 7/3/2024] +55 88 9442-7058: # Sistema de Gerenciamento de Alunos Do Curso de Progamação do Senac

<img src="https://i0.wp.com/multarte.com.br/wp-content/uploads/2020/09/senac-logomarca.jpg?w=860&ssl=1" alt="Exemplo imagem">

Este script em Python implementa um sistema simples de gerenciamento de alunos que permite aos usuários cadastrar, consultar e excluir registros de alunos. Abaixo está uma visão geral das funcionalidades e estrutura do código:

## Funcionalidades

### Cadastro de Aluno (cadastrar_aluno()):

- *Solicitação de Dados:*
  - Nome completo do aluno.
  - Data de nascimento do aluno, validada para garantir que o aluno tenha pelo menos 4 anos de idade.
  - E-mail válido do aluno.
  - Endereço completo do aluno, incluindo rua, bairro e número da residência.
  - Número de contato do aluno, formatado para padrão local.
  - Nome completo do responsável pelo aluno.
  - Número de contato do responsável, formatado para padrão local.
  - Número de identidade do aluno, formatado com dígitos e separador.
  - Grau de escolaridade do aluno.

- *Geração Automática de Matrícula:*
  - Cada aluno cadastrado recebe uma matrícula única, baseada na data e hora do cadastro.

### Consulta de Aluno (consultar_aluno()):

- *Consulta por Matrícula:*
  - Permite buscar alunos específicos usando sua matrícula única gerada no cadastro.
  - Exibe todos os detalhes cadastrados do aluno encontrado, incluindo nome, data de nascimento, idade, e-mail, endereço, contato, responsável, grau de escolaridade, matrícula e identidade.

- *Consulta de Dados dos Responsáveis:*
  - Além dos detalhes do aluno, oferece a opção de consultar apenas os dados do responsável pelo aluno encontrado.

- *Listagem de Todos os Alunos Matriculados:*
  - Apresenta uma lista completa de todos os alunos atualmente registrados no sistema, exibindo seus nomes e matrículas.

### Exclusão de Aluno (excluir_aluno()):

- *Remoção Segura de Dados:*
  - Permite excluir um aluno do sistema após confirmação do usuário, usando a matrícula como identificador único.
  - Confirmação solicitada para evitar exclusões acidentais.

### Menu Principal (menu()):

- *Interface Interativa:*
  - Apresenta um menu claro com opções numeradas para facilitar a navegação.
  - Limpa a tela do console entre transições de menu para melhorar a experiência do usuário.
    ## :cyclone: Fluxo Principal De Requisitos:
1. O usuário seleciona a opção "Adicionar Novo Aluno".
2. O sistema solicita as informações do aluno (nome, idade, matrícula, curso).
3. O usuário insere as informações e confirma.
4. O sistema valida as informações e adiciona o novo aluno no banco de dados.
5. O sistema confirma a adição do aluno e exibe os detalhes inseridos.

## :sparkles: Características do Cadastro de Alunos

A proposta é de criar um sistema deinformação, que colete os seguintes dados:

* Nome do Aluno
* Data de Nascimento
* Gênero
* Responsável
* CPF do aluno
* CPF do responsável
* Estado
* Cidade
* CEP
* Endereço e numero
* Num. Celular do ALuno
* Num. Celular do Responsável
* Grau de Escolaridade

> O programa deve receber esses dados, editar esses dados, atualizar esses dados e deletar esses dados.

### :space_invader: Backend
Menu Principal: 

 1. Cadastrar Aluno
 2. Consultar Aluno
 3. Excluir Aluno  
 4. Sair
 Digite sua opção: 
 --> 
`           `

- Funcionalidades essenciais: adicionar aluno, excluir aluno, consultar aluno.
- Classifique os dados segundo os tipos das variáveis (numéricos, literais ou lógicos) que irão armazená-los.

Variáveis literais: nome do aluno, sexo, endereço, cidade, estado, nome do pai, nome da mãe.
Variáveis numéricas: telefone, CEP, RG, data de nascimento, grau de escolaridade.

### :computer: Frontend

- Menu de Ações do APP:
  - Cadastrar ALuno
  - Consultar ALuno
  - Excluir Aluno
  - Listar Alunos
  - Sair

- Janelas para cada ação executada pelo usuário

- Janela de Erro - Atributo vazio

## Colaboradores
### RESPONSAVEIS PELO README E O CONSULTAR ALUNO
- Marcos David e Marcos Graziel![be61fb2a-4314-45d3-b8f2-33b53661b317](https://github.com/marcosgbin/cadastro_de_aluno01/assets/168863262/1a4b66cc-5e49-401f-8612-e4df0bbc7ff0)





### RESPONSAVEIS POR CADASTRAR E EXCLUIR ALUNO E A CRIAÇÃO DOS DIAGRAMAS DE CASO DE USO E DESCREVENDO PROJETO
- David Andrade e Erik Jasen![7d770ff4-927f-4b1f-8827-370a0a63ef7c](https://github.com/marcosgbin/cadastro_de_aluno01/assets/168863262/4285abd4-81ae-4d21-b3d0-9cf1258b032c)

### RESPONSAVEIS PELO FRONT END E BANCO DE DADOS
- kauã e Madson![1b51ab62-d219-4046-a8da-56b04130e622](https://github.com/marcosgbin/cadastro_de_aluno01/assets/168863262/49f83ab8-e2aa-460b-b2df-79602254ea35)


## Execução do Programa

Para executar o programa, basta rodar o script Python. O menu principal guiará o usuário através das opções disponíveis para interação com o sistema de gerenciamento de alunos.

## Melhorias Futuras

- Implementação de tratamento de erros mais robusto para garantir a integridade dos dados.
- Persistência de dados utilizando um banco de dados para armazenamento durável.
- Melhorias na interface do usuário para uma experiência mais intuitiva.
- Adição de funcionalidades como atualização de registros de alunos.

Este sistema foi desenvolvido como parte de um projeto colaborativo envolvendo os colaboradores listados acima, cada um contribuindo com sua expertise para o seu desenvolvimento e aprimoramento.