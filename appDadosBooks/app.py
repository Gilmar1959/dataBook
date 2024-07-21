from avaliacoes_books import lista_comentarios_clientes
from analise_sentimento import analise_sentimento

for texto in lista_comentarios_clientes:
    sent_comments = analise_sentimento(texto)
    print(f"O comentário: '{texto}' tem o seguinte sentimento: {sent_comments}")