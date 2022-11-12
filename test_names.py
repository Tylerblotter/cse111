from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full():
    assert make_full_name("Sally", "Brown") == "Brown;Sally"
    assert make_full_name("Tyler", "Blotter") == "Blotter;Tyler"
    assert make_full_name("Madison", "Blotter") == "Blotter;Madison"
    assert make_full_name("Jonas", "Nunn") == "Nunn;Jonas"
    assert make_full_name("Jo", "Nunn") == "Nunn;Jo"
    assert make_full_name("Jo-ann", "Nunn") == "Nunn;Jo-ann"

def test_extract_family_name():
    assert extract_family_name("Lopez-avena; Sally") == "Lopez-avena"
    assert extract_family_name("Bo; Sally") == "Bo"
    assert extract_family_name("Cornelious; Sally") == "Cornelious"
    assert extract_family_name("Blotter; Sally") == "Blotter"
    assert extract_family_name("Birch; Sally") == "Birch"
    assert extract_family_name("Keh; Sally") == "Keh"

def test_extract_given_name():
    assert extract_given_name("Brown; Jonathan") == "Jonathan"
    assert extract_given_name("Brown; Kevin") == "Kevin"
    assert extract_given_name("Brown; Larry-Nash") == "Larry-Nash"
    assert extract_given_name("Brown; Taylor") == "Taylor"
    assert extract_given_name("Brown; Ty") == "Ty"
    assert extract_given_name("Brown; Treyvon") == "Treyvon"

pytest.main(["-v", "--tb=line", "-rN", __file__])