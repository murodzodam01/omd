from morse import encode, decode
import pytest


@pytest.mark.parametrize(
    "morse_coded, decoded_result",
    [
        ("-- .- ..", "MAI"),
        ("... --- ...", "SOS"),
        ("-- --", "MM"),
        ("", ""),
    ],
)
def test_decode_morse_pytest(morse_coded, decoded_result):
    assert decode(morse_coded) == decoded_result


if __name__ == "__main__":
    morse_msg = """
    -- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----."""
    decoded_msg = decode(morse_msg)
    print(decoded_msg)
    assert morse_msg == encode(decoded_msg)
