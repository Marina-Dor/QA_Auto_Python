import pytest
from unittest.mock import patch
from lesson_10.src.homework_10 import log_event


class TestLogEvent:
    @staticmethod
    def generate_expected_output(username: str, status: str):
        return f"Login event - Username: {username}, Status: {status}"

    # Checking correct return value
    @pytest.mark.parametrize("username, status", [
        ('user1', 'success'),
        ('user2', 'expired'),
        ('user3', 'failed')
        ])
    def test_log_event(self, username, status):
        expected_output = self.generate_expected_output(username, status)
        assert log_event(username, status) == expected_output

    # Checking correct log levels
    @pytest.mark.parametrize("username, status, log_level", [
        ('user1', 'success', 'info'),
        ('user2', 'expired', 'warning'),
        ('user3', 'failed', 'error')
        ])
    @patch('lesson_10.src.homework_10.logging.getLogger')
    def test_log_event_levels_correct(self, mock_get_logger, username, status, log_level):
        mock_logger = mock_get_logger.return_value
        log_event(username, status)
        expected_output = self.generate_expected_output(username, status)
        getattr(mock_logger, log_level).assert_called_once_with(expected_output)
