import pytest
import logging


# Setting up logger
logger = logging.getLogger("test_logger")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("test_search.log")
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

BASE_URL = "http://127.0.0.1:8080"


@pytest.mark.parametrize(
    "sort_by, limit",
    [
        ("price", 5),
        ("year", 10),
        ("brand", 3),
        ("price", 0),
        ("year", 50),
        ("brand", 100),
        (None, 10),  # Without sorting
    ]
)
class TestCarsApp:
    def test_search_cars(self, session, sort_by, limit):
        # Testing cars search with different parameters

        search_url = f"{BASE_URL}/cars"
        params = {}

        if sort_by:
            params["sort_by"] = sort_by
        if limit is not None:
            params["limit"] = limit

        response = session.get(search_url, params=params)

        # Results logging
        log_message = (f"GET request to {search_url} with params={params} returned status {response.status_code} "
                       f"and response {response.json()}")
        logger.info(log_message)
        print(log_message)

        # Check list:
        # 1. Response status code should be 200
        # 2. Response should be a list
        # 3. Results limit should be according to parameters:
        #         ("price", 5),
        #         ("year", 10),
        #         ("brand", 3),
        #         ("price", 0),
        #         ("year", 50),
        #         ("brand", 100),
        #         (None, 10),
        assert response.status_code == 200, f"Expected code 200, but got {response.status_code}"
        data = response.json()
        assert isinstance(data, list), "The result should be a list"
        if limit > 0:
            assert len(data) <= limit, f"The limit of {limit} results was exceeded"
