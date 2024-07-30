import os
import subprocess

# Directorios de entrada y salida
tex_dir = 'salidas_tex'
pdf_dir = 'pdfs_generados'

# Crear el directorio de salida si no existe
if not os.path.exists(pdf_dir):
    os.makedirs(pdf_dir)

# Compilar todos los archivos .tex en el directorio de entrada y guardar los PDF en el directorio de salida
for filename in os.listdir(tex_dir):
    if filename.endswith('.tex'):
        tex_filepath = os.path.join(tex_dir, filename)
        pdf_filename = os.path.splitext(filename)[0] + '.pdf'
        pdf_filepath = os.path.join(pdf_dir, pdf_filename)
        
        try:
            subprocess.run(['pdflatex', '-output-directory', pdf_dir, tex_filepath], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error al compilar {tex_filepath}: {e}")

print("Compilación de PDFs completada.")