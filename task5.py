#Make sure to un-comment the function line below when you are done.
#Remember to name your function correctly.
def string_length(str):
    return len(str)
#DO NOT remove lines below here,
#this is designed to test your code.
def test_string_length():
  assert string_length('hello!') == 6
  assert string_length('banana') == 6
  assert string_length('8') == 1
  assert string_length('funnyguys') == 9
  assert string_length('101') == 3
  print("YOUR CODE IS CORRECT! TASK 5")
#test your code by un-commenting the line(s) below
test_string_length()