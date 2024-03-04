import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;
import java.util.List;

public class PlanetSystem extends JPanel {

    private static final int FRAME_WIDTH = 800;
    private static final int FRAME_HEIGHT = 600;
    private static final int SUN_RADIUS = 50;
    private static final int[] PLANET_RADIUS = {10, 15, 20, 25, 30};
    private static final Color[] PLANET_COLORS = {
            Color.BLUE,     // Merkur
            Color.GREEN,    // Venus
            Color.RED,      // Erde
            Color.ORANGE,   // Mars
            Color.YELLOW    // Jupiter
    };
    private static final int[] PLANET_ORBIT_RADIUS = {100, 150, 200, 250, 300};
    private static final double[] PLANET_MASSES = {0.33, 4.87, 5.97, 0.642, 1898}; // Massen der Planeten in Erdmassen
    private static final double GRAVITATIONAL_CONSTANT = 6.67430e-11; // Gravitationskonstante in m^3/kg/s^2

    private List<Planet> planets;

    public PlanetSystem() {
        setPreferredSize(new Dimension(FRAME_WIDTH, FRAME_HEIGHT));
        initializePlanets();
        Timer timer = new Timer(20, e -> {
            updatePlanets();
            repaint();
        });
        timer.start();
    }

    private void initializePlanets() {
        planets = new ArrayList<>();
        for (int i = 0; i < PLANET_RADIUS.length; i++) {
            planets.add(new Planet(PLANET_ORBIT_RADIUS[i], PLANET_RADIUS[i], PLANET_COLORS[i], PLANET_MASSES[i]));
        }
    }

    private void updatePlanets() {
        for (Planet planet : planets) {
            Vector2D acceleration = new Vector2D(0, 0);
            for (Planet other : planets) {
                if (planet != other) {
                    Vector2D direction = Vector2D.subtract(other.getPosition(), planet.getPosition());
                    double distanceSquared = direction.magnitudeSquared();
                    double forceMagnitude = GRAVITATIONAL_CONSTANT * planet.getMass() * other.getMass() / distanceSquared;
                    Vector2D force = direction.normalized().scale(forceMagnitude);
                    acceleration = acceleration.add(force.scale(1 / planet.getMass()));
                }
            }
            planet.update(acceleration);
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        drawSun(g);
        drawPlanets(g);
    }

    private void drawSun(Graphics g) {
        g.setColor(Color.YELLOW);
        g.fillOval(FRAME_WIDTH / 2 - SUN_RADIUS, FRAME_HEIGHT / 2 - SUN_RADIUS, SUN_RADIUS * 2, SUN_RADIUS * 2);
    }

    private void drawPlanets(Graphics g) {
        for (Planet planet : planets) {
            int x = (int) Math.round(planet.getPosition().getX()) + FRAME_WIDTH / 2;
            int y = (int) Math.round(planet.getPosition().getY()) + FRAME_HEIGHT / 2;
            int radius = planet.getRadius();
            g.setColor(planet.getColor());
            g.fillOval(x - radius, y - radius, radius * 2, radius * 2);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Planetensystem mit Gravitationssimulation");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.getContentPane().add(new PlanetSystem());
            frame.pack();
            frame.setLocationRelativeTo(null);
            frame.setVisible(true);
        });
    }
}

class Vector2D {
    private final double x;
    private final double y;

    public Vector2D(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double magnitudeSquared() {
        return x * x + y * y;
    }

    public double magnitude() {
        return Math.sqrt(magnitudeSquared());
    }

    public Vector2D normalized() {
        double mag = magnitude();
        return new Vector2D(x / mag, y / mag);
    }

    public Vector2D add(Vector2D other) {
        return new Vector2D(x + other.x, y + other.y);
    }

    public static Vector2D subtract(Vector2D a, Vector2D b) {
        return new Vector2D(a.x - b.x, a.y - b.y);
    }

    public Vector2D scale(double scalar) {
        return new Vector2D(x * scalar, y * scalar);
    }
}

class Planet {
    private Vector2D position;
    private Vector2D velocity;
    private int radius;
    private Color color;
    private double mass; // in kg

    public Planet(int orbitRadius, int radius, Color color, double mass) {
        this.position = new Vector2D(orbitRadius, 0);
        this.velocity = new Vector2D(0, Math.sqrt(GRAVITATIONAL_CONSTANT * PlanetSystem.PLANET_MASSES[2] / orbitRadius));
        this.radius = radius;
        this.color = color;
        this.mass = mass * 5.972e24; // Erdmassen in kg
    }

    public Vector2D getPosition() {
        return position;
    }

    public int getRadius() {
        return radius;
    }

    public Color getColor() {
        return color;
    }

    public double getMass() {
        return mass;
    }

    public void setMass(double mass) {
        this.mass = mass;
    }

    public void update(Vector2D acceleration) {
        velocity = velocity.add(acceleration);
        position = position.add(velocity);
    }
}
