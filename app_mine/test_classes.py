from classes import Phone
import pytest

# Tests for class properties
def test_init_user_name():
    phone = Phone("Jhon","123","j@j.com")
    assert phone.user_name == "Jhon"

def test_init_phone_num():
    phone = Phone("Jhon","123","j@j.com")
    assert phone.phone_num == "123"

def test_init_email_address():
    phone = Phone("Jhon","123","j@j.com")
    assert phone.email_address == "j@j.com"

# Test instance methods derived from the Phone class
# Expected outcome: insertion of its data into another instance or notice for invalid input
phone = Phone("Jhon","123","j@j.com")
phone2 = Phone("Boss","321","b@b.com")
def test_call_method():
    phone.call("321")
    rec = phone2.history["call"][0]
    assert rec["name"] == phone.user_name
    assert rec["num"] == phone.phone_num

def test_call_method_exception():
    assert phone.call("333") == "[!] The number you called is no longer in service."

def test_email_method():
    phone.email("b@b.com","hey")
    rec = phone2.history["email"][0]
    assert rec["address"] == phone.email_address
    assert rec["text"] == "hey"

def test_email_method_exception():
    assert phone.email("c@c.com","hey") == "[!] The address doesn\'t exist."
    assert phone.email("j@j.com","") == "[!] Text shoud not be empty."