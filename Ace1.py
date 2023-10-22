dic = {
  "musicas": [
    {"nome": "Hey Jude", "banda": "Beatles"},
    {"nome": "November Rain", "banda": "Guns N' Roses"},
    {"nome": "How Deep Is Your Love", "banda": "Bee Gees"},
  ],
  "filmes": {
    "X-men": ["Wolverine", "Xavier", "Tempestade", "Vampira", "Magneto", "Ciclope", "Gambit"],
    "Avengers": ["Homem de Ferro", "Hulk", "Thanos", "Capitão América", "Thor", "Capitã Marvel", "Homem-Aranha"],
    "Star Wars": ["Luke", "Leia", "C-3PO", "Darth Vader", "Obi-Wan", "Yoda", "R2-D2", "Han Solo", "Chewbacca"]
  }
}

def func1(a, b, c, d):
  for x in a:
    if x[b] == d:
      return x[c]
  return "naosei"

print("Hey Jude" == dic["musicas"][0])
print("Thor" in dic["filmes"]["Avengers"])
print("Homem de Ferro" in dic["musicas"][2])
print(dic["filmes"]["X-men"][3] == "Vampira")
print(dic["musicas"][0]["banda"] == "Beatles")
print(dic["filmes"]["Star Wars"][2] == "Leia")
print(func1(dic["filmes"], 1, 2, "Homem de Ferro"))
print("Hey Jude" in dic["musicas"]["Beatles"])
print(func1(dic["musicas"], "banda", "nome", "Hey Jude") == "Beatles")
print(func1(dic["musicas"], "banda", "nome", "Guns N' Roses") == "November Rain")
print("Han Solo" in dic["jogos"]["Mortal Kombat II"])
print("Han Solo" in dic["filmes"]["Star Wars"])
print("Super-homem" in dic["filmes"]["Avengers"])
print(func1(dic, ["filmes"], ["musicas"], "Avengers", "Capitão América"))
print(func1(dic, ["filmes"], ["musicas"], "Avengers", "Capitão América"))
print(func1(dic, ["filmes"], ["musicas"], "Avengers", "Capitão América"))
print("Han Solo" in dic["jogos"]["Star Wars"])
print(dic["musicas"][2]["nome"] == "How Deep Is Your Love")