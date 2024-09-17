""" Module Responsible for running the game """
from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console

from actions import EscapeAction, MovementAction
from entity import Entity
from input_handlers import EventHandler


class Engine:
    """ Class that operates the flow of the game """
    def __init__(
            self, entities: Set[Entity],
            event_handler: EventHandler,
            player: Entity
            ):
        self.entities = entities
        self.event_handler = event_handler
        self.player = player

    def handle_events(self, events: Iterable[Any]) -> None:
        """Method for tracking events """
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            if isinstance(action, MovementAction):
                self.player.move(dx=action.dx, dy=action.dy)

            elif isinstance(action, EscapeAction):
                raise SystemExit()

    def render(self, console: Console, context: Context) -> None:
        """ Method used for rendering the screen """
        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(console)

        console.clear()
