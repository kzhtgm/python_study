import abc


class Title(abc.ABC):
    @abc.abstractmethod
    def calc_salary(self):
        pass

    def template_method(self):
        title_name = self._title_name()
        return "{0} template method called.".format(title_name)

    @abc.abstractmethod
    def _title_name(self):
        pass


class GroupManager(Title):
    __name: str = "default name"

    def calc_salary(self):
        return 100

    def _title_name(self):
        return "GroupManager"


class SeniorManager(Title):
    def calc_salary(self):
        return 200

    def _title_name(self):
        return "SeniorManager"
