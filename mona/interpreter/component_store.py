from mona.interpreter.component.component import Component


class ComponentStore:
    def __init__(self):
        self._next_seq_id: int = -1
        self.seg_by_seq_id: dict[int, Component] = dict()

    def register(self, cmp: Component) -> None:
        seq_id: int = cmp.seq_id
        if seq_id in self.seg_by_seq_id:
            raise RuntimeError(
                f"Cannot override component with sequence id {seq_id}. "
                f"Replacing "
                f"'{self.seg_by_seq_id[seq_id]}"
                f"' with "
                f"'{cmp}'"
                f"."
            )
        self.seg_by_seq_id[seq_id] = cmp

    @property
    def next_seq_id(self) -> int:
        self._next_seq_id += 1
        return self._next_seq_id

    @next_seq_id.setter
    def next_seq_id(self, next_seq_id: int):
        raise RuntimeError(
            "Cannot manually set next_seq_id value for ComponentStore objects."
        )
