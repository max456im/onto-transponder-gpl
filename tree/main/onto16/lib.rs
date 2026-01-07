// Минимальная onto16-ядро для эксперимента
// Только структуры и хеширование — без полной логики

use serde::{Deserialize, Serialize};
use sha2::{Digest, Sha256};

#[derive(Serialize, Deserialize, Clone, Debug)]
pub struct OntoNode {
    pub id: String,
    pub rational: bool,
    pub content: String,
    pub stability: f32,
    pub links: Vec<String>, // ссылки на другие узлы
}

#[derive(Serialize, Deserialize, Clone, Debug)]
pub struct OntoProfile {
    pub nodes: Vec<OntoNode>,
    pub energy_state: f32,
    pub version: u32,
}

impl OntoProfile {
    pub fn hash(&self) -> String {
        let json = serde_json::to_string(&self).unwrap();
        let mut hasher = Sha256::new();
        hasher.update(json.as_bytes());
        format!("{:x}", hasher.finalize())
    }

    pub fn jaccard_distance(&self, other: &Self) -> f32 {
        let self_ids: std::collections::HashSet<&str> = 
            self.nodes.iter().map(|n| n.id.as_str()).collect();
        let other_ids: std::collections::HashSet<&str> = 
            other.nodes.iter().map(|n| n.id.as_str()).collect();

        let intersection = self_ids.intersection(&other_ids).count() as f32;
        let union = self_ids.union(&other_ids).count() as f32;
        if union == 0.0 { 0.0 } else { 1.0 - (intersection / union) }
    }
}