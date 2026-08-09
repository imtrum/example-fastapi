import pytest
from app.calculations import add,subtract, BankAccount, InsufficientFunds


@pytest.fixture 
def zero_bank_account():
    print("creating empty bank account")
    return BankAccount()


@pytest.fixture 
def bank_account():
    return BankAccount(50)


@pytest.mark.parametrize("nums1, nums2, expected", [
    (3,2,5),
    (6,6,12),
    (5,5,10 )
])
def test_add(nums1,nums2,expected):
    print("testing add function")
    sum = add(nums1,nums2)
    assert sum == expected

def test_subtract():
    assert subtract(8,4) == 4

def test_bank_set_initial_account(bank_account):
    assert bank_account.balance == 50


def test_bank_default_amount(zero_bank_account):
    print("test my bank account")
    assert zero_bank_account.balance == 0

def test_withdraw(bank_account):
    bank_account.withdraw(30)
    assert bank_account.balance == 20


def  test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200) 