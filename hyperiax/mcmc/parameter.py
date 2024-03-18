from __future__ import annotations
from abc import ABC, abstractmethod

class Parameter(ABC):
    def __init__(self, value) -> None:
        self.value = value

    @abstractmethod
    def update(self, value, accepted): ...

    @abstractmethod
    def propose(self, key) -> Parameter: ...

    @abstractmethod
    def log_prior(self):
        pass