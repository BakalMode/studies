def read_tilln(n,file):

  lst = list(file.readlines())
  lastline = lst[len(lst)-1]

  for line in range(1,len(lst)):

    if n!=0:

        print(lst[len(lst)-line])
        n-=1



n = 5
file = "C:\\Users\\turht\\Desktop\\haciendo.txt"
with open(file, "r") as f:

    read_tilln(n,f)


listt = ["45","hjg","765","ytry"]

