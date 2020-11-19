from src import app
import src.user as user
import src.group as group
import src.auth as auth

# User
app.add_url_rule('/users/<string:id>', 'user-get', user.get, methods = ['GET'])
app.add_url_rule('/users', 'user-insert', user.insert, methods = ['POST'])
app.add_url_rule('/users', 'user-update', user.update, methods = ['PUT'])
app.add_url_rule('/users/<string:id>/groups', 'user-groups-get', user.groups, methods = ['GET'])

# Login
app.add_url_rule('/login', 'login', auth.login, methods = ['POST'])

# Grouups
app.add_url_rule('/groups/<string:id>', 'group-get', group.get, methods = ['GET'])
app.add_url_rule('/groups', 'group-insert', group.insert, methods = ['POST'])
app.add_url_rule('/groups/<string:group_id>/add/<string:user_id>', 'group-add-user', group.add_user, methods = ['GET'])
app.add_url_rule('/groups/<string:group_id>/join', 'group-join', group.join, methods = ['GET'])
