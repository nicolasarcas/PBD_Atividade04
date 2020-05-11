#1
users = [
    #setando um gênero e um idade para cada usuário    
    {"id": 0, "name": "Hero","gender":"m","age":18},    
    {"id": 1, "name": "Dunn","gender":"m","age":20},    
    {"id": 2, "name": "Sue","gender":"f","age":14},    
    {"id": 3, "name": "Chi","gender":"f","age":16},    
    {"id": 4, "name": "Thor","gender":"m","age":18},    
    {"id": 5, "name": "Clive","gender":"m","age":24},    
    {"id": 6, "name": "Hicks","gender":"m","age":22},    
    {"id": 7, "name": "Devin","gender":"m","age":17},    
    {"id": 8, "name": "Kate","gender":"f","age":19},    
    {"id": 9, "name": "Klein","gender":"m","age":20}, 
]
    
friendships = [    
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),    
    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9) 
]

#criando em user o atributo friends
for user in users:
    user["friends"] = []

#tuple unpacking
for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])


#2
def friends_by_gender(user, gender):
    f = 0
    m = 0
    #verificando cada amigo do usuario
    for friend in  user['friends']:
        #caso o gênero seja f o contador feminino aumenta
        if friend['gender'] == 'f':
            f+=1
        #caso o gênero seja m o contador masculino aumenta
        elif friend['gender'] == 'm':
            m+=1
    #a função retorna uma tupla com a quantidade de amigos de cada gênero
    return (f,m)

#dicionario de amigos separados por id e gênero
dictionary_friends_by_id_by_gender = {
    #para cada usuario será setada a chave do dicionario com seu id, e o valor será formado
    #por uma tupla, contendo o numero de amigos do sexo feminino e masculino
    user["id"] : (friends_by_gender(user)) for user in users
}

print(dictionary_friends_by_id_by_gender)

  