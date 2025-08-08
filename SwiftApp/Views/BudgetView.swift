import SwiftUI

struct BudgetView: View {
    @State private var items: [BudgetItem] = [
        BudgetItem(id: UUID(), description: "Venue", cost: 2000),
        BudgetItem(id: UUID(), description: "Catering", cost: 3500)
    ]
    @State private var newDescription = ""
    @State private var newCost = ""

    var totalCost: Double {
        items.reduce(0.0) { $0 + $1.cost }
    }

    var body: some View {
        VStack {
            List {
                ForEach(items) { item in
                    HStack {
                        Text(item.description)
                        Spacer()
                        Text("$\(item.cost, specifier: \"%.2f\")")
                    }
                }
                .onDelete { indexSet in
                    items.remove(atOffsets: indexSet)
                }
            }
            HStack {
                TextField("Description", text: $newDescription)
                TextField("Cost", text: $newCost)
                    .keyboardType(.decimalPad)
                Button("Add") {
                    guard let cost = Double(newCost), !newDescription.isEmpty else { return }
                    items.append(BudgetItem(id: UUID(), description: newDescription, cost: cost))
                    newDescription = ""
                    newCost = ""
                }
            }
            .padding()
            Text("Total: $\(totalCost, specifier: \"%.2f\")")
                .bold()
                .padding(.top)
        }
        .navigationTitle("Budget")
    }
}
