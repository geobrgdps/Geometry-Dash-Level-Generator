from backend.src.models.level import GDLevel, GDObject, LevelMeta


class GameplayEngine:
    """
    Engine responsável por gerar layouts básicos de gameplay (blocos e espinhos).
    """

    # Constantes do Geometry Dash (cada bloco mede 30x30 unidades no grid)
    GRID_SIZE = 30.0

    # IDs de objetos padrão do Geometry Dash
    ID_BLOCK = 1
    ID_SPIKE = 8

    @classmethod
    def generate_layout(cls, meta: LevelMeta, length_blocks: int = 20) -> GDLevel:
        """
        Gera um nível simples contendo um chão de blocos e espinhos espaçados.
        """
        level = GDLevel(meta=meta)

        for i in range(length_blocks):
            x_pos = i * cls.GRID_SIZE
            y_pos = 0.0  # Nível do chão

            # Adiciona o bloco do chão
            floor_block = GDObject(
                object_id=cls.ID_BLOCK,
                x=x_pos,
                y=y_pos
            )
            level.add_object(floor_block)

            # Adiciona um espinho a cada 4 blocos (exceto no início)
            if i > 3 and i % 4 == 0:
                spike = GDObject(
                    object_id=cls.ID_SPIKE,
                    x=x_pos,
                    y=y_pos + cls.GRID_SIZE
                )
                level.add_object(spike)

        return level
      
