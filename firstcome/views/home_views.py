import flask

from infrastructure.view_modifers import response
import services.user_service as user_service
from viewmodels.account.register_viewmodel import RegisterViewModel

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET'])
@response(template_file='index.html')
def index_get():
    vm = RegisterViewModel()
    return vm.to_dict()


@blueprint.route('/', methods=['POST'])
@response(template_file='index.html')
def index_post():
    vm = RegisterViewModel()
    vm.validate()

    if vm.error:
        return vm.to_dict()

    user = user_service.create_user(vm.name, vm.email)

    if not user:
        vm.error = 'The account could not be created.'
        return vm.to_dict()

    return flask.redirect('/users')
