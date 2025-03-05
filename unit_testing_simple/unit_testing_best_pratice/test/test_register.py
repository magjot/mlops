import sys
import os
import pytest
import io

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from register import validate_username, validate_email, validate_password, register_user


def test_validate_username():
    assert validate_username("validUser") == True
    assert validate_username("user name") == False  # Spaces not allowed
    assert validate_username("") == False  # Cannot be empty

def test_validate_email():
    assert validate_email("user@example.com") == True
    assert validate_email("userexample.com") == False  # Missing '@'
    assert validate_email("user@com") == False  # Missing '.'

def test_validate_password():
    assert validate_password("Passw0rd!") == True  # Valid password
    assert validate_password("password") == False  # No numbers, no special char
    assert validate_password("12345678") == False  # No letters
    assert validate_password("Passw0rd") == False  # No special char
    assert validate_password("Short1!") == False  # Too short

def test_register_user():
    assert register_user("validUser", "user@example.com", "Passw0rd!") == "Registration successful"
    assert register_user("", "user@example.com", "Passw0rd!") == "Invalid username"
    assert register_user("validUser", "userexample.com", "Passw0rd!") == "Invalid email"
    assert register_user("validUser", "user@example.com", "password") == "Invalid password"

def test_mock_user_input(monkeypatch):
    """Simulate user input using monkeypatch and io.StringIO"""
    monkeypatch.setattr('sys.stdin', io.StringIO("validUser\nuser@example.com\nPassw0rd!\n"))
    assert register_user("validUser", "user@example.com", "Passw0rd!") == "Registration successful"
 
