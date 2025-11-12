# conftest.py

import pytest

# pytest configuration

@pytest.fixture
def sample_fixture():
    # Setup code
    yield 'fixture data'
    # Teardown code
