from fpdf import FPDF


class FileFormatter:
    file_path = None

    def open_file(self, file):
        self.file_path = file

    def format_file(self):
        names = open(self.file_path, 'r').readlines()
        names_matched = list(filter(lambda name: (name[0] == names[len(names) - 1]), names[:-1]))
        final_list = list(map(lambda name: name[:-1], names_matched))
        final_list.sort()
        self.write_pdf(final_list)

    @staticmethod
    def write_pdf(name_list):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        for i, name in enumerate(name_list):
            pdf.cell(200, 10, txt=name, ln=i+1, align='C')
        pdf.output("names.pdf")
