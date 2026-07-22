from backend.src.parser.prompt_parser import PromptParser
from backend.src.engine.gameplay_engine import GameplayEngine
from backend.src.exporter.gmd_exporter import GMDExporter


def generate_level_from_prompt(prompt: str, length_blocks: int = 30) -> str:
    """
    Função principal que orquestra todo o fluxo do GDL:
    Prompt -> Metadata -> Gameplay Layout -> Geometry Dash String.
    """
    # 1. Interpreta o texto fornecido
    meta = PromptParser.parse(prompt)
    
    # 2. Gera a estrutura de gameplay (blocos e espinhos)
    level = GameplayEngine.generate_layout(meta, length_blocks=length_blocks)
    
    # 3. Converte a estrutura para o formato nativo do GD
    level_string = GMDExporter.to_level_string(level)
    
    return level_string


if __name__ == "__main__":
    # Teste de execução direta do pipeline
    prompt_exemplo = "Crie uma fase Demon inspirada em Nine Circles com velocidade 2x"
    
    print("=== PROJETO GDL (Geometry Dash Level Generator) ===")
    print(f"Prompt de entrada: '{prompt_exemplo}'\n")
    
    resultado = generate_level_from_prompt(prompt_exemplo, length_blocks=10)
    
    print("Resultado da geração (String GD):")
    print(resultado)
    print("\n✓ Pipeline do backend executado com sucesso!")
  
