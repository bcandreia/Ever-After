import Foundation

struct PlannerTask: Identifiable, Codable {
    let id: UUID
    var title: String
    var isCompleted: Bool
}
