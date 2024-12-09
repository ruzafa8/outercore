class Baloon extends Aircraft {
    public Baloon(long pId, String pName, Coordinates pCoordinates) {
        super(pId, pName, pCoordinates);
    }

    @Override
    public void updateConditions();
}
