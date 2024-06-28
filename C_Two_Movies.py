def max_company_rating(n, likes_first, likes_second):
  """
  This function calculates the maximum possible company rating.

  Args:
      n: The number of people.
      likes_first: List of 1s (liked), -1s (disliked), or 0s (neutral) for the first movie.
      likes_second: List of 1s (liked), -1s (disliked), or 0s (neutral) for the second movie.

  Returns:
      The maximum possible company rating.
  """
  # Calculate the maximum rating achievable if all reviews go to the first movie.
  max_rating_first = sum(likes_first)

  # Calculate the maximum rating achievable if all reviews go to the second movie.
  max_rating_second = sum(likes_second)

  # Find the total number of neutral reviews for each movie.
  neutral_first = likes_first.count(0)
  neutral_second = likes_second.count(0)

  # Consider cases where some neutral reviews can improve the rating of the lower-rated movie.
  if max_rating_first < max_rating_second:
    # Use neutral reviews on the first movie to potentially improve the second movie's rating.
    potential_gain = min(neutral_first, abs(max_rating_first - max_rating_second))
    max_rating_first += potential_gain
  else:
    # Use neutral reviews on the second movie to potentially improve the first movie's rating.
    potential_gain = min(neutral_second, abs(max_rating_second - max_rating_first))
    max_rating_second += potential_gain

  # Return the maximum rating of the company (minimum of first and second movie's rating).
  return max(max_rating_first, max_rating_second)

if __name__ == "__main__":
  num_tests = int(input())
  for _ in range(num_tests):
    num_people = int(input())
    likes_first = list(map(int, input().split()))
    likes_second = list(map(int, input().split()))
    max_rating = max_company_rating(num_people, likes_first, likes_second)
    print(max_rating)
