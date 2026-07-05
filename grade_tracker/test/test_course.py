import pytest
from notenverwaltung.course import Course


def test_course_creation_with_defaults():
  """Test that a course initializes with correct default grades."""
  course = Course("CS101", "Intro to Computer Science")
  assert course.course_id == "CS101"
  assert course.name == "Intro to Computer Science"
  assert course.max_grade == 100.0
  assert course.passing_grade == 50.0


def test_course_creation_with_custom_grades():
  """Test that custom max and passing grades are set correctly."""
  course = Course("MATH201", "Calculus", max_grade=6.0, passing_grade=4.0)
  assert course.max_grade == 6.0
  assert course.passing_grade == 4.0


def test_invalid_max_grade_raises_value_error():
  """Test that max_grade must be strictly greater than 0."""
  with pytest.raises(ValueError):
    Course("CS101", "Intro to CS", max_grade=0)

  with pytest.raises(ValueError):
    Course("CS101", "Intro to CS", max_grade=-10)


def test_invalid_passing_grade_raises_value_error():
  """Test passing_grade rules (0 < passing_grade <= max_grade)."""
  # Passing grade cannot be 0 or negative
  with pytest.raises(ValueError):
    Course("CS101", "Intro to CS", max_grade=100, passing_grade=0)

  with pytest.raises(ValueError):
    Course("CS101", "Intro to CS", max_grade=100, passing_grade=-5)

  # Passing grade cannot exceed max_grade
  with pytest.raises(ValueError):
    Course("CS101", "Intro to CS", max_grade=100, passing_grade=101)


def test_readable_str_representation():
  """Test the __str__ output matches the expected pattern."""
  course = Course("CS101", "Intro to CS")
  assert str(course) == "Course: Intro to CS (CS101) | Pass/Max: 50.0/100.0"
