# app/populate.py
from .database import SessionLocal
from .models import Message

frases = [
    "Acredite no seu potencial e vá além.",
    "Grandes jornadas começam com um pequeno passo.",
    "Você é mais forte do que imagina.",
    "O sucesso é a soma de pequenos esforços diários.",
    "Persista, porque grandes conquistas levam tempo.",
    "Confie em si mesmo e tudo será possível.",
    "Desafios existem para serem superados.",
    "Cada dia é uma nova oportunidade de recomeçar.",
    "A disciplina é a ponte entre metas e realizações.",
    "Você é capaz de mais do que sonha.",
    "Sonhar grande e sonhar pequeno dá o mesmo trabalho.",
    "A ação é a chave fundamental para todo sucesso.",
    "Transforme obstáculos em degraus para a vitória.",
    "Acredite: seu esforço será recompensado.",
    "Nenhum sonho é grande demais para quem acredita.",
    "Paciência e persistência são irmãs do sucesso.",
    "A única maneira de vencer é nunca desistir.",
    "Mantenha o foco, a força e a fé.",
    "Coragem é agir mesmo com medo.",
    "Seja hoje melhor do que ontem.",
    "Tudo o que você precisa já está dentro de você.",
    "Grandes sonhos exigem grandes esforços.",
    "Falhar é parte do caminho para o sucesso.",
    "Quem acredita sempre alcança.",
    "Nunca é tarde para começar.",
    "Pequenas ações diárias constroem grandes vitórias.",
    "Permaneça firme. Grandes coisas levam tempo.",
    "A mente é o limite: vá além.",
    "Acredite no processo e continue andando.",
    "Você é a única pessoa que pode mudar sua história.",
    "Gratidão transforma o que temos em suficiente."
]

def popular_banco():
    db = SessionLocal()
    try:
        for frase in frases:
            nova_mensagem = Message(text=frase)
            db.add(nova_mensagem)
        db.commit()
        print("✅ Banco populado com 31 mensagens motivacionais!")
    except Exception as e:
        print("Erro ao popular banco:", e)
    finally:
        db.close()

if __name__ == "__main__":
    popular_banco()
