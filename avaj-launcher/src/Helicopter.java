class Helicopter extends Aircraft {
    public Helicopter(long pId, String pName, Coordinates pCoordinates) {
        super(pId, pName, pCoordinates);
    }

    @Override
    public void updateConditions();
}
