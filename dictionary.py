x =  {
    'age' : 12,
    'username' : 'McIzation',
    'weapons' : None,
    'is_active' : False,
    'clan' : 'Poland',
}
x.update(weapons = 'glock')
x.update({'is_banned' : False})
x.update(is_banned = True)

y = x.copy()
y.update(age = 13, username = 'baqbaek')

print(x)
print(y)