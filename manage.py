#!/usr/bin/env python
import os
import sys
import dotenv
import os
dotenv.load_dotenv()


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_tools_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django.") from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
