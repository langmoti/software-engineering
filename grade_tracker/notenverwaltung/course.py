from dataclasses import dataclass


@dataclass
class Course:
  course_id: str
  name: str
  max_grade: float = 100.0
  passing_grade: float = 50.0

  def __post_init__(self) -> None:
    """Validates grades after initialization."""
    if self.max_grade <= 0:
        raise ValueError(f"max_grade must be greater than 0. Got: {self.max_grade}")

    if not (0 < self.passing_grade <= self.max_grade):
        raise ValueError(f"passing_grade must be greater than 0 and less than or equal to max_grade ({self.max_grade}). Got: {self.passing_grade}" )

  def __str__(self) -> str:
    """Returns a user-friendly string representation."""
    return f"Course: {self.name} ({self.course_id}) | Pass/Max: {self.passing_grade}/{self.max_grade}"
