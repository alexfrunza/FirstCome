from services import user_service
from viewmodels.shared.viewmodelbase import ViewModelBase


class UserViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()

        self.users_count = user_service.get_users_count()
        self.users_info = user_service.get_users()