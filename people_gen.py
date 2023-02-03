import random as r
import string
import names

class People:
  people = []

  def __init__(self,count=50):
    self.persons(count)

  def persons(self,count):
    for x in range(count):
      people = names.get_full_name().split(' ')
      dict_data = {
        'name':people[0],
        'surname':people[1],
        'phone':self.phone(),
        'email':self.email(people[0],people[1]),
        'slug':self.slug(),
        'address':self.adress(),
        'twitter':f"{people[0]}_{people[1].upper()}"
      }
      self.people.append(dict_data)
    return self.people


  def phone(self):
    phone_num = f"+994{r.choice(['55','50','70','77'])}856{r.randint(1111,9991)}"
    return phone_num

  def email(self,name,sname):
    emails = f"{name.lower()}_{sname[0].lower()}@gmail.com"
    return emails
  
  def slug(self,letters = 8):
    slugs = ''.join(r.choices(list(string.ascii_letters),k=letters))
    return slugs

  def adress(self):
    street_name = names.get_full_name()
    street_num = r.randint(500,10000)
    item = r.choice(list(string.ascii_uppercase))
    return f"{street_name} st. {street_num}{item}"



