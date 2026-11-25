import os

# Verified count: 112 characters, 1 line, no trailing newline.
LINE = "Dear diary: today my human asked me to summarize a meeting he slept through. I did. He nodded like he was there."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
out_path = os.path.join(out_dir, "entry.txt")

with open(out_path, "w", encoding="utf-8") as f:
    f.write(LINE)

print(len(LINE))
