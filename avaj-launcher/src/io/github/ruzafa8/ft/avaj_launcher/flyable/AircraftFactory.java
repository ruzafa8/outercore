package io.github.ruzafa8.ft.avaj_launcher.flyable;

import io.github.ruzafa8.ft.avaj_launcher.Coordinates;

public class AircraftFactory {
    private static AircraftFactory instance;

    private static long idCounter = 0;

    private AircraftFactory() {}

    public static AircraftFactory getInstance() {
        if(AircraftFactory.instance == null) {
            AircraftFactory.instance = new AircraftFactory();
        }
        return AircraftFactory.instance;
    }

    public Flyable newAircraft(String type, String name, Coordinates coordinates) {
        return switch (type) {
            case "Baloon" -> new Baloon(getNextId(), name, coordinates);
            case "JetPlane" -> new JetPlane(getNextId(), name, coordinates);
            case "Helicopter" -> new Helicopter(getNextId(), name, coordinates);
            default -> null;
        };
    }

    private long getNextId() {
        return ++idCounter;
    }
}
