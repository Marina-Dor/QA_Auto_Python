import os

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:123456aA!@localhost/student_management_docker")
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL", "postgresql://postgres:123456aA!@localhost/test_student_management")
