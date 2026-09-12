# Cómo publicar este portafolio en GitHub Pages

## Opción recomendada: repositorio `TUUSUARIO.github.io`

### 1. Crear una cuenta en GitHub
Si aún no tienes una, crea una cuenta en GitHub.

### 2. Crear el repositorio

En GitHub:

1. Presiona **New repository**.
2. Como nombre usa exactamente:

```text
TUUSUARIO.github.io
```

Ejemplo:

```text
carlosmoreno.github.io
```

3. Selecciona **Public**.
4. No necesitas agregar README desde GitHub porque este proyecto ya incluye uno.
5. Crea el repositorio.

### 3. Subir los archivos

La forma más sencilla, sin usar comandos:

1. Descomprime `carlos_moreno_portfolio_v4.zip`.
2. Entra al repositorio creado en GitHub.
3. Presiona:

```text
Add file → Upload files
```

4. Arrastra **el contenido interno** de la carpeta `carlos_moreno_portfolio_v4`.
5. No subas la carpeta contenedora como una sola carpeta adicional.
6. Deben quedar en la raíz archivos como:

```text
_quarto.yml
index.qmd
portfolio.qmd
README.md
```

y las carpetas:

```text
.github/
assets/
projects/
```

7. Escribe un mensaje como:

```text
Initial portfolio
```

8. Presiona **Commit changes**.

### 4. Activar GitHub Pages

En el repositorio:

```text
Settings → Pages
```

En **Build and deployment / Source**, selecciona:

```text
GitHub Actions
```

El repositorio ya contiene:

```text
.github/workflows/publish.yml
```

Ese workflow instala Quarto, genera la web y la publica.

### 5. Esperar la primera publicación

Abre:

```text
Actions
```

en la parte superior del repositorio.

Deberías ver el workflow:

```text
Publish Quarto website to GitHub Pages
```

Cuando aparezca un check verde, la página debería estar disponible en:

```text
https://TUUSUARIO.github.io
```

---

# Cómo actualizar el portafolio después

Cada vez que cambies texto, agregues fotografías o modifiques una página:

1. Sube los archivos modificados a GitHub.
2. Haz un nuevo commit.
3. GitHub Actions vuelve a compilar la página.
4. La web publicada se actualiza automáticamente.

---

# Dónde poner las fotografías

Guárdalas dentro de:

```text
assets/images/
```

Recomendación:

```text
assets/images/
├── thesis/
├── cybathlon/
├── candel/
├── borealis/
├── preservation/
├── unet/
├── fpga/
└── vscan/
```

Por ejemplo:

```text
assets/images/cybathlon/team-cybathlon-2024.webp
assets/images/thesis/perfusion-platform.webp
```

Luego reemplaza un bloque vacío como:

```html
<div class="image-slot">
  ...
</div>
```

por Markdown:

```markdown
![Plataforma de perfusión](assets/images/thesis/perfusion-platform.webp)
```

Dentro de archivos ubicados en `projects/`, la ruta relativa será normalmente:

```markdown
![Plataforma de perfusión](../assets/images/thesis/perfusion-platform.webp)
```

---

# Recomendación para las imágenes

Para la web:

- usar `.webp` o `.jpg`;
- ancho recomendado: 1400–2000 px;
- evitar subir originales de 15–30 MB;
- comprimir antes de publicar;
- usar nombres descriptivos;
- no subir información confidencial, datos identificables de pacientes o propiedad intelectual no autorizada.

---

# Edición local opcional

Si instalas Quarto en tu computador puedes previsualizar la web antes de subirla:

```bash
quarto preview
```

Y para generar la web completa:

```bash
quarto render
```

La salida queda en:

```text
_site/
```
