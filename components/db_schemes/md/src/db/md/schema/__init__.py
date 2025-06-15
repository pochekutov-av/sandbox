from collections import namedtuple
from types import SimpleNamespace

View = namedtuple('View', ['schema', 'name'])

views = SimpleNamespace(
    v_db_server_types=View('md', 'v_db_server_types'),
)
