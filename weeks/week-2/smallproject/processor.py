from bs4 import BeautifulSoup


class Processor:
    def __init__(self, text):
        self.text = text

    def extract_crew_names(self):
        soup = BeautifulSoup(
            self.text, "html.parser"
        )  # spécifier le parser serait une bonne idée

        divs_crew = soup.find_all("td", class_="trsbas0")
        divs_crew_names = [
            div.find("b").text for div in divs_crew if div.find("b") is not None
        ]

        return divs_crew_names
