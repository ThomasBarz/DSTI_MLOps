import io
import sys

sys.path += ['C:/Users/thoma/Documents/DSTI/MLOps/DSTI_MLOps/testing/credentials_testing/src']

from cred_sample import *

# Email :

def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra.adaltas.com'))
    assert get_email_from_input() is None

def test_email_with_user_input_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltascom'))
    assert get_email_from_input() is None

def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltas.com'))
    assert get_email_from_input() == 'petra@adaltas.com'

# Username

def test_username_with_user_input_spaces(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('te st'))
    assert get_username_from_input() is None

def test_username_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('test'))
    assert get_username_from_input() == 'test'

# Password

def test_pw_with_user_input_6_chars(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('pass1!'))
    assert get_password_from_input() is None

def test_pw_with_user_input_no_number(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('passpass!'))
    assert get_password_from_input() is None

def test_pw_with_user_input_no_letter(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('12121212!'))
    assert get_password_from_input() is None

def test_pw_with_user_input_no_special(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('passpass1'))
    assert get_password_from_input() is None

def test_pw_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('passpass1!'))
    assert get_password_from_input() == 'passpass1!'