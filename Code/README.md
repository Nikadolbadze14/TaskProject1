# task project

## klass: User

- `first_name`: მომხმარებლის სახელი
- `last_name`: მომხმარებლის გვარი
- `email`: მომხმარებლის ელ-ფოსტა
- `tasks`: დავალებების სია, რომლებიც მინიჭებულია ამ მომხმარებელზე
- `assign_task(task)`: ამატებს დავალებას მომხმარებელზე
- `unassign_task(task)`: აშორებს დავალებას მომხმარებლისგან

## class: Task

- `title`: დავალებს სახელი
- `priority`: პრიორიტეტი (მაგ. High, Medium, Low)
- `status`: სტათუსი ("To Do", "In Progress", "Done" და სხვა)
- `assigned_to`: ვის აქვს მინიჭებული დავალება
- `mark_status(new_status)`: სტატუსის შეცვლა

## class: Project

- `name`: პროექტისს სახელი
- `description`: პროექტის აღწერა
- `users`: მონაწილე მომხმარებლების სია
- `tasks`: დავალებების სია
- `add_user(user)`: პროექტში მომხმარებლის დამატება
- `add_task(task)`: პროექტში დაავალების დამატება