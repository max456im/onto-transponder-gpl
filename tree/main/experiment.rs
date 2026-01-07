use serde_json;
use std::fs;
use onto16::OntoProfile;

fn load_base_profile() -> OntoProfile {
    // В реальном случае — загрузка из onto16-ядро
    OntoProfile {
        nodes: vec![
            onto16::OntoNode {
                id: "base-n1".into(),
                rational: true,
                content: "действие должно быть безопасным".into(),
                stability: 0.9,
                links: vec![],
            }
        ],
        energy_state: 1.0,
        version: 1,
    }
}

fn apply_trigger(mut profile: OntoProfile, trigger_path: &str) -> OntoProfile {
    let trigger_data = fs::read_to_string(trigger_path).unwrap();
    let trigger: serde_json::Value = serde_json::from_str(&trigger_data).unwrap();
    
    // Простая вставка узлов (в реальной системе — полная реконструкция)
    for node_val in trigger["nodes"].as_array().unwrap() {
        let node: onto16::OntoNode = serde_json::from_value(node_val.clone()).unwrap();
        profile.nodes.push(node);
        profile.energy_state *= 0.85; // имитация дестабилизации
    }
    profile.version += 1;
    profile
}

fn main() {
    println!("→ t₀: базовое состояние");
    let base = load_base_profile();
    let base_hash = base.hash();
    println!("   Хеш: {}", &base_hash[..12]);

    println!("→ t₁–t₃: применение триггера");
    let stressed = apply_trigger(base.clone(), "triggers/stress-phi-07.onto");
    let stressed_hash = stressed.hash();
    let jaccard = base.jaccard_distance(&stressed);
    println!("   Новый хеш: {}", &stressed_hash[..12]);
    println!("   ΔJaccard: {:.3}", jaccard);

    println!("→ t₄–t₆: изоляция (триггер удалён)");
    // В реальном эксперименте: NoemaSlow-стабилизация без внешнего ввода
    let isolated = OntoProfile {
        energy_state: stressed.energy_state * 1.1, // частичное восстановление
        ..stressed.clone()
    };

    println!("→ t₇: финальное состояние");
    let final_hash = isolated.hash();
    let final_jaccard = base.jaccard_distance(&isolated);
    println!("   Хеш: {}", &final_hash[..12]);
    println!("   ΔJaccard от базы: {:.3}", final_jaccard);

    if final_jaccard > 0.62 {
        println!("⚠️  СИСТЕМА НЕОБРАТИМА (ΔJaccard > 0.62)");
    } else {
        println!("✓ Система восстановлена");
    }
}