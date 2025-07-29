# Ticksy

A task management application built with Django.

## 📊 Entity Relationship Diagram (ERD)

The Ticksy system has three main entities: User, Category, and Task.

```
┌─────────────────────┐         ┌─────────────────────┐         ┌─────────────────────┐
│       User          │         │      Category       │         │        Task         │
│                     │         │                     │         │                     │
├─────────────────────┤         ├─────────────────────┤         ├─────────────────────┤
│ id (PK)             │◄────────┤ id (PK)             │◄────────┤ id (PK)             │
│ username (UNIQUE)   │    │    │ name (UNIQUE)       │    │    │ title               │
│ email               │    │    │                     │    │    │ due_date (NULL)     │
│ password            │    │    └─────────────────────┘    │    │ completed (BOOL)    │
│ first_name          │    │                               │    │ category_id (FK)    │
│ last_name           │    │                               │    │ user_id (FK)        │
│ date_joined         │    │                               │    │                     │
│ is_active           │    │                               │    └─────────────────────┘
│ ...                 │    │                               │
└─────────────────────┘    │                               │
                           │                               │
           One-to-Many     │               One-to-Many     │
           (1:N)           │               (1:N)           │
                           └───────────────────────────────┘

### Basic Description

The database has three tables:

- **User**: Stores user account information (uses Django's built-in User model)
- **Category**: Stores task categories (like "Work", "Personal", etc.)
- **Task**: Stores individual tasks with title, due date, and completion status

### Relationships

- Each user can have many tasks (One-to-Many)
- Each category can have many tasks (One-to-Many)
- Each task belongs to one user and one category

This simple structure allows users to organize their tasks by category and track completion status.