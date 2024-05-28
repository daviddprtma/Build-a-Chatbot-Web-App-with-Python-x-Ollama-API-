import reflex as rx

from reflex_ollama import style
from reflex_ollama.state import State

component_map = {
    "h1": lambda text: rx.heading(
        text, size="5", margin_y="1em"
    ),
    "h2": lambda text: rx.heading(
        text, size="3", margin_y="1em"
    ),
    "h3": lambda text: rx.heading(
        text, size="1", margin_y="1em"
    ),
    "code": lambda text: rx.code(text, color="#C9494F", style=dict(background_color="white")),
    "codeblock": lambda text, **props: rx.code_block(
        text, **props, theme="dark", margin_y="1em"
    ),
    "a": lambda text, **props: rx.link(
        text, **props, color="blue", _hover={"color": "red"}
    ),
}


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.markdown(
                r"{}".format(question),
                style=style.question_style,
            ),
            text_align="right"),
        rx.box(
            rx.markdown(
                r"{}".format(answer),
                style=style.answer_style,
                component_map=component_map
            ),
            text_align="left"
        ),
        margin_y="1em",
        width="90%",
        spacing="10"
    )


def action_bar() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.input(
                id="input_box",
                placeholder="Ask me anything",
                style=style.input_style,
                on_change=State.set_question,
                on_key_down=State.key_enter,
            ),
            width="90%"
        ),
        rx.box(
            rx.button(
                "Ask",
                style=style.button_style,
                on_click=State.answer,
            ),
            width="auto"
        ),
        spacing="4",
        width="100%"
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


def index() -> rx.Component:
    return rx.tablet_and_desktop(
        rx.container(
            chat(), action_bar(), align="center"
        ),
        width="100%"
    )


app = rx.App()
app.add_page(index)