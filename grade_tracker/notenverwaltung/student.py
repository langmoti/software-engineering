from dataclasses import dataclass


@dataclass
class Student:
  student_id: str
  first_name: str
  last_name: str
  email: str

  def __post_init__(self) -> None:
    """Validates fields after initialization."""
    # Validate non-empty names
    if not self.first_name.strip():
        raise ValueError("first_name cannot be empty or whitespace.")
    if not self.last_name.strip():
        raise ValueError("last_name cannot be empty or whitespace.")

    # Validate email contains '@'
    if "@" not in self.email:
        raise ValueError(f"Invalid email address: '{self.email}'")

  @property
  def full_name(self) -> str:
    """Returns the student's full name."""
    return f"{self.first_name} {self.last_name}"

  def __str__(self) -> str:
    """Returns a user-friendly, readable string representation."""
    return f"Student: {self.full_name} (ID: {self.student_id}, Email: {self.email})"
