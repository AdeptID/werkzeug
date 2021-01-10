from ..datastructures import EnvironHeaders
from ..useragents import UserAgent
from ..utils import cached_property


class UserAgentMixin:
    """Adds a `user_agent` attribute to the request object which
    contains the parsed user agent of the browser that triggered the
    request as a :class:`~werkzeug.useragents.UserAgent` object.
    """

    headers: EnvironHeaders

    @cached_property
    def user_agent(self) -> UserAgent:
        """The current user agent."""
        return UserAgent(self.headers.get("User-Agent", ""))  # type: ignore
