# This file was auto-generated by Fern from our API Definition.

from .resources.event.client import AsyncEventClient, EventClient
from .resources.generations.client import AsyncGenerationsClient, GenerationsClient
from .resources.score.client import AsyncScoreClient, ScoreClient
from .resources.span.client import AsyncSpanClient, SpanClient
from .resources.trace.client import AsyncTraceClient, TraceClient


class FintoLangfuse:
    def __init__(
        self, *, environment: str, x_langfuse_sdk_name: str, x_langfuse_sdk_version: int, username: str, password: str
    ):
        self._environment = environment
        self.x_langfuse_sdk_name = x_langfuse_sdk_name
        self.x_langfuse_sdk_version = x_langfuse_sdk_version
        self._username = username
        self._password = password
        self.event = EventClient(
            environment=self._environment,
            x_langfuse_sdk_name=self.x_langfuse_sdk_name,
            x_langfuse_sdk_version=self.x_langfuse_sdk_version,
            username=self._username,
            password=self._password,
        )
        self.generations = GenerationsClient(
            environment=self._environment,
            x_langfuse_sdk_name=self.x_langfuse_sdk_name,
            x_langfuse_sdk_version=self.x_langfuse_sdk_version,
            username=self._username,
            password=self._password,
        )
        self.score = ScoreClient(
            environment=self._environment,
            x_langfuse_sdk_name=self.x_langfuse_sdk_name,
            x_langfuse_sdk_version=self.x_langfuse_sdk_version,
            username=self._username,
            password=self._password,
        )
        self.span = SpanClient(
            environment=self._environment,
            x_langfuse_sdk_name=self.x_langfuse_sdk_name,
            x_langfuse_sdk_version=self.x_langfuse_sdk_version,
            username=self._username,
            password=self._password,
        )
        self.trace = TraceClient(
            environment=self._environment,
            x_langfuse_sdk_name=self.x_langfuse_sdk_name,
            x_langfuse_sdk_version=self.x_langfuse_sdk_version,
            username=self._username,
            password=self._password,
        )


class AsyncFintoLangfuse:
    def __init__(
        self, *, environment: str, x_langfuse_sdk_name: str, x_langfuse_sdk_version: int, username: str, password: str
    ):
        self._environment = environment
        self.x_langfuse_sdk_name = x_langfuse_sdk_name
        self.x_langfuse_sdk_version = x_langfuse_sdk_version
        self._username = username
        self._password = password
        self.event = AsyncEventClient(
            environment=self._environment,
            x_langfuse_sdk_name=self.x_langfuse_sdk_name,
            x_langfuse_sdk_version=self.x_langfuse_sdk_version,
            username=self._username,
            password=self._password,
        )
        self.generations = AsyncGenerationsClient(
            environment=self._environment,
            x_langfuse_sdk_name=self.x_langfuse_sdk_name,
            x_langfuse_sdk_version=self.x_langfuse_sdk_version,
            username=self._username,
            password=self._password,
        )
        self.score = AsyncScoreClient(
            environment=self._environment,
            x_langfuse_sdk_name=self.x_langfuse_sdk_name,
            x_langfuse_sdk_version=self.x_langfuse_sdk_version,
            username=self._username,
            password=self._password,
        )
        self.span = AsyncSpanClient(
            environment=self._environment,
            x_langfuse_sdk_name=self.x_langfuse_sdk_name,
            x_langfuse_sdk_version=self.x_langfuse_sdk_version,
            username=self._username,
            password=self._password,
        )
        self.trace = AsyncTraceClient(
            environment=self._environment,
            x_langfuse_sdk_name=self.x_langfuse_sdk_name,
            x_langfuse_sdk_version=self.x_langfuse_sdk_version,
            username=self._username,
            password=self._password,
        )
