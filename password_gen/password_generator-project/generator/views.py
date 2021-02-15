from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
import string
import random
from datetime import datetime


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    lower, upper, numbers, specials = (False, ) * 4
    def clamp(n, minn, maxn): return max(min(maxn, n), minn)

    length = clamp(int(request.GET.get('length', '12')), 8, 18)

    if request.GET.get('lowercase'):
        lower = True
    if request.GET.get('uppercase'):
        upper = True
    if request.GET.get('numbers'):
        numbers = True
    if request.GET.get('specials'):
        specials = True

    if has_two_options(lower, upper, numbers, specials):
        thepassword = generate_pwd(length, lower, upper, numbers, specials)
        return render(request, 'generator/password.html', {'password': thepassword})
    else:
        # redirect with flash of message indicating error
        messages.add_message(request, messages.ERROR,
                             "ERROR: 2 or more options must be selected.")
        return redirect('home')


def about(request):
    return render(request, 'generator/about.html')


def has_two_options(lower: bool, upper: bool, numbers: bool, specials: bool) -> bool:
    """
    Returns True if 2 or more options are selected based on the boolean values.

    Args:
        lower (bool): If lowercase is selected
        upper (bool): If uppercase is selected
        numbers (bool): If numbers is selected
        specials (bool): If special characters is selected

    Returns:
        bool: 2 or more options are True
    """
    truth_values = (lower, upper, numbers, specials)
    true_count = sum(1 for v in truth_values if v)
    return true_count >= 2


def generate_pwd(passwd_length: int, lower: bool = False, upper: bool = False, numbers: bool = False, specials=False) -> str:
    """
    Generates password given length, whether it will be upper case, has numbers, or with special characters.

    Args:
        passwd_length (int): Length of password to be generated
        lower (bool, optional): Whether password has lowercase. Defaults to False.
        upper (bool, optional): Whether password has uppercase. Defaults to False.
        numbers (bool, optional): Whether password has numbers. Defaults to False.
        specials (bool, optional): Whether password has specials. Defaults to False.

    Returns:
        str: Generated password
    """
    assert passwd_length > 0
    random.seed(datetime.now())
    chars = ''

    if lower:
        chars += string.ascii_lowercase
    if upper:
        chars += string.ascii_uppercase
    if numbers:
        chars += string.digits
    if specials:
        chars += string.punctuation

    passwd = ''
    for _ in range(passwd_length):
        passwd += random.choice(chars)

    return passwd
