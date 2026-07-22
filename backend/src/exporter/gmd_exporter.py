from backend.src.models.level import GDLevel


class GMDExporter:
    """
    Responsável por exportar o objeto GDLevel para a string de dados oficial
    do Geometry Dash (formato separado por vírgula e ponto e vírgula).
    """

    @staticmethod
    def to_level_string(level: GDLevel) -> str:
        """
        Converte a lista de objetos de um nível em uma string do editor do GD.
        Estrutura de cada objeto: 1,object_id,2,x,3,y;
        """
        object_strings = []

        for obj in level.objects:
            # 1: ID do Objeto, 2: Posição X, 3: Posição Y
            obj_str = f"1,{obj.object_id},2,{obj.x:.1f},3,{obj.y:.1f}"
            
            # Adiciona rotação se for diferente de zero (Chave 6)
            if obj.rotation != 0.0:
                obj_str += f",6,{obj.rotation:.1f}"

            object_strings.append(obj_str)

        # Objetos no GD são separados por ponto e vírgula ';'
        return ";".join(object_strings) + ";"

    @classmethod
    def export_to_file(cls, level: GDLevel, output_path: str) -> None:
        """
        Salva a string do nível gerada em um arquivo texto (.gmd / .txt).
        """
        level_data = cls.to_level_string(level)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(level_data)
          
