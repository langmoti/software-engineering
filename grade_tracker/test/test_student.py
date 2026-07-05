import pytest
from notenverwaltung.student import Student


def test_valid_student_creation():
  student = Student("S123", "Jane", "Doe", "jane.doe@example.com")
  assert student.student_id == "S123"
  assert student.full_name == "Jane Doe"


def test_readable_str_representation():
  student = Student("S123", "Jane", "Doe", "jane.doe@example.com")
  assert str(student) == "Student: Jane Doe (ID: S123, Email: jane.doe@example.com)"


def test_empty_names_raise_value_error():
  with pytest.raises(ValueError):
    Student("S123", "", "Doe", "jane.doe@example.com")

  with pytest.raises(ValueError):
    Student("S123", "Jane", "   ", "jane.doe@example.com")


def test_invalid_email_raises_value_error():
  with pytest.raises(ValueError):
    Student("S123", "Jane", "Doe", "janedoe.example.com")
