import java.util.ArrayList;

public class TiendaDeVideojuegos {
    private ArrayList<Videojuego> videojuegos;

    public TiendaDeVideojuegos() {
        this.videojuegos = new ArrayList<>();
    }

    public boolean addVideojuego(Videojuego nuevo) {
        for (Videojuego x : videojuegos) {
            if (x.getPlataforma().equals(nuevo.getPlataforma()) && x.getTitulo().equals(nuevo.getTitulo())) {
                System.out.println("El videojuego " + nuevo.getTitulo() + " no se ha añadido porque ya existe.");
                return false;
            }
        }
        videojuegos.add(nuevo);
        return true;
    }

    public boolean deleteVideojuego(int pos) {
        if (pos < videojuegos.size() && pos >= 0) {
            videojuegos.remove(pos);
            return true;
        } else {
            System.out.println("ERROR: Posición incorrecta.");
            return false;
        }
    }

    public void deleteVideojuego(Videojuego videojuego) {
        if(videojuegos.contains(videojuego)) videojuegos.remove(videojuego);
        else System.out.println("ERROR: El videojuego no existe en la tienda.");
    }

    public String mostrarPosicionesYTitulos() {
        StringBuilder toret = new StringBuilder("Lista de videojuegos:\n");
        for (int i = 0; i < videojuegos.size(); i++) {
            toret.append(i + " " + videojuegos.get(i).getTitulo() + " " + videojuegos.get(i).getPlataforma() + "\n");
        }
        return toret.toString();
    }

    @Override
    public String toString() {
        StringBuilder toret = new StringBuilder("Tienda:\n");
        for (Videojuego videojuego: videojuegos) {
            toret.append(videojuego.toString());
        }
        return toret.toString();
    }
}
