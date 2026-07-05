import pytest
from notenverwaltung.course import Course
from notenverwaltung.grade import Grade
from notenverwaltung.student import Student


@pytest.fixture
def sample_student():
  return Student("S123", "Jane", "Doe", "jane.doe@example.com")


@pytest.fixture
def default_course():
  return Course("CS101", "Intro to CS", max_grade=100.0, passing_grade=50.0)


@pytest.fixture
def custom_course():
  return Course("MATH201", "Calculus", max_grade=6.0, passing_grade=4.0)


def test_valid_grade_creation(sample_student, default_course):
  grade = Grade(student=sample_student, course=default_course, score=85.0, date="2026-07-05",)
  assert grade.score == 85.0
  assert grade.notes == ""


def test_score_validation_boundaries(sample_student, default_course):
  # Score below zero
  with pytest.raises(ValueError):
    Grade(sample_student, default_course, score=-1.0, date="2026-07-05")

  # Score above maximum grade
  with pytest.raises(ValueError):
    Grade(sample_student, default_course, score=101.0, date="2026-07-05")


def test_invalid_date_format_raises_error(sample_student, default_course):
  with pytest.raises(ValueError):
    Grade(sample_student, default_course, score=80.0, date="05-07-2026")


def test_properties_with_default_course(sample_student, default_course):
  # Test an 'A' grade passing
  grade_a = Grade(sample_student, default_course, score=92.5, date="2026-07-05")
  assert grade_a.is_passing is True
  assert grade_a.percentage == 92.5
  assert grade_a.letter_grade == "A"

  # Test an 'F' grade failing exactly on edge
  grade_f = Grade(sample_student, default_course, score=49.9, date="2026-07-05")
  assert grade_f.is_passing is False
  assert grade_f.letter_grade == "F"


def test_properties_with_custom_course(sample_student, custom_course):
  """Verifies properties scale correctly with custom max_grade thresholds."""
  # A score of 4.5 out of 6.0 = 75% -> Grade C
  grade = Grade(sample_student, custom_course, score=4.5, date="2026-07-05")
  assert grade.is_passing is True  # 4.5 >= 4.0 passing threshold
  assert grade.percentage == 75.0
  assert grade.letter_grade == "C"


def test_readable_str_representation(sample_student, default_course):
  grade = Grade(sample_student, default_course, score=85.0, date="2026-07-05")
  expected = "Grade: Jane Doe | Intro to CS | Score: 85.0/100.0 (B) | [PASSED]"
  assert str(grade)== expected
