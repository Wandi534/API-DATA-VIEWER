import flet as ft
from flet import Column, Text, TextField, Button
import requests
import json


def main(page: ft.Page):
    page.title ="Web Scraper" #title of the page

    url_field = TextField(value="", hint_text="URL", text_align="Left", autofocus=True)
    result_txt = Text(value="", text_align="Left")

    def scrape(e):
        url = url_field.value
        url_field.value=""

        response = requests.get(url)
        json_data = json.loads(response.text)

        names = [item["name"] for item in json_data]

        result_txt.value = "\n".join(names)

        page.update()

    page.add(
        Column(
           [
                url_field,
                Button(content="Scrape", on_click=scrape),
                ft.Divider(),
                result_txt,
           ]
       )
   )
 
if __name__ == "__main__":
    ft.run(main)
