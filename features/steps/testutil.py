# file:features/steps/testutil.py
# ----------------------------------------------------------------------------
# TEST SUPPORT:
# ----------------------------------------------------------------------------
class NamedNumber(object):
  """Map named numbers into numbers."""
  MAP = {
      "one": 1,
      "two": 2,
      "three": 3,
      "four":  4,
      "five":  5,
      "six":   6,
  } # Dict
  
  @classmethod
  def from_string(cls, named_number):
      name = named_number.strip().lower()
      return cls.MAP[name]
