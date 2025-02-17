public class Videojuego {
    private String titulo;
    private String plataforma;
    private double precio;

    public Videojuego() {
        this.titulo = "Titulo por definir";
        this.plataforma = "Plataforma por definir";
        this.precio = 0;
    }

    public Videojuego(String titulo, String plataforma, double precio) {
        this.titulo = titulo;
        this.plataforma = plataforma;
        this.precio = precio;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getPlataforma() {
        return plataforma;
    }

    public double getPrecio() {
        return precio;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public void setPlataforma(String plataforma) {
        this.plataforma = plataforma;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    public void setPrecio(double precio, boolean iva) {
        if (iva) this.precio = precio + 1.21;
        else this.precio = precio;
    }

    @Override
    public String toString() {
        return "Videojuego {" +
                " \nTítulo: " + getTitulo() +
                " \nPlataforma: " + getPlataforma() +
                " \nPrecio: " + getPrecio() + "\n}\n";
    }
}
