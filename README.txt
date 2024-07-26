# Documentación del Script de Conversión de Imágenes 🖼️

Este script permite convertir imágenes a escala de grises y representarlas mediante caracteres ASCII.Me fascina el arte ASCII y quería explorar algo.

## Funciones Principales 🔧

### `Img_Convert(path)`

Convierte una imagen especificada por su ruta (`path`) a escala de grises, redimensionándola a 96x54 píxeles. Luego, representa cada pixel de la imagen como un carácter ASCII basado en su intensidad de color. Los caracteres utilizados son `*`, `+`, `-`, `.`, y espacios en blanco.

#### Parámetros:
- `path`: Ruta completa o nombre de archivo de la imagen a convertir.

#### Ejemplo de uso:

### `main()`

Función principal que maneja la interacción con el usuario. Permite al usuario seleccionar si desea convertir una imagen o salir del programa. Si elige convertir una imagen, se le solicita la ruta de la imagen y luego se llama a `Img_Convert`.

#### Flujo de selección:
1. Se muestra un menú con las opciones disponibles.
2. El usuario ingresa `1` para convertir una imagen o `2` para salir.
3. Si elige convertir una imagen, se le solicita la ruta de la imagen.
4. La imagen se convierte utilizando `Img_Convert`.
5. Si elige salir, el programa termina.

## Ejecución del Script 🚀

Para ejecutar este script, asegúrate de tener instalados los paquetes necesarios (`PIL`, `numpy`). Puedes instalarlos usando pip:

