if __name__ == "__main__":
  # Using Python Set difference() method to find the difference between sets

  """
  s1.difference(s2, s3, ...)
  """

  s1 = {"Python", "Java", "C++"}
  s2 = {"C#", "Java", "C++"}
  s = s1.difference(s2)

  print(s1)
  print(s2)
  print(s)

  # Using Python set difference operator (-) to find the difference between sets

  """
  s = s1 - s2
  """

  s1 = {"Python", "Java", "C++"}
  s2 = {"C#", "Java", "C++"}
  s = s1 - s2

  print(s1)
  print(s2)
  print(s)
