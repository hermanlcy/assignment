#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import webbrowser


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'synchroniser.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # print(sys.argv)
    webbrowser.open('http://localhost:8000')
    execute_from_command_line(['.\\manage.py', 'runserver'])
    # execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # print('installing pip.....')
    # os.system('sudo apt install python3-pip -y')
    # print('installing required packages')
    # os.system('pip3 install -r requirements.txt')
    main()
