"""
created by Nagaj at 13/05/2021
"""
from constants import PROMPT, INVALID, CHOICES


def validated_cmd():
    cmd = input(PROMPT).strip().lower()
    while cmd not in CHOICES:
        cmd = input(INVALID.format(cmd=cmd)).strip().lower()
    return cmd
