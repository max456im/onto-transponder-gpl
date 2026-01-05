# hardware_probe.py
# Автоопределение режима работы на основе среды выполнения.
# Сохраняет приоритет onto144-профиля; использует hardware только при его отсутствии.

import os
import platform
import sys

def detect_execution_environment() -> str:
    """
    Определяет тип среды:
    - 'mobile' (Android, iOS через утилиты)
    - 'desktop'
    - 'server'
    - 'embedded'
    """
    system = platform.system().lower()
    if system == "linux":
        # Проверка на Android
        if "ANDROID_ARGUMENT" in os.environ or "ANDROID_DATA" in os.environ:
            return "mobile"
        # Проверка на embedded (например, Raspberry Pi)
        if os.path.exists("/proc/cpuinfo") and "raspberrypi" in open("/proc/cpuinfo").read().lower():
            return "embedded"
        return "server" if "SERVER" in os.environ else "desktop"
    elif system == "darwin":
        # iOS (в Python-среде редко, но если через Pyto и т.п.)
        if "IOS" in os.environ or "IPHONEOS_DEPLOYMENT_TARGET" in os.environ:
            return "mobile"
        return "desktop"
    elif system == "windows":
        return "desktop"
    else:
        return "unknown"

def infer_preferred_architecture_from_hardware() -> str:
    """
    Возвращает рекомендуемую архитектуру на основе среды:
    - mobile/embedded → behav_mod (реактивный, для сангвиника/холерика)
    - desktop/server → onto_richness (рефлексивный, для меланхолика)
    """
    env = detect_execution_environment()
    if env in ("mobile", "embedded"):
        return "behav_mod"
    else:
        return "onto_richness"

def should_use_hardware_hint(profile_arch: str = None) -> str:
    """
    Возвращает архитектуру:
    - если задан profile_arch → использовать его (приоритет onto144)
    - иначе → инференс из hardware
    """
    if profile_arch in ("behav_mod", "onto_richness"):
        return profile_arch
    return infer_preferred_architecture_from_hardware()