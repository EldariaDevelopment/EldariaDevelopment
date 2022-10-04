class Almond:
  def __init__(self, pronouns, name, age, tools):
    self.name = name
    self.pronouns = pronouns
    self.tools = tools

  def Almond(self):
    print("Name:", self.name)
    print("Pronouns:", self.pronouns)
    print("Tools:", self.tools)
    

Almond = Almond("She/Her", "Almond", "VS Code, Intellij")
Almond.Almond()
