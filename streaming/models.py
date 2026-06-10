from django.db import models

class Streaming(models.Model):
    nome = models.CharField(max_length=50) # Nome do serviço de streaming
    preco_total = models.DecimalField(max_digits=6, decimal_places=2) # Preço total do plano de streaming, posteriormente dividido pelos membros
    max_membros = models.PositiveIntegerField() # Número maximo de membros permitido em um mesmo plano de streaming
    descricao = models.TextField(blank=True) # Descrição (opcional) do serviço de streaming

    def preco_por_membro(self):
        return round(self.preco_total / self.participantes.count(), 2) # Calcula o valor arredondado que cada membro paga

    def preco_dono(self): # Resolve o dilema da divisão de valores, fazendo o dono do grupo assumir a diferença
        total = self.participantes.count()  # Quantia de participantes no grupo
        valor_membro = round(self.preco_total / total, 2)  # Valor arredondado de cada membro
        total_cobrado = valor_membro * (total - 1)  # Total pago pelos membros excluindo o dono
        return round(self.preco_total - total_cobrado, 2)  # Valor sobressalente pago pelo dono


    def __str__(self):
        return self.nome # Retorna o nome do serviço de streaming quando objeto for chamado na interface ref.(Django streaming 01)