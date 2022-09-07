import sys
import re
import json

file = sys.argv[1]

boxes = []
with open(file) as f:
    boxes_text = f.readlines()

    for text in boxes_text:
        items = text.split(";")

        box = {
            "number": int(items[0]),
            "name": items[2],
            "format": items[1],
            "content": []
        }

        for item in items[3:]:
            item = item.replace("\n", "")
            if not item:
                continue
            if not item:
                # if empty
                continue
            if re.match(r"^[0-9]+\*", item):
                # count is given
                box["content"].append(
                    {
                        "name": re.split(r"^[0-9]+\*", item, 1)[1].strip(),
                        "count": int(item.split("*")[0].strip())
                    }
                )
            else:
                box["content"].append({"name": item, "count": None})

        boxes.append(box)

with open(sys.argv[1][:-3] + "json", "w") as f:
    json.dump(boxes, f, indent="  ")