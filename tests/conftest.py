from hypothesis.strategies import composite, text


@composite
def template_variables(draw):
    s1 = draw(text(min_size=1))
    s2 = draw(text(min_size=1))
    return s1 + "_" + s2, s1 + " " + s2
