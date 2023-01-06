from app.codecov import translate_color

def test_translate_color():
    assert translate_color("aliceblue") == "#f0f8ff"
    assert translate_color("antiquewhite") == "#faebd7"
    assert translate_color("antiquewhite1") == "#ffefdb"
    assert translate_color("") == "No color entered"
    assert translate_color("not a color") == "Color not found"

    
