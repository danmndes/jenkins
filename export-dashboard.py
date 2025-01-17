import requests
from fpdf import FPDF

GRAFANA_URL = "http://localhost:3000"
API_KEY = ""
DASHBOARD_UID = "main"

# Export Dashboard as Image
def export_dashboard_as_image():
    headers = ''#{"Authorization": f"Bearer {API_KEY}"}
    params = {"width": 1920, "height": 1080}
    response = requests.get(f"{GRAFANA_URL}/render/d/{DASHBOARD_UID}/dashboard-name", headers=headers, params=params)
    if response.status_code == 200:
        with open("dashboard.png", "wb") as f:
            f.write(response.content)
        print("Dashboard image exported as dashboard.png")
        return "dashboard.png"
    else:
        print(f"Failed to render dashboard: {response.status_code}, {response.text}")
        return None

# Convert Image to PDF
def convert_image_to_pdf(image_path, output_pdf):
    pdf = FPDF()
    pdf.add_page()
    pdf.image(image_path, x=10, y=10, w=190)  # Adjust the size and position as needed
    pdf.output(output_pdf)
    print(f"PDF generated as {output_pdf}")

# Main Function
def export_dashboard_to_pdf():
    image_path = export_dashboard_as_image()
    if image_path:
        convert_image_to_pdf(image_path, "dashboard.pdf")

# Execute the script
export_dashboard_to_pdf()
