package io.github.ruzafa8.ft.avaj_launcher;

public class AircraftFactory {
    private static AircraftFactory instance;

    private AircraftFactory() {}

    public static AircraftFactory getInstance() {
        if(AircraftFactory.instance == null) {
            AircraftFactory.instance = new AircraftFactory();
        }
        return AircraftFactory.instance;
    }
}
