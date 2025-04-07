import java.util.ArrayList;

public class Clase {
    public static ArrayList<Alumno> alumnos = new ArrayList<>();

    public static void addAlumno(Alumno alumno) {
        alumnos.add(alumno);
    }

    public static void showAlumnos() {
        for (Alumno alumno: alumnos) {
            System.out.println(alumno.toString());
        }
    }

    public static void showAlumnosSummary() {
        for (int i = 0; i < alumnos.size(); i++) {
            System.out.println(i + " " + alumnos.get(i).showName());
        }
    }

    public static boolean deleteAlumno(int pos) {
        try {
            alumnos.remove(pos);
            return true;
        } catch (IndexOutOfBoundsException e) {
            System.out.println(e.getMessage());
            return false;
        }
    }

    public static double notaMediaClase() {
        double sum = 0;
        for (Alumno alumno: alumnos) sum += alumno.notaMedia();
        if (!alumnos.isEmpty()) return sum/ alumnos.size();
        else return -1;
    }

    public static Alumno mejorAlumno() {
        if (alumnos.isEmpty()) return null;
        int pos = 0;
        for (int i = 1; i < alumnos.size(); i++) {
            if (alumnos.get(i).notaMedia() > alumnos.get(pos).notaMedia()) {
                pos = i;
            }
        }
        return alumnos.get(pos);
    }
}
