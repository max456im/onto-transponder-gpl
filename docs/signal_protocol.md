# Signal Protocol (NoemaFast Input Interface)

## Обзор

Протокол входных сигналов **NoemaFast** определяет формат, семантику и правила валидации внешних стимулов, поступающих в транспондер на этапе **быстрого внимания** (prospective thinking). Эти сигналы инициируют обработку в режиме **NoemaFast → NoemaSlow** (для меланхолика) или **NoemaSlow → NoemaFast** (для сангвиника/холерика), в зависимости от привязанной темпераментной архитектуры.

Сигналы **не содержат биометрических или персональных данных пользователя**. Вместо этого они выражают **факты активности**, **онтологические события** или **контекстуальные маркеры**, закодированные в соответствии со спецификацией `signal-schema.json`.

---

## Структура сигнала

Каждый входной сигнал — это JSON-объект, соответствующий следующей схеме:

```json
{
  "signal_id": "urn:onto:sig:2026:abc123",
  "timestamp": "2026-01-05T14:30:00Z",
  "source": "onto-emitter/medical/v1",
  "context_class": "medical_diagnosis",
  "ontic_facts": [
    { "predicate": "has_symptom", "object": "fever_39C" },
    { "predicate": "reported_by", "object": "triage_agent_alpha" }
  ],
  "stakes_level": "high", // low | medium | high
  "vma_signature": "..." // опционально, обязательно при stakes_level = high
}
```

### Поля

| Поле | Тип | Обязательность | Описание |
|------|-----|----------------|----------|
| `signal_id` | URI (URN) | Да | Уникальный идентификатор сигнала в пространстве onto-событий. |
| `timestamp` | ISO 8601 UTC | Да | Момент генерации сигнала. |
| `source` | строка | Да | Источник в формате `domain/subsystem/version`. |
| `context_class` | строка | Да | Онтологический класс контекста (например, `medical_diagnosis`, `game_event`, `social_interaction`). |
| `ontic_facts` | массив | Да | Набор предикатно-объектных пар, выражающих факты без субъектной привязки. |
| `stakes_level` | enum | Да | Уровень этической значимости: `low`, `medium`, `high`. |
| `vma_signature` | строка (base64) | Условно | Обязателен при `stakes_level = high`; подпись, подтверждённая через VMA-модуль. |

---

## Правила обработки

1. **Валидация**  
   Все сигналы проходят строгую проверку через `signal_validator.py` против `signal-schema.json`. Невалидные сигналы отбрасываются без логирования содержимого (только ID и статус ошибки).

2. **Темпераментный маршрутизатор**  
   После валидации сигнал передаётся в архитектурный модуль (`onto_richness.py` или `behav_mod.py`), выбранный на основе профиля из `onto144_connector.py`.

3. **VMA Enforcement**  
   При `stakes_level = high` отсутствие корректной `vma_signature` приводит к **автоматическому отклонению сигнала** и генерации внутреннего алерта (без внешнего уведомления).

4. **Отсутствие субъекта**  
   Сигналы **не содержат `user_id`, `device_fingerprint` или `location`**. Вся персонализация происходит через связывание с профилем `onto144` **внутри транспондера**, а не через входные данные.

---

## Примеры

### Низкий уровень (игровой контекст)
```json
{
  "signal_id": "urn:onto:sig:2026:g789",
  "timestamp": "2026-01-05T14:35:22Z",
  "source": "onto-emitter/gaming/v2",
  "context_class": "player_action",
  "ontic_facts": [
    { "predicate": "performed_action", "object": "cast_spell_fireball" },
    { "predicate": "within_zone", "object": "arena_north" }
  ],
  "stakes_level": "low"
}
```

### Высокий уровень (медицинский контекст)
```json
{
  "signal_id": "urn:onto:sig:2026:m456",
  "timestamp": "2026-01-05T14:40:11Z",
  "source": "onto-emitter/clinical/v1",
  "context_class": "treatment_recommendation",
  "ontic_facts": [
    { "predicate": "recommends_procedure", "object": "emergency_splenectomy" },
    { "predicate": "contraindicated_with", "object": "allergy_penicillin" }
  ],
  "stakes_level": "high",
  "vma_signature": "MEUCIQD...ABc="
}
```

---

## Примечания по безопасности

- Все сигналы принимаются **только через зашифрованные каналы** (TLS 1.3+ или эквивалент в onto-инфраструктуре).
- Повторная отправка сигнала с тем же `signal_id` игнорируется (идемпотентность).
- Сигналы с `stakes_level = high` логируются только в зашифрованном виде и доступны только модулям с VMA-доступом.

> **Философский принцип**: Сигнал — это онтологическое событие, а не отражение пользователя. Транспондер реагирует на **структуру мира**, а не на **идентичность наблюдателя**.

--- 

*См. также: `emission_protocol.md` (выходной формат onto16r), `transponder_architecture.md` (режимы обработки).*