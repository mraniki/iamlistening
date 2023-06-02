"""
iamlistening Unit Testing
"""

from datetime import datetime
import pytest
from iamlistening import Listener

@pytest.fixture
def bot():
    """return fmo"""
    return Listener()


@pytest.fixture
async def test_init(bot):
    """return valid order"""
    await bot.start()

# @pytest.fixture
# def result_standard_order():
#     """return standard expected results"""
#     return {
#         "action": "BUY",
#         "instrument": "EURUSD",
#         "stop_loss": 200,
#         "take_profit": 400,
#         "quantity": 2,
#         "order_type": None,
#         "leverage_type": None,
#         "comment": None,
#         "timestamp": datetime.now()
#     }


# @pytest.fixture
# def standard_short_order():
#     """return valid order"""
#     return "Buy EURUSD"


# @pytest.fixture
# def standard_crypto_order():
#     """return valid order"""
#     return "LONG ETHUSD sl=200 tp=400 q=2%"


# @pytest.fixture
# def standard_short_crypto_order():
#     """return valid order"""
#     return "buy WBTC"


# @pytest.fixture
# def standard_order_with_emoji():
#     """return emoji type order"""
#     return """⚡️⚡️ #BNB/USDT ⚡️⚡️
#     Exchanges: ByBit USDT, Binance Futures
#     Signal Type: Regular (Long)
#     Leverage: Cross (20.0X)"""


# @pytest.fixture
# def invalid_order():
#     """return fmo"""
#     return "hello World"


# @pytest.fixture
# def bot_command():
#     return "/bal"


# @pytest.fixture
# def invalid_order_2():
#     """return fmo"""
#     return "This is not an order"


# @pytest.mark.asyncio
# async def test_search_valid_order(fmo, standard_short_crypto_order):
#     """Search Testing"""
#     assert await fmo.search(standard_short_crypto_order) is True


# @pytest.mark.asyncio
# async def test_search_no_order(fmo, invalid_order_2):
#     """Search Testing"""
#     assert await fmo.search(invalid_order_2) is False


# @pytest.mark.asyncio
# async def test_search_no_order_command(fmo, bot_command):
#     """Search Testing"""
#     assert await fmo.search(bot_command) is False


# @pytest.mark.asyncio
# async def test_search_exception(fmo):
#     """Search Testing"""
#     mystring = ""
#     assert await fmo.search(mystring) is False


# @pytest.mark.asyncio
# async def test_search_normal_order(fmo,standard_order):
#     """Search Testing"""
#     assert await fmo.search(standard_order) is True


# @pytest.mark.asyncio
# async def test_search_normal_order_variation(fmo,standard_crypto_order):
#     """Search Testing"""
#     assert await fmo.search(standard_crypto_order) is True


# @pytest.mark.asyncio
# async def test_identify_order(fmo, standard_short_crypto_order):
#     """Identify Testing"""
#     result = await fmo.identify_order(standard_short_crypto_order)
#     assert result is not None


# @pytest.mark.asyncio
# async def test_identify_order_invalid_input(fmo, invalid_order):
#     """Identify Testing"""
#     result = await fmo.identify_order(invalid_order)
#     assert str(result).startswith("Expected")


# @pytest.mark.asyncio
# async def test_invalid_get_order(fmo, invalid_order):
#     """get order Testing"""
#     result = await fmo.get_order(invalid_order)
#     assert result is None


# @pytest.mark.asyncio
# async def test_valid_get_order(fmo, standard_order, result_standard_order):
#     """get order Testing"""
#     result = await fmo.get_order(standard_order)
#     assert result["action"] == result_standard_order["action"]
#     assert result["instrument"] == result_standard_order["instrument"]
#     assert int(result["stop_loss"]) == result_standard_order["stop_loss"]
#     assert int(result["take_profit"]) == result_standard_order["take_profit"]
#     assert int(result["quantity"]) == result_standard_order["quantity"]
#     assert result["order_type"] == result_standard_order["order_type"]
#     assert result["leverage_type"] == result_standard_order["leverage_type"]
#     assert result["comment"] == result_standard_order["comment"]
#     assert type(result["timestamp"] is datetime)


# @pytest.mark.asyncio
# async def test_short_valid_get_order(fmo, standard_short_order, result_standard_order):
#     """get order Testing"""
#     result = await fmo.get_order(standard_short_order)
#     assert result["action"] == result_standard_order["action"]
#     assert result["instrument"] == result_standard_order["instrument"]
#     assert int(result["quantity"]) == 1
#     assert type(result["timestamp"] is datetime)


# @pytest.mark.asyncio
# async def test_contains_emoji_standard_order(fmo, standard_order):
#     """check emoji"""
#     result = await fmo.contains_emoji(standard_order)
#     assert result is False


# @pytest.mark.asyncio
# async def test_contains_emoji_standard_order_with_emoji(fmo):
#     """check emoji"""
#     result = await fmo.contains_emoji("⚡")
#     assert result is True


# @pytest.mark.asyncio
# # async def test_contains_emoji_standard_order_with_emoji_2(fmo, standard_order_with_emoji):
# #     """check emoji"""
# #     result = await fmo.contains_emoji(standard_order_with_emoji)
# #     assert result is True

# @pytest.mark.asyncio
# async def test_exception_handling():
#     # Simulate an exception
#     def func_that_raises():
#         raise ValueError("Test error")

#     # Call the function and verify that it returns None
#     result = None
#     try:
#         result = func_that_raises()
#     except Exception:
#         result = None

#     # Check that the function returned None
#     assert result is None
