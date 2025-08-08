import SwiftUI

struct TasksView: View {
    @State private var tasks: [PlannerTask] = [
        PlannerTask(id: UUID(), title: "Book Venue", isCompleted: false),
        PlannerTask(id: UUID(), title: "Send Invitations", isCompleted: false)
    ]
    @State private var newTaskTitle: String = ""

    var body: some View {
        VStack {
            List {
                ForEach($tasks) { $task in
                    HStack {
                        Text(task.title)
                        Spacer()
                        Button(action: { task.isCompleted.toggle() }) {
                            Image(systemName: task.isCompleted ? "checkmark.square" : "square")
                                .foregroundColor(task.isCompleted ? .green : .primary)
                        }
                    }
                }
                .onDelete { indexSet in
                    tasks.remove(atOffsets: indexSet)
                }
            }
            HStack {
                TextField("New Task", text: $newTaskTitle)
                Button("Add") {
                    guard !newTaskTitle.isEmpty else { return }
                    tasks.append(PlannerTask(id: UUID(), title: newTaskTitle, isCompleted: false))
                    newTaskTitle = ""
                }
            }
            .padding()
        }
        .navigationTitle("Tasks")
    }
}
