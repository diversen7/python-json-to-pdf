from json_to_html import JsonToHtml
import pdfkit

json_to_html = JsonToHtml()
json_data = json_to_html.read_json_file("json/test2.json")

html = json_to_html.to_html(json_data)

template = "templates/template.html"
template_str = json_to_html.read_string_from_file(template)

html = template_str.replace("{{content}}", html)

json_to_html.write_to_file("output/index.html", html)

# pdfkit.from_file("./output/index.html", "./output/test.pdf")

pdfkit.from_file("output/index.html", "output/output.pdf", options={"enable-local-file-access": ""})





