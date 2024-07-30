import csv
import os

# Crear directorios si no existen
output_dir = 'salidas_tex'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
# Leer datos del CSV
with open('datos.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        nombre = row['Nombre']
        dni = row['DNI']
        
        # Crear nombre de archivo
        safe_nombre = nombre  
        filename = os.path.join(output_dir, f"constancia_{safe_nombre}.tex")
        
        # Contenido del archivo .tex
        content = f"""
        \\documentclass{{article}}
        \\usepackage[a4paper, landscape, margin=1cm]{{geometry}}
        \\usepackage{{graphicx}}
        \\usepackage{{xcolor}}
        \\usepackage{{tikz}}
        \\usepackage{{fancyhdr}}
        \\usepackage{{tcolorbox}}
        \\definecolor{{airforceblue}}{{rgb}}{{0.36, 0.54, 0.66}}
        \\usepackage{{parskip}}
        \\usepackage[pages=all]{{background}}

        \\backgroundsetup{{
        scale=1,
        color=black,
        opacity=2,
        angle=0,
        contents={{%
        \\includegraphics[width=\\paperwidth,height=\\paperheight]{{Imagenes/2}}
        }}
        }}

        \\pagestyle{{empty}}

        \\begin{{document}}
        \\vspace*{{-15pt}}
        \\begin{{center}}
        \\begin{{Huge}}
        \\textbf{{UNIVERSIDAD NACIONAL DE INGENIERÍA}}
        \\end{{Huge}}
        \\\\
        \\begin{{huge}}
        OFICINA DE TECNOLOGÍAS DE LA INFORMACIÓN
        \\end{{huge}}
        \\end{{center}}
        \\vspace{{30pt}}
        \\begin{{center}}
        \\begin{{tikzpicture}}
        \\node[anchor=north, align=center, text=airforceblue, font=\\bfseries\\Huge] at ([yshift=-5cm]current page.north) {{
                CERTIFICADO
            }};
        \\end{{tikzpicture}}
        \\\\[0.5cm]
        {{\\large Otorgado a}}
        \\end{{center}}
        \\begin{{center}}
        \\begin{{tikzpicture}}
        \\node[anchor=north, align=center, font=\\bfseries\\LARGE] at ([yshift=-8cm]current page.north) {{
                \\vspace{{0.5cm}}
                \\underline{{\\textsc{{{nombre}}}}} 
            }};
        \\end{{tikzpicture}}
        \\end{{center}}
        \\begin{{center}}
        \\begin{{tikzpicture}}
        \\node[anchor=north, align=center, font=\\normalsize, text width=20cm] at ([yshift=-12cm]current page.north) {{
                {{\\large Identificado con DNI {dni} por haber aprobado el curso de}}\\\\
                \\textbf{{{{\\Large GESTIÓN DE PROYECTOS 1}}}}\\\\
                {{\\large Realizado del 20 de mayo al 29 de mayo del presente, con una duración de 16 horas.}}
            }};
        \\end{{tikzpicture}}
        \\end{{center}}
        \\vspace{{40pt}}
        \\begin{{tikzpicture}}
        \\node[anchor=south, align=center, font=\\normalsize] at ([yshift=2cm]current page.south) {{
            \\hspace*{{100pt}}  Lima, junio de 2024
            }};
        \\end{{tikzpicture}}
        \\hspace{{300pt}}
        \\begin{{tikzpicture}}
        \\node[anchor=south east, xshift=-1cm, yshift=1cm, font=\\small] at (current page.south east) {{
                \\begin{{tabular}}{{c}}
                    \\rule{{6cm}}{{0.4pt}} \\\\
                    \\textbf{{Mag. Ing. Rubén Arturo Borja Rosales}}\\\\
                    Jefe OTI - UNI
                \\end{{tabular}}}};
        \\end{{tikzpicture}}
        \\begin{{center}}
        \\begin{{tikzpicture}}
        \\node[anchor=south west, xshift=1cm, yshift=1cm] at (current page.south west) {{
                \\includegraphics[height=6cm]{{Imagenes/1}}
            }};
        \\end{{tikzpicture}}
        \\end{{center}}
        \\begin{{center}}
        \\fbox{{\\makebox[5cm][c]{{N$^{{\\circ}}$ Certificado 016-0003405}}}}
        \\end{{center}}

        \\end{{document}}
        """
        
        # Guardar el archivo .tex
        with open(filename, 'w', encoding='utf-8') as texfile:
            texfile.write(content)
print("Archivos .tex generados con éxito.")