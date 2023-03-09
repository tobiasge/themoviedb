from unittest.mock import patch

import pytest

from themoviedb import routes, schemas


@pytest.mark.asyncio
async def test_credit_details(get_data, assert_data):
    data = get_data("credits/details")
    credit_id = 123

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        credit = await routes.Credit(credit_id).details()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/credit/{credit_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            },
        )

    assert isinstance(credit, schemas.Credit)
    assert assert_data(credit, data)
