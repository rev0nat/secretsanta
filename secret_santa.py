import random

sorted = {
	"henri": "",
	"no": "",
	"brice": "",
	"ines": "",
	"emeric": "",
	"anteo": "",
	"julia": ""
}

cheese = ["roquefort", "rocamadour", "chèvre", "caprice des dieux", "chedar", "camembert", "chaussé aux moines"]


def assign_fuckers(key):
	if sorted[key] != "":
		return
	chosen_one = random.choice(list(sorted.keys()))
	if sorted[key] == "" and chosen_one not in sorted.values() and chosen_one != key:
		sorted[key] = chosen_one
	assign_fuckers(key)


for key, value in sorted.items():
	assign_fuckers(key)
	with open(f"/Users/anteo/code/perso/secret/secret_santa/secret_sorted_data/{key}.txt", "a") as f:
		f.write(f"Tu sens le {random.choice(cheese)} aujourd'hui, j'adore quand tu fouettes <3. Tu offres un cadeau à {sorted[key]}, à hauteur de 20 balles.")	
