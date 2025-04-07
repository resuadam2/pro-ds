public class Alumno {
    private String nombre, apellido1, apellido2;
    private double[] notas;

    public Alumno(String nombre, String apellido1, String apellido2, double[] notas) {
        this.nombre = nombre;
        this.apellido1 = apellido1;
        this.apellido2 = apellido2;
        this.notas = notas;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido1() {
        return apellido1;
    }

    public void setApellido1(String apellido1) {
        this.apellido1 = apellido1;
    }

    public String getApellido2() {
        return apellido2;
    }

    public void setApellido2(String apellido2) {
        this.apellido2 = apellido2;
    }

    public double[] getNotas() {
        return notas;
    }

    public void setNotas(double[] notas) {
        this.notas = notas;
    }

    private String capitalize(String in) {
        return in.substring(0,1).toUpperCase() + in.substring(1).toLowerCase();
    }

    public double notaMedia() {
        double sum = 0;
        for (double nota : notas) sum += nota;
        if (notas.length > 0) return sum/notas.length;
        else return 0;
    }

    public String showName() {
        StringBuilder sb = new StringBuilder();
        sb.append(capitalize(apellido1)).append(" ").append(capitalize(apellido2)).append(", ").append(capitalize(nombre)).append("\n");
        return sb.toString();
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(capitalize(apellido1)).append(" ").append(capitalize(apellido2)).append(", ").append(capitalize(nombre)).append("\n");
        for (int i = 0; i < notas.length; i++) {
            sb.append("Tema ").append(i).append(": ").append(notas[i]).append("\n");
        }
        double media = notaMedia();
        String result = String.format("%.2f", media);
        sb.append("Nota media: ").append(result).append("\n");
        sb.append("---------------------------\n");
        return sb.toString();
    }
}
