"""Simple error handling utilities."""
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def handle_error(err: Exception) -> None:
    """Log an error and display a friendly message."""
    logger.error("An error occurred", exc_info=err)
    print(f"Error: {err}")
