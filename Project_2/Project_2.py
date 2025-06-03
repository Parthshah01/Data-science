from bs4 import BeautifulSoup

def load_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        return content

def extract_products(soup):
    products = []

    product_elements = soup.find_all(name="div", class_="product")

    for product in product_elements:
        Name = product.find("h1").text
        Company = product.find("h2").text
        Model = product.find("h3").text

        products.append({"Name": Name, "Company": Company, "Model": Model})

    return products

html_content = load_html("Electronics_store.html")
soup = BeautifulSoup(html_content, "html.parser")
products =  extract_products(soup)

for product in products:
    print(f"Name:{product['Name']}")
    print (f"Company:{product['Company']}")
    print (f"Model:{product['Model']}")
    print("---------------------------------")