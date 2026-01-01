```python
# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 OntoCoder Collective

from typing import Any, Optional, Dict
from .base import BaseIngress

class BinaryIngress(BaseIngress):
    """
    Fallback for raw bytes.
    Intended for future protobuf/msgpack/encrypted streams.
    Currently captures only size and type.
    """

    def parse(self, raw: Any) -> Optional[Dict[str, Any]]:
        if isinstance(raw, bytes):
            return {
                "type": "binary_blob",
                "content": {
                    "size_bytes": len(raw),
                    "sample_prefix": raw[:16].hex(),  # First 16 bytes as hex
                },
            }
        return None
```