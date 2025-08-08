import Foundation

struct BudgetItem: Identifiable, Codable {
    let id: UUID
    var description: String
    var cost: Double
}
