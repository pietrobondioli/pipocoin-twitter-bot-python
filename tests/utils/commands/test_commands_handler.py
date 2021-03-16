import pytest
from pipocoin.utils.commands import commands_handler


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
def test_diff_command(test_input, expected):
    assert commands_handler.get_command_stack(test_input) == expected
