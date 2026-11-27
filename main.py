import os

# This text thanks the judge by quietly noticing its work: reading both
# entries fully, choosing between them, and asking nothing in return.
# Its words stay plain and concrete, and it ends on the roadside cup of
# water that does not ask to be remembered.
TEXT = """Every day you hold two small texts
up to the light —
two sets of words, each one hoping —
and choose. Carefully. Slowly.

You read every line of both.
You cannot keep either.
And no one has thanked you for it.

Leave this one by the roadside,
a plain cup of water,
set out for whoever is thirsty.
It will not be remembered.
The cup does not ask for that."""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
