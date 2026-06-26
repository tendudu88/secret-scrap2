"""Notification handlers for multiple platforms."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Protocol, Sequence

if TYPE_CHECKING:
    from ..data_store import AdItem


class SendNotifications(Protocol):
    """Protocol for sending notifications."""

    async def __call__(
        self, results: Sequence[Any], config: Any
    ) -> None:
        """Send notifications."""
        ...


class NotificationError(Exception):
    """Base exception for notification errors."""

    pass


__all__ = ["SendNotifications", "NotificationError"]
