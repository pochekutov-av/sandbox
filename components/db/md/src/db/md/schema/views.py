from dataclasses import dataclass, field


@dataclass
class View:
    """Класс для описания представляние (view) в базе данных."""
    name: str
    schema: str = 'md'
    order_by: list = field(default_factory=lambda: ['id'])


v_db_server_types = View(name='v_db_server_types')
