import SwiftUI

struct DashboardView: View {
    var body: some View {
        NavigationView {
            List {
                NavigationLink(destination: GuestListView()) {
                    Label("Guest List", systemImage: "person.3")
                }
                NavigationLink(destination: TasksView()) {
                    Label("Tasks", systemImage: "checkmark.circle")
                }
                NavigationLink(destination: BudgetView()) {
                    Label("Budget", systemImage: "dollarsign.circle")
                }
            }
            .navigationTitle("Wedding Planner")
        }
    }
}
