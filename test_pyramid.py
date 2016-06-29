import Pyramid

def test_height_equal_to_zero():
	assert Pyramid.check_height("0") == -1

def test_height_less_than_zero():
	assert Pyramid.check_height("-5") == -1

def test_height_is_int():
	assert Pyramid.check_height("f") == -1

def test_height_is_greater_than_23():
	assert Pyramid.check_height("24") == -1

def test_height_is_valid():
	assert Pyramid.check_height("5") == 5

def test_pyramid_line_1_height_5():
	assert Pyramid.build_line(1, 5) == "    ##"

def test_pyramid_line_7_height_7():
	assert Pyramid.build_line(7, 7) == "########"