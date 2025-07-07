from pdf2image import convert_from_path

# Ruta del PDF
pdf_path = r"C:\Users\flore\Desktop\Profesional\CV_APP\imagenes\Microsoft Power BI Data.pdf"

# Convertir solo la primera página con alta resolución (dpi=400)
images = convert_from_path(pdf_path, dpi=300, first_page=1, last_page=1)

# Guardar la imagen en PNG
output_path = r"C:\Users\flore\Desktop\Profesional\CV_APP\imagenes\bi.png"
images[0].save(output_path, "PNG")

print(f"Imagen guardada en: {output_path}")