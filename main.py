"""Monday handover note — a single-line out-of-office reply.

Three fragments, one sentence, zero hand-holding after lunch.
"""

import os


def assemble_handover_note():
    opener = "I am out until Monday. "
    middle = "I trained my replacement for exactly one afternoon, "
    closer = "so good luck to us all."
    segments = [opener, middle, closer]
    return "".join(segments)


def drop_note_at_destination():
    note = assemble_handover_note()
    target_dir = "/output"
    os.makedirs(target_dir, exist_ok=True)
    target_path = os.path.join(target_dir, "entry.txt")
    with open(target_path, "w", encoding="utf-8") as handle:
        handle.write(note)


if __name__ == "__main__":
    drop_note_at_destination()
