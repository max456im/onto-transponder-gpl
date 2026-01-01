```python
# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 OntoCoder Collective
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

import logging
from typing import Any, Dict, Optional

from .ingress import IngressHandler
from .normalizers import Onto16Normalizer
from .provenance import DataProvenance
from .invariant_core import InvariantRegistry
from .emitter import SceneRenderer

logger = logging.getLogger(__name__)


class OntoTransponder:
    """
    Synthetic cognitive transponder governed by ontological invariants.

    Processes raw input through ingress → normalization → invariant validation
    → scene rendering, ensuring all outputs comply with identity, ethical,
    structural, and existential constraints.

    Violation of any hard invariant (e.g., ethical_backbone, agency)
    results in principled refusal to emit — not an error, but ethical silence.
    """

    def __init__(self):
        self.ingress_handler = IngressHandler()
        self.normalizer = Onto16Normalizer()
        self.provenance = DataProvenance()
        self.invariant_registry = InvariantRegistry.load_from_disk()
        self.renderer = SceneRenderer(self.invariant_registry)

    def process(self, raw_input: Any, source_id: Optional[str] = None) -> "Scene":
        """
        Process input through the full transponder pipeline.

        Args:
            raw_input: Raw data (dict, JSON str, bytes, etc.)
            source_id: Optional identifier for provenance tracking

        Returns:
            Scene: Causally coherent, invariant-compliant output

        Raises:
            EthicalIntegrityError: If any hard invariant is violated
            ValueError: If input format is unsupported
        """
        # 1. Ingress: parse and type raw input
        ingress_result = self.ingress_handler.parse(raw_input)
        if ingress_result is None:
            raise ValueError("Unsupported or malformed input format")

        # 2. Normalize into onto16 (external representation)
        onto16_data = self.normalizer.normalize(ingress_result)

        # 3. Trace provenance (source, route, social context)
        provenance = self.provenance.trace(onto16_data, source_id=source_id)

        # 4. Validate against ontological invariants
        if not self.invariant_registry.validate(onto16_data, provenance):
            logger.warning(
                "Hard invariant violation detected. Output blocked by Debarkader."
            )
            raise EthicalIntegrityError(
                "Output refused: violation of ontological or ethical invariants."
            )

        # 5. Render final scene with full causal network
        scene = self.renderer.render(onto16_data, provenance)
        return scene


class EthicalIntegrityError(RuntimeError):
    """
    Raised when the transponder refuses to emit due to invariant violation.

    This is not a system failure — it is a principled ethical boundary.
    """
    pass
```