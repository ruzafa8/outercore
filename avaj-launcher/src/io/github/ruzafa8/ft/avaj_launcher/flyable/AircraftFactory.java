package io.github.ruzafa8.ft.avaj_launcher.flyable;

import io.github.ruzafa8.ft.avaj_launcher.Coordinates;
import io.github.ruzafa8.ft.avaj_launcher.SimulationException;

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
        return switch (type.toUpperCase()) {
            case "BALOON" -> new Baloon(getNextId(), name, coordinates);
            case "JETPLANE" -> new JetPlane(getNextId(), name, coordinates);
            case "HELICOPTER" -> new Helicopter(getNextId(), name, coordinates);
            default -> throw new SimulationException(type + " is not a valid Aircraft type");
        };
    }

    private long getNextId() {
        return ++idCounter;
    }
}
