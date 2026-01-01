```python
# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 OntoCoder Collective

from abc import ABC, abstractmethod
from typing import Any, Optional, Dict

class BaseIngress(ABC):
    """
    Abstract base for all ingress parsers.
    Each ingress must return a structured dict or None.
    No semantic interpretation is allowed at this stage.
    """

    @abstractmethod
    def parse(self, raw: Any) -> Optional[Dict[str, Any]]:
        """
        Parse raw input into a normalized dictionary.

        Must include:
          - 'type': str (e.g., 'json_query', 'websocket_event', 'binary_blob')
          - 'content': original or minimally structured payload

        Returns None if format is unsupported.
        """
        pass
```
