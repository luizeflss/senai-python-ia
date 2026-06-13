import sqlite3
from agno.agent import Agent
from agno.models.openai import OpenAIChat

API_KEY = "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"
DB_FILE = "tarefas.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("CREATE TABLE IF NOT EXISTS tarefas (id INTEGER PRIMARY KEY AUTOINCREMENT, descricao TEXT NOT NULL, status TEXT DEFAULT 'pendente')")
    conn.commit()
    conn.close()

def adicionar_tarefa(descricao: str) -> str:
    """Adiciona uma nova tarefa."""
    conn = sqlite3.connect(DB_FILE)
    conn.execute("INSERT INTO tarefas (descricao) VALUES (?)", (descricao,))
    conn.commit()
    conn.close()
    return f"✅ Tarefa adicionada: '{descricao}'"

def listar_tarefas() -> str:
    """Lista todas as tarefas."""
    conn = sqlite3.connect(DB_FILE)
    rows = conn.execute("SELECT id, descricao, status FROM tarefas").fetchall()
    conn.close()
    if not rows:
        return "📋 Nenhuma tarefa cadastrada."
    return "\n".join([f"[{r[0]}] {r[1]} — {r[2]}" for r in rows])

def concluir_tarefa(id_tarefa: int) -> str:
    """Marca uma tarefa como concluída pelo ID."""
    conn = sqlite3.connect(DB_FILE)
    cur = conn.execute("UPDATE tarefas SET status='concluída' WHERE id=?", (id_tarefa,))
    conn.commit()
    conn.close()
    return f"✅ Tarefa #{id_tarefa} concluída." if cur.rowcount else f"❌ ID {id_tarefa} não encontrado."

def remover_tarefa(id_tarefa: int) -> str:
    """Remove uma tarefa pelo ID."""
    conn = sqlite3.connect(DB_FILE)
    cur = conn.execute("DELETE FROM tarefas WHERE id=?", (id_tarefa,))
    conn.commit()
    conn.close()
    return f"🗑️ Tarefa #{id_tarefa} removida." if cur.rowcount else f"❌ ID {id_tarefa} não encontrado."

init_db()

# Carrega tarefas existentes e injeta no contexto do agente
tarefas_atuais = listar_tarefas()

API_KEY = os.getenv("API_KEY")
agent = Agent(
    model=OpenAIChat(
        id="meta/llama-3.1-8b-instruct",
        api_key=API_KEY,
        base_url="https://integrate.api.nvidia.com/v1",
        instructions=contexto
    ),
    instructions=f"""Você é um gerenciador de tarefas com memória persistente.
As tarefas abaixo já existiam do banco de dados de sessões anteriores:

{tarefas_atuais}

Use sempre as ferramentas disponíveis para adicionar, listar, concluir ou remover tarefas.
Quando o usuário perguntar o que tem salvo, use listar_tarefas para mostrar o estado atual.""",
    markdown=True
)

print("🤖 Gerenciador de Tarefas (digite 'sair' para encerrar)\n")

while True:
    entrada = input("Você: ").strip()
    if entrada.lower() == "sair":
        break
    agent.print_response(entrada, stream=True)
    print()