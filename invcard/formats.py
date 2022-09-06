import json
from fpdf import FPDF

class BoxFormat:

    FORMAT = None
    MAX_LINES = 0

    def __init__(self, name: str, number: int, content: list[dict]):
        self.name = name
        self.number = number
        self.content = content

        self.pdf = None

    def generate(self):
        if len(self.content) > self.MAX_LINES:
            raise ValueError(f"Zu viele gelistete Gegenstände für diese Format. Erlaubt: {self.MAX_LINES} (angegeben: {len(self.content)})")

        # generate basic pdf
        self.pdf = FPDF('L', 'mm', self.FORMAT)
        self.pdf.set_title(f"{self.number} {self.name}")
        self.pdf.set_subject(f"Kiste {self.number}")
        self.pdf.set_author("DLRG Ortsgruppe Heidenheim")
        self.pdf.set_creator("inventory-card-generator")

        self.pdf.set_font('Arial', 'B', 16)
        self.pdf.set_text_color(253, 235, 30)
        self.pdf.add_page()

class EuroBox(BoxFormat):
    FORMAT = json.load(open("./formats.json"))["euro"]
    MAX_LINES = 12

    def generate(self):
        # generate basic pdf
        super().generate()

        # add images
        self.pdf.image('red_background.png', x=0, y=0, w=160, h=120, type='', link='')
        self.pdf.image("logo.png", x=10, y=105, w=100)

        # add title
        self.pdf.set_font_size(24)
        self.pdf.cell(40, 10, self.name)

        self.pdf.set_font_size(32)
        self.pdf.cell(100, 10, str(self.number), align="R")

        # add content
        self.pdf.set_font_size(14)
        self.pdf.set_y(22)

        for c in self.content:
            self.pdf.set_x(15)
            self.pdf.cell(20, 10, str(c["count"]), align="R")
            self.pdf.set_x(40)
            self.pdf.cell(100, 10, c["name"])

            self.pdf.set_y(self.pdf.get_y() + 6)

        # output pdf
        self.pdf.output(f"{self.number} {self.name}.pdf", "F")

class NEuroBox(BoxFormat):
    FORMAT = json.load(open("./formats.json"))["neuro"]
    MAX_LINES = 9

    def generate(self):
        # generate basic pdf
        super().generate()

        # add images
        self.pdf.image('red_background.png', x=0, y=0, w=120, h=90, type='', link='')
        self.pdf.image("logo.png", x=10, y=77, w=90, )

        # add title
        self.pdf.set_font_size(18)
        self.pdf.cell(20, 10, self.name)

        self.pdf.set_font_size(22)
        self.pdf.cell(83, 10, str(self.number), align="R")

        # add content
        self.pdf.set_font_size(12)
        self.pdf.set_y(20)

        with self.pdf.unbreakable() as pdf:
            for c in self.content:
                pdf.set_x(10)
                pdf.cell(20, 10, str(c["count"]), align="R")
                pdf.set_x(35)
                pdf.cell(100, 10, c["name"])

                pdf.set_y(pdf.get_y() + 5)

        # output pdf
        self.pdf.output(f"{self.number} {self.name}.pdf")

class SmallBox(BoxFormat):
    FORMAT = json.load(open("./formats.json"))["small"]
    MAX_LINES = 8

    def generate(self):
        # generate basic pdf
        super().generate()
        self.pdf.set_margin(5)
        self.pdf.set_top_margin(3)

        # add images
        self.pdf.image('red_background.png', x=0, y=0, w=120, h=50, type='', link='')
        self.pdf.image("logo.png", x=5, y=43, w=50, )

        # add title
        self.pdf.set_font_size(14)
        self.pdf.cell(25, 5, self.name)

        self.pdf.set_font_size(18)
        self.pdf.cell(85, 5, str(self.number), align="R")

        # add content
        self.pdf.set_font_size(8)
        self.pdf.set_y(10)

        with self.pdf.unbreakable() as pdf:
            for c in self.content:
                pdf.set_x(5)
                pdf.cell(15, 7, str(c["count"]), align="R")
                pdf.set_x(20)
                pdf.cell(100, 7, c["name"])

                pdf.set_y(pdf.get_y() + 3.5)

        # output pdf
        self.pdf.output(f"{self.number} {self.name}.pdf")

def main():
    box = SmallBox("Strömungsretterausrüstung", 401,
                  [
                      {"name": "Helikopterstützräder", "count": 1000},
                      {"name": "Helikopterstützräder", "count": 1000},
                      {"name": "Helikopterstützräder", "count": 1000},
                      {"name": "Helikopterstützräder", "count": 1000},
                      {"name": "Helikopterstützräder", "count": 1000},
                      {"name": "Helikopterstützräder", "count": 1000},
                      #{"name": "Helikopterstützräder", "count": 1000},
                      #{"name": "Helikopterstützräder", "count": 1000},
                      #{"name": "Helikopterstützräder", "count": 1000},
                      #{"name": "Helikopterstützräder", "count": 1000},
                      {"name": "Helikopterstützräder mit extraweicher Gummischicht", "count": 100000},
                      {"name": "Helikopterstützräder", "count": 1}])
    box.generate()

if __name__ == "__main__":
    main()