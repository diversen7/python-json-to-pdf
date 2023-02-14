import json


class JsonToHtml:
    def __init__(self):
        self.level = 0
        self.new_level = True
        pass

    @staticmethod
    def read_json_file(json_file):
        with open(json_file, "r") as f:
            return json.load(f)

    @staticmethod
    def read_string_from_file(file_name):
        with open(file_name, "r") as f:
            return f.read()

    # write string to file
    @staticmethod
    def write_to_file(file_name, string):
        with open(file_name, "w") as f:
            f.write(string)


    def iterate(self, json_data):

        html = ""
        if isinstance(json_data, dict):

            self.level += 1
            self.new_level = True

            for key, value in json_data.items():
                if self.new_level:

                    if isinstance(value, list):
                        html += self.get_heading(key)
                        html += self.iterate(value)
                        continue

                    if self.is_primitive(value):
                        html += self.get_heading(key)
                        html += self.get_paragraph(value)
                        continue

                    html += self.get_heading(key)
                    self.new_level = False

                html += self.iterate(value)
                
            self.level -= 1
            return html

        elif isinstance(json_data, list):

            for item in json_data:
                html += self.iterate(item)

            return html

        else:
            return self.get_paragraph(json_data)

    def get_tabs(self):
        num_tabs = self.level - 1
        tabs = "\t" * num_tabs
        return tabs

    def get_heading(self, heading):
        
        if self.level > 6:
            return f"{self.get_tabs()}<h6>{heading}</h6>\n"

        return f"{self.get_tabs()}<h{self.level}>{heading}</h{self.level}>\n"

    def is_primitive(self, value):
        return isinstance(value, (bool, str, int, float))

    def get_paragraph(self, text):
        return f"{self.get_tabs()}<p>{text}</p>\n"

    def to_html(self, json_data):
        return self.iterate(json_data)
