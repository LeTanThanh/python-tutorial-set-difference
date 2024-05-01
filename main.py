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

  # The set difference() method vs set difference operator (-)

  scores = {7, 8, 9}
  numbers = [9, 10]
  new_scores = scores.difference(numbers)

  print(scores)
  print(numbers)
  print(new_scores)

  scores = {7, 8, 9}
  numbers = [9, 10]
  # new_scores = scores - numbers
  # TypeError
