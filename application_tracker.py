"""Track applied jobs and their statuses."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class Application:
    description: str
    status: str = "applied"


@dataclass
class ApplicationTracker:
    applications: List[Application] = field(default_factory=list)

    def add_application(self, description: str) -> None:
        self.applications.append(Application(description=description))

    def list_applications(self) -> List[str]:
        return [f"{app.description} - {app.status}" for app in self.applications]

