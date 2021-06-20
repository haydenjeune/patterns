"""Allows for saving and restoring the previous state of an object without
breaking encapsulation of that object"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


class BaseMemento(ABC):
    @abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def get_snapshot_date(self) -> str:
        raise NotImplementedError()


@dataclass
class EditorSnapshot(BaseMemento):
    """A memento class. This should be immuable"""
    text: str
    selection: str
    cursor_position: int
    # consider making this state private, and storing a reference to the editor here,
    # then we can implement the restore method on the snapshot and not expose the
    # state anywhere


@dataclass
class Editor:
    """Just an editor with some private internal state"""

    _text: str
    _selection: str
    _cursor_position: int

    def save(self) -> EditorSnapshot:
        return EditorSnapshot(self._text, self._selection, self._cursor_position)

    def restore(self, snapshot: EditorSnapshot):
        self._text = snapshot.text
        self._selection = snapshot.selection
        self._cursor_position = snapshot.cursor_position

    def some_operation(self):
        pass


@dataclass
class SomeCommand:
    _backup: EditorSnapshot
    _editor: Editor

    def execute(self):
        self._backup = self._editor.save()

        # whatever other command stuff, eg.
        self._editor.some_operation()

    def undo(self):
        self._editor.restore(self._backup)
