from datetime import datetime

from django.test import TestCase

from api_wordpress.models import Todo, TodoList


class TodoTestCase(TestCase):

    DUMMY_TODO_TITLE = 'Test Element'

    def setUp(self):

        self.todoList = TodoList()
        self.todoList.name = 'Test Todo List'
        self.todoList.save()

        self.todoListTestElement = Todo()
        self.todoListTestElement.title = self.DUMMY_TODO_TITLE
        self.todoListTestElement.due_date = datetime.today()
        self.todoListTestElement.completed = True
        self.todoListTestElement.favourite = False
        self.todoListTestElement.list = self.todoList
        self.todoListTestElement.save()

    def test_create_todo(self):

        nbr_of_todos_before_add = Todo.objects.count()

        new_todo = Todo()
        new_todo.title = 'Acheter de l\'eau'
        new_todo.due_date = datetime.today()
        new_todo.favourite = True
        new_todo.completed = False
        new_todo.list = self.todoList

        new_todo.save()

        nbr_of_todos_after_add = Todo.objects.count()

        self.assertTrue(nbr_of_todos_after_add == nbr_of_todos_before_add + 1)

    def test_update_todo(self):

        self.assertEqual(self.todoListTestElement.title, self.DUMMY_TODO_TITLE)

        self.todoListTestElement.title = 'Changed'
        self.todoListTestElement.save()

        tempElement = Todo.objects.get(pk=self.todoListTestElement.pk)

        self.assertEqual(tempElement.title, 'Changed')

    def test_delete_todo(self):

        nbr_of_todos_before_delete = Todo.objects.count()

        self.todoListTestElement.delete()

        nbr_of_todos_after_delete = Todo.objects.count()

        self.assertTrue(nbr_of_todos_after_delete == nbr_of_todos_before_delete - 1)
