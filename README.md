# projeto-cadastro-de-alunos
Projeto integrador da equipe de progrmador de sistemas do curso do Senac


Matrícula do Aluno (README)

1.Esse programa realiza uma matrícula, consúlta e exclusão de alunos de uma lista, coletando seus dados e os dados do seu responsável.

1.1. Matrícula de Alunos.
Ao matrícular o aluno é inserido o nome, data de nascimento, email, contato, rua, bairro e número de residência, nome do responsável e contato do responsável, RG do aluno, grau de escolaridade. Seus dados
são salvos e é gerado uma matrícula de 10 dígitos de acordo com o ano, mês e ordem de matrícula no mês e ano.

1.2. Consulta de Alunos.
Com a matrícula que é gerada ao matricular o aluno, você poderá ter a opção de consultar todas as informações do aluno, somente os dados do responsável ou ver a lista de todos os alunos com o nome e matrícula.

1.3. Excluir Alunos.
Você poderá pesquisar o aluno que deseja excluir com o uso da matrícula do mesmo. Ao inserir a matrícula o programa retornará com uma pergunta para confirmação da exclusão do aluno, mostrando seu nome e matrícula.
Caso o usuário queira confirmar a exclusão deve digitar "s" e teclar "Enter", caso deseje cancelar será necessário apenas declar "Enter".

Diagrama de fluxo do sistema:

```mermaid
graph TD
    A[Menu_Principal] -->|1. Cadastrar Aluno| B[Cadastrar Aluno]
    A -->|2. Consultar Aluno| C[Consultar Aluno]
    A -->|3. Excluir Aluno| D[Excluir Aluno]
    A -->|4. Sair| E[Sair]

    B --> B1[Insira o nome do aluno nome e sobrenome]
    B1 --> B2{Nome válido?}
    B2 -->|Sim| B3[Insira a data de nascimento]
    B2 -->|Não| B1
    B3 --> B4{Data válida e aluno tem pelo menos 4 anos?}
    B4 -->|Sim| B5[Insira o e-mail]
    B4 -->|Não| B3
    B5 --> B6{E-mail válido?}
    B6 -->|Sim| B7[Insira a rua]
    B6 -->|Não| B5
    B7 --> B8[Insira o bairro]
    B8 --> B9[Insira o número da residência]
    B9 --> B10{Número válido?}
    B10 -->|Sim| B11[Insira o número de contato do aluno]
    B10 -->|Não| B9
    B11 --> B12{Contato válido?}
    B12 -->|Sim| B13[Insira o nome do responsável]
    B12 -->|Não| B11
    B13 --> B14{Nome do responsável válido?}
    B14 -->|Sim| B15[Insira o número de contato do responsável]
    B14 -->|Não| B13
    B15 --> B16{Contato válido?}
    B16 -->|Sim| B17[Insira o RG do aluno]
    B16 -->|Não| B15
    B17 --> B18{RG válido?}
    B18 -->|Sim| B19[Insira o grau de escolaridade]
    B18 -->|Não| B17
    B19 --> B20[Gerar matrícula]
    B20 --> B21[Salvar dados do aluno]
    B21 --> A

    C -->|Se há alunos cadastrados| C1[Listar alunos]
    C1 --> A
    C -->|Se não há alunos cadastrados| C2[Mensagem: Nenhum aluno cadastrado]
    C2 --> A

    D --> D1[Digite a matrícula do aluno a ser excluído]
    D1 --> D2{Matrícula encontrada?}
    D2 -->|Sim| D3[Confirmação de exclusão]
    D2 -->|Não| D6[Mensagem: Matrícula não encontrada]
    D3 -->|Confirmar| D4[Excluir aluno]
    D4 --> D5[Mensagem: Aluno excluído com sucesso]
    D3 -->|Cancelar| A
    D5 --> A
    D6 --> A

    E --> F[Fim]


```
