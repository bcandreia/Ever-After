import Foundation

struct Guest: Identifiable, Codable {
    let id: UUID
    var name: String
    var rsvp: Bool
}
