from api.controllers import Total
from django_mock_queries.query import MockSet, MockModel

def test_TotalCost():
  # Arrange
  order = MockSet(
    MockModel(quantity=2, item=MockModel(price=10)),
    MockModel(quantity=1, item=MockModel(price=5))
  )
  deliveryFee = 2.5
  # Act
  total = Total.calculate(order, deliveryFee)
  # Assert
  assert total == round((2*10 + 1*5 + 2.5) * 1.0825, 2)

def test_TotalCost_ZeroResult_ReturnsZero():
  # Arrange
  order = MockSet(
    MockModel(quantity=0, item=MockModel(price=0))
  )
  deliveryFee = 0
  # Act
  total = Total.calculate(order, deliveryFee)
  # Assert
  assert total == 0
