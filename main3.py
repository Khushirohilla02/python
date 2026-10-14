from nicegui import ui

ui.label('Hello NiceGUI!')
ui.button('Click me!', on_click=lambda: ui.notify('You clicked me!'))

ui.run()

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Label
from textual.containers import Horizontal

class CounterApp(App):
    """A simple Textual TUI application to count numbers."""
    
    # Bind keyboard shortcuts to specific actions
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"), ("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Label("Count: 0", id="counter_label")
        with Horizontal():
            yield Button("Minus", id="minus_btn", variant="error")
            yield Button("Plus", id="plus_btn", variant="success")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button click events dynamically."""
        label = self.query_one("#counter_label", Label)
        # Extract the current number from the label string
        current_count = int(str(label.renderable).split(": ")[1])

        if event.button.id == "plus_btn":
            current_count += 1
        elif event.button.id == "minus_btn":
            current_count -= 1

        label.update(f"Count: {current_count}")

if __name__ == "__main__":
    app = CounterApp()
    app.run()

                
                  