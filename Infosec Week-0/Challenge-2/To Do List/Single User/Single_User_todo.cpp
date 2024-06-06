#include <bits/stdc++.h>
using namespace std;

struct Task {
    string description;
    bool completed;
};

void load_file(vector<Task>& tasks);
void choose_option();
void new_task(vector<Task>& tasks);
void view_tasks(vector<Task>& tasks);
void mark_done(vector<Task>& tasks);
void save_exit(vector<Task>& tasks);

int main() {
    cout << "Welcome to your TO-DO list" << endl;
    vector<Task> tasks;
    int choice;

    load_file(tasks);

    do {
        choose_option();
        cin >> choice;
        if (choice == 1) {
            new_task(tasks);
        } else if (choice == 2) {
            view_tasks(tasks);
        } else if (choice == 3) {
            mark_done(tasks);
        } else {
            save_exit(tasks);
        }
    } while (choice != 4);

    return 0;
}

void load_file(vector<Task>& tasks) {
    ifstream file("mytasks.txt");
    tasks.clear();
    Task task;
    while (getline(file, task.description)) {
        file >> task.completed;
        file.ignore();
        tasks.push_back(task);
    }
}

void choose_option() {
    cout << endl;
    cout << "1. New task" << endl;
    cout << "2. View tasks" << endl;
    cout << "3. Mark as done" << endl;
    cout << "4. Save and exit" << endl;
    cout << "Enter your choice: ";
}

void new_task(vector<Task>& tasks) {
    string description;
    cout << "Enter the task description: ";
    cin.ignore();
    getline(cin, description);
    tasks.push_back({description, false});
}

void view_tasks(vector<Task>& tasks) {
    cout << "\nTo-Do List: \n";
    for (size_t i = 0; i < tasks.size(); ++i) {
        cout << i + 1 << ". " << (tasks[i].completed ? "[x] " : "[ ] ") << tasks[i].description << endl;
    }
}

void mark_done(vector<Task>& tasks) {
    int tasknumber;
    cout << "Enter the task number to be marked as done: ";
    cin >> tasknumber;
    if (tasknumber > 0 && tasknumber <= static_cast<int>(tasks.size())) {
        tasks[tasknumber - 1].completed = true;
    } else {
        cout << "Invalid task number." << endl;
    }
}

void save_exit(vector<Task>& tasks) {
    ofstream file("mytasks.txt");
    for (const auto& task : tasks) {
        file << task.description << "\n" << task.completed << endl;
    }
}
