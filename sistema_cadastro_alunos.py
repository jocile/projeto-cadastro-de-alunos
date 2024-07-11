import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import datetime

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('alunos.db')
cursor = conn.cursor()

# Criação da tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        matricula TEXT PRIMARY KEY,
        nome TEXT,
        data_nascimento TEXT,
        idade INTEGER,
        genero TEXT,
        cpf TEXT,
        contato TEXT,
        rua TEXT,
        numero_residencia TEXT,
        cidade TEXT,
        estado TEXT,
        cep TEXT,
        nome_responsavel TEXT,
        cpf_responsavel TEXT,
        contato_responsavel TEXT,
        grau_escolaridade TEXT
    )
''')
conn.commit()

# Função para gerar matrícula
def gerar_matricula():
    cursor.execute('SELECT COUNT(*) FROM alunos')
    contador_aluno = cursor.fetchone()[0] + 1
    agora = datetime.datetime.now()
    ano = agora.year
    mes = agora.month
    numero_sequencial = f'{contador_aluno:04d}'
    matricula = f'{ano}{mes:02d}{numero_sequencial}'
    return matricula

# Função para calcular idade a partir da data de nascimento
def calcular_idade(data_nascimento):
    data_nascimento = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
    hoje = datetime.datetime.now()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

# Função para validar CPF
def validar_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    return True

# Função para cadastrar aluno no banco de dados
def cadastrar_aluno():
    def cadastrar():
        # Obtenção dos valores dos campos
        nome = entry_nome.get().strip().title()
        data_nascimento = entry_data_nascimento.get().strip()
        idade = calcular_idade(data_nascimento)
        genero = combo_genero.get()
        cpf = entry_cpf.get().strip()
        contato = entry_contato.get().strip()
        rua = entry_rua.get().strip().title()
        numero_residencia = entry_numero_residencia.get().strip()
        cidade = entry_cidade.get().strip().title()
        estado = entry_estado.get().strip().title()
        cep = entry_cep.get().strip()
        nome_responsavel = entry_nome_responsavel.get().strip().title()
        cpf_responsavel = entry_cpf_responsavel.get().strip()
        contato_responsavel = entry_contato_responsavel.get().strip()
        grau_escolaridade = combo_grau_escolaridade.get()

        # Verificação se todos os campos obrigatórios estão preenchidos
        if (nome and data_nascimento and genero and validar_cpf(cpf) and contato and rua and numero_residencia
            and cidade and estado and cep and nome_responsavel and validar_cpf(cpf_responsavel) and contato_responsavel
            and grau_escolaridade):

            matricula = gerar_matricula()

            # Inserção dos dados no banco de dados
            cursor.execute('''
                INSERT INTO alunos VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (matricula, nome, data_nascimento, idade, genero, cpf, contato, rua, numero_residencia, cidade,
                  estado, cep, nome_responsavel, cpf_responsavel, contato_responsavel, grau_escolaridade))
            conn.commit()

            messagebox.showinfo("Sucesso", f"Aluno {nome} cadastrado com sucesso! Matrícula: {matricula}")
        else:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos corretamente.")

    cadastrar_window = tk.Toplevel()
    cadastrar_window.title("Cadastrar Aluno")

    label_nome = tk.Label(cadastrar_window, text="Nome do Aluno:")
    label_nome.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    entry_nome = tk.Entry(cadastrar_window, width=50)
    entry_nome.grid(row=0, column=1, padx=10, pady=5, columnspan=2)

    label_data_nascimento = tk.Label(cadastrar_window, text="Data de Nascimento (dd/mm/aaaa):")
    label_data_nascimento.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
    entry_data_nascimento = tk.Entry(cadastrar_window, width=20)
    entry_data_nascimento.grid(row=1, column=1, padx=10, pady=5)

    label_genero = tk.Label(cadastrar_window, text="Gênero:")
    label_genero.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
    generos = ['Masculino', 'Feminino', 'Outro']
    combo_genero = ttk.Combobox(cadastrar_window, values=generos, width=18, state="readonly")
    combo_genero.grid(row=2, column=1, padx=10, pady=5)

    label_cpf = tk.Label(cadastrar_window, text="CPF do Aluno:")
    label_cpf.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
    entry_cpf = tk.Entry(cadastrar_window, width=20)
    entry_cpf.grid(row=3, column=1, padx=10, pady=5)

    label_contato = tk.Label(cadastrar_window, text="Número para Contato (11 dígitos):")
    label_contato.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
    entry_contato = tk.Entry(cadastrar_window, width=20)
    entry_contato.grid(row=4, column=1, padx=10, pady=5)

    label_rua = tk.Label(cadastrar_window, text="Rua:")
    label_rua.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
    entry_rua = tk.Entry(cadastrar_window, width=50)
    entry_rua.grid(row=5, column=1, padx=10, pady=5, columnspan=2)

    label_numero_residencia = tk.Label(cadastrar_window, text="Número da Residência:")
    label_numero_residencia.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
    entry_numero_residencia = tk.Entry(cadastrar_window, width=20)
    entry_numero_residencia.grid(row=6, column=1, padx=10, pady=5)

    label_cidade = tk.Label(cadastrar_window, text="Cidade:")
    label_cidade.grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
    entry_cidade = tk.Entry(cadastrar_window, width=50)
    entry_cidade.grid(row=7, column=1, padx=10, pady=5, columnspan=2)

    label_estado = tk.Label(cadastrar_window, text="Estado:")
    label_estado.grid(row=8, column=0, padx=10, pady=5, sticky=tk.W)
    entry_estado = tk.Entry(cadastrar_window, width=20)
    entry_estado.grid(row=8, column=1, padx=10, pady=5)

    label_cep = tk.Label(cadastrar_window, text="CEP:")
    label_cep.grid(row=9, column=0, padx=10, pady=5, sticky=tk.W)
    entry_cep = tk.Entry(cadastrar_window, width=20)
    entry_cep.grid(row=9, column=1, padx=10, pady=5)

    label_nome_responsavel = tk.Label(cadastrar_window, text="Nome do Responsável:")
    label_nome_responsavel.grid(row=10, column=0, padx=10, pady=5, sticky=tk.W)
    entry_nome_responsavel = tk.Entry(cadastrar_window, width=50)
    entry_nome_responsavel.grid(row=10, column=1, padx=10, pady=5, columnspan=2)

    label_cpf_responsavel = tk.Label(cadastrar_window, text="CPF do Responsável:")
    label_cpf_responsavel.grid(row=11, column=0, padx=10, pady=5, sticky=tk.W)
    entry_cpf_responsavel = tk.Entry(cadastrar_window, width=20)
    entry_cpf_responsavel.grid(row=11, column=1, padx=10, pady=5)

    label_contato_responsavel = tk.Label(cadastrar_window, text="Contato do Responsável (11 dígitos):")
    label_contato_responsavel.grid(row=12, column=0, padx=10, pady=5, sticky=tk.W)
    entry_contato_responsavel = tk.Entry(cadastrar_window, width=20)
    entry_contato_responsavel.grid(row=12, column=1, padx=10, pady=5)

    label_grau_escolaridade = tk.Label(cadastrar_window, text="Grau de Escolaridade:")
    label_grau_escolaridade.grid(row=13, column=0, padx=10, pady=5, sticky=tk.W)
    graus = ['Fundamental', 'Médio']
    combo_grau_escolaridade = ttk.Combobox(cadastrar_window, values=graus, width=18, state="readonly")
    combo_grau_escolaridade.grid(row=13, column=1, padx=10, pady=5)

    button_cadastrar = tk.Button(cadastrar_window, text="Cadastrar", command=cadastrar)
    button_cadastrar.grid(row=14, column=1, padx=10, pady=10, sticky=tk.E)

# Função para consultar um aluno
def consultar_aluno():
    def buscar():
        matricula = entry_matricula_consulta.get().strip()

        cursor.execute('SELECT * FROM alunos WHERE matricula = ?', (matricula,))
        aluno = cursor.fetchone()

        if aluno:
            resultado_text.config(state=tk.NORMAL)
            resultado_text.delete(1.0, tk.END)
            resultado_text.insert(tk.END, f"Matrícula: {aluno[0]}\n")
            resultado_text.insert(tk.END, f"Nome: {aluno[1]}\n")
            resultado_text.insert(tk.END, f"Data de Nascimento: {aluno[2]}\n")
            resultado_text.insert(tk.END, f"Idade: {aluno[3]}\n")
            resultado_text.insert(tk.END, f"Gênero: {aluno[4]}\n")
            resultado_text.insert(tk.END, f"CPF: {aluno[5]}\n")
            resultado_text.insert(tk.END, f"Contato: {aluno[6]}\n")
            resultado_text.insert(tk.END, f"Rua: {aluno[7]}\n")
            resultado_text.insert(tk.END, f"Número da Residência: {aluno[8]}\n")
            resultado_text.insert(tk.END, f"Cidade: {aluno[9]}\n")
            resultado_text.insert(tk.END, f"Estado: {aluno[10]}\n")
            resultado_text.insert(tk.END, f"CEP: {aluno[11]}\n")
            resultado_text.insert(tk.END, f"Nome do Responsável: {aluno[12]}\n")
            resultado_text.insert(tk.END, f"CPF do Responsável: {aluno[13]}\n")
            resultado_text.insert(tk.END, f"Contato do Responsável: {aluno[14]}\n")
            resultado_text.insert(tk.END, f"Grau de Escolaridade: {aluno[15]}\n")
            resultado_text.config(state=tk.DISABLED)
        else:
            messagebox.showwarning("Aviso", "Aluno não encontrado.")

    consultar_window = tk.Toplevel()
    consultar_window.title("Consultar Aluno")

    label_matricula = tk.Label(consultar_window, text="Matrícula do Aluno:")
    label_matricula.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    entry_matricula_consulta = tk.Entry(consultar_window, width=30)
    entry_matricula_consulta.grid(row=0, column=1, padx=10, pady=5)

    button_buscar = tk.Button(consultar_window, text="Buscar", command=buscar)
    button_buscar.grid(row=0, column=2, padx=10, pady=5)

    resultado_text = tk.Text(consultar_window, height=15, width=80, state=tk.DISABLED)
    resultado_text.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

# Função para listar todos os alunos
def listar_alunos():
    listar_window = tk.Toplevel()
    listar_window.title("Listar Alunos")

    scrollbar = tk.Scrollbar(listar_window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = tk.Listbox(listar_window, yscrollcommand=scrollbar.set, width=100)
    listbox.pack(padx=10, pady=10)

    scrollbar.config(command=listbox.yview)

    cursor.execute('SELECT matricula, nome FROM alunos')
    alunos = cursor.fetchall()

    for aluno in alunos:
        listbox.insert(tk.END, f"{aluno[0]} - {aluno[1]}")

# Função para excluir um aluno
def excluir_aluno():
    def excluir():
        matricula = entry_matricula_excluir.get().strip()

        if matricula:
            # Verifica se a matrícula existe no banco de dados
            cursor.execute('SELECT * FROM alunos WHERE matricula = ?', (matricula,))
            aluno = cursor.fetchone()

            if aluno:
                # Matrícula existe, então pode excluir
                cursor.execute('DELETE FROM alunos WHERE matricula = ?', (matricula,))
                conn.commit()
                messagebox.showinfo("Sucesso", f"Aluno com matrícula {matricula} excluído.")
            else:
                # Matrícula não existe
                messagebox.showerror("Erro", "Matrícula não encontrada. Insira uma matrícula existente.")
        else:
            messagebox.showerror("Erro", "Insira a matrícula do aluno.")

    excluir_window = tk.Toplevel()
    excluir_window.title("Excluir Aluno")

    label_matricula_excluir = tk.Label(excluir_window, text="Matrícula do Aluno:")
    label_matricula_excluir.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    entry_matricula_excluir = tk.Entry(excluir_window, width=30)
    entry_matricula_excluir.grid(row=0, column=1, padx=10, pady=5)

    button_excluir = tk.Button(excluir_window, text="Excluir", command=excluir)
    button_excluir.grid(row=1, column=1, padx=10, pady=5)

# Função principal
def menu_principal():
    root = tk.Tk()
    root.title("Sistema de Gerenciamento de Alunos")

    label_titulo = tk.Label(root, text="Menu Principal", font=("Helvetica", 16))
    label_titulo.pack(pady=10)

    button_cadastrar = tk.Button(root, text="Cadastrar Aluno", width=30, command=cadastrar_aluno)
    button_cadastrar.pack(pady=10)

    button_consultar = tk.Button(root, text="Consultar Aluno", width=30, command=consultar_aluno)
    button_consultar.pack(pady=10)

    button_excluir = tk.Button(root, text="Excluir Aluno", width=30, command=excluir_aluno)
    button_excluir.pack(pady=10)

    button_listar = tk.Button(root, text="Listar Alunos", width=30, command=listar_alunos)
    button_listar.pack(pady=10)

    button_sair = tk.Button(root, text="Sair", width=30, command=root.quit)
    button_sair.pack(pady=10)

    root.mainloop()

# Execução do programa
if __name__ == "__main__":
    menu_principal()

conn.close()