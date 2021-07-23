from jinja2 import Template


def render_accommodations():
    t = Template("Hello {{ something }}")

    print(t.render(something="World"))
