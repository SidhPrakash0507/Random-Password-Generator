import random
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "!@#$%^&*;,/"

length = 14

x = lowercase+uppercase+number+symbol

y = "".join(random.sample(x,length))

print(f"The Password That You Genrated is{y}")

