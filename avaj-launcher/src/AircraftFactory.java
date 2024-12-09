class AircraftFactory {
    private static AircraftFactory aircraftFactory;

    private AircraftFactory() {}

    public Flyable newAircraft(String pType, String pName, Coordinates pCoordinates);

    public static AircraftFactory getInstance() {
        if (this.aircraftFactory == null) {
            this.aircraftFactory = new AircraftFactory();
        }
        return this.aircraftFactory;
    }
}