from logic_utils import check_guess, parse_guess

# Note: check_guess returns a (outcome, message) tuple, so we unpack the
# outcome before asserting.

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Regression tests for the input-validation bugs ---
# Each parse_guess call returns (ok, value, error_message).

def test_negative_input_is_rejected():
    # Bug: -1 was accepted and burned an attempt. It should be rejected.
    ok, value, error = parse_guess("-1", 1, 100)
    assert ok is False
    assert value is None
    assert "Negative" in error

def test_out_of_range_input_is_rejected():
    # Bug: 101 was accepted even though the range is 1..100.
    ok, value, error = parse_guess("101", 1, 100)
    assert ok is False
    assert value is None
    assert "range" in error.lower()

def test_non_numeric_input_is_rejected():
    # Bug: "Hola" was accepted instead of being flagged as invalid.
    ok, value, error = parse_guess("Hola", 1, 100)
    assert ok is False
    assert value is None
    assert error is not None

def test_valid_input_is_accepted():
    # A normal in-range guess should pass cleanly.
    ok, value, error = parse_guess("42", 1, 100)
    assert ok is True
    assert value == 42
    assert error is None

def test_empty_input_is_rejected():
    ok, value, error = parse_guess("", 1, 100)
    assert ok is False
    assert value is None
    assert error is not None

def test_range_respects_difficulty_bounds():
    # 30 is valid on Normal (1..100) but out of range on Easy (1..20).
    ok_normal, _, _ = parse_guess("30", 1, 100)
    ok_easy, _, _ = parse_guess("30", 1, 20)
    assert ok_normal is True
    assert ok_easy is False
