import SwiftUI

struct GuestListView: View {
    @State private var guests: [Guest] = [
        Guest(id: UUID(), name: "Alice", rsvp: true),
        Guest(id: UUID(), name: "Bob", rsvp: false)
    ]
    @State private var newGuestName: String = ""

    var body: some View {
        VStack {
            List {
                ForEach(guests) { guest in
                    HStack {
                        Text(guest.name)
                        Spacer()
                        Image(systemName: guest.rsvp ? "checkmark.circle" : "xmark.circle")
                            .foregroundColor(guest.rsvp ? .green : .red)
                    }
                }
            }
            HStack {
                TextField("New Guest Name", text: $newGuestName)
                Button("Add") {
                    guard !newGuestName.isEmpty else { return }
                    guests.append(Guest(id: UUID(), name: newGuestName, rsvp: false))
                    newGuestName = ""
                }
            }
            .padding()
        }
        .navigationTitle("Guest List")
    }
}
