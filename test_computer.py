import computer

def test_computer_pick():
    options = ["rock", "rock", "rock"]
    computer_pick = computer.pick(options)
    assert computer_pick == "rock"