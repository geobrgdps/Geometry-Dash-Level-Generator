from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class GDObject:
    """
    Representa um único objeto dentro do editor do Geometry Dash.
    ID 1 = Bloco Básico, ID 2 = Espinho Básico, etc.
    """
    object_id: int
    x: float
    y: float
    rotation: float = 0.0
    flip_x: bool = False
    flip_y: bool = False
    group_id: Optional[int] = None


@dataclass
class LevelMeta:
    """
    Guarda os metadados do nível solicitados no Prompt ou Interface.
    """
    name: str = "GDL Generated Level"
    description: str = "Created with Geometry Dash Level Generator"
    artist: str = "Unknown"
    song_id: int = 0
    difficulty: str = "Auto"
    speed: int = 1  # 1x, 2x, 3x, 4x


@dataclass
class GDLevel:
    """
    Representa a estrutura completa do nível antes de ser convertida para .gmd
    """
    meta: LevelMeta = field(default_factory=LevelMeta)
    objects: List[GDObject] = field(default_factory=list)

    def add_object(self, obj: GDObject) -> None:
        """Adiciona um novo objeto à lista do nível."""
        self.objects.append(obj)

    def count_objects(self) -> int:
        """Retorna a quantidade total de objetos inseridos."""
        return len(self.objects)
      
