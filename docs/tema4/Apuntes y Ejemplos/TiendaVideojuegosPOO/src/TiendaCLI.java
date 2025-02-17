import java.util.Scanner;

public class TiendaCLI {
    private static TiendaDeVideojuegos tienda = new TiendaDeVideojuegos();
    private static Scanner sc = new Scanner(System.in);

    private static void mostrarMenu() {
        System.out.println("1. Mostrar videojuegos.");
        System.out.println("2. Añadir un nuevo videojuego.");
        System.out.println("3. Eliminar un videojuego.");
        System.out.println("4. Salir.");
    }

    public static void tienda() {
        crearVideojuegosDePrueba();
        String opcionSeleccionada = "";
        System.out.println("BIENVENIDO AL PROGRAMA DE LA TIENDA DE VIDEOJUEGOS:");
        while(!opcionSeleccionada.equals("4")) {
            mostrarMenu();
            opcionSeleccionada = sc.nextLine();
            switch (opcionSeleccionada) {
                case "1" -> mostrarVideojuegos();
                case "2" -> nuevoVideojuego();
                case "3" -> eliminarVideojuego();
                case "4" -> terminarPrograma();
                default -> System.out.println("Entrada invállida. \nSeleccione una opción disponible.");
            }
        }
    }

    private static void crearVideojuegosDePrueba() {
        tienda.addVideojuego(new Videojuego("Super Mario Bros", "N64", 300));
        tienda.addVideojuego(new Videojuego("Pokemon Esmeralda", "GBA", 150));
        tienda.addVideojuego(new Videojuego("Dragon Quest VIII", "PS2", 100));
        tienda.addVideojuego(new Videojuego("Super Mario Run", "Android", 0));
    }

    private static void eliminarVideojuego() {
        System.out.println(tienda.mostrarPosicionesYTitulos());
        System.out.println("Seleccione el videojuego a borrar (introduzca el número correspondiente):");
        int pos = -1;
        try {
            pos = Integer.parseInt(sc.nextLine());
        } catch (NumberFormatException exception) {
            System.out.println("Debe introducir un número.");
        }
        if(tienda.deleteVideojuego(pos)) {
            System.out.println("Videojuego borrado correctamente.");
        } else {
            System.out.println("No se ha podido borrar el videojuego seleccionado.");
        }
    }

    private static void nuevoVideojuego() {
        boolean datosCorrectos = false;
        String titulo = "", plataforma = "";
        double precio = 0;
        while(!datosCorrectos) {
            try {
                System.out.println("Introduzca el título del videojuego:");
                titulo = sc.nextLine();
                if (titulo.isBlank()) {
                    System.out.println("El título no puede estar en blanco.");
                    continue;
                }
                System.out.println("Introduzca la plataforma del videojuego:");
                plataforma = sc.nextLine();
                if (plataforma.isBlank()) {
                    System.out.println("La plataforma no puede estar en blanco.");
                    continue;
                }
                System.out.println("Introduzca el precio del videojuego:");
                precio = Double.parseDouble(sc.nextLine());
                datosCorrectos = true;
            } catch (NumberFormatException e) {
                System.out.println("Debe introducir un número.");
            }
        }
        Videojuego nuevo = new Videojuego(titulo, plataforma, precio);
        if (tienda.addVideojuego(nuevo)){
            System.out.println("Videojuego añadido correctamente.");
        } else {
            System.out.println("El videojuego no se ha añadido porque ya existe para esa plataforma.");
        }
    }

    private static void mostrarVideojuegos() {
        System.out.println(tienda);
    }

    private static void terminarPrograma() {
        System.out.println("Fin del programa");
        sc.close();
    }

    public static TiendaDeVideojuegos getTienda() {
        return tienda;
    }

    public static void setTienda(TiendaDeVideojuegos tienda) {
        TiendaCLI.tienda = tienda;
    }
}
