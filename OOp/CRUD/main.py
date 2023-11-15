from view_mixins import *


class Post(CrateMixin, ReadMixin, UpdateMixin, DeleteMixin, SaveMixin):
    pass

class Comment(CrateMixin, ReadMixin, DeleteMixin, SaveMixin):
    pass

class Like(CrateMixin, ReadMixin, DeleteMixin):
    pass