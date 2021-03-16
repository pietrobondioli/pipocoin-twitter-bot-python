import pytest
from pipocoin.utils import commands_util


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("$pipo test - command command_ _command_- test test",
            ["command", "command_", "_command_"]),
        ("$pipo test -command  __   command- test",
            ["command", "__", "command"]),
        ("$pipo test -command-",
            ["command"]),
    ],
)
def test_get_command_stack(test_input, expected):
    assert commands_util.get_command_stack(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("- command command_ _command_-",
            ["command", "command_", "_command_"]),
        ("-command  __   command-",
            ["command", "__", "command"]),
        ("-command-",
            ["command"]),
    ],
)
def test_get_command_stack_from_command_string(test_input, expected):
    assert commands_util.get_command_stack_from_command_string(
        test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("$pipo test - command command_ _command_- test test",
            "- command command_ _command_-"),
        ("$pipo test -command  __   command- test",
            "-command  __   command-"),
        ("$pipo test -command-",
            "-command-"),
    ],
)
def test_get_command_string_from_status(test_input, expected):
    assert commands_util.get_command_string_from_status(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (["", "test", "0", 8, "", "test"],
            ["test", "0", 8, "test"]),
        (["", "command", "", "", "command_", "", "_command_", ""],
            ["command", "command_", "_command_"]),
    ],
)
def test_filter_empty_commands_from_stack(test_input, expected):
    assert commands_util.filter_empty_commands_from_stack(
        test_input) == expected
