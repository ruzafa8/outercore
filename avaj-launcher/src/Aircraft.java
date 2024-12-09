class Aircraft extends Flyable {
    protected long id;
    protected String name;
    protected Coordinates coordinates;

    protected Aircraft(long pId, String pName, Coordinates pCoordinates) {
        this.id = pId;
        this.name = pName;
        this.coordinates = pCoordinates;
    }

    @Override
    public void updateConditions() {
        // Should I implement it here? or better make class abstract?
    }
}
