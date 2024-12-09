class JetPlane extends Aircraft {
    public JetPlane(long pId, String pName, Coordinates pCoordinates) {
        super(pId, pName, pCoordinates);
    }

    @Override
    public void updateConditions();
}
