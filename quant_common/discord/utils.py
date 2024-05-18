import json
from typing import List, Dict, Optional, Any


def format_data(data: dict) -> List[Dict[str, Optional[Any]]]:
    return [*map(lambda x: {"name": x, "value": f"```json\n{json.dumps(data[x], indent=4, ensure_ascii=False)}\n```"},
                 data)]
