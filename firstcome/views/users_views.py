import flask

from infrastructure.view_modifers import response
from viewmodels.account.users_viewmodel import UserViewModel

blueprint = flask.Blueprint('users', __name__, template_folder='templates')


@blueprint.route('/users')
@response(template_file='users.html')
def users():
    vm = UserViewModel()

    return vm.to_dict()
