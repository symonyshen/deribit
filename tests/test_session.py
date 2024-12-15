from deribit.session import Session


def test_test_session_connection():
    """
    Test the connection on the test environment of Deribit.
    """
    session = Session(base_url='https://test.deribit.com/api/v2', debug=True)
    response = session.execute_get_request(
        end_point='public/get_historical_volatility',
        params={
            'currency': 'BTC',
        }
    )
    assert response.status_code == 200