import abc

import telegram as tg
import telegram.ext as tg_ext


class BaseMessages(abc.ABC):
    @abc.abstractmethod
    def start(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def help(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def echo(self, text: str) -> str:
        pass


class RegularUser(BaseMessages):
    def start(self) -> str:
        return 'Првиет!'

    def help(self) -> str:
        return 'Вам нужно приобрести подписку'

    def echo(self, text: str) -> str:
        return f'{text}'


class PremiumUser(RegularUser):
    def start(self) -> str:
        return 'Здравствуйте!'

    def help(self) -> str:
        return 'Наш менеджер скоро свяжется с вами!'


def get_messages(user: tg.User) -> BaseMessages:
    if not user.is_premium:
        return PremiumUser()
    return RegularUser()
