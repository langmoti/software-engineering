from dataclasses import dataclass
from datetime import datetime
from notenverwaltung.course import Course
from notenverwaltung.student import Student


@dataclass
class Grade:
  student: Student
  course: Course
  score: float
  date: str  # ISO format (YYYY-MM-DD)
  notes: str = ""

  def __post_init__(self) -> None:
    """Validates score limits and date format after initialization."""
    # Validate score boundaries based on the linked course
    if not (0 <= self.score <= self.course.max_grade):
      raise ValueError(f"Score must be between 0 and {self.course.max_grade}. Got: {self.score}")

    # Validate that date is in a valid ISO format
    try:
      datetime.fromisoformat(self.date)
    except ValueError:
      raise ValueError(f"Invalid date format: '{self.date}'. Must be ISO format (e.g., 'YYYY-MM-DD').")

  @property
  def is_passing(self) -> bool:
    """Returns True if the score meets or exceeds the course passing threshold."""
    return self.score >= self.course.passing_grade

  @property
  def percentage(self) -> float:
    """Calculates the percentage performance out of the max possible course grade."""
    return (self.score / self.course.max_grade) * 100

  @property
  def letter_grade(self) -> str:
    """Maps the calculated percentage to a standard letter grade."""
    pct = self.percentage
    if pct >= 90.0:
      return "A"
    elif pct >= 80.0:
      return "B"
    elif pct >= 70.0:
      return "C"
    elif pct >= 60.0:
      return "D"
    else:
      return "F"

  def __str__(self) -> str:
    """Returns a user-friendly string representation of the grade."""
    status = "PASSED" if self.is_passing else "FAILED"
    return f"Grade: {self.student.full_name} | {self.course.name} | Score: {self.score}/{self.course.max_grade} ({self.letter_grade}) | [{status}]"
      
