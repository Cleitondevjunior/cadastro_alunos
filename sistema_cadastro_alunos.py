import psycopg2
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# --------------------------------------------------
# FUNÇÕES DE ACESSO AO BANCO DE DADOS
# --------------------------------------------------
def conectar():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="db_escola",  # ajuste conforme seu banco
            user="",       # ajuste conforme seu usuário
            password=""        # ajuste conforme sua senha
        )
        # Você pode descomentar a linha abaixo para visualizar no console:
        # print("Conexão estabelecida!")
        return conn
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível conectar ao banco de dados: {e}")
        return None
# ---------- ALUNOS ----------

# Função para cadastrar um novo aluno no banco de dados
def cadastrar_aluno(nome):  # Define a função 'cadastrar_aluno' que recebe o nome do aluno como parâmetro.
    conn = conectar()  # Estabelece uma conexão com o banco de dados usando a função 'conectar'.
    if conn:  # Verifica se a conexão foi bem-sucedida.
        cur = conn.cursor()  # Cria um cursor para executar comandos SQL.
        cur.execute("INSERT INTO alunos (nome) VALUES (%s)", (nome,))  # Insere um novo aluno na tabela 'alunos'.
        conn.commit()  # Confirma as mudanças no banco de dados.
        cur.close()  # Fecha o cursor para liberar recursos.
        conn.close()  # Fecha a conexão com o banco de dados.

# Função para listar todos os alunos cadastrados
def listar_alunos():  # Define a função 'listar_alunos' que retorna todos os alunos da tabela.
    conn = conectar()  # Estabelece a conexão com o banco de dados.
    if conn:  # Verifica se a conexão foi bem-sucedida.
        cur = conn.cursor()  # Cria um cursor para executar comandos SQL.
        cur.execute("SELECT id, nome FROM alunos ORDER BY id")  # Executa um comando SQL para selecionar todos os alunos, ordenados pelo ID.
        rows = cur.fetchall()  # Recupera todos os resultados da consulta e os armazena em 'rows'.
        cur.close()  # Fecha o cursor.
        conn.close()  # Fecha a conexão com o banco de dados.
        return rows  # Retorna a lista de alunos encontrados.
    return []  # Retorna uma lista vazia caso a conexão não seja bem-sucedida.

# Função para buscar alunos com base em um termo de pesquisa
def buscar_alunos(termo):  # Define a função 'buscar_alunos' que recebe um termo de busca como parâmetro.
    conn = conectar()  # Estabelece a conexão com o banco de dados.
    if conn:  # Verifica se a conexão foi bem-sucedida.
        cur = conn.cursor()  # Cria um cursor para executar comandos SQL.
        cur.execute("SELECT id, nome FROM alunos WHERE nome ILIKE %s ORDER BY id", ('%' + termo + '%',))  # Executa um comando SQL que busca alunos cujos nomes correspondam ao termo, ignorando maiúsculas/minúsculas.
        rows = cur.fetchall()  # Recupera todos os resultados da consulta e os armazena em 'rows'.
        cur.close()  # Fecha o cursor.
        conn.close()  # Fecha a conexão com o banco de dados.
        return rows  # Retorna os alunos encontrados.
    return []  # Retorna uma lista vazia caso a conexão não seja bem-sucedida.

# Função para atualizar o nome de um aluno
def atualizar_aluno(id_aluno, novo_nome):  # Define a função 'atualizar_aluno' que recebe o ID do aluno e o novo nome como parâmetros.
    conn = conectar()  # Estabelece a conexão com o banco de dados.
    if conn:  # Verifica se a conexão foi bem-sucedida.
        cur = conn.cursor()  # Cria um cursor para executar comandos SQL.
        cur.execute("UPDATE alunos SET nome=%s WHERE id=%s", (novo_nome, id_aluno))  # Executa um comando SQL para atualizar o nome do aluno com o ID fornecido.
        conn.commit()  # Confirma as mudanças no banco de dados.
        cur.close()  # Fecha o cursor.
        conn.close()  # Fecha a conexão com o banco de dados.

# Função para deletar um aluno
def deletar_aluno(id_aluno):  # Define a função 'deletar_aluno' que recebe o ID do aluno como parâmetro.
    conn = conectar()  # Estabelece a conexão com o banco de dados.
    if conn:  # Verifica se a conexão foi bem-sucedida.
        cur = conn.cursor()  # Cria um cursor para executar comandos SQL.
        cur.execute("DELETE FROM alunos WHERE id=%s", (id_aluno,))  # Executa um comando SQL para remover o aluno com o ID fornecido.
        conn.commit()  # Confirma as mudanças no banco de dados.
        cur.close()  # Fecha o cursor.
        conn.close()  # Fecha a conexão com o banco de dados.

# ---------- PROFESSORES ----------

# Função para cadastrar um novo professor no banco de dados
def cadastrar_professor(nome):  # Define a função 'cadastrar_professor' que recebe o nome do professor como parâmetro.
    conn = conectar()  # Estabelece uma conexão com o banco de dados utilizando a função 'conectar'.
    if conn:  # Verifica se a conexão foi bem-sucedida.
        cur = conn.cursor()  # Cria um cursor para executar comandos SQL.
        cur.execute("INSERT INTO professores (nome) VALUES (%s)", (nome,))  # Executa um comando SQL para inserir um novo professor na tabela 'professores'.
        conn.commit()  # Confirma as mudanças feitas no banco de dados.
        cur.close()  # Fecha o cursor para liberar recursos.
        conn.close()  # Fecha a conexão com o banco de dados.

# Função para listar todos os professores cadastrados
def listar_professores():  # Define a função 'listar_professores' que retorna todos os professores da tabela.
    conn = conectar()  # Estabelece uma conexão com o banco de dados.
    if conn:  # Verifica se a conexão foi bem-sucedida.
        cur = conn.cursor()  # Cria um cursor para executar comandos SQL.
        cur.execute("SELECT id, nome FROM professores ORDER BY id")  # Executa um comando SQL para selecionar todos os professores, ordenados pelo ID.
        rows = cur.fetchall()  # Recupera todos os resultados da consulta e os armazena em 'rows'.
        cur.close()  # Fecha o cursor.
        conn.close()  # Fecha a conexão com o banco de dados.
        return rows  # Retorna a lista de professores encontrados.
    return []  # Retorna uma lista vazia caso a conexão não seja bem-sucedida.

# Função para buscar professores com base em um termo de pesquisa
def buscar_professores(termo):  # Define a função 'buscar_professores' que recebe um termo de busca como parâmetro.
    conn = conectar()  # Estabelece a conexão com o banco de dados.
    if conn:  # Verifica se a conexão foi bem-sucedida.
        cur = conn.cursor()  # Cria um cursor para executar comandos SQL.
        cur.execute("SELECT id, nome FROM professores WHERE nome ILIKE %s ORDER BY id", ('%' + termo + '%',))  # Executa um comando SQL que busca professores cujos nomes contenham o termo, ignorando maiúsculas/minúsculas.
        rows = cur.fetchall()  # Recupera todos os resultados da consulta e os armazena em 'rows'.
        cur.close()  # Fecha o cursor.
        conn.close()  # Fecha a conexão com o banco de dados.
        return rows  # Retorna os professores encontrados.
    return []  # Retorna uma lista vazia caso a conexão não seja bem-sucedida.

# Função para atualizar o nome de um professor
def atualizar_professor(id_prof, novo_nome):  # Define a função 'atualizar_professor' que recebe o ID do professor e o novo nome como parâmetros.
    conn = conectar()  # Estabelece a conexão com o banco de dados.
    if conn:  # Verifica se a conexão foi bem-sucedida.
        cur = conn.cursor()  # Cria um cursor para executar comandos SQL.
        cur.execute("UPDATE professores SET nome=%s WHERE id=%s", (novo_nome, id_prof))  # Executa um comando SQL para atualizar o nome do professor com o ID fornecido.
        conn.commit()  # Confirma as mudanças no banco de dados.
        cur.close()  # Fecha o cursor.
        conn.close()  # Fecha a conexão com o banco de dados.

# Função para deletar um professor
def deletar_professor(id_prof):  # Define a função 'deletar_professor' que recebe o ID do professor como parâmetro.
    conn = conectar()  # Estabelece a conexão com o banco de dados.
    if conn:  # Verifica se a conexão foi bem-sucedida.
        cur = conn.cursor()  # Cria um cursor para executar comandos SQL.
        cur.execute("DELETE FROM professores WHERE id=%s", (id_prof,))  # Executa um comando SQL para remover o professor com o ID fornecido.
        conn.commit()  # Confirma as mudanças no banco de dados.
        cur.close()  # Fecha o cursor.
        conn.close()  # Fecha a conexão com o banco de dados.

# ---------- DISCIPLINAS ----------

# Função para cadastrar uma nova disciplina no banco de dados
def cadastrar_disciplina(nome, professor_id):  # Define a função 'cadastrar_disciplina' que recebe o nome da disciplina e o ID do professor como parâmetros.
    conn = conectar()  # Estabelece uma conexão com o banco de dados usando a função 'conectar'.
    if conn:  # Verifica se a conexão foi bem-sucedida.
        cur = conn.cursor()  # Cria um cursor para executar comandos SQL.
        cur.execute("INSERT INTO disciplinas (nome, professor_id) VALUES (%s, %s)", (nome, professor_id))  # Insere uma nova disciplina associada ao professor na tabela 'disciplinas'.
        conn.commit()  # Confirma as alterações no banco de dados.
        cur.close()  # Fecha o cursor para liberar recursos.
        conn.close()  # Fecha a conexão com o banco de dados.

# Função para listar todas as disciplinas cadastradas
def listar_disciplinas():  # Define a função 'listar_disciplinas' que retorna todas as disciplinas armazenadas na tabela.
    conn = conectar()  # Estabelece a conexão com o banco de dados.
    if conn:  # Verifica se a conexão foi bem-sucedida.
        cur = conn.cursor()  # Cria um cursor para executar comandos SQL.
        cur.execute("SELECT id, nome, professor_id FROM disciplinas ORDER BY id")  # Executa um comando SQL para selecionar todas as disciplinas, ordenadas pelo ID.
        rows = cur.fetchall()  # Recupera todos os resultados da consulta e os armazena em 'rows'.
        cur.close()  # Fecha o cursor.
        conn.close()  # Fecha a conexão com o banco de dados.
        return rows  # Retorna a lista de disciplinas encontradas.
    return []  # Retorna uma lista vazia caso a conexão não seja bem-sucedida.

# Função para buscar disciplinas com base em um termo de pesquisa
def buscar_disciplinas(termo):  # Define a função 'buscar_disciplinas' que recebe um termo de busca como parâmetro.
    conn = conectar()  # Estabelece a conexão com o banco de dados.
    if conn:  # Verifica se a conexão foi bem-sucedida.
        cur = conn.cursor()  # Cria um cursor para executar comandos SQL.
        cur.execute("SELECT id, nome, professor_id FROM disciplinas WHERE nome ILIKE %s ORDER BY id", ('%' + termo + '%',))  # Executa um comando SQL que busca disciplinas cujos nomes correspondam ao termo, ignorando maiúsculas/minúsculas.
        rows = cur.fetchall()  # Recupera todos os resultados da consulta e os armazena em 'rows'.
        cur.close()  # Fecha o cursor.
        conn.close()  # Fecha a conexão com o banco de dados.
        return rows  # Retorna as disciplinas encontradas.
    return []  # Retorna uma lista vazia caso a conexão não seja bem-sucedida.

# Função para atualizar os dados de uma disciplina
def atualizar_disciplina(id_disc, novo_nome, professor_id):  # Define a função 'atualizar_disciplina' que recebe o ID da disciplina, um novo nome e o ID do professor como parâmetros.
    conn = conectar()  # Estabelece a conexão com o banco de dados.
    if conn:  # Verifica se a conexão foi bem-sucedida.
        cur = conn.cursor()  # Cria um cursor para executar comandos SQL.
        cur.execute("UPDATE disciplinas SET nome=%s, professor_id=%s WHERE id=%s", (novo_nome, professor_id, id_disc))  # Executa um comando SQL para atualizar os dados da disciplina.
        conn.commit()  # Confirma as alterações no banco de dados.
        cur.close()  # Fecha o cursor.
        conn.close()  # Fecha a conexão com o banco de dados.

# Função para deletar uma disciplina
def deletar_disciplina(id_disc):  # Define a função 'deletar_disciplina' que recebe o ID da disciplina como parâmetro.
    conn = conectar()  # Estabelece a conexão com o banco de dados.
    if conn:  # Verifica se a conexão foi bem-sucedida.
        cur = conn.cursor()  # Cria um cursor para executar comandos SQL.
        cur.execute("DELETE FROM disciplinas WHERE id=%s", (id_disc,))  # Executa um comando SQL para remover a disciplina com o ID fornecido.
        conn.commit()  # Confirma as alterações no banco de dados.
        cur.close()  # Fecha o cursor.
        conn.close()  # Fecha a conexão com o banco de dados.


# ---------- MATRÍCULAS (Associação entre alunos e disciplinas) ----------
def matricular_aluno_disciplina(aluno_id, disciplina_id):
    conn = conectar()
    if conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO alunos_disciplinas (aluno_id, disciplina_id) VALUES (%s, %s)", (aluno_id, disciplina_id))
        conn.commit()
        cur.close()
        conn.close()

def listar_matriculas():
    conn = conectar()
    if conn:
        cur = conn.cursor()
        query = """
        SELECT ad.aluno_id, a.nome AS aluno, ad.disciplina_id, d.nome AS disciplina
        FROM alunos_disciplinas ad
        JOIN alunos a ON a.id = ad.aluno_id
        JOIN disciplinas d ON d.id = ad.disciplina_id
        ORDER BY ad.aluno_id;
        """
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    return []

def buscar_matriculas(termo):
    conn = conectar()
    if conn:
        cur = conn.cursor()
        query = """
        SELECT ad.aluno_id, a.nome AS aluno, ad.disciplina_id, d.nome AS disciplina
        FROM alunos_disciplinas ad
        JOIN alunos a ON a.id = ad.aluno_id
        JOIN disciplinas d ON d.id = ad.disciplina_id
        WHERE a.nome ILIKE %s OR d.nome ILIKE %s
        ORDER BY ad.aluno_id;
        """
        like_term = '%' + termo + '%'
        cur.execute(query, (like_term, like_term))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    return []

# --------------------------------------------------
# INTERFACE GRÁFICA COM NOTEBOOK (ABAS)
# --------------------------------------------------

# Aba de Alunos
class AlunosTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Gerenciar Alunos", font=("Arial", 14)).pack(pady=5)
        
        # Área de busca
        search_frame = tk.Frame(self)
        search_frame.pack(pady=5)
        tk.Label(search_frame, text="Buscar Aluno:").pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(search_frame, text="Buscar", command=self.buscar).pack(side=tk.LEFT, padx=5)
        
        # Área de cadastro/edição
        input_frame = tk.Frame(self)
        input_frame.pack(pady=5)
        tk.Label(input_frame, text="Nome do Aluno:").grid(row=0, column=0, padx=5, pady=5)
        self.nome_entry = tk.Entry(input_frame)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Botões de ação
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Adicionar", command=self.adicionar_aluno).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Atualizar", command=self.atualizar_aluno).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Deletar", command=self.deletar_aluno).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Limpar", command=self.limpar_campos).grid(row=0, column=3, padx=5)
        
        # Treeview para exibir os alunos
        self.tree = ttk.Treeview(self, columns=("id", "nome"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("nome", text="Nome")
        self.tree.column("id", width=50, anchor=tk.CENTER)
        self.tree.column("nome", width=200, anchor=tk.W)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=5)
        self.tree.bind("<<TreeviewSelect>>", self.selecionar_item)
        self.refresh_tree()

    def refresh_tree(self):
        self.tree.delete(*self.tree.get_children())
        for aluno in listar_alunos():
            self.tree.insert("", tk.END, values=aluno)

    def buscar(self):
        termo = self.search_entry.get().strip()
        registros = buscar_alunos(termo) if termo else listar_alunos()
        self.tree.delete(*self.tree.get_children())
        for aluno in registros:
            self.tree.insert("", tk.END, values=aluno)

    def adicionar_aluno(self):
        nome = self.nome_entry.get().strip()
        if not nome:
            messagebox.showwarning("Aviso", "Digite o nome do aluno")
            return
        cadastrar_aluno(nome)
        messagebox.showinfo("Sucesso", "Aluno adicionado com sucesso!")
        self.refresh_tree()
        self.limpar_campos()

    def atualizar_aluno(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione um aluno para atualizar")
            return
        aluno_id, _ = self.tree.item(selected, "values")
        novo_nome = self.nome_entry.get().strip()
        if not novo_nome:
            messagebox.showwarning("Aviso", "Digite o novo nome do aluno")
            return
        atualizar_aluno(aluno_id, novo_nome)
        messagebox.showinfo("Sucesso", "Aluno atualizado com sucesso!")
        self.refresh_tree()
        self.limpar_campos()

    def deletar_aluno(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione um aluno para deletar")
            return
        aluno_id, _ = self.tree.item(selected, "values")
        if messagebox.askyesno("Confirmar", "Tem certeza que deseja deletar este aluno?"):
            deletar_aluno(aluno_id)
            messagebox.showinfo("Sucesso", "Aluno deletado com sucesso!")
            self.refresh_tree()
            self.limpar_campos()

    def limpar_campos(self):
        self.nome_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)
        self.tree.selection_remove(self.tree.selection())

    def selecionar_item(self, event):
        selected = self.tree.focus()
        if selected:
            _, nome = self.tree.item(selected, "values")
            self.nome_entry.delete(0, tk.END)
            self.nome_entry.insert(0, nome)

# Aba de Professores
class ProfessoresTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Gerenciar Professores", font=("Arial", 14)).pack(pady=5)
        
        search_frame = tk.Frame(self)
        search_frame.pack(pady=5)
        tk.Label(search_frame, text="Buscar Professor:").pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(search_frame, text="Buscar", command=self.buscar).pack(side=tk.LEFT, padx=5)
        
        input_frame = tk.Frame(self)
        input_frame.pack(pady=5)
        tk.Label(input_frame, text="Nome do Professor:").grid(row=0, column=0, padx=5, pady=5)
        self.nome_entry = tk.Entry(input_frame)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=5)
        
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Adicionar", command=self.adicionar_professor).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Atualizar", command=self.atualizar_professor).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Deletar", command=self.deletar_professor).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Limpar", command=self.limpar_campos).grid(row=0, column=3, padx=5)
        
        self.tree = ttk.Treeview(self, columns=("id", "nome"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("nome", text="Nome")
        self.tree.column("id", width=50, anchor=tk.CENTER)
        self.tree.column("nome", width=200, anchor=tk.W)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=5)
        self.tree.bind("<<TreeviewSelect>>", self.selecionar_item)
        self.refresh_tree()

    def refresh_tree(self):
        self.tree.delete(*self.tree.get_children())
        for prof in listar_professores():
            self.tree.insert("", tk.END, values=prof)

    def buscar(self):
        termo = self.search_entry.get().strip()
        registros = buscar_professores(termo) if termo else listar_professores()
        self.tree.delete(*self.tree.get_children())
        for prof in registros:
            self.tree.insert("", tk.END, values=prof)

    def adicionar_professor(self):
        nome = self.nome_entry.get().strip()
        if not nome:
            messagebox.showwarning("Aviso", "Digite o nome do professor")
            return
        cadastrar_professor(nome)
        messagebox.showinfo("Sucesso", "Professor adicionado com sucesso!")
        self.refresh_tree()
        self.limpar_campos()

    def atualizar_professor(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione um professor para atualizar")
            return
        prof_id, _ = self.tree.item(selected, "values")
        novo_nome = self.nome_entry.get().strip()
        if not novo_nome:
            messagebox.showwarning("Aviso", "Digite o novo nome do professor")
            return
        atualizar_professor(prof_id, novo_nome)
        messagebox.showinfo("Sucesso", "Professor atualizado com sucesso!")
        self.refresh_tree()
        self.limpar_campos()

    def deletar_professor(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione um professor para deletar")
            return
        prof_id, _ = self.tree.item(selected, "values")
        if messagebox.askyesno("Confirmar", "Tem certeza que deseja deletar este professor?"):
            deletar_professor(prof_id)
            messagebox.showinfo("Sucesso", "Professor deletado com sucesso!")
            self.refresh_tree()
            self.limpar_campos()

    def limpar_campos(self):
        self.nome_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)
        self.tree.selection_remove(self.tree.selection())

    def selecionar_item(self, event):
        selected = self.tree.focus()
        if selected:
            _, nome = self.tree.item(selected, "values")
            self.nome_entry.delete(0, tk.END)
            self.nome_entry.insert(0, nome)

# Aba de Disciplinas (usa combobox para selecionar professor pelo nome)
class DisciplinasTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Gerenciar Disciplinas", font=("Arial", 14)).pack(pady=5)
        
        search_frame = tk.Frame(self)
        search_frame.pack(pady=5)
        tk.Label(search_frame, text="Buscar Disciplina:").pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(search_frame, text="Buscar", command=self.buscar).pack(side=tk.LEFT, padx=5)
        
        input_frame = tk.Frame(self)
        input_frame.pack(pady=5)
        tk.Label(input_frame, text="Nome da Disciplina:").grid(row=0, column=0, padx=5, pady=5)
        self.nome_entry = tk.Entry(input_frame)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Professor:").grid(row=1, column=0, padx=5, pady=5)
        self.prof_combobox = ttk.Combobox(input_frame, state="readonly")
        self.prof_combobox.grid(row=1, column=1, padx=5, pady=5)
        self.atualizar_professores()  # Preenche a combobox com os nomes dos professores
        
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Adicionar", command=self.adicionar_disciplina).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Atualizar", command=self.atualizar_disciplina).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Deletar", command=self.deletar_disciplina).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Limpar", command=self.limpar_campos).grid(row=0, column=3, padx=5)
        
        self.tree = ttk.Treeview(self, columns=("id", "nome", "professor"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("professor", text="Professor")
        self.tree.column("id", width=50, anchor=tk.CENTER)
        self.tree.column("nome", width=150, anchor=tk.W)
        self.tree.column("professor", width=100, anchor=tk.CENTER)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=5)
        self.tree.bind("<<TreeviewSelect>>", self.selecionar_item)
        self.refresh_tree()

    def atualizar_professores(self):
        professors = listar_professores()
        self.prof_map = {prof[1]: prof[0] for prof in professors}
        self.prof_combobox['values'] = list(self.prof_map.keys())
        if self.prof_combobox['values']:
            self.prof_combobox.current(0)

    def refresh_tree(self):
        self.tree.delete(*self.tree.get_children())
        for disc in listar_disciplinas():
            # Exibe o nome do professor em vez do id
            prof_id = disc[2]
            professor_nome = next((p[1] for p in listar_professores() if p[0] == prof_id), "")
            self.tree.insert("", tk.END, values=(disc[0], disc[1], professor_nome))

    def buscar(self):
        termo = self.search_entry.get().strip()
        registros = buscar_disciplinas(termo) if termo else listar_disciplinas()
        self.tree.delete(*self.tree.get_children())
        for disc in registros:
            prof_id = disc[2]
            professor_nome = next((p[1] for p in listar_professores() if p[0] == prof_id), "")
            self.tree.insert("", tk.END, values=(disc[0], disc[1], professor_nome))

    def adicionar_disciplina(self):
        nome = self.nome_entry.get().strip()
        professor_nome = self.prof_combobox.get()
        if not nome or not professor_nome:
            messagebox.showwarning("Aviso", "Digite o nome da disciplina e selecione um professor")
            return
        professor_id = self.prof_map.get(professor_nome)
        if not professor_id:
            messagebox.showerror("Erro", "Professor selecionado não encontrado")
            return
        cadastrar_disciplina(nome, professor_id)
        messagebox.showinfo("Sucesso", "Disciplina adicionada com sucesso!")
        self.refresh_tree()
        self.limpar_campos()

    def atualizar_disciplina(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione uma disciplina para atualizar")
            return
        disc_id, _ , _ = self.tree.item(selected, "values")
        novo_nome = self.nome_entry.get().strip()
        professor_nome = self.prof_combobox.get()
        if not novo_nome or not professor_nome:
            messagebox.showwarning("Aviso", "Digite o novo nome e selecione um professor")
            return
        professor_id = self.prof_map.get(professor_nome)
        if not professor_id:
            messagebox.showerror("Erro", "Professor selecionado não encontrado")
            return
        atualizar_disciplina(disc_id, novo_nome, professor_id)
        messagebox.showinfo("Sucesso", "Disciplina atualizada com sucesso!")
        self.refresh_tree()
        self.limpar_campos()

    def deletar_disciplina(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione uma disciplina para deletar")
            return
        disc_id, _ , _ = self.tree.item(selected, "values")
        if messagebox.askyesno("Confirmar", "Tem certeza que deseja deletar esta disciplina?"):
            deletar_disciplina(disc_id)
            messagebox.showinfo("Sucesso", "Disciplina deletada com sucesso!")
            self.refresh_tree()
            self.limpar_campos()

    def limpar_campos(self):
        self.nome_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)
        self.prof_combobox.set('')
        self.atualizar_professores()
        self.tree.selection_remove(self.tree.selection())

    def selecionar_item(self, event):
        selected = self.tree.focus()
        if selected:
            disc_id, nome, professor_nome = self.tree.item(selected, "values")
            self.nome_entry.delete(0, tk.END)
            self.nome_entry.insert(0, nome)
            self.prof_combobox.set(professor_nome)

# Aba de Matrículas (usa comboboxes para selecionar aluno e disciplina pelo nome)
class MatriculasTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Gerenciar Matrículas", font=("Arial", 14)).pack(pady=5)
        
        search_frame = tk.Frame(self)
        search_frame.pack(pady=5)
        tk.Label(search_frame, text="Buscar Matrículas:").pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(search_frame, text="Buscar", command=self.buscar).pack(side=tk.LEFT, padx=5)
        
        assoc_frame = tk.Frame(self)
        assoc_frame.pack(pady=5)
        tk.Label(assoc_frame, text="Aluno:").grid(row=0, column=0, padx=5, pady=5)
        self.aluno_combobox = ttk.Combobox(assoc_frame, state="readonly")
        self.aluno_combobox.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(assoc_frame, text="Disciplina:").grid(row=1, column=0, padx=5, pady=5)
        self.disc_combobox = ttk.Combobox(assoc_frame, state="readonly")
        self.disc_combobox.grid(row=1, column=1, padx=5, pady=5)
        
        self.atualizar_alunos()
        self.atualizar_disciplinas()
        
        tk.Button(assoc_frame, text="Matricular", command=self.matricular).grid(row=2, column=0, columnspan=2, pady=5)
        
        self.tree = ttk.Treeview(self, columns=("aluno_id", "aluno", "disciplina_id", "disciplina"), show="headings")
        self.tree.heading("aluno_id", text="ID Aluno")
        self.tree.heading("aluno", text="Aluno")
        self.tree.heading("disciplina_id", text="ID Disciplina")
        self.tree.heading("disciplina", text="Disciplina")
        self.tree.column("aluno_id", width=80, anchor=tk.CENTER)
        self.tree.column("aluno", width=150, anchor=tk.W)
        self.tree.column("disciplina_id", width=80, anchor=tk.CENTER)
        self.tree.column("disciplina", width=150, anchor=tk.W)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=5)
        self.refresh_tree()

    def atualizar_alunos(self):
        alunos = listar_alunos()
        self.aluno_map = {aluno[1]: aluno[0] for aluno in alunos}
        self.aluno_combobox['values'] = list(self.aluno_map.keys())
        if self.aluno_combobox['values']:
            self.aluno_combobox.current(0)

    def atualizar_disciplinas(self):
        discs = listar_disciplinas()
        self.disc_map = {disc[1]: disc[0] for disc in discs}
        self.disc_combobox['values'] = list(self.disc_map.keys())
        if self.disc_combobox['values']:
            self.disc_combobox.current(0)

    def refresh_tree(self):
        self.tree.delete(*self.tree.get_children())
        for assoc in listar_matriculas():
            self.tree.insert("", tk.END, values=assoc)

    def buscar(self):
        termo = self.search_entry.get().strip()
        regs = buscar_matriculas(termo) if termo else listar_matriculas()
        self.tree.delete(*self.tree.get_children())
        for assoc in regs:
            self.tree.insert("", tk.END, values=assoc)

    def matricular(self):
        aluno_nome = self.aluno_combobox.get()
        disc_nome = self.disc_combobox.get()
        if not aluno_nome or not disc_nome:
            messagebox.showwarning("Aviso", "Selecione um aluno e uma disciplina")
            return
        aluno_id = self.aluno_map.get(aluno_nome)
        disc_id = self.disc_map.get(disc_nome)
        if not aluno_id or not disc_id:
            messagebox.showerror("Erro", "Aluno ou disciplina não encontrado")
            return
        try:
            matricular_aluno_disciplina(aluno_id, disc_id)
            messagebox.showinfo("Sucesso", "Matrícula realizada com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao matricular: {e}")
            return
        self.refresh_tree()
        self.search_entry.delete(0, tk.END)
        self.aluno_combobox.set('')
        self.disc_combobox.set('')
        self.atualizar_alunos()
        self.atualizar_disciplinas()

# --------------------------------------------------
# Janela Principal com Notebook
# --------------------------------------------------
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Escolar - CRUD, Busca e Matrículas")
        self.geometry("900x600")
        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True)
        
        alunos_tab = AlunosTab(notebook)
        professores_tab = ProfessoresTab(notebook)
        disciplinas_tab = DisciplinasTab(notebook)
        matriculas_tab = MatriculasTab(notebook)
        
        notebook.add(alunos_tab, text="Alunos")
        notebook.add(professores_tab, text="Professores")
        notebook.add(disciplinas_tab, text="Disciplinas")
        notebook.add(matriculas_tab, text="Matrículas")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
