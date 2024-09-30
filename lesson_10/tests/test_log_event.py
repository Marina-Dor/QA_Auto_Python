import pytest
from lesson_10.src.homework_10 import log_event


class TestLogEvent:
    file_path = 'lesson_10/login_system.log'

    # Reading from file
    def read_log_file(self, file_path):
        with open(self.file_path, 'r', encoding='utf-8') as log_file:
            content = log_file.read()
        return content

    @pytest.mark.parametrize("username, status, level", [
        ('user1', 'success', "INFO"),
        ('user2', 'expired', "WARNING"),
        ('user3', 'failed', "ERROR")
    ])
    def test_log_event(self, username, status, level):
        log_event(username, status)
        log_content = self.read_log_file(self.file_path)

        # Checking the level is correct
        assert level in log_content

        # Checking log record is correct
        expected_record = f"Login event - Username: {username}, Status: {status}"
        assert expected_record in log_content
