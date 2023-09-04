#forループを用いた場合
list = ["水","金","地","火","木","土","天","海","冥"]
for lists in list:
  print(lists)

#whileループを用いた場合
list = ["水","金","地","火","木","土","天","海","冥"]
while list:
  lists = list.pop(0)
  print(lists)
