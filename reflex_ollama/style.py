# style.py
import reflex as rx

# Common styles for questions and answers.
shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "20%"
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
    max_width="50em",
    display="inline-block",
)

# Set specific styles for questions and answers.
question_style = message_style | dict(
    margin_left=chat_margin,
    background_color="#7C50F0",
    color="white"
)
answer_style = message_style | dict(
    margin_right=chat_margin,
    background_color="#F95CBA",
    color="white"
)

# Styles for the action bar.
input_style = dict(
    border_width="2px", box_shadow=shadow
)

button_style = dict(
    background_color=rx.color("accent", 10),
    box_shadow=shadow,
)