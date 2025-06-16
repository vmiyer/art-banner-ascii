from ascii_art_banner.banner import generate

def test_generate():
    result = generate("Hello")
    print(result)
    assert "Hello" not in result  # Should be rendered in ASCII art
    assert len(result) > 0
