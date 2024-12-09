class Coordinates {
    private int longitude;
    private int latitude;
    private int height;

    public Coordinates(int pLongitude, int pLatitude, int pHeight) {
        this.longitude = pLongitude;
        this.latitude = pLatitude;
        this.height = pHeight;
    }

    public int getLongitude() {
        return this.longitude;
    }

    public int getLatitude() {
        return this.latitude;
    }

    public int getHeight() {
        return this.height;
    }
}
