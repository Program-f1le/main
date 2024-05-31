from fastapi import FastAPI

app = FastAPI(
    title= 'Users'
)

my_users = [
    {'id': 1, 'role': 'admin', 'name': 'Taler'},
    {'id': 2, 'role': 'user', 'name': 'Raden'},
    {'id': 3, 'role': 'moder', 'name': 'Taison'},
]

@app.get('/user/{user_id}')
def get_user(user_id: int):
    return [user for user in my_users if user.get('id') == user_id]

@app.post('/user/{user_id}')
def change_user(user_id: int, new_name: str = '0', new_role: str = '0'):
    current_user = [user for user in my_users if user.get('id') == user_id][0]
    if new_name != '0':
        current_user['name'] = new_name
    if new_role != '0':
        current_user['role'] = new_role
    return {'status': 200, 'date': current_user}


@app.post('/user')
def create_user(new_name: str, new_role: str):
    new_user = {'id': my_users[-1].get('id') + 1, 'role': new_role, 'name': new_name}
    my_users.append(new_user)
    return {'status': 200, 'data': my_users}
