def find_single_number(arr):
  # TODO: Write your code here
  res = 0
  for i in arr:
  	res = res ^ i
  return res


def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))

main()
