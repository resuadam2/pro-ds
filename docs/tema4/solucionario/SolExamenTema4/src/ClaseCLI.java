import java.util.Scanner;

public class ClaseCLI {
    private static Scanner sc = new Scanner(System.in);

    public static void gestionClase() {
        String option = "";
        showMenu();
        option = sc.nextLine();
        while (!option.equals("0")) {
            switch (option) {
                case "1" -> mostrarAlumnado();
                case "2" -> addNewAlumno();
                case "3" -> borrarAlumno();
                case "4" -> mediaClase();
                case "5" -> bestAlumno();
                default -> System.out.println("Seleccione una opción válida.");
            }
            showMenu();
            option = sc.nextLine();
        }
        System.out.println("Fin del programa.");
        sc.close();
    }

    private static void bestAlumno() {
        if (Clase.mejorAlumno() ==  null) System.out.println("La lista está vacía.");
        else {
            System.out.println("El mejor alumno/a es " + Clase.mejorAlumno().showName() + " con una media de " + Clase.mejorAlumno().notaMedia());
        }
    }

    private static void mediaClase() {
        if (Clase.notaMediaClase() == -1) System.out.println("La lista está vacía.");
        else System.out.println("Nota media de la clase: " + Clase.notaMediaClase());
    }

    private static void borrarAlumno() {
        boolean isNotValid = true;
        while(isNotValid) {
            Clase.showAlumnosSummary();
            System.out.println("Seleccione la posición del alumno/a a eliminar.");
            System.out.println("Pulse S|s para volver al menú principal.");
            String option = sc.nextLine();
            if (option.equalsIgnoreCase("s")) {
                isNotValid = false;
            } else {
                try {
                    if (Clase.deleteAlumno(Integer.parseInt(option))) {
                        System.out.println("Alumno/a ELIMINADO/A.");
                        isNotValid = false;
                    }
                    else System.out.println("Posición incorrecta, no existe tal alumno/a");
                } catch (NumberFormatException e) {
                    System.out.println("Debe introducir un número válido.");
                }
            }
        }
    }

    private static void addNewAlumno() {
        String nombre = validateString("el nombre del alumno/a");
        String apellido1 = validateString("el primer apellido");
        String apellido2 = validateString("el segundo apellido");
        double[] notas = new double[4];
        for (int i = 0; i < notas.length; i++) {
            notas[i] = validateDouble("nota del tema " + (i+1));
        }
        Clase.addAlumno(new Alumno(nombre, apellido1, apellido2, notas));
    }

    private static String validateString(String peticion) {
        String toret = "";
        while(toret.isBlank()) {
            System.out.println("Introduzca " + peticion);
            toret = sc.nextLine();
            if (!toret.isBlank()) return toret;
            else System.out.println("No puede introducir " + peticion + " vacío.");
        }
        return toret;
    }

    private static double validateDouble(String peticion) {
        double toret = 0;
        boolean isNotValid = true;
        while(isNotValid) {
            try {
                System.out.println("Introduzca " + peticion);
                System.out.println("Las notas deben estar entre 0 y 10.");
                toret = Double.parseDouble(sc.nextLine());
                if (toret < 0 || toret > 10) throw new NumberFormatException();
                else isNotValid = false;
            } catch (NumberFormatException e) {
                System.out.println("Debe introducir un número válido.");
            }
        }
        return toret;
    }

    private static void mostrarAlumnado() {
        if (Clase.alumnos.isEmpty()) System.out.println("Lista vacía.");
        else Clase.showAlumnos();
    }

    private static void showMenu() {
        System.out.println("Seleccione una opción del menú:");
        System.out.println("1- Mostrar alumnado.");
        System.out.println("2- Añadir alumno/a.");
        System.out.println("3- Eliminar alumno/a.");
        System.out.println("4- Nota media de la clase.");
        System.out.println("5- Alumno/a con la mejor media de la clase.");
        System.out.println("0- Salir del programa.");
        System.out.println();
    }
}
