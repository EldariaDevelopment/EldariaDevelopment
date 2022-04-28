class Almond:
  def __init__(self, pronouns, name, age, tools):
    self.name = name
    self.pronouns = pronouns
    self.age = age
    self.tools = tools

  def Almond(self):
    print("Name:", self.name)
    print("Age:", self.age)
    print("Pronouns:", self.pronouns)
    print("Tools:", self.tools)
    

Almond = Almond("She/Her", "Almond", 14, "VS Code, Intellij")
Almond.Almond()
