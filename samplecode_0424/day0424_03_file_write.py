import random

hanguls = list("가나다라마바사아자차카타파하")

with open("info.txt", "w", encoding="UTF-8") as file:
    for i in range(5):
        
        str_name = random.choice(hanguls) + random.choice(hanguls)
        n_weight = random.randrange(40, 100)
        n_height = random.randrange(140, 200)
        
        file.write("{}, {}, {}\n".format(str_name, n_weight, n_height))