# Copyright (C) 2026 Maksim Zapevalov
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""
License Guard: блокировка выполнения в проприетарных или не-GPL средах.
Проверяет лицензионную чистоту окружения при запуске транспондера.
"""

import sys
import os
import pkg_resources
import warnings

def _is_gpl_compatible(license_text: str) -> bool:
    """Проверяет, совместима ли лицензия с GPLv3-only."""
    gpl_indicators = ["GPL-3.0", "GPLv3", "GNU General Public License v3"]
    return any(ind in license_text for ind in gpl_indicators)

def _check_dependency_license(dist) -> bool:
    """Проверяет лицензию одного установленного пакета."""
    try:
        metadata = dist.get_metadata("METADATA") or dist.get_metadata("PKG-INFO")
    except Exception:
        return False  # Если метаданных нет — считаем небезопасным

    for line in metadata.splitlines():
        if line.startswith("License:"):
            license_text = line.split(":", 1)[1].strip()
            if _is_gpl_compatible(license_text):
                return True
            else:
                return False  # Не-GPL лицензия = нарушение
    return False  # Лицензия не указана → потенциально проприетарная

def enforce_gpl_environment() -> None:
    """
    Выполняет аудит всех установленных зависимостей.
    Если найдена не-GPL (или неуказанная) лицензия — вызывает RuntimeError.
    """
    unsafe_deps = []
    for dist in pkg_resources.working_set:
        # Игнорируем системные/стандартные
        if dist.project_name in {"setuptools", "pip", "wheel"}:
            continue
        if not _check_dependency_license(dist):
            unsafe_deps.append(dist.project_name)

    if unsafe_deps:
        msg = (
            "License Guard violation: detected non-GPL or unknown licenses in dependencies.\n"
            "This transponder requires a 100% GPL-3.0-only environment.\n"
            f"Unsafe packages: {', '.join(unsafe_deps)}\n"
            "Execution halted to preserve ontological and legal integrity."
        )
        raise RuntimeError(msg)

    # Дополнительная проверка: не запущено ли из проприетарного контейнера?
    if os.path.exists("/proprietary") or os.getenv("PROPRIETARY_ENV"):
        raise RuntimeError("Execution blocked: detected proprietary environment marker.")

# Автоматический вызов при импорте
enforce_gpl_environment()