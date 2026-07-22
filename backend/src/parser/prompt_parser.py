import re
from backend.src.models.level import LevelMeta


class PromptParser:
    """
    Parser baseado em regras textuais para extrair metadados do nível.
    No futuro, este módulo receberá integração com IA avançada.
    """

    @staticmethod
    def parse(prompt: str) -> LevelMeta:
        meta = LevelMeta()
        
        # Normaliza o texto para minúsculas para facilitar a busca de termos
        text = prompt.lower()
        
        # Identifica a dificuldade com base em palavras-chave
        if "demon" in text:
            meta.difficulty = "Demon"
        elif "harder" in text:
            meta.difficulty = "Harder"
        elif "insane" in text:
            meta.difficulty = "Insane"
        elif "easy" in text:
            meta.difficulty = "Easy"
        elif "normal" in text:
            meta.difficulty = "Normal"
        elif "hard" in text:
            meta.difficulty = "Hard"

        # Extrai a velocidade caso o usuário especifique (ex: 2x, 3x)
        speed_match = re.search(r'(\d)x', text)
        if speed_match:
            meta.speed = int(speed_match.group(1))

        # Atribui uma versão inicial limpa do prompt como o nome do nível
        meta.name = prompt[:30].strip().title()

        return meta
      
