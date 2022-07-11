import pytest

@pytest.fixture(scope="module",autouse=True)
def check_kdfreq(card):
    if card.is_emulated_gnuk:
        pytest.skip("Emulation requires KDF setup", allow_module_level=True)
    if card.is_gnuk2:
        pytest.skip("Gnuk2 requires KDF setup", allow_module_level=True)
