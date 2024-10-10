import pytest
from lesson_16.src.homework_16_1_Employee import TeamLead


@pytest.fixture
def team_lead():
    team_lead = TeamLead("Maryna", 100000, "QA", 5)


def test_team_lead_attributes_available(team_lead):
    assert hasattr(team_lead, "name"), "Attribute 'name' is missing."
    assert hasattr(team_lead, "salary"), "Attribute 'salary' is missing."
    assert hasattr(team_lead, "department"), "Attribute 'department' is missing."
    assert hasattr(team_lead, "team_size"), "Attribute 'salary' is missing."


def test_team_lead_attributes_missing(team_lead):
    assert not hasattr(team_lead, "programming_language"), "Unexpected attribute 'programming_language' was found"
